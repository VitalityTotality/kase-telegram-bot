from fpdf import FPDF
import datetime

def generate_pdf_report(portfolio, prices, total_profit):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Инвестиционный отчёт", ln=True, align="C")
    pdf.cell(200, 10, txt=f"Дата: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", size=10)
    pdf.cell(40, 10, "Тикер", border=1)
    pdf.cell(40, 10, "Кол-во", border=1)
    pdf.cell(40, 10, "Цена покупки", border=1)
    pdf.cell(40, 10, "Текущая цена", border=1)
    pdf.cell(30, 10, "Прибыль", border=1)
    pdf.ln()

    for ticker, data in portfolio.items():
        current = prices[ticker]["current"]
        profit = prices[ticker]["profit"]
        pdf.cell(40, 10, ticker, border=1)
        pdf.cell(40, 10, str(data["quantity"]), border=1)
        pdf.cell(40, 10, str(data["buy_price"]), border=1)
        pdf.cell(40, 10, f"{current:.2f}", border=1)
        pdf.cell(30, 10, f"{profit:.2f}", border=1)
        pdf.ln()

    pdf.ln(5)
    pdf.cell(200, 10, f"Итоговая прибыль: {total_profit:.2f}", ln=True)

    file_path = "portfolio_report.pdf"
    pdf.output(file_path)
    return file_path
