from datetime import datetime, timedelta

#-----
#Account Detials
#-----
account_type = "Savings" #Savings/Current
available_balance = 100000
daily_total = 200000
daily_transaction_count = 5

#---
# Beneficiary details
# ----
beneficiary_verified = True
beneficiary_active = True

#Beneficiary added 5 hours ago
beneficiary_added_time=datetime.now() - timedelta(hours=5)

#------
# OTP Details
# -----
otp_entered = True
otp_generated_time = datetime.now() - timedelta(minutes=3)


# -----
# Transfer Request
#  -----

transfer_amount = 6000

# -----
# function to calculate charges
# ----

def calculate_charges(amount):
    if amount<= 1000:
        return 5
    elif amount <= 10000:
        return 10
    elif amount <= 100000:
        return 15
    else:
        return 25
    
# ------
# function to check minimum available_balance
# ----

def minimum_balance(account_type):
    if account_type == "Savings":
        return 10000
    else:
        return 25000
    

# ------
# Main Validation function
# ------

def validate_transfer():

    #Rule 1: Transfer amount validation
    if transfer_amount < 1:
        return "Transfer Failed: Minimum amount is ₹1"  

    if transfer_amount > 200000:
        return "Transfer failed: Maximum transfer limit is ₹ 200000"

    #Rule 2: Daily limit validation
    if daily_total + transfer_amount > 500000:
        return "Transfer failed: Daily transfer limit exceeded"
    
    #Rule 3: Transaction count validation
    if daily_transaction_count >= 10:
        return "Transfer failed: Maximum 10 transactions allowed per day"
    
    #Rule 4: Beneficiary validation
    if not beneficiary_active:
        return "Transfer failed: Beneficary is inactive"
    
    if not beneficiary_verified:
        return "Transfer failed: Beneficary is not verified"
    
    #Rule 5: Cooling period validation

    cooling_period = datetime.now() - beneficiary_added_time

    if cooling_period.total_seconds() < 4 * 60 * 60:
        return "Transfer Failed: Beneficiary cooling period active"
    
    # Rule 6: Charges Calcultation
    charges = calculate_charges(transfer_amount)

    total_deduction = transfer_amount + charges

    # Rule 7: Minimum Balance Validation
    min_balance = minimum_balance(account_type)

    remaining_balance = available_balance - total_deduction

    if remaining_balance < min_balance:
        return "Transfer failed: Minimum balance is not maintained"
    
    # Rule 8: OTP Validation
    if transfer_amount > 5000:

        if not otp_entered:
            return "Transfer Failed: OTP required"
        
        otp_age = datetime.now() - otp_generated_time

        if otp_age.total_seconds() > 5 * 60:
            return "Transfer Failed: OTP Expired"
        
    #Success
    return f"""
    Transfer Successful
    Transfer Amount : ₹{transfer_amount}
    Charges         :₹{charges}
    Total Deducted  :₹{total_deduction}
    Remaining Balance : ₹{remaining_balance}
    """
# -------
# Execute transfer
# -----

result = validate_transfer()
print(result)



    