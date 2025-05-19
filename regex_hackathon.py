import re

""" def extract_emails(text):
   # Extracts email addresses from a string.
    return re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text) """

# Email Validation
def is_valid_email(email):
    if not email:
        return False
    if '@' not in email:
        return False
    parts = email.split('@')
    if len(parts) != 2:
        return False
    local_part, domain_part = parts
    if not local_part or not domain_part:
        return False
    if '.' not in domain_part:
        return False
    if email.endswith('.'):
        return False
    return True

def extract_emails_with_validation(text):
    """Extracts email addresses and performs basic validation."""
    extracted_emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    valid_emails = [email for email in extracted_emails if is_valid_email(email)]
    return valid_emails

""" def extract_urls(text):
    # Extracts URLs from a string.
    return re.findall(r"https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/\S*)?", text) """

# URL Validation
def is_valid_url(url):
    if not url or not url.startswith(('http://', 'https://')) or '.' not in url.split('//', 1)[-1]:
        return False
    parts = url.split('//', 1)[-1].split('/')
    if not parts[0]:
        return False
    if url.endswith('.'):
        return False
    return True

def extract_urls_with_validation(text):
    extracted_urls = re.findall(r"https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/\S*)?", text)
    valid_urls = [url for url in extracted_urls if is_valid_url(url)]
    return valid_urls

""" def extract_phone_numbers(text):
    # Extracts phone numbers from a string (various formats).
    return re.findall(r"(?:\d{3}|\(\d{3}\))[-.\s]?\d{3}[-.\s]?\d{4}", text) """

# Phone Number Validation
def is_valid_phone_number(phone):
    cleaned_phone = re.sub(r'[^0-9]', '', phone)
    return len(cleaned_phone) == 10

def extract_phone_numbers_with_validation(text):
    extracted_phones = re.findall(r"(?:\d{3}|\(\d{3}\))[-.\s]?\d{3}[-.\s]?\d{4}", text)
    valid_phones = [phone for phone in extracted_phones if is_valid_phone_number(phone)]
    return valid_phones

""" def extract_credit_card_numbers(text):
    # Extracts credit card numbers from a string (with or without hyphens/spaces).
    return re.findall(r"\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}", text) """

# Credit Card Number Validation (Basic Length Check)
def is_valid_credit_card(cc_num):
    cleaned_cc = re.sub(r'[^0-9]', '', cc_num)
    return 13 <= len(cleaned_cc) <= 19  # Basic length check

def extract_credit_card_numbers_with_validation(text):
    extracted_ccs = re.findall(r"\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}", text)
    valid_ccs = [cc for cc in extracted_ccs if is_valid_credit_card(cc)]
    return valid_ccs

""" def extract_times(text):
    # Extracts time in 12-hour and 24-hour formats from a string.
    time_24hr = re.findall(r'\b(?:[01]\d|2[0-3]):[0-5]\d\b', text)
    time_12hr = re.findall(r'\b(?:0?[1-9]|1[0-2]):[0-5]\d\s?(?:AM|PM)\b', text, re.IGNORECASE)
    return time_24hr + time_12hr """

# Time Validation
def is_valid_time(time_str):
    if re.match(r"^(0?[1-9]|1[0-2]):[0-5]\d\s?(?:AM|PM)$", time_str, re.IGNORECASE):
        return True
    if re.match(r"^(?:[01]\d|2[0-3]):[0-5]\d$", time_str):
        return True
    return False

def extract_times_with_validation(text):
    extracted_times_24hr = re.findall(r'\b(?:[01]\d|2[0-3]):[0-5]\d\b', text)
    extracted_times_12hr = re.findall(r'\b(?:0?[1-9]|1[0-2]):[0-5]\d\s?(?:AM|PM)\b', text, re.IGNORECASE)
    all_extracted_times = extracted_times_24hr + extracted_times_12hr
    valid_times = [t for t in all_extracted_times if is_valid_time(t)]
    return valid_times

""" def extract_hashtags(text):
    # Extracts hashtags from a string.
    return re.findall(r"#\w+", text) """

# Hashtag Validation (Basic Check for Non-Whitespace)
def is_valid_hashtag(hashtag):
    return hashtag.startswith('#') and len(hashtag) > 1 and not re.search(r'\s', hashtag[1:])

def extract_hashtags_with_validation(text):
    extracted_hashtags = re.findall(r"#\w+", text)
    valid_hashtags = [tag for tag in extracted_hashtags if is_valid_hashtag(tag)]
    return valid_hashtags

# Example usage:
text_data = """
Contact us at home@example.com or firstname.lastname@company.co.uk. or @gmail.com. or chief@gmail.com.
Visit our website at https://www.skip.com or https://subdomain.racing.org/page or running.
Call us at (123) 456-7890, 123-456-7890, or 123.456.7890 or 123456789a.
Use credit card number 1234-5678-9012-3456 or 1111 2222 3333 4444 or 111a 222b 333c 444d.
Meeting at 14:30 or 2:30 PM or 6.
Check out this# #amazing #Python code!
"""

emails = extract_emails_with_validation(text_data)
urls = extract_urls_with_validation(text_data)
phone_numbers = extract_phone_numbers_with_validation(text_data)
credit_cards = extract_credit_card_numbers_with_validation(text_data)
times = extract_times_with_validation(text_data)
hashtags = extract_hashtags_with_validation(text_data)

print("Emails:", emails)
print("URLs:", urls)
print("Phone Numbers:", phone_numbers)
print("Credit Card Numbers:", credit_cards)
print("Times:", times)
print("Hashtags:", hashtags)