#!/usr/bin/env python
#-*- coding: utf-8 -*-

#	alias c2='python /home/dbustaflex666/Python/sf_Python/pythonCourseArguments.py'
#	alias c2='python pythonCourseArguments.py names, tofile'
#	grep -r 'phrase' /home/dbustaflexitlap/Python/sf_Python

from sys import argv
from datetime import datetime
import random
import pandas as pd

script, names, tofile = argv

#=============================================================
#=============================================================

def space ( ) :
	print ( '\n' )
#=============================================================
#=============================================================

def print_numbers_to ( number ) :
	for i in range ( 1, number + 1 ) :		
		print ( i )	
#print_numbers_to ( 50 ) #Replace the number argument with an actual integer
#=============================================================
#=============================================================		

def convert ( amount, rate ) :
	print ( '\nAmount:', amount, ' ', 'rate:', rate, '\nConversion: ', ( amount * rate ) )
#convert ( 55, 1.75 ) #Replace amount and rate arguments with actual integers here
#=============================================================
#=============================================================		

def return_bigger ( a, b ) :
	if a > b :
		return a
	elif a < b :
		return b
	else :
		return 0
#print ( return_bigger ( 5, 10 ) ) #Replace arguments a and b with actual integers here
#=============================================================
#=============================================================		

def factorial ( number ) :
	score = 1
	while number > 1 :
		score *= number
		number = number - 1
	return score
#print ( factorial ( 5 ) ) #Replace the number argument with an actual integer
#=============================================================
#=============================================================	

def find_divisors ( x ) :
	for i in range ( 2,  x - 1 ) :
		if x % i == 0 :
			print ( i )
	space ( )
#find = int ( input ( '\nEnter a number:	' ) )
#find_divisors ( find )
#=============================================================
#=============================================================	
	
def dog_to_human ( dog_age = 1 ) :
	return dog_age * 7
#dog = int ( input ( '\nEnter the dog\'s age:	' ) )
#print ( dog_to_human ( dog ) )
#=============================================================
#=============================================================	

def water_supply ( age = 75, amount = 2 ) :
	return age * 365 * amount
#print ( water_supply ( 75, 2 ) )
#=============================================================
#=============================================================	

def calculate_area ( r, pi = 3.14 ) :
	return pi * r * r
#print ( '\nThe area of the circle is', calculate_area ( 3.14, area ), 'inches.' )
#area = int ( input ( '\nEnter the radius of the circle to calculate it\'s area in inches:	' ) )
#=============================================================
#=============================================================	

def calculate_cone_area ( r = 1, pi = 3.14, h = 1 ) :
	return ( 1.0 / 3 ) * pi * r * r * h
#cone_area1 = int ( input ( '\nEnter the radius of the cone in inches:	' ) )
#cone_area2 = int ( input ( '\nEnter the height of the cone in inches:	' ) )
#print ( '\nThe area of the cone is', calculate_cone_area ( r = cone_area1, h = cone_area2 ), 'inches.\n' )
#=============================================================
#=============================================================	

def sum_between ( a, b ) :
	count = 0
	if b < a :
		return None
	for i in range ( a, b + 1 ) :
		count += i
	return count
#print ( '\n', sum_between ( 1, 10 ), '\n' )
#=============================================================
#=============================================================

#Create a function that will convert gross salary to net salary. Name function convert_gross_to_net ( salary ). The function should print:
#Your salary gross: {x}
#Salary after social contributions: {y}
#Net salary after tax: {z} 
def calculate_social_contributions ( amount ) :#helper function 1
	if amount < 200 :
		return 0
	elif amount < 1000 :
		return 100
	else :
		return 200
#--------------------------------------------------------------------------------------------------------------------------------------------------------------	

def calculate_tax ( amount ) :#helper function 2
	if amount > 3000 :
		return 300 + ( amount - 3000 ) * 0.20
	else :
		return amount * 0.10
#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def convert_gross_to_net ( salary ) :#Main function
	print ( '\nYour salary gross:', salary )
	after_social = salary - calculate_social_contributions ( salary )
	print ( '\nSalary after social contributions:', after_social )
	after_tax = after_social - calculate_tax ( after_social )
	print ( '\nNet salary after tax:', after_tax, '\n' )

#convert_gross_to_net ( 5000 )
#=============================================================
#=============================================================

def factorial ( number ) :
	score = 1
	for i in range ( 1, number + 1 ) :
		score *= i
	return score
#=============================================================
#=============================================================

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

#draw_pattern ( 1, 1 )
#=============================================================
#=============================================================

def find_monthly_savings ( amount, years ) :
# if I wanted to save $5000 in 5 years, how much should I put away each month to reach that objective
# (years * 12) = var1
# (amount) / var1 = monthly savings
# if amount <= 0 return None
	if amount <= 0 or years <= 0 :
		return None
	else :
		var1 = ( years * 12 )
		amount2 = ( amount / var1 )
		print ( amount2 )
	return amount2

#print ( find_monthly_savings ( 0, 3 ) )
#=============================================================
#=============================================================

def calculate_rental_cost ( days = 1, age = 30 ) :
	dev = [ ]
	for i in range ( 1, days + 1 ) :
		if i % 7 == 0 :
			dev.append ( i )

	if age >= 30 :
		discount = len ( dev ) * 100
		return ( 100 * days ) - discount
	elif age < 30 :
		discount = len ( dev ) * 220
		return ( 220 * days ) - discount

#print ( calculate_rental_cost ( 2, 25 ) )
#age = int ( input ( '\nEnter your age:	' ) )
#rental_days = int ( input ( '\nHow many days of rental?:	' ) )
#total_cost = float ( calculate_rental_cost ( rental_days, age ) )
#print ( '\nYour total cost for rental is', total_cost, 'dollars.\n' )
"""
Another way of doing it...
def calculate_rental_cost ( days = 1, age = 30 ) :
	if age < 30 :
		base_fare = 220
	else :
		base_fare = 100
	discount = days // 7
	days -= discount
	return days * base_fare

print ( calculate_rental_cost ( 8, 35 ) )
"""
#name = input ( '\nHello, what is your name?	' )
#print ( '\nHello,', name )
#=============================================================
#=============================================================

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
#=============================================================
#=============================================================

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
#=============================================================
#=============================================================----------------------------------------------------------Working with Lists

tourist_arrivals = [ 7.8, 9.0, 10.4, 10.9, 14.7, 22.7, 22.3, 14.8, 11.4, 8.6, 9.1 ]
months = [ 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December' ]
if len ( tourist_arrivals ) == 12 :
	pass
else :
	print ( '\nIncorrect number of months.' )
space ( )

for i in tourist_arrivals :
	print ( i, 'million tourists should increase to', i * 1.08 )
space ( )

for i in range ( 0, len ( tourist_arrivals ) ) :
	print ( 'Tourist arrivals in', months [ i ], '2016 were', tourist_arrivals [ i ], 'million people.' )
		
space ( )
#=============================================================
#=============================================================

supermarkets = [ 'Tesco', 'Aldi', 'Morrisons', 'Co-op', 'Iceland' ]
for i in supermarkets :
	if 'Lidl' not in supermarkets :
		supermarkets.append ( 'Lidl' )
		print ( i )
	else :
		print ( i )
space ( )
#=============================================================
#=============================================================

world_population = [ 7128, 7213, 7299, 7383, 7467, 7550, 7633 ]
for i in range ( 1, len ( world_population ) ) :
	growth = world_population [ i ] - world_population [ i - 1 ]
	year = 2012 + i
	print ( 'In year', year, '\b, the increase in population was', growth, 'millions.' )
space ( )
#=============================================================
#=============================================================

def count_even ( input_list ) :
	even = [ ]
	for i in input_list :
		if i % 2 == 0 :
			even.append ( i )
	return len ( even )

sample_list = [ -1, 0, 1, 3, 5, -3, 7, 9, -2, 0, 6, 22.5, 68 ]
print ( count_even ( sample_list ) )

space ( )
#=============================================================
#=============================================================

def delete_first_element ( input_list ) :
	del input_list [ 0 ]

print ( sample_list )
delete_first_element ( sample_list )
print ( sample_list )

space ( )
#=============================================================
#=============================================================

def delete_first_element2 ( input_list ) :
	copy_list = list ( input_list )
	del copy_list [ 0 ]
	return copy_list

print ( 'Original:', sample_list )
new_list = delete_first_element2 ( sample_list )
print ( 'Modified copy:', new_list, '\nUnmodified original', sample_list, ' == ', sample_list )

space ( )
#=============================================================
#=============================================================

def get_absolute_values ( input_list ) :
	absolutes = [ ]
	copy_list = list ( input_list )
	for i in copy_list :
		absolutes.append ( abs ( i ) )
	return absolutes

sample_list = [ -1, 0, 1, 3, 5, -3, 7, 9, -2, 0, 6, 22.5, 68 ]
print ( sample_list, '\n', get_absolute_values ( sample_list ) )
space ( )
#=============================================================
#=============================================================

def get_absolute_values2 ( input_list ) :
	new_list = list ( input_list )
	for i in range ( 0, len ( new_list ) ) :
		if new_list [ i ] < 0 :
			new_list [ i ] = -new_list [ i ]
	return new_list
	
print ( get_absolute_values2 ( sample_list ) )
space ( )
#=============================================================
#=============================================================

athletes_weights = [ 162, 172, 159, 135 ]
for i in athletes_weights :
	print ( i * 0.45 )
space ( )
#=============================================================
#=============================================================

experiment_results = [ 12, 47, 8, 9, 1, 7 ]

for i in experiment_results :
	if i == max ( experiment_results ) or i == min ( experiment_results ) :
		experiment_results.remove ( i )
print ( experiment_results )	
space ( )
#=============================================================
#=============================================================
miles = [ 25, 35, 60, 75, 15, 55 ]

def miles_to_km ( x ) :
	converted_miles = [ ]
	for i in x :
		converted_miles.append ( i * 1.6 )
	return converted_miles

print ( miles_to_km ( miles ) )
space ( )
#=============================================================
#=============================================================

def miles_to_km2 ( x ) :
	for i in range ( 0, len ( x ) ) :
		x [ i ] *= 1.6 # multiply 1.6 to x which is a new list
	return x# <--don't return in learn python

print ( miles_to_km2 ( miles ) )
space ( )
#=============================================================----------------------------------------------------------------Dictionaries
#=============================================================

os_releases = { 
	2007 : 'Windows Vista', 
	2009 : 'Windows 7', 
	2012 : 'Windows 8', 
	2013 : 'Windows 8.1', 
	2015 : 'Windows 10' 
}

print ( os_releases [ 2012 ] )
os_releases [ 2001 ] = 'Windows XP'
del os_releases [ 2001 ]
space ( )
#=============================================================
#=============================================================
'''
user_key = int ( input ( 'Enter a year between 2000 and 2018 to check if there was a Windows release:	' ) )
if user_key in os_releases :
	print ( '\nA major version found:', os_releases [ user_key ] )
else :
	print ( '\nNo major version found.' )
'''
space ( )
#=============================================================
#=============================================================

for i in os_releases.keys ( ) :#for loop to find keys
	print ( os_releases [ i ], 'was released in', i )
space ( )
#=============================================================
#=============================================================

os_lengths = { }
for i in os_releases.values ( ) :#adding the values of one dictionary to an empty dictionary, then displaying the new dictionary values with length of those values 
	os_lengths [ i ] = len ( i )
print ( os_lengths )
space ( )
#=============================================================
#=============================================================

for key, value in os_releases.items ( ) :# for loop prints key-value pairs with items() function
	print ( key, '=', value )
space ( )
#=============================================================
#=============================================================

for i in os_releases.keys ( ) :#for loop to find keys
	print ( os_releases [ i ], 'was released in', i, '\b,', i - 1985, 'years after Windows 1.0.' )
space ( )
#=============================================================
#=============================================================

for key, value in os_releases.items ( ) :
	print ( value, 'was released in', key, '\b,', key - 1985, 'years after Windows 1.0.' )
#=============================================================
#=============================================================
user_input = input ( '\nPlease provide some text: ' )
letter_frequencies = { }#create an empty dictionary

for line in user_input :#iterate over each word in line
	line = line.strip ( )#remove the leading spaces and newline character
	line = line.lower ( )
	words = line.split ( ' ' )#split the line into words

	for i in words :
		if i in letter_frequencies :#check if the word is already in dictionary
			letter_frequencies [ i ] += 1#increment count of word by 1
		else :
			letter_frequencies [ i ] = 1#add the word to dictionary with count 1
space ( )
for key, value in letter_frequencies.items ( ) :
	print ( key, ':', value )

space ( )
#=============================================================
#=============================================================

user_input = input ( 'Please provide some text: ' )
word_frequencies = { }#create an empty dictionary
line = user_input.lower ( )
words = line.split ( ' ' )

for i in words :
	if i in word_frequencies :
		word_frequencies [ i ] += 1
	else :
		word_frequencies [ i ] = 1
space ( )
for key, value in word_frequencies.items ( ) :
	print ( key, ':', value )
space ( )
#=============================================================
#=============================================================

user_input = input ( 'Please provide some text: ' )#code does the same as above 
word_frequencies = { }

for i in user_input.split ( ) :
	if i in word_frequencies :
		word_frequencies [ i ] += 1
	else :
		word_frequencies [ i ] = 1
space ( )
for key, value in word_frequencies.items ( ) :
	print ( key, ':', value )
space ( )
#=============================================================
#=============================================================




space ( )
#=============================================================
#=============================================================
