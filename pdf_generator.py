from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib import colors
from reportlab.lib.units import mm
from datetime import datetime  # Import datetime module for formatting dates
from styles import get_styles

def create_invoice(details):
    pdf = SimpleDocTemplate("joke_invoice.pdf", pagesize=A4, rightMargin=20, leftMargin=20, topMargin=20, bottomMargin=20)
    elements = []
    styles = get_styles()

    # Helper function to format dates
    def format_date(date_str):
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%B %-d, %Y")

    # Add company logo
    logo_path = "assets/company_logo.png"
    logo = Image(logo_path, width=100, height=50)
    elements.append(logo)
    elements.append(Spacer(1, 12))

    # Add company information
    company_info = Paragraph(f"{details['company_name']}<br />{details['company_address']}<br />{details['company_phone']}<br />{details['company_email']}<br />{details['company_website']}", styles['CompanyInfo'])
    elements.append(company_info)
    elements.append(Spacer(1, 12))

    # Add the title
    title = Paragraph("INVOICE", styles['InvoiceTitle'])
    elements.append(title)
    elements.append(Spacer(1, 12))

    # Add recipient and date details
    recipient = Paragraph(f"<b>To:</b> {details['recipient_name']}<br />{details['recipient_address']}", styles['RecipientInfo'])
    date = Paragraph(f"<b>Date:</b> {format_date(details['date'])}", styles['RecipientInfo'])
    invoice_number = Paragraph(f"<b>Invoice #:</b> {details['invoice_number']}", styles['RecipientInfo'])
    payment_terms = Paragraph(f"<b>Payment Terms:</b> {details['payment_terms']}", styles['RecipientInfo'])
    due_date = Paragraph(f"<b>Due Date:</b> {format_date(details['due_date'])}", styles['RecipientInfo'])
    elements.extend([recipient, date, invoice_number, payment_terms, due_date, Spacer(1, 12)])

    # Configure table data with improved styling
    table_data = [
        [Paragraph("Description", styles['TableHeader']),
         Paragraph("Quantity", styles['TableHeader']),
         Paragraph("Unit Price", styles['TableHeader']),
         Paragraph("Total", styles['TableHeader']),
         Paragraph("Tax", styles['TableHeader']),
         Paragraph("Date", styles['TableHeader'])]
    ]
    for item in details['items']:
        row = [
            Paragraph(item['description'], styles['TableContent']),
            Paragraph(str(item['quantity']), styles['TableContent']),
            Paragraph(f"{item['unit_price']} kisses", styles['TableContent']),
            Paragraph(f"{item['total']} kisses", styles['TableContent']),
            Paragraph(f"{item['tax']} kisses", styles['TableContent']),
            Paragraph(format_date(item['date']), styles['TableContent'])
        ]
        table_data.append(row)

    # Create and style the table
    table = Table(table_data, colWidths=[90*mm, 20*mm, 25*mm, 25*mm, 25*mm, 25*mm])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey])
    ]))

    elements.append(Spacer(1, 12))  # Add Spacer before the table
    elements.append(table)
    elements.append(Spacer(1, 12))  # Add Spacer after the table

    # Add subtotal, tax due, and total due
    subtotal = Paragraph(f"<b>Subtotal:</b> {details['subtotal']} kisses", styles['TotalDue'])
    tax_due = Paragraph(f"<b>Tax Due:</b> {details['tax_due']} kisses", styles['TotalDue'])
    total_due = Paragraph(f"<b>Total Due:</b> {details['total_due']} kisses", styles['TotalDue'])
    notes = Paragraph("<b>Notes:</b> Payment accepted in hugs, kisses, and happy moments. Thank you for all the wonderful times we've shared. Here's to many more! 💖", styles['Notes'])
    elements.extend([subtotal, tax_due, total_due, Spacer(1, 12), notes])

    # Add footnote
    if "footnote" in details:
        footnote = Paragraph(details["footnote"], styles['Footer'])
        elements.append(Spacer(1, 24))  # Add Spacer before the footnote
        elements.append(footnote)

    # Add footer
    footer = Paragraph("Love & Laughter Co. | 123 Happy St, Joytown, Love Country | (123) 456-7890 | info@loveandlaughter.com | www.loveandlaughter.com", styles['Footer'])
    elements.append(Spacer(1, 24))  # Add Spacer before the footer
    elements.append(footer)

    # Build the PDF
    pdf.build(elements)