# Words Per Day Calculator Script
# By: Maureen Davey (http://www.maureenldavey.com)
# This is a basic Python script meant to calculate how many words you have left to meet your word count goal in a specified amount of time.

from datetime import datetime
import math

def __format_datetime(string):
	return datetime.strptime(string, "%m/%d/%Y %H:%M:%S")

print "Welcome to the Words Per Day Calculator Script."

print "---------------------------------------------------------------"

print "Please answer a few questions about your project, and we will calculate your remaining words per day needed to meet your goal."

start_date = raw_input("What is the starting date for your writing project? It can be today, but it can also be a past or future date. (Please answer in the format m/d/yyyy, where the year is four digits.) ")
start_date_full = start_date + " 00:00:01"
end_date = raw_input("What is the ending date/deadline? (Please answer in the format m/d/yyyy, where the year is four digits.) ")
end_date_full = end_date + " 23:59:59"
words_total = raw_input("What is the total number of words you need to complete within that timeframe? ")
words_so_far = raw_input("Have you written any words so far that should be included in the total? (If not, just enter 0). ")
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