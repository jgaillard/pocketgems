'''
This script populates the database from a csv file.
With the following columns:
User	Install_Date	Device_Type

'''
import csv
from models.user import User
from datetime import datetime
from mongoengine import connect

connect('pocketgems')

def load(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader, None)  # skip the headers
        for row in reader:
            user_id = int(row[0])
            install_date = datetime.strptime(row[1], "%m/%d/%Y")
            device_type = row[2]

            create_user(user_id, install_date, device_type)

    print('User collection successfully populated.')

def create_user(user_id, install_date, device_type):
    user = User()
    user.user_id = user_id
    user.install_date = install_date
    user.device_type = device_type
    user.save()

if __name__ == '__main__':
    load('data/Data_Science_HW_Users.csv')
