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

def extract_credit_card_numbers(text):
    """Extracts credit card numbers from a string (with or without hyphens/spaces)."""
    return re.findall(r"\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}", text)

def extract_times(text):
    """Extracts time in 12-hour and 24-hour formats from a string."""
    time_24hr = re.findall(r'\b(?:[01]\d|2[0-3]):[0-5]\d\b', text)
    time_12hr = re.findall(r'\b(?:0?[1-9]|1[0-2]):[0-5]\d\s?(?:AM|PM)\b', text, re.IGNORECASE)
    return time_24hr + time_12hr

def extract_hashtags(text):
    """Extracts hashtags from a string."""
    return re.findall(r"#\w+", text)

# Example usage:
text_data = """
Contact us at home@example.com or firstname.lastname@company.co.uk.
Visit our website at https://www.skip.com or https://subdomain.racing.org/page.
Call us at (123) 456-7890, 123-456-7890, or 123.456.7890.
Use credit card number 1234-5678-9012-3456 or 1111 2222 3333 4444.
Meeting at 14:30 or 2:30 PM.
Check out the #amazing #Python code!
"""

emails = extract_emails(text_data)
urls = extract_urls(text_data)
phone_numbers = extract_phone_numbers(text_data)
credit_cards = extract_credit_card_numbers(text_data)
times = extract_times(text_data)
hashtags = extract_hashtags(text_data)

print("Emails:", emails)
print("URLs:", urls)
print("Phone Numbers:", phone_numbers)
print("Credit Card Numbers:", credit_cards)
print("Times:", times)
print("Hashtags:", hashtags)