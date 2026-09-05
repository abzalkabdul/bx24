from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

router = Router()

class Reg(StatesGroup):
    name: State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f"Hello. {message.from_user.first_name}, your ID is {message.from_user.id}")

@router.message(Command("/help"))
async def help(message: Message):
    await message.answer("Wait please, our staff are working on this right now.")

@router.message(Command('reg'))
async def reg_first(message: Message, state:)
