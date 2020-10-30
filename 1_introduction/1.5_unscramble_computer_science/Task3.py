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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.
"""
# for each call, verify if calling number is in Bangalore
# extract code
# 3 cases: fixed nb, phone nb & telemarketer nb

# helper function: extract code


def extract_code(number):
    """Helper function:
        Returns the code for fixed number, prefix for mobile number and 140 for telemarketers's number.
        Input: number is a string.
        Output: code is a string.
        """
    if "(" in number:
        return number.split(")")[0].strip("(")
    elif " " in number:
        return number[:4]
    else:
        return number[:3]

# test extract_code function
"""
for text in texts[:10]:
    print(extract_code(text[0]))
    
print('\n')

for call in calls[-10:]:
    print(extract_code(call[1]))
"""

def find_calls_from_bangalore():
    code_list = set()
    for call in calls:
        # check whether the call is from Bangalore
        if extract_code(call[0]) == "080":
            code_list.add(extract_code(call[1]))
    for code in sorted(list(code_list)):
        print(code, '\n')

print("The numbers called by people in Bangalore have codes: ")
find_calls_from_bangalore()



"""
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# for each call, verify if calling number is in Bangalore: increment total call by 1
# verify if answering number is in Bangalore: increment by 1

def bangalore_calls_percentage():
    total_bangalore_calls = 0
    bangalore_to_bangalore_calls = 0
    for call in calls:
        if extract_code(call[0]) == "080":
            total_bangalore_calls += 1
            if extract_code(call[1]) == "080":
                bangalore_to_bangalore_calls += 1
    return bangalore_to_bangalore_calls/total_bangalore_calls*100

print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(bangalore_calls_percentage()))