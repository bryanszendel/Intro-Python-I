"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime, date

if len(sys.argv) > 3:
  print("include only month [01], and year [2020] in your command")
  
today = date.today()
print(today)

if len(sys.argv) > 1:
  cur_month = int(sys.argv[1])
else: 
  cur_month = int(today.month)

if len(sys.argv) > 2:
  cur_year = int(sys.argv[2])
else:
  cur_year = int(today.year)

new_cal = calendar.TextCalendar()
print(new_cal.formatmonth(cur_year, cur_month, w=3))