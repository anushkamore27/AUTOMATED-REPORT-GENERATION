import pandas as pd
from fpdf import FPDF

data = pd.read_csv('data.csv')

average_score = data['Score'].mean()
highest_score = data['Score'].max()
lowest_score = data['Score'].min()
top_student = data.loc[data['Score'].idxmax()]['Name']

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)

pdf.cell(200, 10, "Student Score Report", ln=True, align='C')
pdf.ln(10)


pdf.set_font("Arial", '', 12)
pdf.cell(200, 10, f"Average Score: {average_score:.2f}", ln=True)
pdf.cell(200, 10, f"Highest Score: {highest_score} (by {top_student})", ln=True)
pdf.cell(200, 10, f"Lowest Score: {lowest_score}", ln=True)
pdf.ln(10)


pdf.set_font("Arial", 'B', 12)
pdf.cell(100, 10, "Name", border=1)
pdf.cell(50, 10, "Score", border=1)
pdf.ln()

pdf.set_font("Arial", '', 12)
for index, row in data.iterrows():
    pdf.cell(100, 10, row['Name'], border=1)
    pdf.cell(50, 10, str(row['Score']), border=1)
    pdf.ln()

pdf.output("student_report.pdf")
print("PDF report generated successfully!")
