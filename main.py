# main.py

from data import invoice_details
from pdf_generator import create_invoice

if __name__ == "__main__":
    create_invoice(invoice_details)
