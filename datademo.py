'''
import csv
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
'''
import pandas as pd

df = pd.read_csv('data.csv')

print(df.to_string())
