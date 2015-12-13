Words Per Day Calculator Script
---------------------------------------------------------------
By: Maureen Davey (http://www.maureenldavey.com)

This is a basic Python script meant to calculate word goal counts and target end dates for writing projects.

To calculate your needed words per day to meet a deadline:

Input your start date, end date, total words required, and any words you've done so far.  If you're already past your start date or your start date is today, the script will also ask if you want to include today in your calculations.  It will calculate your remaining words per day and tell you how many days you have left until your deadline.

Alternatively, you can enter the number of words per day you're aiming to write, along with your required total, and the script will calculate what your end date will be.

The script verifies that you did not leave any inputs blank, and that numeric variables are in fact numbers.  If you are already partway through a project, you can also enter the number of words you've already written.

This script is open source, please re-use/modify this script to meet your needs.  And of course, keep on writing!

Note: This script was written for Python 2.x.  It may not work with Python 3 and above.


Installation Instructions
---------------------------------------------------------------

* Confirm Python is installed on your system.  Opening your terminal and entering `python -V` should give you a version number if it is installed
* Download the script
* Run the script from the terminal:
```python
python wpd-calculator.py```

This script also requires the python-dateutil module (http://labix.org/python-dateutil for Python < 3.0, newer versions here https://github.com/dateutil/dateutil) to be installed.  The python-dateutil module was written by Gustavo Niemeyer.


To Do
---------------------------------------------------------------
* Confirm dates are inputted in the proper format (i.e. m/d/Y)
* Throw an error if your end date is before your start date or the dates don't logically make sense
* Be able to calculate additional stats, like an average WPD count to date, or if the end date is already past, if you met your goal and how much you were over/under
* Test/update for newer versions of Python
