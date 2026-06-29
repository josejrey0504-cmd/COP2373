# Jose Reyes
# Programming Exercise 6
# This program validates phone numbers, Social Security numbers,
# and ZIP codes using regular expressions.

import re


# This function checks if the phone number is in the correct format.
def validate_phone_number(phone_number):
    # This regular expression matches the format 123-456-7890.
    pattern = r"^\d{3}-\d{3}-\d{4}$"

    # Return True if the phone number matches the pattern.
    return re.fullmatch(pattern, phone_number) is not None


# This function checks if the Social Security number is valid.
def validate_social_security_number(ssn):
    # This regular expression matches the format 123-45-6789.
    pattern = r"^\d{3}-\d{2}-\d{4}$"

    # Return True if the Social Security number matches the pattern.
    return re.fullmatch(pattern, ssn) is not None


# This function checks if the ZIP code is valid.
def validate_zip_code(zip_code):
    # This regular expression matches the formats 12345 or 12345-6789.
    pattern = r"^\d{5}(-\d{4})?$"

    # Return True if the ZIP code matches the pattern.
    return re.fullmatch(pattern, zip_code) is not None


# This function displays whether the value entered is valid.
def display_result(item_name, is_valid):
    # Check if the value is valid.
    if is_valid:
        print(f"{item_name} is valid.")
    else:
        print(f"{item_name} is invalid.")


# This function tests the validation functions using valid and invalid examples.
def run_tests():
    print("\nTesting Validation Functions")

    # Valid and invalid phone numbers.
    test_phone_numbers = [
        "123-456-7890",
        "1234567890",
        "123-45-6789"
    ]

    # Valid and invalid Social Security numbers.
    test_ssns = [
        "123-45-6789",
        "123456789",
        "12-345-6789"
    ]

    # Valid and invalid ZIP codes.
    test_zip_codes = [
        "12345",
        "12345-6789",
        "1234",
        "123456"
    ]

    # Test each phone number.
    for phone in test_phone_numbers:
        display_result(phone, validate_phone_number(phone))

    # Test each Social Security number.
    for ssn in test_ssns:
        display_result(ssn, validate_social_security_number(ssn))

    # Test each ZIP code.
    for zip_code in test_zip_codes:
        display_result(zip_code, validate_zip_code(zip_code))


# The main function controls the program.
def main():
    # Ask the user to enter a phone number.
    phone_number = input(
        "Enter a phone number (123-456-7890): "
    )

    # Ask the user to enter a Social Security number.
    ssn = input(
        "Enter a Social Security number (123-45-6789): "
    )

    # Ask the user to enter a ZIP code.
    zip_code = input(
        "Enter a ZIP code (12345 or 12345-6789): "
    )

    # Display the validation results.
    print("\nValidation Results")
    display_result(
        "Phone number",
        validate_phone_number(phone_number)
    )
    display_result(
        "Social Security number",
        validate_social_security_number(ssn)
    )
    display_result(
        "ZIP code",
        validate_zip_code(zip_code)
    )

    # Test the functions using valid and invalid examples.
    run_tests()


# Start the program.
if __name__ == "__main__":
    main()