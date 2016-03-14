'''
This script populates the database from a csv file.
With the following columns:
user	story	chapter	ts	install_date	device_type	read_date
'''
import csv
from models.read import Read
from datetime import datetime
from mongoengine import connect

connect('pocketgems')

def load(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader, None)  # skip the headers
        for row in reader:
            user_id = int(row[0])
            title = row[1].replace('.','-')
            chapter = int(row[2])
            timestamp = datetime.strptime(row[3], "%m/%d/%Y %H:%M")
            install_date = datetime.strptime(row[4], "%m/%d/%Y")
            device_type = row[5]
            read_date = datetime.strptime(row[6], "%m/%d/%Y")

            create_read(user_id, title, chapter, timestamp, device_type)
    print('Read collection successfully populated.')

def create_read(user_id, title, chapter, timestamp, device_type):
    read = Read()
    read.user_id = user_id
    read.story_title = title
    read.chapter = chapter
    read.timestamp = timestamp
    read.device_type = device_type
    read.save()

if __name__ == '__main__':
    load('data/Data_Science_Homework.csv')
