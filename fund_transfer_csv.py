import csv
from datetime import datetime, timedelta

# Function to calculate charges

def calculate_charges(amount):

    if amount<= 1000:
        return 5

    elif amount<= 10000:
        return 10
    elif amount <= 100000:
        return 15
    else:
        return 25
    
# Function for minimum balance

def minimum_balance(account_type):

    if account_type == "Savings":
        return 10000
    
    else:
        return 25000
    
# Validation function

def validate_transfer(data):

    account_type = data["account_type"]
    available_balance = int(data["available_balance"].strip())
    daily_total = int(data["daily_total"].strip())
    daily_transaction_count = int(data["daily_transaction_count"].strip())

    beneficiary_verified = data["beneficiary_verified"].strip().lower() == "true"
    beneficiary_active = data["beneficiary_active"].strip().lower() == "true"

    transfer_amount = int(data["transfer_amount"].strip())
    transfer_amount = int(data["transfer_amount"].strip())

    otp_entered = data["otp_entered"].strip().lower() == "true"

    otp_minutes = int(data["otp_minutes"].strip())

    charges = calculate_charges(transfer_amount)

    # Transfer limit validation
    if transfer_amount < 1:
        return "Failed : Minimum transfer amount is ₹1"

    if transfer_amount > 200000:
        return "Failed : Maximum transfer limit exceeded"

    # Daily limit validation
    if daily_total + transfer_amount > 500000:
        return "Failed : Daily transfer limit exceeded"

    # Transaction count validation
    if daily_transaction_count > 10:
        return "Failed : Maximum 10 transactions allowed"

    # Beneficiary validation
    if not beneficiary_active:
        return "Failed : Beneficiary inactive"

    if not beneficiary_verified:
        return "Failed : Beneficiary not verified"

    # Balance validation
    total_deduction = transfer_amount + charges

    remaining_balance = available_balance - total_deduction

    min_balance = minimum_balance(account_type)

    if remaining_balance < min_balance:
        return "Failed : Minimum balance violation"

    # OTP validation
    if transfer_amount > 5000:

        if not otp_entered:
            return "Failed : OTP required"

        otp_generated_time = datetime.now() - timedelta(minutes=otp_minutes)

        otp_age = datetime.now() - otp_generated_time

        if otp_age.total_seconds() > 5 * 60:
            return "Failed : OTP expired"

    return f"""
    SUCCESS
    Transfer Amount : ₹{transfer_amount}
    Charges         : ₹{charges}
    Total Deducted  : ₹{total_deduction}
    Remaining Balance : ₹{remaining_balance}
    """


# ----------------------------------------
# Read CSV File
# ----------------------------------------
with open("transfer_data.csv", mode="r") as file:

    csv_reader = csv.DictReader(file)

    for row in csv_reader:

        print("-----------------------------------")
        print(validate_transfer(row))
