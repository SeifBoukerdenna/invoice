from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

# Invoice details
invoice_details = {
    "recipient": "Your Girlfriend's Name",
    "date": "2024-07-09",
    "invoice_number": "001",
    "items": [
        {"description": "Romantic Dinner Date", "quantity": "1 evening", "unit_price": "100 kisses", "total": "100 kisses"},
        {"description": "Movie Night Cuddles", "quantity": "3 movies", "unit_price": "50 hugs per movie", "total": "150 hugs"},
        {"description": "Beach Day Fun", "quantity": "1 day", "unit_price": "200 smiles", "total": "200 smiles"},
        {"description": "Ice Cream Date", "quantity": "2 scoops", "unit_price": "1 laugh per scoop", "total": "2 laughs"},
        {"description": "Late-Night Talks", "quantity": "5 hours", "unit_price": "10 heartbeats per hour", "total": "50 heartbeats"},
        {"description": "Surprise Picnic", "quantity": "1 picnic", "unit_price": "50 butterflies", "total": "50 butterflies"},
        {"description": "Handwritten Love Notes", "quantity": "10 notes", "unit_price": "5 blushes per note", "total": "50 blushes"},
        {"description": "Stargazing Night", "quantity": "1 night", "unit_price": "100 twinkles", "total": "100 twinkles"},
        {"description": "Inside Jokes", "quantity": "Unlimited", "unit_price": "Priceless", "total": "Priceless"},
        {"description": "Support & Encouragement", "quantity": "Infinite", "unit_price": "Unconditional Love", "total": "Infinite"}
    ],
    "total_due": "More Love and Fun Memories!"
}

def create_invoice(details):
    # Create a PDF document
    pdf = SimpleDocTemplate("joke_invoice.pdf", pagesize=A4)
    elements = []

    # Add the title
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    title = Paragraph("INVOICE", title_style)
    elements.append(title)

    # Add recipient and date details
    subtitle_style = ParagraphStyle(name='Subtitle', fontSize=12, leading=14)
    recipient = Paragraph(f"<b>To:</b> {details['recipient']}", subtitle_style)
    date = Paragraph(f"<b>Date:</b> {details['date']}", subtitle_style)
    invoice_number = Paragraph(f"<b>Invoice #:</b> {details['invoice_number']}", subtitle_style)
    elements.extend([Spacer(1, 12), recipient, date, invoice_number, Spacer(1, 12)])

    # Create table data
    table_data = [["Description", "Quantity", "Unit Price", "Total"]]
    for item in details['items']:
        row = [item['description'], item['quantity'], item['unit_price'], item['total']]
        table_data.append(row)

    # Create the table
    table = Table(table_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(table)

    # Add total due
    total_due = Paragraph(f"<b>Total Due:</b> {details['total_due']}", subtitle_style)
    notes = Paragraph("<b>Notes:</b> Payment accepted in hugs, kisses, and happy moments. Thank you for all the wonderful times we've shared. Here's to many more! 💖", subtitle_style)
    elements.extend([Spacer(1, 12), total_due, Spacer(1, 12), notes])

    # Build the PDF
    pdf.build(elements)

# Create the invoice
create_invoice(invoice_details)
