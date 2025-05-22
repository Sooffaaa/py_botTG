import re
from aiogram import Router, types, F
from filters import IsOwnerFilter
from bot import BotDB

personal_router = Router()

@personal_router.message(commands=["start"])
async def cmd_start(message: types.Message):
    if not BotDB.user_exists(message.from_user.id):
        BotDB.add_user(message.from_user.id)

    await message.answer("Добро пожаловать!")


@personal_router.message(commands=["spend", "s", "earned", "e"], commands_prefix="/!")
async def record(message: types.Message):
    cmd_text = message.text.lower()
    expense_commands = ('/spend', '/s', '!spend', '!s')
    income_commands = ('/earned', '/e', '!earned', '!e')

    operation = "-"
    if any(cmd_text.startswith(cmd) for cmd in income_commands):
        operation = "+"

    for variant in expense_commands + income_commands:
        cmd_text = cmd_text.replace(variant, "").strip()

    if not cmd_text:
        return await message.reply("Не введена сумма!")

    amount_matches = re.findall(r"\d+(?:[.,]\d+)?", cmd_text)
    if not amount_matches:
        return await message.reply("Не удалось определить сумму!")

    value = float(amount_matches[0].replace(",", "."))
    BotDB.add_record(message.from_user.id, operation, value)

    if operation == "-":
        await message.reply("✅ Запись о <u><b>расходе</b></u> успешно внесена!")
    else:
        await message.reply("✅ Запись о <u><b>доходе</b></u> успешно внесена!")


@personal_router.message(commands=["history", "h"], commands_prefix="/!")
async def history(message: types.Message):
    cmd_text = message.text.lower()
    history_aliases = ('/history', '/h', '!history', '!h')
    period_aliases = {
        "day": ('today', 'day', 'сегодня', 'день'),
        "month": ('month', 'месяц'),
        "year": ('year', 'год'),
    }

    for variant in history_aliases:
        cmd_text = cmd_text.replace(variant, "").strip()

    period = "day"
    if cmd_text:
        for key, aliases in period_aliases.items():
            if cmd_text in aliases:
                period = key
                break

    records = BotDB.get_records(message.from_user.id, period)

    if not records:
        return await message.reply("Записей не обнаружено!")

    answer = f"⏳ История операций за <b>{period_aliases[period][-1]}</b>:\n\n"
    for record in records:
        operation = "➖ Расход" if record[2] == "-" else "➕ Доход"
        answer += f"<b>{operation}</b> - {record[3]} <i>({record[4]})</i>\n"

    await message.reply(answer)


@personal_router.message(IsOwnerFilter(), commands=["ping"], commands_prefix="!/")
async def cmd_ping_bot(message: types.Message):
    await message.reply("<b>👊 Up & Running!</b>")

