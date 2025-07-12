from aiogram import types, Dispatcher
from kase_parser import get_portfolio_profit
from pdf_report import generate_pdf_report
import datetime

portfolio = {
    "AIRA": {"quantity": 100, "buy_price": 120},
    "KEGC": {"quantity": 200, "buy_price": 850},
    "MSFT_KZ": {"quantity": 50, "buy_price": 35000},
    "AAPL_KZ": {"quantity": 30, "buy_price": 40000},
    "ASBN": {"quantity": 3000, "buy_price": 18},
}

async def cmd_start(message: types.Message):
    await message.answer("Привет! Отправь команду /report для получения отчёта по портфелю.")

async def cmd_report(message: types.Message):
    prices, total_profit = get_portfolio_profit(portfolio)
    pdf_path = generate_pdf_report(portfolio, prices, total_profit)
    await message.answer_document(open(pdf_path, "rb"))

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=["start"])
    dp.register_message_handler(cmd_report, commands=["report"])
