'''
This script populates the database from a csv file.
With the following columns:
User	Install_Date	Device_Type

'''
import csv
from models.story import Story
from datetime import datetime
from mongoengine import connect

connect('pocketgems')

def load(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            title = row[1].replace('.','-')
            number_of_reads = int(row[0])
            create_story(title, number_of_reads)

    print('Story collection successfully populated.')

def create_story(title, number_of_reads):
    story = Story()
    story.title = title
    story.number_of_reads = number_of_reads
    story.save()

if __name__ == '__main__':
    load('data/Data_Science_HW_Stories.csv')
