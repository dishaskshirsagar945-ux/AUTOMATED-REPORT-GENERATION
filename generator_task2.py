import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from datetime import datetime

data = pd.read_csv("student_data2.csv")

average_marks = data["Marks"].mean()
highest_marks = data["Marks"].max()
lowest_marks = data["Marks"].min()

file_name = "Student_Report.pdf"
pdf = SimpleDocTemplate(file_name, pagesize=A4)

styles = getSampleStyleSheet()
elements = []

elements.append(Paragraph("<b>Student Marks Report</b>", styles["Title"]))
elements.append(Spacer(1, 12))

date_text = f"Report Generated on: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
elements.append(Paragraph(date_text, styles["Normal"]))
elements.append(Spacer(1, 12))

elements.append(Paragraph(f"Average Marks: {average_marks:.2f}", styles["Normal"]))
elements.append(Paragraph(f"Highest Marks: {highest_marks}", styles["Normal"]))
elements.append(Paragraph(f"Lowest Marks: {lowest_marks}", styles["Normal"]))
elements.append(Spacer(1, 12))

table_data = [data.columns.tolist()] + data.values.tolist()

table = Table(table_data)
table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
    ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
]))

elements.append(table)

pdf.build(elements)

print("✅ Student_Report.pdf generated successfully!")