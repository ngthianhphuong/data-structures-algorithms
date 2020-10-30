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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# np array containing all calling, answering numbers
calling = np.array(calls)[:, 0]
answering = np.array(calls)[:, 1]

# np array containing all numbers that send and receive texts
send_texts = np.array(texts)[:, 0]
receive_texts = np.array(texts)[:, 1]

# take the elements that are in calling and not are in answering, send_texts and receive_texts
telemarketers = np.setdiff1d(np.setdiff1d(np.setdiff1d(calling, answering), send_texts), receive_texts)

# remove true telemarketer numbers
possible_telemarketers = [number for number in list(telemarketers) if extract_code(number) != "140"]

for number in sorted(possible_telemarketers):
    print(number, '\n')
