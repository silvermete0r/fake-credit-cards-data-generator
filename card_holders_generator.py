from faker import Faker
import json
from datetime import datetime, timedelta
import random

fake = Faker()

def generate_fake_transaction():
    transaction_id = fake.uuid4()
    amount = fake.random.uniform(1.0, 500.0)
    date = datetime.utcnow().isoformat()
    merchant = fake.company()
    
    return {
        "TransactionID": transaction_id,
        "Amount": round(amount, 2),
        "Date": date,
        "Merchant": merchant
    }

def generate_fake_credit_card():
    card_id = fake.uuid4()
    card_number = fake.credit_card_number(card_type='mastercard')
    card_holder_name = fake.name()
    expiry_date = fake.credit_card_expire()
    cvv = fake.credit_card_security_code(card_type='mastercard')
    
    transactions = [generate_fake_transaction() for _ in range(random.randint(1, 5))]
    
    return {
        "CardID": card_id,
        "CardNumber": card_number,
        "CardHolderName": card_holder_name,
        "ExpiryDate": expiry_date,
        "CVV": cvv,
        "Transactions": transactions
    }

def generate_fake_cardholder():
    user_id = fake.uuid4()
    username = fake.user_name()
    password = "hashedPassword" + str(fake.random_int(100, 999))
    email = fake.email()
    
    credit_cards = [generate_fake_credit_card() for _ in range(random.randint(1, 3))]
    
    return {
        "UserID": user_id,
        "Username": username,
        "Password": password,
        "Email": email,
        "CreditCards": credit_cards
    }

def generate_fake_data(num_records):
    fake_data = [generate_fake_cardholder() for _ in range(num_records)]
    return fake_data

if __name__ == "__main__":
    num_records = 1000
    fake_data_list = generate_fake_data(num_records)

    with open("data/CardHolders.json", "w") as json_file:
        json.dump(fake_data_list, json_file, indent=2)

    print("Data saved to CardHolders.json.")