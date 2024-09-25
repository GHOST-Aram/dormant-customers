import re
import pandas as pd

def extract_phone_numbers(text):
    # Regular expression to find phone numbers
    phone_regex = r'\b\d{10}\b'  # Assumes phone numbers are 10 digits long
    phone_numbers = re.findall(phone_regex, text)
    
    # Create a list of dictionaries with 'Customer' and 'Phone Number'
    phone_data = [{'Customer': f'dorman_customer_{i+1}', 'Phone Number': number} for i, number in enumerate(phone_numbers)]
    
    return phone_data

def save_to_excel(phone_data, filename):
    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(phone_data)
    
    # Write the DataFrame to an Excel file
    df.to_excel(filename, index=False)

# Example input with mixed text and phone numbers
text = """
Some random text with phone numbers like 1234567890 and 0987654321.
Here's another number 1122334455 mixed in the text.
"""

# Extract phone numbers
phone_data = extract_phone_numbers(text)

# Save the result to an Excel file
save_to_excel(phone_data, 'dorman_customers.xlsx')

print("Phone numbers saved to dorman_customers.xlsx.")
