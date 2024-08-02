from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

def create_timetable_pdf(file_path, timetable_data, days):
    pdf = SimpleDocTemplate(file_path, pagesize=letter, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=30)
    elements = []
    data = [["Day", "Time", "Class", "Classroom"]]
    for day, schedule in timetable_data.items():
        for time, details in schedule.items():
            data.append([day, time, details["Class"], details["Classroom"]])
    table = Table(data, colWidths=[1.2*inch, 1.5*inch, 2.5*inch, 1.5*inch])
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black)
    ])
    table.setStyle(style)

    elements.append(table)

    pdf.build(elements)

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
timetable_data = {
    "Monday": {
        "11:30 am - 1:00 pm": {"Class": "Digital Image Processing", "Classroom": "H-105"},
        "2:00 pm - 3:30 pm": {"Class": "Topics in Applied Optimization", "Classroom": "H-103"},
        "5:00 pm - 6:30 pm": {"Class": "Introduction to Economics", "Classroom": "H-103"}
    },
    "Tuesday": {
        "2:00 pm - 3:30 pm": {"Class": "Mobile Robotics", "Classroom": "H-101"}
    },
    "Wednesday": {
        "11:30 am - 1:00 pm": {"Class": "Robotics: Dynamics and Control", "Classroom": "H-102"}
    },
    "Thursday": {
        "11:30 am - 1:00 pm": {"Class": "Digital Image Processing", "Classroom": "H-105"},
        "2:00 pm - 3:30 pm": {"Class": "Topics in Applied Optimization", "Classroom": "H-103"},
        "5:00 pm - 6:30 pm": {"Class": "Introduction to Economics", "Classroom": "H-103"}
    },
    "Friday": {
        "2:00 pm - 3:30 pm": {"Class": "Mobile Robotics", "Classroom": "H-101"}
    },
    "Saturday": {
        "11:30 am - 1:00 pm": {"Class": "Robotics: Dynamics and Control", "Classroom": "H-102"}
    }
}

create_timetable_pdf("timetable.pdf", timetable_data, days)
