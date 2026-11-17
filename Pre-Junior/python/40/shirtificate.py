from fpdf import FPDF


name: str = input("Enter your name: ")

pdf = FPDF(orientation="P", format="A4")
shirt_top: int = 35
shirt_width: int = 190

pdf.add_page()
pdf.image("shirtificate.png", (pdf.w - shirt_width) / 2, shirt_top, shirt_width)
pdf.set_font("helvetica", "", 40)
pdf.cell(0, 15, "CS50 Shirtificate", align="C")
pdf.set_y(shirt_top + 70)
pdf.set_font("helvetica", "", 20)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 10, f"{name} took CS50", align="C")
pdf.output("shirtificate.pdf")
