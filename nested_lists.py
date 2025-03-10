#!/usr/bin/env python
#-*- coding: utf-8 -*-

#	alias n='python /home/dbustaflexitlap/Python/sf_Python/nested_lists.py'
#	alias n='python nested_lists.py names, tofile'
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
print ( '\n\n\t\t\t\t\tNested lists - introduction\n' )
#4 different places, 3 days
#                    c1     c2      c3     c4
donations_day1 = [ 345.0, 287.80, 119.27, 329.30 ]# r1
donations_day2 = [ 294.25, 349.0, 178.90, 262.34 ]# r2
donations_day3 = [ 294.25, 349.0, 178.90, 262.34 ]# r3

# more effiicient way
donations = [
#       place1  place2  place3  place4
	[ 345.0, 287.80, 119.27, 329.30 ],# day1
	[ 294.25, 349.0, 178.90, 262.34 ],# day2
	[ 294.25, 349.0, 178.90, 262.34 ]# day3
]
		
hackathon_results = [
	[ 'HackKittens', '01011Brasil', 'GoForCode' ],
	[ '01011Brasil', 'NullPointerException', 'WeAreCode' ],
	[ 'FromIndiaWithCode', 'MutexLovers', 'HackKittens' ],
	[ 'WeAreCode', 'HackKittens', 'ThePyhonists' ]
]

for i in hackathon_results :
	for j in i :
		print ( j )
#=============================================================
#=============================================================--------------Accessing single elements
print ( '\n\n\t\t\t\t\tAccessing single elements\n' )
print ( hackathon_results [ 1 ] [ 1 ] )# access 2nd element of the 2nd list 
print ( hackathon_results [ 2 ] [ 0 ] )# access 1st element from the 3rd list 
#=============================================================
#=============================================================--------------Non-rectangular lists
print ( '\n\n\t\t\t\t\tNon-rectangular lists\n' )
hackathon_results2 = [
	[ 'HackKittens', '01011Brasil', 'GoForCode' ],
	[ '01011Brasil', 'NullPointerException', 'WeAreCode' ],
	[ 'FromIndiaWithCode' ],
	[ 'WeAreCode', 'HackKittens', 'ThePyhonists' ]
]
print ( hackathon_results2 [ 2 ] [ 0 ] )
#=============================================================
#=============================================================--------------Multidimensional nested lists
print ( '\n\n\t\t\t\t\tMultidimensional nested lists\n' )
three_dimensions = [
	[ [ 1, 2 ], [ 3, 4 ] ],
	[ [ 5, 6 ], [ 7, 8 ] ]
]
print ( three_dimensions [ 0 ] [ 0 ] [ 1 ] ) # access 2
print ( three_dimensions [ 0 ] [ 1 ] [ 1 ] ) # access 4
#=============================================================
#=============================================================--------------Iterating over values
print ( '\n\n\t\t\t\t\tIterating over values\n' )
#Nested for loops are needed to iterate over all values in a multidimensional list 
# Create a set named hackathon_winners
# Add all unique team names from the hackathon_results

hackathon_results = [
	[ 'HackKittens', '01011Brasil', 'GoForCode' ],
	[ '01011Brasil', 'NullPointerException', 'WeAreCode' ],
	[ 'FromIndiaWithCode', 'MutexLovers', 'HackKittens' ],
	[ 'WeAreCode', 'HackKittens', 'ThePythonists' ]
]

hackathon_winners = set ( )

for n_list in hackathon_results :# grab the contents of the nested list
	for winners in n_list :# grab the individual elements of that list
		hackathon_winners.add ( winners )# add them to the empty set for non-redundancy
print ( hackathon_winners )
#=============================================================
#=============================================================--------------Calculating metrics for entire nested lists
print ( '\n\n\t\t\t\t\tCalculating metrics for entire nested lists\n' )
# Calculating average value from all values in nested list 

total_sum = 0
number_of_donations = 0

donations = [
	[ 345.0, 287.80, 119.27, 329.30 ],
	[ 294.25, 349.0, 178.90, 262.34 ],
	[ 401.0, 456.45, 289.43, 319.27 ]
]

for n_list in donations :
	for element in n_list :
		total_sum += element# add each individual value to the total_sum ( 345.0 + 287.80 + 119.27... )
		number_of_donations += 1# each time j passes a value down the pipe, count up 1 ( 1, 2, 3... )
	average = ( round ( total_sum / number_of_donations, 2 ) )# take total sum value of all donations / number of donations and round 2 decimals
	print ( average )  
space ( )
#---------------------------------------------------------------------------------------------------------------
# Calculate how many times each team scored higher than 75 points
# Create a 'count_good_results' dictionary
# The keys will be the team names, values will be number of times a given team scored higher than 75 points

hackathon_results = [ # list
	[ ( 'HackKittens', 78 ), ( '01011Brasil', 71 ), ( 'GoForCode', 65 ) ],# [ list ( tuple ) ]
	[ ( '01011Brasil', 93 ), ( 'NullPointerException', 92 ), ( 'WeAreCode', 89 ) ],
	[ ( 'FromIndiaWithCode', 87 ), ( 'MutexLovers', 86 ), ( 'HackKittens', 83 ) ],
	[ ( 'WeAreCode', 97 ), ( 'HackKittens', 85 ), ( 'ThePythonists', 63 ) ]
]

count_good_results = { }

for n_list in hackathon_results :
	for element in n_list :
		team, score = element
		if score > 75 :
			count_good_results [ team ] = count_good_results.get ( team, 0 ) + 1
		else :
			count_good_results [ team ] = count_good_results.get ( team, 0 ) + 0
print ( count_good_results )
#=============================================================
#=============================================================--------------Calculating metrics for nested list rows
print ( '\n\n\t\t\t\t\tCalculating metrics for nested list rows\n' )

donations = [
	[ 345.0, 287.80, 119.27, 329.30 ],
	[ 294.25, 349.0, 178.90, 262.34 ],
	[ 401.0, 456.45, 289.43, 319.27 ]
]

for n_list in donations :
	daily_sum = 0# temp variable inside outer loop before inner loop invoked
	for element in n_list : 
		daily_sum += element
	print ( daily_sum )
space ( )
#---------------------------------------------------------------------------------------------------------------
# For each of the 4 applications, find and print the average score given to the podium finishers

hackathon_results = [
#    location1             location2              location3
  [ ( 'HackKittens', 78 ), ( '01011Brasil', 71 ), ( 'GoForCode', 65 ) ],# day1
  [ ( '01011Brasil', 93 ), ( 'NullPointerException', 92 ), ( 'WeAreCode', 89 ) ],# day2
  [ ( 'FromIndiaWithCode', 87 ), ( 'MutexLovers', 86 ), ( 'HackKittens', 83 ) ],# day3
  [ ( 'WeAreCode', 97 ), ( 'HackKittens', 85 ), ( 'ThePythonists', 63 ) ]# day4
]

for contest in hackathon_results :
	score_values = 0
	for team_score in contest :
		_, score = team_score
		score_values += score 
	print ( 'Average score: ', ( round ( score_values / len ( contest ), 2 ) ) )
#=============================================================
#=============================================================--------------Calculating metrics for nested list columns
print ( '\n\n\t\t\t\t\tCalculating metrics for nested columns\n' )
donations = [
	[ 345.0, 287.80, 119.27, 329.30 ],
	[ 294.25, 349.0, 178.90, 262.34 ],
	[ 401.0, 456.45, 289.43, 319.27 ]
]
place_sums = [ 0, 0, 0, 0 ]

for i, line in enumerate ( donations ) :# i = index number of row, line = row values of entire row 
	for j, value in enumerate ( line ) :# j = index number of row, value = individual row values
		place_sums [ j ] += value# column sums
print ( place_sums )
space ( )

#---------------------------------------------------------------------------------------------------------------
# Create a list named 'averages' that will store 3 elements:
# The average application score among all winners
# The average application score among all runners-up
# The average application score among all third-place finishers
  
Hackathon_results = [
	[ ( 'HackKittens', 78 ), ( '01011Brasil', 71 ), ( 'GoForCode', 65 ) ],
	[ ( '01011Brasil', 93 ), ( 'NullPointerException', 92 ), ( 'WeAreCode', 89 ) ],
	[ ( 'FromIndiaWithCode', 87 ), ( 'MutexLovers', 86 ), ( 'HackKittens', 83 ) ],
	[ ( 'WeAreCode', 97 ), ( 'HackKittens', 85 ), ( 'ThePythonists', 63 ) ]
] 
averages = [ 0, 0, 0 ]

for i, line in enumerate ( Hackathon_results ) :# index number, row containing team and score 
	for j, team_score in enumerate ( line ) :
		_, score = team_score
		averages [ j ] += score
for i in averages [ : ] :
	if i == i :
		averages.remove ( i )
		averages.append ( i / 4 )
print ( averages )
#=============================================================
#=============================================================--------------Modifying elements
print ( '\n\n\t\t\t\t\tModifying elements\n' )
# To modify elements of nested lists we need to iterate over indexes. Indexing over values won't work	

donations = [
	[ 345.0, 287.80, 119.27, 329.30 ],
	[ 294.25, 349.0, 178.90, 262.34 ],
	[ 401.0, 456.45, 289.43, 319.27 ]
]
for i in range ( len ( donations ) ) :
	for j in range ( len ( donations [ i ] ) ) :
		donations [ i ] [ j ] *= 0.88
	print ( donations [ i ] )
space ( )
#---------------------------------------------------------------------------------------------------------------
# You are given hackathon_teams nested list that contains only team names. 
#We now need to modify this list to store an abbreviated name for each team. 
#Shorten each team name to its first five letters and add a dot (.).
#For instance: 'HackKittens' should become 'HackK.'

hackathon_teams = [
	[ 'HackKittens', '01011Brasil', 'GoForCode' ],
	[ '01011Brasil', 'NullPointerException', 'WeAreCode' ],
	[ 'FromIndiaWithCode', 'MutexLovers', 'HackKittens' ],
	[ 'WeAreCode', 'HackKittens', 'ThePythonists' ]
]
for i, line in enumerate ( hackathon_teams ) :# My version
	for j, line2 in enumerate ( line ) :
		hackathon_teams [ i ] [ j ] = line2 [ 0 : 5 ] + '.'		
print ( hackathon_teams, ' <-- my version\n' )	
#---------------------------------------------------------------------------------------------------------------
for i in range ( len ( hackathon_teams ) ) :# Their version
	for j in range ( len ( hackathon_teams [ i ] ) ) :
		hackathon_teams [ i ] [ j ] = hackathon_teams [ i ] [ j ] [ : 5 ] + '.'
print ( hackathon_teams, ' <-----their version' )
#=============================================================
#=============================================================--------------Nested lists game board representations Part 1
print ( '\n\n\t\t\t\t\tNested lists as game board representations: Part 1\n' )
#Create a function named is_board_correct ( input_board ) that accepts a game board in the format shown in the template code. 
#Function should count number of obstacles on the board (represented by 'x') and return True if there are exactly three obstacles. 
#If there is any other number of obstacles, the function should return False.

game_board = [
	[ '_', '_', 'x', '_', '_' ],
	[ '_', '_', '_', '_', '_' ],
	[ 'x', '_', '_', '_', '_' ],
	[ '_', '_', '_', 'x', '_' ]
]

incorrect_board = [
	[ '_', 'x', 'x' ],
	[ 'x', 'x', '_' ],
	[ '_', '_', '_' ]
]

def is_board_correct ( input_board ) :
	count = 0
	for i in range ( len ( input_board ) ) :
		for j in range ( len ( input_board [ i ] ) ) :
			if input_board [ i ] [ j ] == 'x' :
				count += 1
	if count == 3 :
		return True
	else :
		return False
	return ( count )
#-------------------------------------------------------------------------
print ( is_board_correct ( game_board ) )
print ( is_board_correct ( incorrect_board ) )
#=============================================================
#=============================================================--------------Nested lists game board representations Part 2
print ( '\n\n\t\t\t\t\tNested lists as game board representations: Part 2\n' )
#Write a function that will move the hero one field to the right – unless the field to the right contains an obstacle or is outside the board.
#Inside our function, we iterate over the nested list until we find the field with our hero. Note three things:
#   1. In the inner loop, we iterate in the range ( len ( board [ i ] ) - 1 ). The "minus one" part means that we don't want to look for the hero in the rightmost column – in that case, we couldn't move the hero anyway.
#   2. The field to the right of the hero is board [ i ] [ j + 1 ]. We first check if the field is not occupied by an obstacle and only then return the updated board.
#   3. If we can't find the hero (for instance, when it's in the rightmost column), we simply return the board "as it is."
# Implement another version of the hero_move_right ( board ) function. This time, when the hero stands in the rightmost column and wants to move right, put him in the leftmost column of the same row.

game_board = [
	[ '-', '-', 'x', '-', '-' ],# 0
	[ '-', '-', '-', '-', 'H' ],# 1
	[ 'x', '-', '-', '-', '-' ],# 2
 	[ '-', '-', '-', 'x', '-' ]# 3
#        0  1  2  3   4
]

def hero_move_right ( board ) :
	for i in game_board :# print initial gameboard
		print ( '\t\t\t\t\t' , '  '.join ( i ) )
	space ( )	

	for i in range ( len ( board ) ) :# count down the rows ( 0, 1, 2, 3 ) = total of 4 rows starting at index 0
		for j in range ( len ( board [ i ] ) ) :# count down the columns as i passes down each row above grabbing the index of each element in each colmn starting over with each column ( 0, 1, 2, 3, 4, 0, 1, 2, 3, 4 ) = 5 columns or 5 elements in each row 
#s			print ( j )
			n = j + 1# replace j with new variable that starts counting at 1 instead of 0 = 1, 2, 3, 4, 5
			if n >= len ( board [ 1 ] ):# if the variable is >= 5
				n = 0
			if board [ i ] [ j ] == 'H' and board [ i ] [ n ] != 'x' :
				board [ i ] [ j ] = '-'
				board [ i ] [ n ] = 'H'
		
				for i in board :
					print ( '\t\t\t\t\t', '  '.join ( i ) )
				space ( )
				return ''

	for i in board :
		print ( '\t\t\t\t\t', '  '.join ( i ) )
	space ( )
	return ''
#-------------------------------------------------------------------------
print ( hero_move_right ( game_board ) )
#=============================================================
#=============================================================--------------Copying nested lists - Manual method
print ( '\n\n\t\t\t\t\tCopying nested lists - Manual method\n' )
donations = [
	[ 345.0, 287.80, 119.27, 329.30 ],
	[ 294.25, 349.0, 178.90, 262.34 ],
	[ 401.0, 456.45, 289.43, 319.27 ]
] 

new_donations = [ ]
#building a copy of nested list one element at a time by appending each element to an empty list 
for i in donations :
	temp_placement = [ ]
	for j in i :
		temp_placement.append ( j )
	new_donations.append ( temp_placement )
space ( )
for i in new_donations :
	print ( i )
space ( )
#---------------------------------------------------------------------------------------------------------------
#Create a function named remove_negative ( nested_list ) that accepts a nested list of numbers.
#The function should return a copy of the nested list with all the negative numbers removed.

sample_numbers = [
	[ 34, -52, 349, 0, 32 ],
	[ 45, 245, 823, 1, 234, -358 ],
	[ 98, -234, -32, -324, -342, 543 ]
]

def remove_negative ( nested_list ) :
	for i in nested_list :
		print ( i )
	space ( )
	
	no_negatives = [ ]
	for i in nested_list :
		temp_positive = [ ]
		for j in i :
			if j == abs ( j ) :
				temp_positive.append ( j )
		no_negatives.append ( temp_positive )
	for i in no_negatives :
		print ( i )	
#	return no_negatives
	return ''
#-------------------------------------------------------------------------
print ( remove_negative ( sample_numbers ) )
#=============================================================
#=============================================================--------------Copying nested lists - deep copy
print ( '\n\n\t\t\t\t\tCopying nested lists - deep copy\n' )

import copy

donations = [
	[ 345.0, 287.80, 119.27, 329.30 ],
	[ 294.25, 349.0, 178.90, 262.34 ],
	[ 401.0, 456.45, 289.43, 319.27 ]
]
new_donations = copy.deepcopy ( donations )

#Create a function named copy_all_caps ( nested_list ) that accepts a nested list of strings and returns a new list with all strings printed in uppercase letters. 
#Don't modify the input list.
#Use the string_name.upper() method to turn all strings into uppercase letters.			
			
hackathon_results = [
	[ 'HackKittens', '01011Brasil', 'GoForCode' ],
	[ '01011Brasil', 'NullPointerException', 'WeAreCode' ],
	[ 'FromIndiaWithCode', 'MutexLovers', 'HackKittens' ],
	[ 'WeAreCode', 'HackKittens', 'ThePythonists' ]
]			

def copy_all_caps ( nested_list ) :
	uppers = [ ]
	for i in nested_list :
		temp = [ ]
		for j in i :
			temp.append ( j.upper ( ) )
		uppers.append ( temp )
	return uppers				
#-------------------------------------------------------------------------
print ( copy_all_caps ( hackathon_results ) )
#=============================================================
#=============================================================--------------Transposing nested lists
print ( '\n\n\t\t\t\t\tTransposing nested lists\n' )
n_list = [
	[ 1, 4, 7, 10 ],
	[ 2, 5, 8, 11 ],
	[ 3, 6, 9, 12 ]
]
list_to_return = [ ]
for i in range ( len ( n_list [ 0 ] ) ) :# iterate over the length of the first nested list, i.e., over the "columns"
	new_row = [ ]#variable for new row created ( an empty list )
	for j in range ( len ( n_list ) ) :# iterate over the outer list's length, i.e, over the "rows"
		new_row.append ( n_list [ j ] [ i ] )#to grab elements via metjod x [ i ] [ j ] one must use for i in range ( len (....)
						       # Add the i-th element from each nested list 
	list_to_return.append ( new_row )# add the new row to the new list 
	
for i in list_to_return :
	print ( i )
space ( )
#---------------------------------------------------------------------------------------------------------------
#Write a function named vertical_flip ( input_list ) that accepts a 2D list and flips it vertically:
s_list = [
	[ 'a1', 'b1', 'c1', 'd1', 'e1' ],
	[ 'a2', 'b2', 'c2', 'd2', 'e2' ],
	[ 'a3', 'b3', 'c3', 'd3', 'e3' ]
]
def vertical_flip ( in_list ) :
	for i in in_list :
		print ( i )
	space ( )

	return_list = [ ]
	for i in range ( len ( in_list [ 0 ] ) ) :
		new_row = [ ]
		for j in range ( len ( in_list ) ) :
			new_row.append ( in_list [ j ] [ i ] )
		return_list.append ( new_row )
	
	for i in return_list :
		print ( i )
	return ''
#-------------------------------------------------------------------------
print ( vertical_flip ( s_list ) )
#=============================================================
#=============================================================--------------Summary
print ( '\n\n\t\t\t\tSummary\n' )
str_list = [
	[ 'a1', 'b1', 'c1', 'd1', 'e1' ],# 0
	[ 'a2', 'b2', 'c2', 'd2', 'e2' ],# 1
	[ 'a3', 'b3', 'c3', 'd3', 'e3' ]# 2
#        0    1    2    3   4
]

int_list = [
	[ 1, 4, 7, 10 ],
	[ 2, 5, 8, 11 ],
	[ 3, 6, 9, 12 ]
]
print ( '\niterating through nested lists:\n' )
for row in str_list :
	for cell in row :
		print ( cell )
print ( 'Grabbing a particular cell' )
print ( str_list [ 1 ] [ 3 ] )
print ( '\nIterating over indexes of a nested list\n' )
for i in range ( len ( str_list ) ) :
	for j in range ( len ( str_list [ i ] ) ) :
		print ( j, str_list [ i ] [ j ] )# -- returns index number, cell associated with index number 
#=============================================================
#=============================================================--------------Quiz 1
print ( '\n\n\t\t\t\t\tQuiz 1\n' )
#Create a function named count_stats ( input_data ), which accepts a 2-dimensional list with numerical elements and returns a tuple with the following three items:
# ( minimum list value, maximum list value, sum of all values )

sample_data = [
	[ 342.3, -34.34, 3489.3, 8834.2 ],
	[ 6430.0, -123.8, 342.9 ]
]

def count_stats ( input_data ) :
	temp_number = [ ]
	sum_values = 0
	for row in input_data :
		for cell in row :
			sum_values += cell
			temp_number.append ( cell )
	return min ( temp_number ), max ( temp_number ), sum_values
#-------------------------------------------------------------------------
print ( count_stats ( sample_data ) )
#=============================================================
#=============================================================--------------Quiz 2
print ( '\n\n\t\t\t\t\tQuiz 2\n' )
#Create a function named hero_move_down ( board ) that accepts a game board and moves the hero ( 'H' ) one field down and returns the modified board. 
#Do not move the hero if the new field is occupied by an obstacle ( 'x' ) or is outside the game board.

game_board = [
	[ '-', '-', 'x', '-', '-' ],# 1
	[ '-', 'H', '-', '-', '-' ],# 2
	[ 'x', '-', '-', '-', '-' ],# 3
	[ '-', '-', '-', 'x', '-' ]# 4
]#       1  2  3  4   5

def hero_move_down ( board ) :
	for row in board :
		print ( '\t\t\t\t\t', '  '.join ( row ) )
	space ( )
	
	for i in range ( len ( board ) ) :
		r = i + 1
		if r >= len ( board ) :
			r = 0	
		for j in range ( len ( board [ i ] ) ) :
			if board [ i ] [ j ] == 'H' and board [ r ] [ j ] != 'x' and r != 0 :
				board [ i ] [ j ] = '-'
				board [ r ] [ j ] = 'H'
		
				for i in board :
					print ( '\t\t\t\t\t', '  '.join ( i ) )
				space ( )
				return ''

	for i in board :
		print ( '\t\t\t\t\t', '  '.join ( i ) )
	space ( )
	return ''
#-------------------------------------------------------------------------
print ( hero_move_down ( game_board ) )
space ( )


