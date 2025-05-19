import re

def extract_emails(text):
    """Extracts email addresses from a string."""
    return re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)