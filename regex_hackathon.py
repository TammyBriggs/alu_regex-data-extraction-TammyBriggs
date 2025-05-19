import re

def extract_emails(text):
    """Extracts email addresses from a string."""
    return re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

def extract_urls(text):
    """Extracts URLs from a string."""
    return re.findall(r"https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/\S*)?", text)

def extract_phone_numbers(text):
    """Extracts phone numbers from a string (various formats)."""
    return re.findall(r"(?:\d{3}|\(\d{3}\))[-.\s]?\d{3}[-.\s]?\d{4}", text)