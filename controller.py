"""
controller.py — glue between view and model.
"""
import io
from pypdf import PdfReader

import model


def list_models():
    return model.list_models()


def read_pdf(pdf_bytes):
    """Extract all text from a PDF (given as bytes)."""
    reader = PdfReader(io.BytesIO(pdf_bytes))
    pages = [page.extract_text() or "" for page in reader.pages]
    return "\n\n".join(pages)


def ask(model_key, question, document_text):
    return model.ask(model_key, question, document_text)
