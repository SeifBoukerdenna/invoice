from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def get_styles():
    styles = getSampleStyleSheet()

    # Custom styles
    styles.add(ParagraphStyle(name='InvoiceTitle', fontSize=24, leading=28, spaceAfter=20, alignment=1))
    styles.add(ParagraphStyle(name='CompanyInfo', fontSize=10, leading=12, spaceAfter=6, alignment=1))
    styles.add(ParagraphStyle(name='RecipientInfo', fontSize=12, leading=14, spaceAfter=12))
    styles.add(ParagraphStyle(name='TableHeader', fontSize=12, leading=14, alignment=1, textColor=colors.whitesmoke, backColor=colors.grey))
    styles.add(ParagraphStyle(name='TableRow', fontSize=10, leading=12, alignment=1, backColor=colors.beige))
    styles.add(ParagraphStyle(name='TableContent', fontSize=10, leading=12, alignment=1, textColor=colors.black))  # Added TableContent style
    styles.add(ParagraphStyle(name='TotalDue', fontSize=12, leading=14, spaceAfter=20))
    styles.add(ParagraphStyle(name='Notes', fontSize=10, leading=12, spaceAfter=20))
    styles.add(ParagraphStyle(name='Footer', fontSize=8, leading=10, alignment=1, textColor=colors.grey))

    return styles