import csv
import random
import os
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

def generate_transaction_data(num_records):
    data = []
    for _ in range(num_records):
        customer_id = fake.uuid4()
        name = fake.name()
        debit_card_number = fake.credit_card_number(card_type=None)
        debit_card_type = fake.credit_card_provider(card_type=None)
        bank_name = fake.company()
        transaction_date = fake.date_time_between(start_date = "-1y", end_date = "now")
        amount_spend = round(random.uniform(10,1000),2)
        data.append([customer_id,name,debit_card_number,debit_card_type,bank_name,transaction_date,amount_spend])
        
    return data

def write_to_csv(data,filename):
    with open(filename,'w',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['customer_id','name','debit_card_number','debit_card_type','bank_name','transaction_date','amount_spend'])
        writer.writerows(data)

def main():
    num_records = 10
    num_days = 40
    output_folder = "transaction_data"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    start_date = datetime.now().date() - timedelta(days = num_days - 1)

    for i in range(num_days):
        date = start_date + timedelta(days = i)
        data = generate_transaction_data(num_records)
        filename = os.path.join(output_folder,f"transactions_{date.strftime('%Y-%m-%d')}.csv")
        write_to_csv(data,filename)
        print(f"data generated for {data} : {filename}")

if __name__ == "__main__":
    main()

