# Words Per Day Calculator Script
# By: Maureen Davey (http://www.maureenldavey.com)
# This is a basic Python script meant to calculate how many words you have left to meet your word count goal in a specified amount of time.

from datetime import datetime
from dateutil.relativedelta import relativedelta

import math

def __format_datetime(string):
	return datetime.strptime(string, "%m/%d/%Y %H:%M:%S")

def __check_numeric(string):
	try:
		float(string)
		return True
	except ValueError:
		return False

print "Welcome to the Words Per Day Calculator Script."

print "---------------------------------------------------------------"

print "Please answer a few questions about your project, and we will calculate your remaining words per day needed to meet your goal."

method = raw_input("Would you like to calculate the number of words needed per day to meet a specific end date, or calculate what the end date would be if you wrote X number of words per day?  Enter A for the first option, B for the second. ")

if method == "A":
	start_date = raw_input("What is the starting date for your writing project?  It can be any past, present, or future date.  (Please answer in the format mm/dd/yyyy, where the year is four digits.) ")
	while(len(start_date) == 0):
		print "Sorry, no input was detected.  Please try again."
		start_date = raw_input("What is the starting date for your writing project?  It can be any past, present, or future date.  (Please answer in the format mm/dd/yyyy, where the year is four digits.) ")
	start_date_full = start_date + " 00:00:00"

	end_date = raw_input("What is the ending date/deadline for your writing project?  This date will be included in the days remaining. (Please answer in the format mm/dd/yyyy, where the year is four digits.) ")
	while(len(end_date) == 0):
		print "Sorry, no input was detected.  Please try again."
		end_date = raw_input("What is the ending date/deadline for your writing project?  This date will be included in the days remaining. (Please answer in the format mm/dd/yyyy, where the year is four digits.) ")
	end_date_full = end_date + " 23:59:59"

	words_total = raw_input("What is the total number of words you need to complete within that timeframe? Just enter the number, no commas (i.e. 50000 for fifty thousand). ")
	while(__check_numeric(words_total) == False):
		print "Sorry, that did not appear to be a number.  Please try again."
		words_total = raw_input("What is the total number of words you need to complete within that timeframe? Just enter the number, no commas (i.e. 50000 for fifty thousand). ")

	words_so_far = raw_input("Have you written any words so far that should be included in the total? Just enter the number, no commas.  (If you are not including any words already written, just enter 0). ")
	while(__check_numeric(words_so_far) == False):
		print "Sorry, that did not appear to be a number.  Please try again."
		words_total = raw_input("What is the total number of words you need to complete within that timeframe? Just enter the number, no commas (i.e. 50000 for fifty thousand). ")

	now = datetime.now()
	today_date = "%s/%s/%s" % (now.month, now.day, now.year)
	today_full = today_date + " %s:%s:%s" % (now.hour, now.minute, now.second)

	#Find out if the timeline has started yet
	delta_until_start = __format_datetime(start_date_full) - __format_datetime(today_full)
	days_until_start = delta_until_start.days

	#Find length of the project timeframe
	delta_project_timeframe = __format_datetime(end_date_full) - __format_datetime(start_date_full)
	project_length_days = delta_project_timeframe.days + 1

	#Calculate info for this user
	words_remaining = int(words_total) - int(words_so_far)

	if days_until_start > 0:
		days_remaining = project_length_days
		print "Your timeline does not begin for another %s days.  We will use the full number of days between your start date and end date, %s, to calculate your needed words per day." % (days_until_start, project_length_days)
		words_per_day = int(math.ceil(float(words_remaining) / project_length_days)) #Must cast at least one value as a float to get 'true' division in Python 2 (versus floor division)
		print "Including your start and end dates, you will need to write at least %s words per day to meet your goal of %s words by the end of %s." % (words_per_day, words_total, end_date)
	else:
		days_remaining_delta = __format_datetime(end_date_full) - __format_datetime(today_full)
		days_remaining = days_remaining_delta.days
		include_today = raw_input("Do you want to include today in your calculations? Answer with Y for yes or N for no. ")
		if include_today == "Y":
			days_remaining = days_remaining + 1
			include_today_phrase = "including today"
		else:
			include_today_phrase = "not including today"
		print "Today is %s, so you have %s days left before your deadline (%s)." % (today_date, days_remaining, include_today_phrase)
		words_per_day = int(math.ceil(float(words_remaining) / days_remaining)) #Must cast at least one value as a float to get 'true' division in Python 2 (versus floor division)
		print "Including your deadline day, you will need to write at least %s words per day to meet your goal (%s) of %s words by the end of %s." % (words_per_day, include_today_phrase, words_total, end_date)
	print "---------------------------------------------------------------"
	print "You have %s words and %s days remaining.  Good luck!" % (words_remaining, days_remaining)
	print "---------------------------------------------------------------"
elif method == "B":
	start_date = raw_input("What is the starting date for your writing project?  It can be any past, present, or future date.  (Please answer in the format mm/dd/yyyy, where the year is four digits.) ")
	while(len(start_date) == 0):
		print "Sorry, no input was detected.  Please try again."
		start_date = raw_input("What is the starting date for your writing project?  It can be any past, present, or future date.  (Please answer in the format mm/dd/yyyy, where the year is four digits.) ")
	start_date_full = start_date + " 00:00:00"

	goal_wpd = raw_input("How many words per day do you plan to write? ")
	while(__check_numeric(goal_wpd) == 0):
		print "Sorry, that did not appear to be a number.  Please try again."
		goal_wpd = raw_input("How many words per day do you plan to write? ")

	goal_total = raw_input("What is the total number of words you plan to write? Just enter the number, no commas (i.e. 50000 for fifty thousand). ")
	while(__check_numeric(goal_total) == 0):
		print "Sorry, that did not appear to be a number.  Please try again."
		goal_total = raw_input("What is the total number of words you plan to write? Just enter the number, no commas (i.e. 50000 for fifty thousand). ")

	words_so_far = raw_input("Have you written any words so far that should be subtracted from your total? Just enter the number, no commas.  (If you are not including any words already written, just enter 0). ")
	while(__check_numeric(words_so_far) == False):
		print "Sorry, that did not appear to be a number.  Please try again."
		words_so_far = raw_input("Have you written any words so far that should be subtracted from your total? Just enter the number, no commas.  (If you are not including any words already written, just enter 0). ")

	#Factor any already written words into the remaining total
	#If the user enters 0, then remaining_words is just equal to goal_total
	remaining_words = int(goal_total) - int(words_so_far)

	#Calculate number of days needed to meet this goal
	days_needed = int(math.ceil(float(remaining_words) / int(goal_wpd))) #Must cast at least one value as a float to get 'true' division in Python 2 (versus floor division)

	#Find end date using relativedelta and convert to mm/dd/YYYY format
	end_date = (__format_datetime(start_date_full) + relativedelta(days=+days_needed)).strftime("%m/%d/%Y")

	print "---------------------------------------------------------------"
	print "If you write %s words per day, including your start date, you will reach %s words on %s.  It will take %s days to reach your goal total." % (goal_wpd, goal_total, end_date, days_needed)
	print "You have %s words remaining.  Good luck!" % (remaining_words)
	print "---------------------------------------------------------------"
