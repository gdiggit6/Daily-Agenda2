#!/usr/bin/env python
#-*- coding: utf-8 -*-

#	alias s='python /home/dbustaflexitlap/Python/sf_Python/sets.py'
#	alias s='python sets.py names, tofile'
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
print ( '\n\n\t\t\t\t\tSets\n' )
letters = { 'a', 'c', 'd', 'e', 'f' }# set
letters2 = ( 'a', 'c', 'd', 'e', 'f' )# tuple
letters3 = [ 'a', 'c', 'd', 'e', 'f' ]# list

letters.add ( 'b' )# add an element
letters.discard ( 'e' )# remove an element
#letters.clear ( )# remove all elements

print ( type ( letters ), type ( letters2 ), type ( letters3 ) )# set, tuple, list
print ( sorted ( letters ) )
space ( )
#=============================================================
#=============================================================------------Sets - Count unique letters--------------------------------------------
print ( '\t\t\t\t\tSets - Count unique letters\n' )
unique_letters = 'bembenek'

def count_unique_letters ( word_string ) :# pass unique_letters through function
	u = set ( )# initialize empty set 
	for i in word_string :# go through each string element
		u.add ( i )# add each element to the u set 
#	print ( sorted ( u ) )# sort the elements and print them one by one
	return ( word_string, len ( u ) )# return the length of the u set, which will only contain unique letters due to the nature of sets
#---------------------------------------------------------------------------
print ( count_unique_letters ( unique_letters ) )
space ( )
#=============================================================
#=============================================================----------Sets - creating sets from lists
print ( '\t\t\t\t\tSets - Creating sets from lists\n' )
cities = [ 'Ladysmith', 'Bruce', 'Eau Claire', 'Cameron', 'Tony', 'Cameron', 'Ladysmith', 'Hayward' ]
print ( list ( cities ), ' <--- cities list', len ( cities ) )
print ( set ( cities ), ' <--- set of elements', len ( set ( cities ) ) )
print ( list ( set ( cities ) ), ' <--- list of the set of elements', len ( list ( set ( cities ) ) ), '\n' )
#---------------------------------------------------------------------------
# You are given a dictionary ( people_cars ) that maps people's names to their car models
# Create a set named car_models that contains only the unique car models found in the people_cars dictionary
people_cars = { 
	'James' : 'Audi', 'Sonya' : 'Honda', 'Anna' : 'Volkswagen', 'Heather' : 'Bentley', 
	'Tim' : 'Toyota', 'Kim' : 'Honda', 'Oliver' : 'Toyota', 'Sam' : 'Bentley'
}

car_models = set ( )# empty set that will contain just the values ( car models ) from the dictionary
for v in people_cars.values ( ) :# focus on value part of the people_cars dictionary
	car_models.add ( v )# add the string values to the car_models set
print ( car_models )
print ( sorted ( car_models ) )# alphabetical representation
space ( )
#=============================================================
#=============================================================---------------Sets - creating lists with unique elements
print ( '\t\t\t\t\tSets - Creating lists with unique elements\n' )
#John, Mark and Stephanie listened to some songs,. We stored the songs they listened to in the order they listened to them in a dictionary named songs_in_order. Now we'd like to create a playlist for each listener. In the playlist, each song should occur only once.
#Create a dictionary named playlists, in which you will store a list of the songs listened to by John, Mark, and Stephanie (in no particular order). Any song that was played many times should occur only once in the list.

songs_in_order = {
  'John'	: [ 
  			'Girls Like You', 'Shallow', 'Faded', 'Sugar', 'Girls Like You', 'Dancing With A Stranger', 'Happy', 'Happy', 'Happy' 
  			], 
  'Mark'	: [ 
  			'Shallow', 'Freaky', 'I can\'t get enough', 'A thousand years', 'A thousand years', 'Rolling in the Deep', 'Someone Like You', 'Rolling in the Deep', 'Halo', 'On The Floor', 'Hello', 				'Shallow' 
  			], 
  'Stephanie'	: [ 
  			'Dua Lipa', 'Shallow', 'Dua Lipa', 'Taki Taki', 'Chandelier', 'Chandelier', 'Blank Space', 'Blank Space', 'Counting Stars', 'Wake Me Up', 'Dua Lipa' 
  			]
}
playlists = { }# initialize empty dictionary
for name, songs in songs_in_order.items ( ) :# for key, values in dictionary items
	playlists [ name ] = list ( set ( songs ) )# create a list of keys for playlists for each key-value pair from songs_in_order dictionary
#--------------------------------------------------------------------------------
#print ( playlists, '\n' )#   <--- initial objective
for k, v in playlists.items ( ) :
	print ( k, v )#   <--- cleaner output 
space ( )
#=============================================================
#=============================================================------------Sets - creating sets with unique element characteristics
print ( '\t\t\t\t\tSets - Creating sets with unique element characteristics\n' )
cities = [ 'Ladysmith', 'Bruce', 'Weyerhaeuser', 'Ladysmith', 'Weyerhaeuser', 'Cameron', 'Rice Lake', 'Ladysmith' ]
first_letters = set ( )
for i in cities :# 
	first_letters.add ( i [ 0 ] )# as i passes through each string, collect the element residing in index 0 of each string and put it in first_letters
print ( first_letters )
#=============================================================

# key rings must be made made particular to the car model found in the people_cars dictionary.
# the size of each key ring will depend on the number of letters in the car model name.
# create a set called car_model_lengths and add all unique car model name length values to it.
# print the following:
# "There will be { x } different sizes of key rings."

car_model_lengths = set ( )
for v in people_cars.values ( ) : # take the values
	car_model_lengths.add ( len ( v ) ) # add the length of that value to the car_model_lengths set 
print ( '\nThere will be', len ( car_model_lengths ), 'different sizes of key rings.\n' ) # count how many elements are in the set 
#=============================================================
#=============================================================------------Anagrams again
print ( '\t\t\t\t\tAnagrams again\n' )
# In the previous part ( code below ) I wrote a function which returned a dictionary of anagrams.
# Here we will count how man "anagram classes" there are.
# Write a function that accepts a list of words ( strings ) and returns the number of different anagram classes in the list.
# [ 'bacd', 'bcad', 'bcda', 'adf' ]
# the correct output is 2.
# The words 'bacd', 'bcad' and 'bcda' are anagrams, so they count as one "anagram class". The word 'adf' is not their anagram, so it belongs to a different class.
# The simplest way to solve this exercise is to use sets. For each word in the list, compute its canonical anagram (e.g. its letters sorted in alphabetical order) and add them to the set. Then return the number of elements in the set.

from b_dic import book_listing
anagram_check = [ 'dog', 'cat', 'dog', 'tac', 'god', 'bird' ]
anagram_check2 = [ 'bacd', 'bcad', 'bcda', 'adf' ]

def find_anagrams ( string_elemets ) :
	anagrams = { }
	for i in string_elemets :
		key = ''.join ( sorted ( i ) )# sort the letters in each word alphabetically
		anagrams [ key ] = anagrams.get ( key, [ ] ) + [ i ]
	return anagrams
print ( find_anagrams ( anagram_check ) )
#--------------------------------------------------------------------------------
space ( )
def count_classes ( string_elemets ) :
	anagram_classes = { }
	for i in string_elemets : # run through the element strings in the list 
		k = ''.join ( sorted ( i ) )
		anagram_classes [ k ] = anagram_classes.get ( k, [ ] ) + [ i ]
	space ( )
	return ( len ( k ) )
print ( count_classes ( anagram_check ) )
#=============================================================
#=============================================================------------Set operations - review
print ( '\n\n\t\t\t\t\tSet operations - review\n' )

nums = { 1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11 }
nums2 = { 2, 4, 6, 8, 8, 9, 10, 11, 12, 13, 13 }
#           1  2   3   4  5   6  7  8   9 10  11 12
words = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'g', 'h', 'i', 'j', 'k' }
words2 = { 'b', 'd', 'f', 'h', 'i', 'j', 'k' }

#1. To find elements that are BOTH in set A AND set B ( in other words, to find the INTERSECTION of sets A and B ) :
print ( sorted ( nums.intersection ( nums2 ) ) )
print ( sorted ( nums & nums2 ) )

print ( sorted ( words.intersection ( words2 ) ) )
print ( sorted ( words & words2 ) )
space ( )
#2. To find elements that are EITHER in set A OR set B ( in other words, to find the UNION of sets A and B - Combine all elements of both sets into one ) :
print ( sorted ( nums.union ( nums2 ) ) )
print ( sorted ( nums | nums2 ) )

print ( sorted ( words.union ( words2 ) ) )
print ( sorted ( words | words2 ) )
space ( )
#3. To find elements that are in set A but NOT in set B ( to find the difference of sets A and B ) :
print ( sorted ( nums.difference ( nums2 ) ) )
print ( sorted ( nums2 - nums ) )

print ( sorted ( words.difference ( words2 ) ) )
print ( sorted ( words2 - words ) )
space ( )
#4. To find elements that are either in set A OR set B but NOT in BOTH sets ( to find the symmetric difference of sets A and B ) :
print ( sorted ( words.symmetric_difference ( words2 ) ) )
print ( sorted ( words2 ^ words ) )
space ( )
#5. Check if set A is a subset of set B :
print ( words.issubset ( words2 ) )
print ( words <= words2 )# is A a subset of B?
print ( words2 <= words )# is B a subset of A?
space ( )
#6. Check if A is a superset of set B :
print ( words.issuperset ( words2 ) )
print ( words >= words2 )
#--------------------------------------------------------------------------------
space ( )
# Write a function that accepts two string
# The function should check if we can create one of these strings using the letters from the other string ( using each letter as many times as we need to )
# the function should return True if word1 can be created from the letters in word2, or if word2 can be created from word1.
# Return False otherwise

word1 = [ 'sun' ]
word2 = [ 'sunsettings' ]
word3 = 'sun'
word4 = 'sunset'

def check_words ( w1, w2 ) :
	x = set ( )
	y = set ( )
	for i in w1 : 
		for j in i :
			x.add ( j )
	for i in w2 :
		for j in i :
			y.add ( j )
	return ( x, y, y >= x or x >= y )
print ( 'word1 & word2: ', check_words ( word1, word2 ) )
print ( 'word3 & word4: ', check_words ( word3, word4 ) )
space ( )
#--------------------------------------------------------------------------------
# the code below is slightly addapted to the fact that the strings below that check_words2 will parse are not a part of a list as above, thereby not necessitating another for loop as above
# a for loop will count a string within a list as a single element, as opposed to a variable directly holding a string which will then count every character as an individual element. 
word_string1 = 'sun'
word_string2 = 'sunset'

def check_words2 ( w1, w2 ) :
	x = set ( )
	y = set ( )
	for i in w1 :
		x.add ( i )
	for i in w2 :
		y.add ( i )
	return ( y >= x or x >= y )
print ( check_words2 ( word_string1, word_string2 ) )
#=============================================================
#=============================================================------------Set operations - exercise
print ( '\n\n\t\t\t\t\tSet operations - exercise\n' )

#Sports hall rented by basketball and volleyball players
#Players buy passes each month.
#There are three monthly passes available: 
#volleyball = $50 per person
#basketball = $45 per person
#both = $60 per person
#calculate how much money the sports hall will earn in a month

volleyball_players = { 
	'John Williams', 'Tom Jones', 'Jessica White', 'James Moore', 'Anne Davis', 'Lara Taylor', 'Conrad Anderson', 'Ronald Martin', 
	'Harry Thompson', 'Anne Wilson', 'Stephanie Lewis', 'Ted Garcia', 'Jane Walker', 'Paul Clark' 
}	
basketball_players = { 
	'John Robinson', 'Steven Clark', 'Jessica White', 'Andrew Rodiguez', 'James Moore', 'Sam Taylor', 'Conrad Anderson', 
	'James Martin', 'Ron Miller', 'Olivia Allen', 'Sophia King', 'Anne Wilson' 
}

v = set ( volleyball_players )
b = set ( basketball_players )

x = len ( v & b ) * 60
y = len ( v - b ) * 50
z = len ( b - v ) * 45
print ( x + y + z )
#=============================================================
#=============================================================------------Multiple set operations
print ( '\n\n\t\t\t\t\tMultiple set operations\n' )

volleyball_players = { 
	'John Williams', 'Tom Jones', 'Jessica White', 'James Moore', 'Anne Davis', 'Lara Taylor', 'Conrad Anderson', 'Ronald Martin', 
	'Harry Thompson', 'Anne Wilson', 'Stephanie Lewis', 'Ted Garcia', 'Jane Walker', 'Paul Clark' 
	}
basketball_players = { 
	'John Robinson', 'Steven Clark', 'Jessica White', 'Andrew Rodiguez', 'James Moore', 'Sam Taylor', 'Conrad Anderson', 'James Martin', 
	'Ron Miller', 'Olivia Allen', 'Sophia King', 'Anne Wilson' 
	}
football_players = { 
	'Liam Boss', 'Emma Lees', 'Amelia Cooper', 'William Howard', 'Oliver Harris', 'Alexander Perry', 'Andrew Rodiguez', 'James Moore', 
	'Michael Long', 'Conrad Anderson', 'Emily Young', 'Samuel Bennett', 'Chloe Richardson', 'Sam Taylor', 'Jackson Perez', 'Charlotte Wright', 
	'David Scott', 'James Moore', 'Oliver Ward', 'Henry Rogers', 'John Harris', 'Victoria Smith', 'Harper Johnson', 'Joseph Allen', 'Nora Brown' 
	}

all_players = set ( volleyball_players | basketball_players | football_players )
new_players = set ( football_players - ( basketball_players | volleyball_players ) )
print ( '\nThere are', len ( all_players ), 'players using the hall,', len ( new_players ), 'of which are new players.' )
#=============================================================
#=============================================================------------Simulating the pawn's moves
print ( '\n\n\t\t\t\t\tSimulating the pawn\'s moves\n' )
# Create a function that return s the position of the pawn after maing a move.
# current_position is a tuple representing the position of the pawn before making a move

def next_position ( current_position, m ) :
	x, y = current_position# ( 0, 0 )
	if m == 'left' :
		new_position = ( x - 1, y )
	elif m == 'right' :
		new_position = ( x + 1, y )
	elif m == 'up' :
		new_position = ( x, y + 1 )
	else :
		new_position = ( x, y - 1 )
	return new_position# ( 1, 0 )

print ( next_position ( ( 0, 0 ), 'right' ) )
print ( next_position ( ( 1, 0 ), 'right' ) )# 1
print ( next_position ( ( 2, 0 ), 'up' ) )# 2
print ( next_position ( ( 2, 1 ), 'down' ) )# 3
print ( next_position ( ( 2, 0 ), 'up' ) )# 4
print ( next_position ( ( 2, 1 ), 'left' ) )# 5 <-- repeat
print ( next_position ( ( 1, 1 ), 'left' ) )# 6 <-- repeat
print ( next_position ( ( 0, 1 ), 'down' ) )# 7
print ( next_position ( ( 0, 0 ), 'right' ) )# 8 <-- repeat
#     ( next_position ( ( 1, 0 ) <-- repeat
#=============================================================
#=============================================================------------Cycle detection
print ( '\n\n\t\t\t\t\tCycle detection\n' )
def next_position ( current_position, move ) :
	x, y = current_position
	if move == 'left' :
		new_position = ( x - 1, y )
	elif move == 'right' :
		new_position = ( x + 1, y )
	elif move == 'up' :
		new_position = ( x, y + 1 )
	else :
		new_position = ( x, y - 1 )
	return new_position
#--------------------------------------------------------------------------------
def repeated_position ( c, moves ) :# c = new_position == ( 1, 0 ), new_position == ( 2, 0 )...
	positions = set ( )
	positions.add ( c )
	counter = 0

	for i in moves :# i == 'right', i == 'right'...
		new_position = next_position ( c, i )# new_position = ( 1, 0 ), new_position = ( 2, 0 )...
		if new_position in positions :
#			return new_position# invoking this will kick you out of loop
			counter += 1
			print ( 'Move', counter, ': ------->  ',  new_position, ' <-- Repeat!' )
			c = new_position
		else :
			counter += 1
			positions.add ( new_position )
			print ( 'Move', counter, ':', new_position )
			c = new_position
	space ( )
	return positions, counter#       <---  comment out the above return call and comment out return -1 if you want to use this for a more verbose output
#	return - 1
print ( repeated_position ( ( 0, 0 ), [ 'right', 'right', 'up', 'down', 'up', 'left', 'left', 'down', 'right' ] ) )	
#=============================================================
#=============================================================------------Simulating machines with sets
print ( '\n\n\t\t\t\t\tSimulating machines with sets\n' )
sm1 = [ 1, 2, 3, 1, 2 ]
sm2 = [ 1, 1, 3, 2, 2, 2 ]
sm3 = [ 1, 1, 1, 1, 3, 1 ]

def count_states ( m_list ) :
	current_levels = ( 0, 0 )
	past_levels = { ( 0, 0 ) }

	for i in m_list :
#		print ( '\nState: ', i, '\n' )
		x, y = current_levels
#		print ( 'current levels: ', ( x, y ), '\n' )
#-----------------------------------------
		if i == 1 :
			new_levels = ( min ( x + 1, 10 ), y )
#			print ( 'new_levels: ', new_levels, '\n' )
		elif i == 3 :
			new_levels = ( x, max ( y - 1, 0 ) )
		else :
			if x > 0 and y < 10 :
				new_levels = ( x - 1, y + 1 )
			else :
				new_levels = ( x, y )				
#---------------------------------------
		if new_levels in past_levels :
			return len ( past_levels )
#			print ( '\nNew level recorded already: ', 'New level: ', new_levels, ' Past levels: ', past_levels, ' Number of elements in past_levels: ', len ( past_levels ), '\n' )
		else :
			past_levels.add ( new_levels )
#			print ( 'New level added to past_levels: ', past_levels )
			current_levels = new_levels		
#---------------------------------------
	return - 1
#	return ''
#---------------------------------------------------------------------------------------------------
#print ( count_states ( sm1 ) )
print ( count_states ( sm3 ) )
space ( )
#=============================================================
#=============================================================------------word banks
print ( '\n\n\t\t\t\t\tWord banks\n' )
# A letter bank of a word is the set of unique letters in this word, i.e, the letter bank for "mississippi" is "ismp" and the letter bank for "road" is "adro"
# Write a function called count_letter_banks ( words ) which, given a list of words, computes the number of different letter banks for words in the list 
w_list = [ 'add', 'dad', 'recasts', 'ercasts', 'creasts' ]# 5 words

def count_letter_banks ( arg_a ) :# takes a list of strings [ 'aabb', 'abcc', 'blahblah'...]
	word_bank = set ( )# dad & add each = 'add' which is two words, 1 word bank of the same set of elements
	for i in arg_a :# i = 'add', 'dad', 'recasts'...
		word_bank.add ( ''.join ( sorted ( set ( i ) ) ) )# set = { 'c', 'a', 'b' } --> sorted ( set ) = ( 'a', 'b', 'c' } --> ''.join ( sorted ( set ) = abc
	return word_bank, len ( word_bank )
#-----------------------------------------------------------------------------------------------------------------
print ( count_letter_banks ( w_list ) )
space ( )
#=============================================================
#=============================================================--------------------------------------------------------------Sets - unique menu ingredients--------------------------------------------
print ( '\n\t\t\t\tSets - Unique menu ingredient list\n' )
menu = {
	'Meat Pie'		: [ 'pork', 'potato', 'paprika', 'egg', 'cream' ],
	'Broccoli Chicken'	: [ 'chicken', 'broccoli', 'cream' ],
	'Eggy Chicken'	: [ 'chicken', 'egg' ],
	'Tortilla Espanola'	: [ 'egg', 'onion', 'potato' ]
}

def count_unique_ingredients ( dishes ) :
	ingredient_list = [ ]
	unique_list = set ( )

	for i in dishes.values ( ) :
		for j in i :
			ingredient_list.append ( j )
	for i in ingredient_list :
		unique_list.add ( ''.join ( i ) )

	return unique_list, len ( unique_list )
#------------------------------------------------------------------------------------------------------------
print ( count_unique_ingredients ( menu ) )
space ( )
