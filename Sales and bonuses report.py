import pandas as pd
import csv
'''
To run the program correctly, the user needs to install packages from the “requirements.txt” file; 
this can be done on the command line by going to the folder with the “requirements.txt” file and typing 
the command “pip install -r requirements.txt”.
'''

df = pd.read_parquet('emails.gzip', engine='fastparquet')
df.to_csv('emails.csv')


with open('emails.csv', 'r') as emails:  # look at the contents
    e = csv.reader(emails)
    for row in e:
        print(row)


with open("emails.csv", newline='') as source, open("emails1.csv", "w", newline='') as dest:
    reader = csv.reader(source)
    writer = csv.writer(dest, delimiter=",", lineterminator="\r\n")
    for line, row in enumerate(reader, 1):
        writer.writerow(row[2:])  # the first two columns are superfluous, let's write the third column to a new file


def delete_duplicates(ad):  # clear the list of duplicates using the function
    li = []  # empty list
    for i in ad:  # loop for sorting duplicates
        if i not in li:
            li.append(i)
    # returns a list with nested lists
    return li


with open("emails1.csv") as f,   open("email.csv", "w", newline='') as dest1:
    writer1 = csv.writer(dest1, delimiter=",", lineterminator="\r\n")  # for recording
    csvreader = csv.reader(f)  # for reading
    for row in delete_duplicates(csvreader):
        writer1.writerow(row)  # write to a new file


with open("email.csv",) as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        print(row)  # Let's print it to see what happens

with open("employess_dict.txt", encoding="utf-8") as file:
    csvreader = csv.reader(file)
    print(file.read())  # look at the contents

with open('salary.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print(row)  # print to see bonuses and salaries

def filter_values(af):  # function for filtering lists
    sp = []
    for i in range(len(af)):
        sp.append(af[i][3])  # we only need column 3, do not forget that numbering starts from 0
    # call the function to calculate the arithmetic average and return this value
    return count_s(sp)


def count_s(ar):  # function for calculating the arithmetic mean
    for i, item in enumerate(ar):
        ar[i] = float(item)  # Let's convert all the necessary salaries and bonuses into float, anyway after division it will be float
    for i in range(len(ar)):
        if len(ar) == 0:
            return 0  # to avoid division by zero
        else:
            return sum(ar) / len(ar)  # arithmetic average - add up all salaries and divide by the number of salaries
            # the same goes for bonuses


with open("salary.csv", newline='') as source, open("avg_sal_2020.csv", "w", newline='') as dest1, \
        open("avg_bon_2020.csv", "w", newline='') as dest2:
    writer1 = csv.writer(dest1, delimiter=",", lineterminator="\r\n")
    writer2 = csv.writer(dest2, delimiter=",", lineterminator="\r\n")
    a = [line.strip().split(';') for line in source.readlines()]
    # filter the data into lists by employee IDs, dates and type of payments for each possible option
    s1 = list(filter(lambda x: x[0] == '1' and ('2019-12-31' < x[1] < '2021-01-01') and x[2] == 'salary', a))
    s2 = list(filter(lambda x: x[0] == '2' and ('2019-12-31' < x[1] < '2021-01-01') and x[2] == 'salary', a))
    s3 = list(filter(lambda x: x[0] == '3' and ('2019-12-31' < x[1] < '2021-01-01') and x[2] == 'salary', a))
    s4 = list(filter(lambda x: x[0] == '4' and ('2019-12-31' < x[1] < '2021-01-01') and x[2] == 'salary', a))
    b1 = list(filter(lambda x: x[0] == '1' and ('2019-12-31' < x[1] < '2021-01-01') and x[2] == 'bonus', a))
    b2 = list(filter(lambda x: x[0] == '2' and ('2019-12-31' < x[1] < '2021-01-01') and x[2] == 'bonus', a))
    b3 = list(filter(lambda x: x[0] == '3' and ('2019-12-31' < x[1] < '2021-01-01') and x[2] == 'bonus', a))
    b4 = list(filter(lambda x: x[0] == '4' and ('2019-12-31' < x[1] < '2021-01-01') and x[2] == 'bonus', a))
    # create a tuple of tuples, where the 2nd value of the nested tuple is obtained by calling a function
    # to calculate the arithmetic mean and filtering the required column
    s = (('Empl_ID', 'Avg_salary'), (1, filter_values(s1)), (2, filter_values(s2)),
         (3, filter_values(s3)), (4, filter_values(s4)))
    b = (('Empl_ID', 'Avg_bonus'), (1, filter_values(b1)), (2, filter_values(b2)),
         (3, filter_values(b3)), (4, filter_values(b4)))
    writer1.writerows(s)  # record salaries for employees
    writer2.writerows(b)  # the same for bonuses, but in the second file


def rep_str(sp_st):  # function to remove unnecessary elements in a string
    st = ''
    r = ['1', '2', '3', '4', ",", ")", "(", "'"]  # a list of what we will not write in a new line
    for m in sp_st:
        if m in r:
            continue
        else:
            st += m  # write it to a line if it is not found in the list r
    # skip the space at the beginning of the line
    return st[1:]  # return value - cleared string with last name, first name and patronymic


with open("employess_dict.txt", encoding="utf-8", newline='') as source, open("fio.csv", "w", newline='') as dest1:
    writer1 = csv.writer(dest1, delimiter=",", lineterminator="\r\n")
    a = [line.strip() for line in source.readlines()]
    # write to a list of tuples, with two values in each tuple - a number and a string cleared by the function
    a1 = [('Empl_ID', 'FIO'), (1, rep_str(a[1])), (2, rep_str(a[2])), (3, rep_str(a[3])), (4, rep_str(a[4]))]
    writer1.writerows(a1)  # write it to a file


# open all the necessary files and create a file (or open it if it exists) to (re)write the data needed for the report
with open("fio.csv") as f, open("avg_sal_2020.csv") as sal, open("avg_bon_2020.csv") as bon, \
        open("email.csv") as email, open("report.csv", "w", newline='') as dest1:
    columns = ["Empl_ID", "Surname_name_patronym", "Salary", "Bonus", "Email"]  # column names
    writer1 = csv.DictWriter(dest1, fieldnames=columns)  # to write to a new file
    writer1.writeheader()  # let's title the table
    # read all the necessary files
    f1 = [line.strip().split(',') for line in f.readlines()]
    sal1 = [line.strip().split(',') for line in sal.readlines()]
    emails = [line.strip().split(',') for line in email.readlines()]
    bon1 = [line.strip().split(',') for line in bon.readlines()]
    # below * for unpacking, otherwise each value will be written in a separate list in the dictionary
    fi1, fi2, fi3, fi4 = *f1[1][1:], *f1[2][1:], *f1[3][1:], *f1[4][1:]
    # Variables with an asterisk cannot be entered into the dictionary, so separate variables were created
    s1, s2, s3, s4 = *sal1[1][1:], *sal1[2][1:], *sal1[3][1:], *sal1[4][1:]
    b1, b2, b3, b4 = *bon1[1][1:], *bon1[2][1:], 0, *bon1[4][1:]
    e1, ea1, e2, e3, e4 = *emails[1][1:], *emails[2][1:], *emails[3][1:], *emails[4][1:], ""
    # Let's create a list with dictionaries, where the key will be the name of the columns
    users = [
        {"Empl_ID": 1, "Surname_name_patronym": fi1, "Salary": s1, "Bonus": b1, "Email": e1},
        {"Empl_ID": 1, "Surname_name_patronym": fi1, "Salary": s1, "Bonus": b1, "Email": ea1},
        {"Empl_ID": 2, "Surname_name_patronym": fi2, "Salary": s2, "Bonus": b2, "Email": e2},
        {"Empl_ID": 3, "Surname_name_patronym": fi3, "Salary": s3, "Bonus": b3, "Email": e3},
        {"Empl_ID": 4, "Surname_name_patronym": fi4, "Salary": s4, "Bonus": b4, "Email": e4}]
    writer1.writerows(users)  # we will record everything in a report file


def clean_for_print(spis):  # function for clearing a list of elements - empty lines
    a2 = []  # let's create an empty list into which we will nest lists cleared of empty lines
    for line in spis:  # for a nested list, if we consider a list with lists in the form of a matrix, then this is a string
        a_1 = []
        for row in line:  # for a column (if viewed as a matrix) or nested list element
            if row == "":  # if there is an element as an empty string
                continue  # we're skipping it
            else:  # otherwise we write the element to the list a_1
                a_1.append(row)
        a2.append(a_1)  # after finishing in the list of elements, insert the cleared list into list a2
    return a2  # return a list of lists, ready for printing and cleared of empty lines



with open("report.csv",) as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        print(row)  # Let's print it to see what happens
# Recorded as needed


with open("report.csv",) as file:
    a = [line.strip().split(',') for line in file.readlines()]
    '''
    we will clear the lists of extra empty lines so that when printing there are no double commas where there are 
    empty lines instead of values
    '''
    # we pass the list of lists “a” to the function for clearing, and then print it line by line
    for line in clean_for_print(a):  # for line printing
        print(*line, sep=", ")  # print with unpacking and delimiter in the form of a comma and a space
