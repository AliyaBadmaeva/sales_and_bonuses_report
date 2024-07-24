# A task in Python for working with lists, dictionaries, tuples

> [!IMPORTANT]
> This is an interesting task that was used to select for an internship at one of the companies.

## The task

It is necessary to write a program in Python that generates a report on the average salary for employees for 2020. Also attached to the task are the data for completing it.
The following files in different formats are attached to the task:

•	emails.gzip

•	salary.csv

•	employess_dict.txt

The enterprise has a database in which information about employees' salaries is stored. The database consists of the following tables:

Table_1: 

Employees(

ID int, -- Employee’s ID 

NAME1 str, -- Employee's surname

NAME2 str, -- Employee's name

NAME3 str -- Employee's partonomic
)

Table_2: 

Salary(
ID int, -- Employee’s ID

dt date, -- Payment date

Salary_Type str, -- Amount type (salary, bonus)

Amount double – paid amount
)
 
Table_3: 

Emails(
ID int, -- ID Email

Empl_ID int, -- Employee’s ID

Email str -- Email address
)

#### Conditions:
1. The report must contain the columns Empl_ID, Surname_name_patronym, Salary, Bonus, Email and correspond to the data presented in the “Expected report result” section

2. Average values for Salary and Bonus are calculated separately

3. If an employee has several emails, the report should contain separate lines for each email

4. The report should NOT contain duplicate rows

#### Additionally:

1. Output is produced through the print function

2. To generate a report, you need to take maximum advantage of the main types of Python collections (list, dict, tuple), without using pandas

An example of a line in the expected format of a report result:
1, Shershukov Viktor Kuzmich, 51750.0, 9583.333333333334, shershuko@mail.ru.


> [!NOTE]
> To run the program correctly, the user needs to install packages from the “requirements.txt” file; this can be done on the command line by going to the folder with the “requirements.txt” file and typing the command “pip install -r requirements.txt”.

