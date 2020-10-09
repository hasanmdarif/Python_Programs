from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Programs must be written for people to read, \
    and only incidentally machine to execute it. Cheers to programmers !")
pdf.output("trial.pdf")
