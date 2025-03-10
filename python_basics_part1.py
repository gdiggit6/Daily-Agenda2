#!/bin/python3
#!/usr/bin/env python
#-*- coding: utf-8 -*-

#	alias a='python /home/dbustaflexitlap/Python/sf_Python/dailyAgenda.py'
#	alias a='python dailyAgenda.py names, tofile'
#--------------------------------------------------------------------------------------------------------
#	alias m='python daily_mirror.py names, tofilel'
#	alias n='python nested_lists.py names, tofile'
#	alias z='python z.py names, tofile'
#	alias e='python e.py names, tofile's
#	alias g='python g.py names, tofile'
#	alias i='python dictionaries.py names, tofile'
#	alias l='python lists.py names, tofile'
#	alias s='python sets.py names, tofile'
#	alias t='python tuples.py names, tofile'

#-----------------------copy from virtual OS to host------------------------
#	cp -ruv /home/dflexjasmin/Python/Python/sf_Python/ /media/sf_Python/

#-----------------------copy from host to virtual OS------------------------
#	mv /media/sf_Python/Python/sf_Python/manipura_rosewood.PNG /home/dbustaflex666/Pictures/Rounds/; chmod 777 /home/dbustaflex666/Pictures/ -R; chown dbustaflex666 /home/dbustaflex666/Pictures/ -R; chgrp dbustaflex666 /home/dbustaflex666/Pictures/ -R

#	grep -r 'phrase' /home/dflexjasmin/Python/Python/sf_Python/
#       grep -r --exclude-from=b_dic.py [ 'phrase' ] /home/dflexjasmin/Python/
#--------------------------------------------------------------------------------------------------------
#	12!!#8FG
# 	#&x9$g!JeV65VQAp
#       PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
from sys import argv
import datetime
#script, names, tofile = argv
#--------------------------------------------------------------------------------------------------------
def space ( ) :
	print ( '\n' )	
#--------------------------------------------------------------------------------------------------------
space ( )
import random
'''
answer = input ( 'What is your height in centimeters? ' )
if int ( answer ) > 185 :
	print ( 'You are very tall' )
else :
	print ( 'You are not very tall' )
space ( )
#-------------------------------------------------------------------------
current_age = int ( input ( 'What is your age? ' ) )
for i in range ( 2, 6 ) :
	print ( 'In', i, 'years, you will be', current_age + i, 'years old!' )

#------------------------------------------------------------------------------------------------------------

space ( )
user_input = input ( 'Please provide a password: 	' )
digit_count = 0
for i in user_input :
	if i.isnumeric ( ) :
		digit_count += 1# for i, go through characters, if there is a number digit_count variable goes up by 1
print ( 'Your password contains', digit_count, 'digits.' )
space ( )
#-------------------------------------------------------------------------------------------------------------

#while loops
space ( )
counter = 1
while counter <= 10 :
	print ( 'Current value: ', counter )
	counter += 1# start counter at 1, count up 1 increment each turn and print 'Current value'
space ( )

#nested for loops
for i in range ( 1, 11 ) :
	for j in range ( 1, 11 ) :
		print ( i, 'x', j, '=', i * j )
space ( )

for i in range ( 1, 10 ) :
	for j in range ( 0, 1 ) :
		print ( str ( i ) * 9 )
space ( )

#nested while loops

final_score = 0
counter = 0
while counter < 3 :
	current_number = input ( 'Please provide a number to add:	' )
	while not current_number.isnumeric ( ) :# keep asking as long as the user provides a number
		current_number = input ( 'That\'s not a number! Try again:	' )
	final_score += int ( current_number )
	counter += 1# keep going through this loop askig for a number until counter == 2 ( 0, 1, 2 = 3 )
print ( 'The score is', final_score )

space ( )

n_numbers = int ( input ( 'How many numbers will be given?	' ) )
mean = 0
counter = 0
while counter < n_numbers :
	n = input ( 'Please provide a number:	' )
	while not n.isnumeric ( ) :
		n = input ( 'Wrong! That\'s not a number! Try again:	' )
	mean += int ( n )# start mean at 0, add user input to current mean value
	counter += 1# increment by 1 each turn after user input
print ( mean / n_numbers )# divide the final mean value by the original value entered by user

space ( )	

#Break with while loops
user_input = input ( 'Please provide a number:	' )
while True :# while true's are used to introduce infinite loops - the condition True is ALWAYS true
	if user_input.isnumeric ( ) :
		break# terminate the whole loop. Once a user provides the necessary condition, the loop immediately terminates
	user_input = input ( 'Not a number! Please provide a number :		' )
print ( 'Your number is:	', user_input )
space ( )

year = input ( 'In what year was Python first released?	' )
while True :
	if year == '1990' :
		break
	year = input ( 'Please try again:	' )
print ( 'Correct!' )

space ( )

# break with for loops
user_input = input ( 'Please provide a nickname for yoursef. Don\'t use digits!	' )
is_valid = True
for character in user_input :
	if character.isdigit ( ) :
		is_valid = False
		break
		
if is_valid == True :
	print ( 'Nickname correct!' )
else :
	print ( 'Nickname incorrect!' )

space ( )
#Identifying primes
user_number = int ( input ( 'Please provide a number from 2 to 1000:	' ) )
is_prime = True
if user_number >= 2 and user_number <= 1000 :
	for i in range ( 2, user_number ) :
		if user_number % i == 0 :# if there is no remainder when user_number is divided by i (i,e there are factors)
			is_prime = False# switch the is_prime variable to False
			print ( user_number, 'is not prime!' )
			break# immediately end the program to prevent iterating all the way up to the user_number
	if is_prime == True :
		print ( user_number, 'is prime!' )
else :# immediately jump to this line if user enters a number outside of the range
	print ( 'Incorrect number!' )

space ( )			
#Continue with while loops
counter = 0
while counter < 10 :
	counter += 1# iterate up to 10 adding 1 to counter on each iteration
	if counter == 3 :
		continue# skips over 3
	print ( 'Current value:	', counter )
space ( )

#even numbers up to 100 not divisible by 6
current_value = 0
while current_value < 100 :
	current_value += 2
	if current_value % 6 == 0 :# simply switch this to != if you want the one's divisible by 6 instead
		continue
	print ( current_value )
print ( 'That\'s enough!' )

space ( )
#Continue with for loops
for i in range ( 1, 11 ) :
	if i % 2 != 0 :
		continue
	print ( i )
space ( )

for i in range ( 1, 15 ) :
	if i % 5 == 0 :
		continue
	print ( 'The remainder of dividing', i, 'by 5 is', i % 5 )

space ( )
#print the value of 10 factorial ( 10!)
score = 1
for i in range ( 1, 11 ) :
	score *= i
print ( score )
space ( )

#Guess the secret number
answer = input ( 'Guess our secret number!	' )
while True :
	if int ( answer ) > 8 :
		answer = input ( 'Too big!	' )
	elif int ( answer ) < 8 :
		answer = input ( 'Too small!	' )
	elif int ( answer ) == 8 :
		break
print ( '\nCorrect!\n' )
#===================================================================================

# Patterns!
for i in range ( 1, 5 ) :
	print ( '-=' * 6 )
	for j in range ( 1 ) :
		print ( '=-' * 6 )
space ( )

def draw_pattern ( rows, columns ) :
	line_to_print = ''
	rows = int ( input ( 'Enter the number of rows:	' ) or 5 )
	columns = int ( input ( 'Enter the number of columns:	' ) or 8 )
	space ( )
	
	for i in range ( 1, rows + 1 ) :
		for j in range ( 1, columns + 1 ) :
			if i % 2 == 0 :
				if j % 2 == 0 : line_to_print += '-'
				else : line_to_print += '='
			else :
				if j % 2 == 0 : line_to_print += '='
				else : line_to_print += '-'
		print ( line_to_print )
		line_to_print = ''
	space ( )
draw_pattern ( 1, 1 )

#Function parameters
def print_numbers_to ( number ) :
	for i in range ( 1, number + 1 ) :
		print ( i )
print_numbers_to ( 50 )

space ( )
#functions with multiple parameters
def convert ( amount, rate ) :
	print ( 'Amount:', amount, 'Rate:', rate, 'Conversion:', amount * rate )
convert ( amount = 55, rate = 1.75 )
space ( )

#functions with return values
def factorial ( number ) :
	score = 1
	while number > 1 :
		score *= number 
		number -= 1
	return score
print ( factorial ( 4 ) )# 4 * 3 * 2 * 1 = 24
space ( )

def return_bigger ( a, b ) :
	if a > b :
		return a
	elif b > a :
		return b
	else :
		return 0
print ( return_bigger ( 7, 9 ) )

space ( )
#Using a function return value 
def factorial ( number ) :
	score = 1
	while number > 1 :
		score *= number 
		number -= 1
	return score
a = factorial ( 3 )
b = factorial ( 4 )	
print ( a + b )

space ( )
def find_divisors ( x ) :
	for i in range ( 2, x - 1 ) :
		if x % i == 0 :
			print ( i )
find_divisors ( 20 )
space ( )

# default argument values
def dog_to_human_age ( dog_age = 1 ) :
	return dog_age * 7
print ( dog_to_human_age ( 3 ) )
print ( dog_to_human_age ( ) )
space ( )
def water_supply ( age = 75, amount = 2 ) :
	return ( age * 365 * amount )
print ( water_supply ( ) )
space ( )
# mandatory and optional arguments together
# You can define a function that will have both mandatory and optional arguments, but mandatory arguments must come first
def calculate_price ( weight, price_per_pound = 1.5, tax = 0.15 ) :
	return weight * price_per_pound * ( 1 + tax )
print ( calculate_price ( 170, 12.0, 0.83 ) )# provided with all arguments
print ( calculate_price ( 170 ) )# provided only one mandatory argument 
print ( calculate_price ( 170, 12.0 ) )# provided the mandatory argment (weight) and the first optional argument (price_per_pound), tax has the default value of 0.15
space ( )

def calculate_area ( r = 1, pi = 3.14 ) :
	return ( pi * r ** 2 )
print ( calculate_area ( 7 ) )
space ( )
#===================================================================================

def find_monthly_savings ( amount, years ) :
# if I wanted to save $x in y years, how much should I put away each month to reach that objective
# (years * 12) = var1
# (amount) / var1 = monthly savings
# if amount <= 0 return None
	if amount <= 0 or years <= 0 :
		return None
	else :
		var1 = ( years * 12 )
		amount2 = ( amount / var1 )
#		print ( amount2 )
	return amount2

print ( find_monthly_savings ( 4000, 1 ) )
space ( )
#===================================================================================

#The ink costs 1.25 per poster
#The printery needs to buy a roll of paper on which the posters will be printed. Each roll costs 50 USD and can make 200 posters. The customer pays for entire rolls.
#Example: To print 1 poster, the customer needs to buy 1 roll of paper (50 USD) and pay for the ink (1.25 USD). Total cost: 51.25
#Example2: To print 50 posters, the customer needs to buy 1 roll (50 USD) and pay for ink (50 * 1.25 = 62.50). Total: 112.50
#Example3: To print 250 posters, customer needs to buy 2 rolls of paper (2 * 50 = 100 USD) and pay for ink (250 * 1.25 = 312.50 ). Total: 412.50
count_posters = int ( input ( '\nHow many posters will be printed? ' ) )
roll = 200
cost = count_posters / roll

if count_posters > roll :
	total = ( cost * 50 ) + ( 1.25 * count_posters )
	print ( '\nThis will cost %s USD.' % total )
else :
	total = ( 1.25 * count_posters ) + 50
	print ( '\nThis will cost %s USD.' % total )
space ( )
#===================================================================================

count_numbers = int ( input ( 'How many numbers do you have?	' ) )
score = 0
for i in range ( 0, count_numbers  ) :
	n = int ( input ( 'Provide a number:	' ) )# will keep asking until range is satisfied
	score += n
print ( '\nThe average is ', ( score / count_numbers ) )

space ( )
#===================================================================================
# Create a function that calculates the cost of a car rental:
# The daily base fare is 100 USD for drivers who are at least 30, or 220 USD for younger drivers
# Every seventh day of the rental is free of charge
# When the arguments are not provided, the function takes the following default values: a 30-year old driver who rents for 1 day

def calculate_rental_cost ( days = 1, age = 30 ) :
	if age < 30 :
		base_fare = 220
	else :
		base_fare = 100
	discount = days // 7
	days -= discount
	return days * base_fare

print ( calculate_rental_cost ( 8, 30 ) )
#===================================================================================
#																	Python Basics Part 2
space ( )
name = input ( 'Hello, what is your name?	' )
print ( '\nHello, ', name )

space ( )
#===================================================================================
def print_parity ( number ) :
	import math
	if math.ceil ( number ) == number :
		number = number
		if number % 2 == 0 :
			return '\nYou provided an even number.'
		else :
			return '\nYou provided an odd number.'
	else :
		return '\nThat is not defined as a natural number.'

#even_or_odd = float ( input ( '\nEnter a natural number:	' ) )
#print ( print_parity ( even_or_odd ) )
space ( )
def print_parity ( number ) :
	if number % 2 == 0 :
		return '\nYou provided an even number.'
	else :
		return '\nYou provided an odd number.'
print ( print_parity ( 13 ) )
space ( )
#===================================================================================
def print_multiples ( n, max ) :
	count = 0
	for i in range ( 1, max ) :
		count += n
		if count <= max  :
			print ( n * i )
		else :
			break
space ( )
print_multiples ( 3, 19 )
space ( )
#===================================================================================

tourist_arrivals = [ 7.8, 9.0, 10.4, 10.9, 14.7, 22.7, 22.3, 14.8, 11.4, 8.6, 9.1, 12.9 ]
months = [ 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December' ]
if len ( tourist_arrivals ) == 12 :
	pass# pass onto the rest of code to continue else the code stops because the shits incorrect
else :
	print ( '\nIncorrect number of months.' )
space ( )
for i in tourist_arrivals :
	print ( i, 'million tourists should increase to', i * 1.08 )
space ( )
for i in range ( 0, len ( tourist_arrivals ) ) :
	print ( 'Tourist arrivals in', months [ i ], '2023 were', tourist_arrivals [ i ], 'million people.' )
space ( )
#===================================================================================
def print_numbers_to ( number ) :
	for i in range ( 1, number + 1 ) :
		print ( i )
print (print_numbers_to ( 21 ) )

def find_divisors ( x ) :
	for i in range ( 2, x - 1 ) :
		if x % i == 0 :
			print ( i )
	space ( )
find = int ( input ( '\nEnter a number:	' ) )
find_divisors ( find )
space ( )
#===================================================================================

def sum_between ( a, b ) :
	count = 0
	if b < a : return None
	for i in range ( a, b + 1 ) :
		count += i
	return count
print ( '\n', sum_between ( 1, 20 ), '\n' )
#===================================================================================

#Create a function that will convert gross salary to net salary. Name function convert_gross_to_net ( salary ). The function should print:
#Your salary gross: {x}
#Salary after social contributions: {y}
#Net salary after tax: {z} 
def calculate_social_contributions ( amount ) :# helper function 1
	if amount < 200 : return 0
	elif amount < 1000 : return 100
	else : return 200
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
def calculate_tax ( amount ) : # helper function 2
	if amount > 3000 : return 300 + ( amount - 3000 ) * 0.20
	else : return amount * 0.10
#--------------------------------------------------------------------------------------------------------------------------------------------------------------	
def convert_gross_to_net ( salary ) :# main function
	print ( '\nYour salary gross:', salary )
	after_social = salary - calculate_social_contributions ( salary )
	print ( '\nSalary after social contributions:', after_social )
	after_tax = after_social - calculate_tax ( after_social )
	print ( '\nNet salary after tax:', after_tax, '\n' )
convert_gross_to_net ( 5000 )
space ( )
#===================================================================================

supermarkets = [ 'Tesco', 'Alldi', 'Morrisons', 'Co-op', 'Iceland' ]
for i in supermarkets :
	if 'Lidi' not in supermarkets :
		supermarkets.append ( 'Lidi' )# if this does not match above line it will create an endless loop
		print ( i )
	else : print ( i )
		#print ( i )
space ( )
#===================================================================================

world_population = [ 7128, 7213, 7299, 7383, 7467, 7550, 7663 ]
for i in range ( 1, len ( world_population ) ) :
	growth = world_population [ i ] - world_population [ i - 1 ]
	year = 2012 + i
	print ( 'In year', year, '\b, the increase in population was', growth, 'millions.' )
space ( )
#===================================================================================

def count_even ( input_list ) :
	even = [ ]
	for i in input_list :
		if i % 2 == 0 :
			even.append ( i )
	print ( even )
	return len ( even )# return the number of elements in the list of even numbers
sample_list = [ -1, 0, 1, 3, 5, -3, 7, 9, -2, 0, 6, 22.5, 68 ]
print ( count_even ( sample_list ) )
space ( )
#===================================================================================

sample_list = [ -1, 0, 1, 3, 5, -3, 7, 9, -2, 0, 6, 22.5, 68 ]
def delete_first_element ( input_list ) :
	del input_list [ 0 ]
print ( sample_list )
delete_first_element ( sample_list )
print ( sample_list )
space ( )
#===================================================================================

A = {			        'Building'			:		'Room A',
				'key 1'			:		[ 81.17, 99.31, 7.34, 54.33, 92.85, 93.95 ] ,
				'key 2'			:		[ 0.10, 19.12, 9.98, 74.38 ] , 
				'key 3'			:		[ 43.11, 49.63 ]
}

B = {				'Building'			:		'Room B',
				'key 1'			:		[ 21.68, 43.84, 45.11, 40.59, 13.59, 10.2 ] ,
				'key 2'			:		[ 70.41, 10.69, 2.37, 59.72 ],
				'key 3'			:		[ 64.65, 71.60 ]
}

C = {				'Building' 			:		'Room C',
				'key 1'			:		[ 53.10, 90.67, 0.68, 49.2, 15.74, 24.54 ],
				'key 2'			:		[ 16.34, 98.50, 26.9, 73.4 ],
				'key 3'			:		[ 77.92, 87.84 ]
}

T = [ A, B, C ]
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
def basic_average ( x ) :
	ba = float ( sum ( x ) ) / len ( x )
	return ba
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
def sum_average ( x ) :
	s1_average = float ( sum ( x [ 'key 1' ] ) ) / len ( x [ 'key 1' ] )
	s2_average = float ( sum ( x [ 'key 2' ] ) ) / len ( x [ 'key 2' ] ) 
	s3_average = float ( sum ( x [ 'key 3' ] ) ) / len ( x [ 'key 3' ] ) 
	return ( s1_average + s2_average + s3_average )
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
def complex_average ( x ) :
	c1 = 0.10 * sum ( x [ 'key 1' ] ) / len ( x [ 'key 1' ] )# 10% of sum of all key1 values / n instances of key1 values
	c2 = 0.30 * sum ( x [ 'key 2' ] ) / len ( x [ 'key 2' ] )# 30% of sum of all key2 values / n instances of key2 values
	c3 = 0.60 * sum ( x [ 'key 3' ] ) / len ( x [ 'key 3' ] )# 60% of sum of all key3 values / n instances of key3 values
	return ( c1 + c2 + c3 ) 
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
def rangeString ( x ) : 
	if x >= 90 : return 'Acceptable range or above'
	elif x >= 80 or x < 90 : return 'Between eighty and ninety'
	elif x >= 70 or x < 80 : return 'Between seventy and eighty'
	elif x >= 60 or x < 70 : return 'Between sixty and seventy'
	else : return 'Below acceptable range' 
	return x
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
def total_average ( x ) :
	e_list = [ ]
	for y in x :
		e_list.append ( complex_average ( y ) )
		return basic_average ( e_list )
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
print ( basic_average ( A [ 'key 3' ] ) )
print ( basic_average ( B [ 'key 3' ] ) )
print ( basic_average ( C [ 'key 3' ] ) )

print ( '\nSum_average of dictionary A\n', sum_average ( A ), '\n' )
print ( 'Sum_average of dictionary B\n', sum_average ( B ), '\n' )
print ( 'Sum_average of dictionary C\n', sum_average ( C ), '\n\n' )

print ( 'Complex Average of dictionary A\n', complex_average ( A ), '\n' )
print ( 'Complex Average of dictionary B\n', complex_average ( B ), '\n' )
print ( 'Complex Average of dictionary C\n', complex_average ( C ), '\n\n' )

print ( 'RangeStrings of sum_averages' )
print ( rangeString ( sum_average ( A ) ) )
print ( rangeString ( sum_average ( B ) ) )
print ( rangeString ( sum_average ( C ) ) )
space ( )
print ( 'RangeStrings of complex_averages' )
print ( rangeString ( complex_average ( A ) ) )
print ( rangeString ( complex_average ( B ) ) )
print ( rangeString ( complex_average ( C ) ) )
space ( )
print ( 'The total average:	', total_average ( T ) )
space ( )

#===================================================================================
instring = input ( '\nEnter a string of text:\n' )
outstring = instring.upper ( )
print ( outstring )

import random
print ( random.randrange ( 1, 1000 ) )
space ( )

#===================================================================================	
r = ( 'Everything moonlit landscape echoes her presence.' )
print ( r )
print ( r.replace ( 'm', 'M' ) )
space ( )
a = 'capitalize'
print ( a )
print ( a.capitalize ( ) )
space ( )
b = 'Convert Strings to loWercase'
print ( b )
print ( b.casefold ( ) )	
space ( )
c = 'Love is the law and love is the bond. How many love times is love here?'
d = c.casefold ( )
print ( c )
print ( 'The word \'love\' appears', d.count ( 'love' ), 'times' )
space ( )
e = 'feniskaren@gmail.com'
f = e.endswith ( 'gmail.com' )
print ( f )
space ( )
g = 'This is a sentence that has the word find in it.'
h = g.find ( 'find' )
i = g.index ( 'find' )
print ( g )
print ( 'The word \'find\' starts at index', i )

space ( )	
from b_dic import book_listing
b = int ( input ( 'Enter an index number for book:	' ) )
print ( book_listing [ b ] )
space ( )	

import os
choice = input (
	'\nWould you like to open a file, create a new file, write to an existing file, or delete a file?\n\n\
	Open a file:			o\n\
	Create a new file:		n\n\
	Write to an existing file:	w\n\
	Delete a file:			d\n\
	Move on:				m\n\
	\n'
	)
	if 'o' in choice :
		choice = input ( 'Name the file you would like to open:	' )
		if os.path.exists ( choice ) :# checking if file exists. If yes, continue to next step...
		f = open ( choice )
		t = open ( choice, 'r' )
		print ( f.read ( ) )
		print ( f.fileno ( ) )
		f.close ( )
		choice2 = input ( # what to do with file
		'\nWhat would you like to do with this file?\n\n\
		Append to it:			a\n\
		Overwrite it:			w\n\
		Move on:				m\n\
		\n'
		if 'a' in choice2 :
			f = open ( choice, 'a' )
			f.write ( 'Add this mufucka!' )
			f.close ( )
			f = open ( choice, 'r' )	
			print ( f.read ( ) )
		elif 'w' in choice2 :
			f = open ( choice, 'w' )
			fwrite = input ( 'Anything you type here will overwrite what is currently in the file!\n' )
			f.write ( fwrite )
			f.close ( )
			f = open ( choice, 'r' )
			print ( f.read ( ) )
		else :
			pass
	else :
		print ( '\nThis file doesn\'t exist\n' )
		pass
	elif 'w' in choice :
		wfile = input ( 'What file would you like to write to?' )
		f = open ( wfile, 'a' )
		fwrite = input ( 'Enter the text you would like appended to the file...\n\n' )
		f.write ( fwrite )
		f.close ( )
		continue
	elif 'n' in choice :
		nfile = input ( 'Enter the name of the file you would like to create followed by \'.txt\'	' )
		f = open ( nfile, 'x' )
		continue
	else :
		pass
space ( )

#===================================================================================
def fem_male ( ) :
	name = input ( 'Provide a Polish name:	' )
	if ( name.endswith ( 'a' ) ) and name != 'Kuba' : return 'This is a female name'
	else : return 'This is a male name'
print ( fem_male ( ) )

#===================================================================================
def password ( ) :
	password = input ( '\nPlease provide a password greater than 8 characters and does not start with @:	' )
	if len ( password ) >= 8 and password.startswith ( '@' ) == False : print ( 'Good' ) 
	else : print ( 'No good' )
password ( )

#===================================================================================
def online ( ) :
	purchase_days_ago = int ( input ( '\nHow many days ago have you purchased the item?	' ) )
	is_used = input ( 'Have you used the item at all [ y / n ]?	' )
	is_broken = input ( 'Has the item broken down on its own [ y / n ]?	' )
	if ( is_broken == 'y' or ( purchase_days_ago <= 14 and is_used == 'n' ) ) : print ( 'Refund' )
	else : print ( 'No refund' )
online ( )
#===================================================================================

def leap_year ( ) :
	year = int ( input ( '\nProvide a year:	' ) )
	if ( year % 4 == 0 and year % 100 != 0 ) or ( year % 400 == 0 ) :# if divisible by 4 but NOT 100 or if it is divisible by 400
		return ( '\nLeap year' )
	else : return ( '\nNot a leap year' )
print ( leap_year ( ) )
#===================================================================================
	
def looping_passwords ( ) :
	user_input = input ( '\nProvide a password:	' )
	digit_count = 0
	for letter in user_input :
		if letter.isnumeric ( ) : digit_count += 1
	print ( '\nYour password contains', digit_count, 'digits.' )
looping_passwords ( )
#===================================================================================

space ( )
def pow2 ( ) :
	counter = 2			
	while counter <= 1024 :
		print ( counter )
		counter *= 2
pow2 ( )
#--------------------------------------------------------------------------------------------------------------------------------------------------------------				
def oddto100 ( ) :		
	current_value = 1		
	while current_value < 100 :
		print ( current_value )
		current_value += 2
oddto100 ( )	
#===================================================================================

def secret_number ( ) :
	secret_n = 7
	user_input = int ( input ( '\nGuess the secret number (0 - 9):	' ) )
	while user_input != secret_n :
		user_input = int ( input ( '\nWrong! Try again (0 - 9):	' ) )
		continue
	if user_input == secret_n :
		print ( '\nCorrect!' )
secret_number ( )
#===================================================================================

def multTable ( ) :
	for i in range ( 1, 11 ) :
		for j in range ( 1, 11 ) :
			print ( i, 'x', j, '=' , i * j )
multTable ( )
#===================================================================================	
	
def nested ( ) :	
	strv = ''
	for i in range ( 1, 10 ) :# Length vertical
		for j in range ( 0, 9 ) :# Length horizontal
			str ( j )
			j = i * 1
			strv += str ( j )
		print ( strv )
		strv = ''
nested ( )

def break_for_prime ( ) :	
	user_number = int ( input ( '\nProvide a number from 2 to 100,000:	' ) )
	is_prime = True
	if user_number >= 2 and user_number <= 100000 :
		for i in range ( 2, user_number ) :
			if ( user_number % i ) == 0 : 
				is_prime = False
				break
		if is_prime == True : print ( user_number, 'is prime' )
		else : print ( user_number, 'is not prime' )
	else : print ( '\nInvalid entry' )
break_for_prime ( )
#===================================================================================

def factorial ( ) :
	fact = int ( input ( '\nEnter a number to output its factorial:	' ) )
	fact = range ( 1, ( fact + 1 ) )
	counter = 1
	for i in fact : counter += i
	print ( counter )
factorial ( )

#===================================================================================
def find_divisors ( ) :
	div = int ( input ( '\nEnter a whole number to compute its divisors:	' ) )
	for i in range ( 2, div - 1 ) :
		if div % i == 0 :
			print ( i )
find_divisors ( )

#===================================================================================
grp1 = { 1, 2, 3 , 5, 20, 17, 33, 55 }
grp2 = { 2, 3, 4, 20, 33, 57 }
print ( grp1,'\n', grp2 )

counter = 0
intersection_grps = [ ]
for i in grp1.intersection ( grp2 ) :
	counter += 1
	intersection_grps.append ( i )
print ( '\nElements found in BOTH group 1 AND group 2:\n\n\t\t\t', intersection_grps, '\n' )
print ( '\nElements found in one group but not the other:\n\n\t\t\t', grp1 ^ grp2, '\n' )
print ( '\nElements found in group 2 but NOT group 1:\n\n\t\t\t', grp2 - grp1, '\n' ) 
print ( '\nElements gound in group 1 but NOT group 2:\n\n\t\t\t', grp1 - grp2, '\n' )

#===================================================================================
print ( '\nReturn a number between 3 and 9:' )
print ( random.randrange ( 3, 9 ) )
print ( '\nReturn a number between 3 and 9 inclusive:' )
print ( random.randint ( 3, 9 ) )
space ( )
#===================================================================================
def get_absolute_values ( input_list ) :
	absolutes = [ ]
	copy_list = list ( input_list ) 
	for i in copy_list :	
		absolutes.append ( abs ( i ) )
	return absolutes

sample_list = [ -1, 0, 1, 3, 5, -3, 7, 9, -2, 0, 6, 22.5, 68 ]
print ( sample_list, '\n\n', get_absolute_values ( sample_list ) )

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
def get_absolute_values2 ( input_list ) :
	new_list = list ( input_list )
	for i in range ( 0, len ( new_list ) ) :
		if new_list [ i ] < 0 :
			new_list [ i ] = -new_list [ i ] 
	return new_list

print ( get_absolute_values2 ( sample_list ) )

#===================================================================================
experiment_results = [ 12, 47, 8, 9, 1, 7 ]
print ( experiment_results )
for i in experiment_results :
	if i == max ( experiment_results ) or i == min ( experiment_results ) :
		experiment_results.remove ( i )
print ( experiment_results )
space  ( )
#===================================================================================
convert = int ( input ( 'Enter miles to convert to km:	' ) )
def miles_to_km ( x ) :
	converted_miles = x * 1.6
	return converted_miles

space ( )
print ( miles_to_km ( convert ) )

miles = [ 25, 35, 60, 75, 15, 55 ]
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
def miles_to_km ( x ) :
	converted_miles = [ ]
	for i in x :
		converted_miles.append ( i * 1.6 )
	return converted_miles

print ( miles )
print ( miles_to_km ( miles ) )
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
def miles_to_km2 ( x ) :
	for i in range ( 0, len ( x ) ) :
		x [ i ] *= 1.6
	return x

print ( miles_to_km2 ( miles ) )
space ( )

#===================================================================================
os_releases = { 
	2007 : 'Windows Vista', 
	2009 : 'Windows 7', 
	2012 : 'Windows 8', 
	2013 : 'Windows 8.1', 
	2015 : 'Windows 10' 
}

print ( os_releases [ 2012 ] )
os_releases [ 2001 ] = 'Windows XP'
print (os_releases [ 2001 ] )
space ( )
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
user_key = int ( input ( 'Enter a year between 2000 and 2018 to check if there was a Windows release:	' ) )
if user_key in os_releases :
	print ( '\nMajor release found:', os_releases [ user_key ] )
else : print ( '\nNo major release found' )
space ( )
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
for i in os_releases.keys ( ) :
	print ( os_releases [ i ], 'was released in', i )
space ( )
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
os_lengths = { }
for i in os_releases.values ( ) :# adding the values of one dictionary to an empty dictionary, then displaying the new dictionary values with lengths of those values
	os_lengths [ i ] = len ( i )
print ( os_lengths )
space ( )
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
for key, value in os_releases.items ( ) :# for loop prints key-value pairs with items() function
	print ( key, '=', value )
space ( )
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
for i in os_releases.keys ( ) :# for loop to find keys
	print ( os_releases [ i ], 'was released in', i, '\b,', i - 1985, 'years after Windows 1.0' )
space ( )
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
for key, value in os_releases.items ( ) :
	print ( value, 'was released in', key, '\b,', key - 1985, 'years after Windows 1.0' )
space ( )

#===================================================================================
user_input = input ( '\nProvide some text:	' )
letter_freq = { }# create an empty dictionary
for line in user_input :# iterate over each word in user_input
	line = line.strip ( )# remove the leading spaces and newline character
	line = line.lower ( )
	words = line.split ( ' ' )# split the line into words
	for i in words :
		if i in letter_freq :# check if the word is already in dictionary
			letter_freq [ i ] += 1# increment count of word by 1
		else : letter_freq [ i ] = 1# add the word to dictionary with count 1
space ( )
for key, value in letter_freq.items ( ) :
	print ( key, ':', value )
space ( )

#===================================================================================
user_input = input ( '\nProvide some text:	' )# code does the same as above except with whole words
word_freq = { }
for i in user_input.split ( ) :
	if i in word_freq : word_freq [ i ] += 1
	else : word_freq [ i ] = 1
space ( )
for key, value in word_freq.items ( ) : print ( key, ':', value )

#===================================================================================
dictionary_values = {
	'key1' : 23,
	'key2' : 54,
	'key3' : 2,
	'key4' : 99,
	'key5' : 32
}
def key_value_pairs ( x ) :
	for key, value in x.items ( ) :
		print ( key, '=', value )
	return x
print ( key_value_pairs ( dictionary_values ) )
space ( )
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
def max_value ( x ) :
	max_dict_value = [ ]
	for i in x.values ( ) :
		max_dict_value.append ( i )
	return max ( max_dict_value )
print ( '\nThe largest value in this dictionary is', max_value ( dictionary_values ), '\b.' )
space ( )
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
def add_ten ( x ) :
	print ( '\nAdding 10 to the even values of a dictionary...\n' )
	for value in x.values ( ) :
		if value % 2 == 0 : 
			value2 = value + 10
			print ( value2, '<-- added 10' )
		else : print ( value )
	for key in x :
		if x [ key ] % 2 == 0 : x [ key ] += 10
	space ( )
	return x
print ( add_ten ( dictionary_values ) )
space ( )
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
def add_ten_more ( x ) :
	new_x = x.copy ( )
	for i in new_x :# for every key in new_x
		if new_x [ i ] % 2 == 0 :# if the value divided by 2 results in no remainder ( even number )
			new_x [ i ] += 10# add 10 to this
	space ( )
	return new_x
print ( add_ten_more ( dictionary_values ) )
space ( )

#===================================================================================
base_prices = {
	'shoes' : 235,
	't-shirt' : 49,
	'pullover' : 109
}
discounts = {
	'shoes' : 40,
	'pullover' : 9
}
def calculate_discount ( base_prices, discounts ) :
	new_value = base_prices.copy ( )
	for i in new_value.keys ( ) :
		for j in discounts.keys ( ) :
			if i == j : print ( i, j, ' <-- match!' )
	return new_value
print ( calculate_discount ( base_prices, discounts ) )
space ( )		
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
def calculate_discount2 ( x, y ) :
	new_value = x.copy ( )
	for i in new_value :
		for j in y :
			if i == j :
				discount = ( ( new_value [ i ] ) - ( y [ j ] ) )
				new_value [ i ] = discount
	return new_value
print ( calculate_discount2 ( base_prices, discounts ) )
space ( )
for i in base_prices :
	print ( base_prices [ i ], ' <--original price' )
space ( )

#===================================================================================
morse = { 
       		 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
	         'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
	         'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
	         'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
	         'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
        	 '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        	 '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--'
}
def trans ( x ) :
	text = input ( '\nEnter a string for morse translation:	' )
	text = text.upper ( )
	for i in text :
		for key, value in x.items ( ) :
			if i == key :
				print ( i, ' ->', value )
	return key	
print ( trans ( morse ) )
space ( )
#--------------------------------------------------------------------------------------------------------------------------------------------------------------

text2 = input ( '\nEnter a string for morse translation:	' )
def trans2 ( x, y ) :
	x = x.upper ( )
	code = [ ]
	for i in x :
		for key, value in y.items ( ) :
			if i == key :
				code.append ( value )
			else : pass
		if i not in y : code.append ( i )
	data = ''
	print ( data )
	return ''.join ( code )
print ( trans2 ( text2, morse ) )
space ( )

#===================================================================================
print ( 'Calculate customer order\n' )
customer_order = { 'cheese' : 3, 'coke' : 2, 'ass juice' : 1, 'bread' : 2, 'butter' : 1}
def calculate_price ( x ) :
	pricelist = { 'bread' : 2.37, 'ham' : 3.48, 'cheese' : 3.09, 'water' : 1.19, 'coke' : 2.58, 'juice' : 4.18, 'butter' : 5.18 }
	total_cost = [ ]
	for key, value in x.items ( ) :# get the key-value pairs from customer_order
		for key2, value2 in pricelist.items ( ) :# get the key-value pairs from pricelist
			if key == key2 :# if the key from the customer_order dictionary matches the key from the pricelist dictionary
				t = ( value * value2 )# multiply their values
				total_cost.append ( t )# append these values to total_cost
	return ( sum ( total_cost ) )# return the sum of all these values
print ( calculate_price ( customer_order ) )
space ( )
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
print ( 'Calculate customer order different code\n' )
pricelist = { 'bread' : 2.37, 'ham' : 3.48, 'cheese' : 3.09, 'water' : 1.19, 'coke' : 2.58, 'juice' : 4.18, 'butter' : 5.18 }
def calculate_price2 ( order ) :
	amount = 0.0
	for key, value in order.items ( ) :
		if key in pricelist :
			amount += value * pricelist [ key ]
	return amount
print ( calculate_price2 ( customer_order ) )
space ( )

#===================================================================================
file = open ( 'codes.txt', 'r' )
print ( file.read ( ) )
file.close ( )
space ( )
#Txt modes:
#	'r' - read
#	'w' - write: a file with the given name is created (or overwirtten if it already exists)for writing only
#	'a' - append: a file with the given name is opened for adding new data at the end
#--------------------------------------------------------------------------------------------------------------------------------------------------------------

with open ( 'user_data.txt', 'w' ) as file :# <--open the file for editing
	nickname = input ( 'What is your nickname?	' )# <--get user input
	age = input ( 'What is your age?	' )
	file.writelines ( '\n' + 'Nickname: ' + nickname + '\n' + 'Age: ' + age )# <--file automatically closes when using the 'with' function after operations
space ( )
file = open ( 'user_data.txt', 'r' )
print ( file.read ( ) )
file.close ( )

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
file = open ( 'codes.txt', 'r' )# this code does not work yet
numbers = [ ]
for i in file :
	i = int ( i )
	numbers.append ( i )
print ( max ( numbers ) )
print ( min ( numbers ) )
file.close ( )

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
subjects = [ 'math', 'biology', 'chemistry', 'physics' ]
file = open ( 'urls.txt', 'w' )# <--file open for editing
for i in subjects :# <--iterate through each element in the subjects list
	for year in range ( 2010, 2019 ) :# <--iterate through each year starting with 2010
		file.writelines ( 'http://imaginary-site.com/download/' +( i )+'-'+str ( year )+'\n' )
file.close ( )
file = open ( 'urls.txt', 'r' )# <--open the file in read-only mode to verify results
print ( file.read ( ) )# <-- present the file contents onscreen
file.close ( )
space ( )
#=============================================================----------------------------------------------------------Exceptions and IOError handling
#=============================================================

file_name = input ( 'Provide the name of a file:	' )
try :
	with open ( file_name, 'r' ) as file :
		print ( 'Read the file successfully!' )
		print ( file.read ( ) )
except IOError :
	print ( '\nThe file does not exist!' )
space ( )

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
while True :
	try :
		file_name = input ( '\nProvide the name of a file:	' )
		space ( )
		with open ( file_name, 'r' ) as file :
			print ( file.read ( ) )
			break
	except IOError :
		print ( '\nCould not read the file. Try another one.\n' )
space ( )
#--------------------------------------------------------------------------------------------------------------------------------------------------------------

username = input ( '\nWhat is your name?	' )
with open ( 'question.txt', 'w' ) as file :
	file.writelines ( 'Your name' + '\n' + username )
file = open ( 'question.txt', 'r' )
print ( file.read ( ) )
file.close ( )
space ( )

#===================================================================================
word = input ( '\nName the word:	' )
def count_word ( file_name, x ) :
	x = x.lower ( )
	count = 0
	with open ( file_name, 'r' ) as f :
		for i in f :
			i = i.strip ( )
			i = i .lower ( )
			for j in word :
				if j == x :
					count += 1
				else :
					count += 0
	return count
print ( '\nThis word occurs ', count_word ( 'codes.txt', word ), 'times.' )
space ( )
'''
#===================================================================================
print ( '\n\t\t\t\tIterating over list elements\n' )
#Track the amount of time I studies each day. Each element in the list represents n minutes studied in a day.
minutes = [ 368, 690, 426, 445, 690, 426, 494, 445, 690, 423, 534, 606, 390 ]
t_minutes = 0# added elements from list
counter = 0# this number will be used in the avg formula
for element in minutes :
	counter += 1# element 1, 2, 3...
	t_minutes += element# e1 + e2, ( e1 + e2 ) + e3...
t_avg = round ( ( t_minutes / counter ) / 60, 2 )# 60 turns the total avg from minutes to hours
print ( 'In a', len ( minutes ), 'day period, I studied for', t_avg, 'hours.\n' )















space ( )
