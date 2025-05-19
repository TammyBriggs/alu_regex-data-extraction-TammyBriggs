# alu_regex-data-extraction-TammyBriggs

## Project Overview

This project is a Python-based solution designed to extract specific data types from large volumes of text using regular expressions. As a Junior Full Stack Developer working on a short-term gig to develop a web application that aggregates data from across the web, the ability to efficiently and accurately extract information like email addresses, URLs, phone numbers, credit card numbers, times, and hashtags is crucial. This script provides functions for each of these data types.

## Implemented Data Extraction

This script implements regular expressions to extract the following six data types:

1.  **Email Addresses:** Extracts email addresses in the format `user@example.com` and `firstname.lastname@company.co.uk`.
2.  **URLs:** Extracts web URLs starting with `http://` or `https://`, including those with subdomains and paths.
3.  **Phone Numbers:** Extracts phone numbers in various common formats such as `(123) 456-7890`, `123-456-7890`, and `123.456.7890`.
4.  **Credit Card Numbers:** Extracts credit card numbers in the format `1234 5678 9012 3456` and `1234-5678-9012-3456`.
5.  **Time:** Extracts time in both 24-hour format (e.g., `14:30`) and 12-hour format with AM/PM (e.g., `2:30 PM`).
6.  **Hashtags:** Extracts words preceded by a hash symbol (`#`), commonly used on social media.

## Setup Instructions

To run this script, you need to have Python 3 installed on your system.

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/](https://github.com/TammyBriggs/alu_regex-data-extraction-TammyBriggs.git
    cd alu_regex-data-extraction-TammyBriggs
    ```

2.  **No Additional Libraries Required:** This script uses Python's built-in `re` module, so no external libraries need to be installed.

3.  **Run the Script:**
    ```bash
    python regex_hackathon.py
    ``
## Code Structure

The Python script `regex_hackathon.py` contains the following functions:

-   `extract_emails(text)`: Extracts email addresses.
-   `extract_urls(text)`: Extracts URLs.
-   `extract_phone_numbers(text)`: Extracts phone numbers.
-   `extract_credit_card_numbers(text)`: Extracts credit card numbers.
-   `extract_times(text)`: Extracts time in both 12-hour and 24-hour formats.
-   `extract_hashtags(text)`: Extracts hashtags.

The script also includes an example usage section that demonstrates how to use these functions with sample input text and prints the extracted data.

## Edge-Case Handling

The regular expressions used in this script are designed to handle some common variations and edge cases:

-   **Email Addresses:** Handles standard email formats with alphanumeric characters, periods, underscores, percentages, pluses, and hyphens before the `@` symbol, and alphanumeric characters, periods, and hyphens in the domain name. It also accounts for top-level domains with at least two letters.
-   **URLs:** Handles both `http` and `https` protocols, optional `www.` subdomain, alphanumeric characters, periods, and hyphens in the domain, and optional paths following the domain.
-   **Phone Numbers:** Accommodates phone numbers with or without parentheses around the area code, and with hyphens, spaces, or periods as separators.
-   **Credit Card Numbers:** Handles credit card numbers with or without hyphens or spaces as separators between the four-digit groups.
-   **Time:** Correctly identifies both 24-hour format times (00:00 to 23:59) and 12-hour format times (1:00 AM to 12:59 PM, with optional leading zero for hours 1-9).
-   **Hashtags:** Extracts words immediately following a `#` symbol, including those with uppercase and lowercase letters and numbers.

While these regex patterns cover many common formats, more complex or unusual formats might not be captured. Further refinement of the regular expressions could be done to handle additional edge cases if required.

## Output Presentation

The example usage in the `regex_hackathon.py` script demonstrates how to call each extraction function and prints the resulting lists of extracted data to the console. The output clearly labels each type of extracted information.

For more comprehensive testing, you can modify the `text_data` variable to include a wider range of inputs and verify the accuracy of the extracted results.

## Further Improvements

-   Implement extraction for the remaining data types (HTML tags and Currency amounts).
-   Enhance the regular expressions to handle more complex edge cases and variations in the data formats.
-   Integrate these functions into a larger web application to process real-world API responses.
-   Add error handling and logging for more robust performance.
