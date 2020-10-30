"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

unique_phone_numbers = set()

for text in texts:
    unique_phone_numbers.update([text[0], text[1]])
                             
for call in calls:
    unique_phone_numbers.update([call[0], call[1]])
                                
print("There are {} different telephone numbers in the records.".format(len(unique_phone_numbers)))


"""
import numpy as np

union = np.union1d(np.array(texts)[:, :2], np.array(calls)[:, :2])

print("There are {} different telephone numbers in the records.".format(len(set(union))))
"""