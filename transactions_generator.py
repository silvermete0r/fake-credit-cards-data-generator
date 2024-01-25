from faker import Faker
import json
from datetime import datetime

fake = Faker()

def generate_fake_transaction():
    transaction_id = fake.uuid4()
    amount = fake.random.uniform(1.0, 1000.0)
    date = fake.date_between(start_date='-1y', end_date='today').strftime('%d/%m/%Y')
    merchant = fake.company()
    
    card_id = fake.uuid4()
    card_number = fake.credit_card_number(card_type='mastercard')
    card_holder_name = fake.name()
    expiry_date = fake.credit_card_expire()
    cvv = fake.credit_card_security_code(card_type='mastercard')
    
    transaction = {
        "TransactionID": transaction_id,
        "Amount": round(amount, 2),
        "Date": date,
        "Merchant": merchant,
        "Card": {
            "CardID": card_id,
            "CardNumber": card_number,
            "CardHolderName": card_holder_name,
            "ExpiryDate": expiry_date,
            "CVV": cvv
        }
    }
    
    return transaction

def generate_fake_data(num_records):
    fake_data = [generate_fake_transaction() for _ in range(num_records)]
    return fake_data

if __name__ == "__main__":
    num_records = 1001
    fake_data_list = generate_fake_data(num_records)

    with open("data/Transactions.json", "w") as json_file:
        json.dump(fake_data_list, json_file, indent=4)

    print("Data saved to Transactions.json.")
