Words Per Day Calculator Script
---------------------------------------------------------------
By: Maureen Davey (http://www.maureenldavey.com)

This is a basic Python script meant to calculate how many words you have left to meet your word count goal in a specified amount of time.

Input your start date, end date, total words required, and any words you've done so far.  If you're already past your start date or your start date is today, the script will also ask if you want to include today in your calculations.  It will calculate your remaining words per day and tell you how many days you have left until your deadline.

The script verifies that you did not leave any inputs blank, and that your current total so far and total required are numbers.

Please re-use/modify this script to meet your needs.  And of course, keep on writing!


Installation Instructions
---------------------------------------------------------------

* Confirm Python is installed on your system
* Download the script
* Run the script from the terminal: python wpd-calculator.py


To Do
---------------------------------------------------------------
* Confirm dates are inputted in the proper format (i.e. m/d/YYYY)
* Throw an error if your end date is before your start date or the dates don't logically make sense
* Be able to calculate additional stats, like an average WPD count to date, or if the end date is already past, if you met your goal and how much you were over/under