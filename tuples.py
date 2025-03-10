#!/usr/bin/env python
#-*- coding: utf-8 -*-

#	alias t='python /home/dbustaflexitlap/Python/sf_Python/tuples.py'
#	alias t='python tuples.py names, tofile'
#	grep -r 'phrase' /home/dbustaflexitlap/Python/sf_Python/
#	cp -ruv /home/dbustaflex666/Python/ /media/sf_Python/
#       grep -r --exclude-from=b_dic.py [ 'phrase' ] /home/dbustaflex666/Python/

#	12!!#8FG
# 	#&x9$g!JeV65VQAp
#       PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
from sys import argv
import datetime
script, names, tofile = argv
#=============================================================
#=============================================================
def space ( ) :
	print ( '\n' )	
#=============================================================
#=============================================================
space ( )
person = ( 'Mark', 28, 'English', 'London' )
print ( '\t\t\t\tRecap\n\n\t\t\t\tAccess second element\n\n' + str ( person [ 1 ] ) )
#---------------------------------------------------------------------------------------------------
print ( '\n\t\t\t\tAccess second and third elements\n' + str ( person [ 1 : 3 ] ) )
#---------------------------------------------------------------------------------------------------
print ( '\n\t\t\t\tIterate over a tuple\n' )
for element in person :
	print ( element )
#---------------------------------------------------------------------------------------------------
print ( '\n\t\t\t\tUnpack a tuple\n' )
name, age, nationality, city = person
print ( name, 'lives in', city )
#---------------------------------------------------------------------------------------------------
print ( '\n\t\t\t\tCreate a function that accepts a tuple and checks if the person is 18 or older\n' )
def print_adult_status ( person ) :
	name, age, _, _, = person # tuple unpacking. Only using name and age, underscores for non-used elements
	if age >= 18 :
		print ( name, 'is of legal age.' )
	else :
		print ( name, 'is NOT of legal age.' )
	return ''
print ( print_adult_status ( person ) )
space ( )
#=============================================================
#=============================================================--------------------------------------------------------------Returning tuples from functions----------------------------------------------
print ( '\n\t\t\t\tReturning tuples from functions\n' )
text = 'Create a function that accepts a string argument and returns a tuple with 3 elements: the count of spaces in the text, the count of commas, and the count of stops.'
def count_spaces_commas_stops ( x ) :
	spaces, commas, stops = 0, 0, 0 # 3 counters set to 0 on 1 line instead of 3
	for i in x :
		if i == ' ' : # if space 
			spaces += 1 # add 1 to spaces counter variable
		elif i == ',' : # if comma
			commas += 1 # add 1 to commas counter variable
		elif i == '.' : # if stop 
			stops += 1 # add 1 to stops couter variable
	return ( spaces, commas, stops ) # return the values that each counter holds
print ( count_spaces_commas_stops ( text ), '\n' )
#---------------------------------------------------------------------------------------------------
# Create a function that accepts a LIST of integer values and returns the smallest, largest, and average values respectively - all in the form of a tuple
def get_min_max_mean ( numbers ) :
	counter = 0 # when a variable is set to an integer, any integer added to it will be n + i = ( n + i )
	for i in numbers : # as each element comes down the pipeline
		counter += i # add that element to the counter variable
	avg = counter / len ( numbers ) # the value counter is now set to divided by n elements in the list of integers
	return ( min ( numbers ), max ( numbers ), avg )
print ( get_min_max_mean ( [ 1, 2, 5, 3, -1, -2, -9 ] ) )
space ( )
#=============================================================
#=============================================================--------------------------------------------------------------Unpacking tuples returned from functions----------------------------------------------
print ( '\n\n\t\t\t\tUnpacking tuples returned from functions\n' )
spaces, commas, stops = count_spaces_commas_stops ( text )
print ( text, '\n\n', 'In the above string, there are', spaces, 'spaces and', stops, 'stops in this string.\n' )
#---------------------------------------------------------------------------------------------------
# Unpack the result of get_min_max_mean ( ) into 3 variables:
# 	min
# 	max
# 	mean
# Use min and max to calculate the difference between the smallest and largest values
def get_min_max_mean2 ( n ) :
	min = n [ 0 ]
	max = n [ 0 ]
	counter = 0

	for i in n :
		counter += i
		if i < min :
			min = i
		if i > max :
			max = i
	mean = counter / len ( n )
	return ( min, max, mean )
#---------------------------------------------------------------------------------------------------
a_integers = [ 1, 2, 5, 3, -1, -2, -9 ] # list of integers
#min, max, mean = get_min_max_mean2 ( a_integers )
min, max, _ = get_min_max_mean2 ( a_integers ) # Use an underscore for unnecessary variables ( variable 'mean' was not called in this example, thus creating a 3rd variable unnecessary )
diff = max - min
print ( '\nThe difference between the min and max values is', diff )
space ( )
#=============================================================
#=============================================================--------------------------------------------------------------Functions operating on tuples as real-world objects----------------------------------------------
print ( '\n\n\t\t\t\tFunctions operating on tuples as real-world objects\n' )
# estimating whether a car is worth the repairs
car_details = ( 'Jeremy', 4000, 800 )

def repair_compare_cost ( car ) :
	_, value, repair = car
	if repair > 4000 and value <= 4000 :
		return ( 'Time to break it off.' )
	elif repair < 1000 and value <= 4000 :
		return ( 'Worth the fix!' )
	else :
		return ( 'May be worth it.' ) 
#---------------------------------------------------------------------------------------------------
print ( repair_compare_cost ( car_details ) )
#---------------------------------------------------------------------------------------------------
new_hire = ( 'Mark Adams', 'SQL Analyst', 4000 )
new_hire2 = ( 'Jessica Black', 'Project Manager', 5320 )
# Create a function that returns an employee's salary after the raise
# Raise is calculated as 10% for those whose position is 'SQL Analyst' and 5% of salary for all others.
def calculated_new_salary ( employee ) :
	_, y, z = employee
	if y == 'SQL Analyst' :
		return ( z * 0.1 ) + z
	else :
		return ( z * 0.05 ) + z
#---------------------------------------------------------------------------------------------------
print ( calculated_new_salary ( new_hire ) )
print ( calculated_new_salary ( new_hire2 ) )
space ( )
#=============================================================
#=============================================================--------------------------------------------------------------Tuples representing states or positions - coordinates----------------------------------------------
print ( '\n\n\t\t\t\tTuples representing states or positions - coordinates\n' )
# Write a function which accepts 2 arguments:
#          1) the current position in the x/y coordinate system
#          2) the movement that was made
# Both arguments are given as two-element tuples, where the first is the ( x ) value and the second is the ( y ) value
# Your task is to return the new position
initial_position = ( 2, 3 )
move = ( 1, - 2 )
def get_new_position ( position, move ) :
	a, b = position
	y, z = move
	return ( a + y, b + z )
#---------------------------------------------------------------------------------------------------
print ( get_new_position ( initial_position, move ) )
space ( )
#=============================================================
#=============================================================--------------------------------------------------------------tuples representing states or positions - traffic lights----------------------------------------------
print ( '\n\n\t\t\t\tTuples representing states or positions - traffic lights\n' )
# Write a function that checks which lights are on at the moment and returns the next traffic light setting
initial_state = ( True, False, False )
def next_simple_lights_state ( current_state ) :
	red, yellow, green = current_state # unpack the tuple argument
	if red :
		if yellow :
			return ( False, False, True )
		else :
			return ( True, True, False )
	else :
		return ( True, False, False )
#---------------------------------------------------------------------------------------------------
print ( next_simple_lights_state ( initial_state ) )
space ( )
#=============================================================
#=============================================================--------------------------------------------------------------iterating over lists in tuples----------------------------------------------
print ( '\n\n\t\t\t\tIterating over lists in tuples\n' )
cars_to_sell = [ # list
	( 'Volvo', 18000, 137000 ),
#      model    cheapest p = 23000
	( 'BMW', 23000, 80000 ), # 1 tuple, 3 elements
#                         top market value = 80000
	( 'Honda', 17000, 75000 ),
	( 'Opel', 12000, 79000 ),
	( 'Ford', 14500, 20000 )
] # end list
def find_cheapest_car ( car_list ) :
	current_cheapest = car_list [ 0 ] # set temp variable to the first tuple that gets sent through
	for i in car_list : # i passes through each tuple down the car list
		if i [ 1 ] < current_cheapest [ 1 ] : # compare second element of tuple to second element of previous tuple, if it is less, 
			current_cheapest = i # current_cheapest variable now set to the lesser element and so on
	return current_cheapest
print ( find_cheapest_car ( cars_to_sell ) )
space ( )
#---------------------------------------------------------------------------------------------------
new_hires = [ 
	( 'Mark Adams', 'SQL Analyst', 4000 ),
	( 'Leslie Burton', 'HR Specialist', 2300 ),
	( 'Dorothy Castillo', 'UX Designer', 3100 )
]
def find_mean_salary ( employee_list ) :
	temp_sum = 0
	for i in employee_list :
		temp_sum += i [ 2 ] # add each 3rd element of each tuple to the temp temp_sum integer variable
	return ( round ( temp_sum / len ( employee_list ), 2 ) ) # average formula with result rounded to 2 decimal places
print ( find_mean_salary ( new_hires ) )
#=============================================================
#=============================================================--------------------------------------------------------------Removing tuples from lists----------------------------------------------
print ( '\n\n\t\t\t\tRemoving tuples from lists\n' )
# remove tuple with car value above $15000
def remove_car ( car_list ) :
	for i in car_list [ : ] : # create a copy of the list of cars, i passes through tuples in that copy so that original list isn't fucked with
		if i [ 1 ] > 15000 : # if the second element value is greater that 15000
			car_list.remove ( i )
	return car_list
print ( remove_car ( cars_to_sell ) )
space ( )
#---------------------------------------------------------------------------------------------------
# remove people whose job titles contain the word "SQL" from the list of new hires
def remove_sql_specialists ( employee_list ) :
	for i in employee_list [ : ] :
		if i [ 1 ] == 'SQL Analyst' : # the element must match specifically, you cannot just set it eq to 'SQL' for example with this code
			employee_list.remove ( i )
	return employee_list
print ( remove_sql_specialists ( new_hires ) )
#=============================================================
#=============================================================--------------------------------------------------------------The zip ( ) function----------------------------------------------
print ( '\n\n\t\t\t\tThe zip ( ) function\n' )
newegg_oled = [ 1796.99, 2696.99, 996.99 ]
amazon_oled = [ 3496.99, 2999.99, 1769.99 ]
for i in zip ( newegg_oled, amazon_oled ) : # function compares elements from same size lists, one to one in a two-column tuple
#	print ( i )
	if i [ 0 ] < i [ 1 ] : # if 1st element of first list is less than 1st element of second list and so on...
		print ( 'Newegg is cheaper by', round ( i [ 1 ] - i [ 0 ], 2 ) )
	elif i [ 1 ] < i [ 0 ] :
		print ( 'Amazon is cheaper by', round ( i [ 0 ] - i [ 1 ], 2 ) ) # if 1st element of second list is less than first element of first list and so on...
	else :
		print ( 'Equal offer' )
space ( )
#---------------------------------------------------------------------------------------------------
# You are given the list of position names and salaries for five employees ( in the same order )
# Compute the average salary of employees who work in any position which has 'SQL' in its name
positions = [ 'SQL Analyst', 'HR Specialist', 'UX Designer', 'Senior SQL Analyst', 'SQL Analyst' ]
salaries = [ 4000, 3000, 5000, 4600, 4200 ] 
n_positions = 0
sql_salaries = 0
for i in zip ( positions, salaries ) : # matches index of positions to index of salaries. i [ 0 ] = positions, i [ 1 ] = salaries
	if 'SQL' in i [ 0 ] : # if 'SQL' in positions
		n_positions += 1
		sql_salaries += i [ 1 ]
print ( 'Average salary for positions related to SQL specialties: ' + str ( round ( sql_salaries / n_positions, 2 ) ) )
#=============================================================
#=============================================================--------------------------------------------------------------The zip ( ) function - lists of different sizes----------------------------------------------
print ( '\n\n\t\t\t\tThe zip ( ) function - lists of different sizes\n' )
#Code works in same way because zip ( ) automatically finds the list with the smaller number of elements. It stops when a zip element ( teeth ) is missing. Other elements ignored
#If you want to iterate over longer list, another method must be used

# Given 2017 and 2018 job titles for 3 employees. At the end of positions_2018 there are additional job titles ( new employees ).
# How many employees changed their job titles?

positions_2017 = [ 'SQL Analyst', 'HR Specialist', 'UX Designer' ]
positions_2018 = [ 'Senior SQL Analyst', 'HR Specialist', 'Chief UX Designer' ]
changed = 0
for i in zip ( positions_2017, positions_2018 ) :
	if i [ 0 ] != i [ 1 ] :
		changed += 1
print ( 'In 2018, ' + str ( changed ) + ' people changed their job titles.\n' )
#=============================================================
#=============================================================--------------------------------------------------------------Summary - Calculating game board positions----------------------------------------------
print ( '\n\t\t\t\tSummary - Calculating game board positions ( my solution )\n' )
# Function must take 2 arguments:
# 1. checkers_positions - a list of all checker positions in a rectangle board during play ( which are tuples ( x, y ).
#                         Each tuple on the list corresponds to the consecutive checker's position during game play.
# 2. treasure_position - the position ( as a tuple of a treasure on that game board
# Calculate how many times the checker's distance from the treasure was less than 2 during a game and return the result.

#                                                              distance = | x1 - x2 |  +  | y1 - y2 |

all_positions = [ ( 6, 3 ), ( 6, 5 ), ( 1, 5 ), ( 9, 7 ), ( 1, 1 ), ( 3, 5 ) ]
treasure = ( 5, 3 )
#---------------------------------------------------------------------------------------------------my solution
def count_near_positions ( checkers_positions, treasure_position ) : # ( all_positions, treasure )
	close_calls = 0
	for i in checkers_positions : # go through tuples in all_positions list
		d = ( treasure_position [ 0 ] - i [ 0 ] ) + ( treasure_position [ 1 ] - i [ 1 ] )
		absd = abs ( d )
		if absd < 2 :
			close_calls += 1
	return close_calls
print ( count_near_positions ( all_positions, treasure ) )
space ( )
#---------------------------------------------------------------------------------------------------their solution
print ( '\n\t\t\t\tSummary - Calculating game board positions ( their solution )\n' )
def count_near_positions2 ( checkers_positions, treasure_position ) :
	counter = 0
	x1, y1 = treasure_position
	for i in checkers_positions : 
		x2, y2 = i
		if abs ( x1 - x2 ) + abs ( y1 - y2 ) < 2 :
			counter += 1
	return counter
print ( count_near_positions ( all_positions, treasure ) )
#=============================================================
#=============================================================--------------------------------------------------------------Summary - Calculating weight change between people----------------------------------------------
print ( '\n\n\t\t\t\tSummary - Calculating weight change\n' )
# Write a function that accepts 2 arguments - which are lists with body weight expressed as float values
# Both lists represent weight values of the same people at two different points in time
# Analyze the weight values, element by element, and return a tuple with 3 counts: number of people who lost weight, identical weight, and number who gained weight

weight_2021 = [ 201.4, 150.8, 290.2, 145.5 ]
weight_2022 = [ 203.5, 147.7, 290.2, 155.9 ]

def get_weight_stats ( wa, wb ) :
	loss, even, gain = 0, 0, 0
	for i in zip ( wa, wb ) :
		if i [ 0 ] > i [ 1 ] :
			loss += 1
		elif i [ 0 ] < i [ 1 ] :
			gain += 1
		else :
			even += 1
	return str ( loss ) + ' lost weight, ' + str ( even ) + ' remained the same, ' + str ( gain ) + ' gained weight.'
print ( get_weight_stats ( weight_2021, weight_2022 ) )
#=============================================================
#=============================================================--------------------------------------------------------------Summary - Finding character occurences----------------------------------------------
print ( '\n\n\t\t\t\tSummary - Finding character occurences\n' )
# Write a function that, given a text and a list of letters, will find all occurences of the given letters, regardless of case.
# Function should return list of tuples of the form ( index, letter )

def find_occurences ( text, letters ) :
	c_indices = [ ]
	for index, character in enumerate ( text ) :
		if character.lower ( ) in letters :
			c_indices.append ( ( index, character ) )
	return ( c_indices )
print ( find_occurences ( 'Write a function that, given a text and a list of letters, will find all occurences of the given letters, regardless of case', [ 'e', 't' ] ) )







space ( )
