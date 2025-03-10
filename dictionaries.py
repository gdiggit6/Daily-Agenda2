#!/usr/bin/env python
#-*- coding: utf-8 -*-

#	alias i='python /home/dbustaflex666/Python/sf_Python/Python Data Structures/Dictionaries/dictionaries.py'
#	alias i='python dictionaries.py names, tofile'
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
space ( )
#=============================================================
#=============================================================--------------------------------------------------------------Dictionaries - Recap----------------------------------------------
# Dictionaries can contain values of any type, but the keys must be immutable - strings, integers, and tuples are allowed, but NOT lists
# You should never add new elements or delete existing elements when iterating over a dictionary

#define dictionary:
scores = { 'John' : 234, 'Mary' : 984, 'Kate' : 453 }
#access an element with the 'kate' key
print ( scores [ 'Kate' ] )
#update a value:
scores [ 'John' ] = 237
print ( scores [ 'John' ] )
#add new element with the 'Alfred' key:
scores [ 'Alfred' ] = 354
#delete an element:
del scores [ 'John' ]
print ( scores )

movies = { 'action' : 7, 'adventure' : 8, 'biography' : 0, 'fantasy' : 5, 'thriller' : 6 }
del movies [ 'biography' ]
movies [ 'western' ] = 3
print ( movies )
# 1. To iterate over dictionary keys:
# 	for k in dictionary :
#	or
#	for k in dictionary.keys ( )
# 2. To iterate over dictionary values:
#	for v in dictionary.values ( ):
# 3. To get both values and keys:
#	for k, v in dictionary.items ( ):
# 4. Dictionarys are often used to count elements:
#votes = [...]
#dict_results = { }
#for k in votes:
#	if k not in dict_results:
#		dict_results [ v ] = 0
#	dict_results [ v ] += 1
# 5. The syntax above can be simplified to:
#votes = [...]
#dict_results = { }
#for v in votes:
#	dict_results [ v ] += dict_results.get ( v, 0 ) + 1
# 6. Dictionaries are also used to group elements by a given characteristic, for instance:
#names = [...]
#groups_dict = { }
#for n in names:
#	key = len ( n )
#	if key not in groups_dict :
#		groups_dict [ key ] = [ ]
#	groups_dict [ key ].append ( n )
# 7. Update the values in a dictionary based on another dictionary :
#dict_1.update ( dict_2 )
#=============================================================
#=============================================================--------------------------------------------------------------dictionaries - iterating methods - review----------------------------------------------
print ( '\n\n\t\t\t\tDictionaries - iterating methods - review\n' )
# Tourist_arrivals dictionary contains numbers of tourist arrivals in years 2012 - 2017
tourist_arrivals = {
	  2017 : 17430580,
	  2016 : 15594157,
	  2015 : 14343323,
	  2014 : 13128416,
	  2013 : 12433727,
	  2012 : 11835160
}
#-------------------------------------------------------------------------------------------------------------------------------------iterate over the keys ( Method 1 )
counter = 0
for k in tourist_arrivals : # i iterates over years in left column
	if k > 2014 : 
		counter += tourist_arrivals [ k ] # adds the value associated with the year key to counter
print ( counter )
#-------------------------------------------------------------------------------------------------------------------------------------iterate over the keys ( Method 2 )
counter2 = 0
for k in tourist_arrivals.keys ( ) :
	if k > 2014 :
		counter2 += tourist_arrivals [ k ] 
print ( counter2 )
space ( )
#-------------------------------------------------------------------------------------------------------------------------------------iterate over the values ( Method 3 )
counter3 = 0
for v in tourist_arrivals.values ( ) :
	counter3 += v
print ( '\nTotal tourist arrivals in Croatia in years 2012-2017: ' + str ( counter3 ) )
# to get both keys and values
max_year = 0
max_arrivals = 0
for k, v in tourist_arrivals.items ( ) :
	if v > max_arrivals : # as v passes through the values, 1st value will be greater than 0, 
		max_arrivals = v # max_arrivals now the value in dictionary. If the next value is less, ignore it. Else max_arrivals gets the value that is more than the previous ultimately
#                                    acquiring the maximum value in the dictionary
		max_year = k
print ( '\nThe best year in terms of tourist arrivals was ' + str ( max_year ) + ' with ' + str ( max_arrivals ) + ' arrivals.' ) 
#-------------------------------------------------------------------------------------------------------------------------------------
# Create a function that accepts a dictionary and returns the difference between the best and worst exam results.
# The results are integers between 0 and 100
exam_results = {
	  'Dominic Vargas'	: 67,
	  'Marion Riley'	: 89,
	  'Candice White'	: 45,
	  'Doreen Goodwin'	: 82,
	  'Janet Hunter'	: 98,
	  'Jaime Page'		: 32,
	  'Neil Fernandez'	: 76,
	  'Jana Frank'		: 38,
	  'Adrienne Perkins'	: 98,
	  'Rosa Mccarthy'	: 34
}

def get_results_range ( exam ) :
	top_score = 0 # set to 0 since any value will continue to be greater which is the goal of the code: each subsequent value following a previous lower one will now replace that lower one
	bottom_score = 100 # reverse logic applied to finding the lowest score
	for v in exam.values ( ) :
		if v > top_score : # same principle of finding greatest score by comparing v to previous value
			top_score = v
		if v < bottom_score :
			bottom_score = v
	return '\nThe difference between the best and worst exam results to a score of ' + str ( top_score - bottom_score ) + ' ( ' + str ( top_score ) + ' - ' + str ( bottom_score ) + ' ).'
print ( get_results_range ( exam_results ) )
#=============================================================
#=============================================================--------------------------------------------------------------Modifying elements in a dictionary----------------------------------------------
print ( '\n\n\t\t\t\tModifying elements in a dictionary\n' )
# Jessica plays a game in which she serves restaurant customers. You are given a dictionary with:
# the names of customers currently sitting ( keys )
# waiting time in minutes ( 1st value in tuple )
# status - if person is still waiting:
#	( 'still waiting' )
#	( 'got the food' )
#	( 'left without eating' ) - customer waits 20 minutes or more

# modify the status of customers who have waited for 20 minutes or more ( and their status is NOT 'got the food'. 
# count how many customers have left

restaurant_customers = { 
	  'John Steven'	: ( 10, 'still waiting' ),
	  'Jane Black'		: ( 5, 'still waiting' ),
	  'Mark Dawson'	: ( 15, 'got the food' ),
	  'Janet Roberts'	: ( 30, 'left without eating' ),
	  'John Parker'	: ( 22, 'still waiting' ),
	  'Anne Edwards'	: ( 18, 'got the food' ),
	  'Mary Rogers'	: ( 7, 'got the food' ),
	  'Emma Reed'	: ( 35, 'got the food' ),
	  'Sophia Steven'	: ( 25, 'still waiting' ),
	  'Amelia Cook'	: ( 32, 'still waiting' ),
	  'John Scott'		: ( 15, 'still waiting' ),
	  'George Famous'	: ( 20, 'still waiting' ),
	  'Jack Baker'		: ( 38, 'got the food' )
}

counter = 0
for k in restaurant_customers :
# k = customer names
# restaurant_customers [ k ] = ( time, status )
	time, status = restaurant_customers [ k ] # takes the two elements from each tuple and separates them into the individual variables
	if time >= 20 and status != 'got the food' : # the customer has been waiting for 20 or more minutes and STILL doesn't have their fucking food...
		status = 'left without eating' # change their status the fact that they walked out
	if status == 'left without eating' : # modify status variable from 'still waiting' to 'left without eating'
		counter += 1 # tally up a dissatisfied customer who left
	restaurant_customers [ k ] = time, status # modify the status of those customers who have waited 20 or more minutes from still waiting to 'left without eating'
print ( str ( counter ) + ' customers left.' )
#=============================================================
#=============================================================--------------------------------------------------------------Counting elements with dictionaries----------------------------------------------
print ( '\n\n\t\t\t\tCounting elements with dictionaries\n' )
# dictionaries are typically used to count how many times a given item appears in a list
platform = [ 'Smartphone', 'Smartphone', 'Desktop', 'Laptop', 'Laptop', 'Laptop', 'Desktop', 'Smartphone', 'Smartphone', 'Laptop' ]
mut = { } # mut = "most used tech"
for device in platform : # pass through each element in the list
	if device not in mut : # if current element in the pipe is not in mut variable
		mut [ device ] = 0 # create a new entry in the dictionary
	mut [ device ] += 1 # add 1 value to the appropriate key already in the dictionary
print ( mut )
space ( )
#-------------------------------------------------------------------------------------------------------------------------------------
# 1. Count the number of votes for each name stored in the variable votes 
# 2. Find the name with the most votes and print { name } is the winner!
votes = [
		'Biden', 'Biden', 'Trump', 'Clinton', 'Desantes', 'Trump', 'Desantes', 'Biden', 'Clinton', 'Biden', 'Trump', 'Desantes', 
		'Biden', 'Biden', 'Desantes', 'Desantes', 'Trump', 'Desantes', 'Clinton', 'Clinton', 'Trump', 'Desantes', 'Biden', 'Desantes' 
]
counted_votes = { }
for i in votes :
	if i not in counted_votes :
		counted_votes [ i ] = 0
	counted_votes [ i ] += 1
count_values = counted_votes.values ( )
max_vote_count = max ( count_values )

for k, v in counted_votes.items ( ) :
	if v == max_vote_count :
		print ( str ( k ) + ' is the winner!' )
#=============================================================
#=============================================================--------------------------------------------------------------Counting elements in tuples with dictionaries----------------------------------------------
print ( '\n\n\t\t\t\tCounting elements with tuples in dictionaries\n' )

nonanon_platform = [ 
		( 'John', 'Smartphone' ), ( 'Alice', 'Smartphone' ), ( 'Kate', 'Desktop' ), ( 'Mary', 'Laptop' ), ( 'Mark', 'Laptop' ), 
		( 'Tim', 'Laptop' ), ( 'Michael', 'Desktop' ), ( 'Samantha', 'Smartphone' ), ( 'Adrian', 'Smartphone' ), ( 'Gray', 'Laptop' )
]
pmu = { } # "platform most used"
for device in nonanon_platform : # pass through each element in the list
	_, platform = device # unpack the tuple, skip name, just assign device to platform variable
	if platform not in pmu : # if current element in the pipe is not in pmu variable
		pmu [ platform ] = 0 # create a new entry in the dictionary for the platform
	pmu [ platform ] += 1 # add 1 value to the appropriate key already in the dictionary
print ( pmu )
space ( )
#-------------------------------------------------------------------------------------------------------------------------------------
# Two data structures
# 1. users - a LIST of TUPLES, in which each tuple contains a user's name along with there respective nationality
# 2. nationality_to_continents - a DICTIONARY in which nationalities are keys and continents are values
users = [# LIST
#      ( 'name', 'nationality ), ( 'name', 'nationality ), ( 'name', 'nationality ),
	( 'Maria', 'Greek' ), ( 'Jean', 'Maltese' ), ( 'Juan', 'Spanish' ), # tuples with ( names, nationality )
	( 'Dima', 'Ukrainian' ), ( 'Agata', 'Thai' ), ( 'Rafal', 'Polish' ),
	( 'Diego', 'Turkish' ), ( 'Stan', 'Panamanian' ), ( 'John', 'Australian' ), 
	( 'Frank', 'Belgian' ), ( 'Jane', 'Canadian' ), ( 'Paul', 'Argentinian' ),
	( 'Taylor', 'Danish' ), ( 'Kate', 'American' ), ( 'Mark', 'Sri Lankan' ), 
	( 'Jane', 'Japanese' ), ( 'Ted', 'Indian' ), ( 'Jean', 'Egyptian' ) 
]

nationality_to_continents = {
#	'nationality' : 'continent', 'nationality' : 'continent', 'nationality' : 'continent'
	'Greek' : 'Europe', 'Maltese' : 'Europe', 'Spanish' : 'Europe',
	'Ukrainian' : 'Europe', 'Thai' : 'Asia', 'Polish' : 'Europe',
	'Turkish' : 'Asia', 'Panamanian' : 'Central America', 'Australian' : 'Australia',
	'Belgian' : 'Europe', 'Canadian' : 'North America', 'Argentinian' : 'South America',
	'Danish' : 'Europe', 'American' : 'North America', 'Sri Lankan' : 'Asia',
	'Japanese' : 'Asia', 'Indian' : 'Asia', 'Egyptian' : 'Africa'
}

users_continents = { }
for k, v in nationality_to_continents.items ( ) :
	if v not in users_continents :
		users_continents [ v ] = 0
	users_continents [ v ] += 1
print ( users_continents )
#=============================================================
#=============================================================--------------------------------------------------------------The get ( ) function---------------------------------------------
print ( '\n\n\t\t\t\tThe get ( ) function\n' )
#pmu = { } # "platform most used"
#for device in nonanon_platform : # pass through each element in the list
#	_, platform = device # unpack the tuple, skip name, just assign device to platform variable
#	if platform not in pmu : # if current element in the pipe is not in pmu variable
#		pmu [ platform ] = 0 # create a new entry in the dictionary for the platform
#	pmu [ platform ] += 1 # add 1 value to the appropriate key already in the dictionary
pmu = { }
for device in nonanon_platform :
	_, platform = device
	pmu [ platform ] = pmu.get ( platform, 0 ) + 1
print ( pmu )
space ( )
#-------------------------------------------------------------------------------------------------------------------------------------
employees = [
	( 'Maria', 'Polish' ), ( 'Jean', 'French' ), ( 'Juan', 'Spanish' ), ( 'Dima', 'Ukrainian' ),
	( 'Agata', 'Polish' ), ( 'Rafal', 'Polish' ), ( 'Diego', 'Spanish' ), ( 'Stan', 'Ukrainian' ) 
]
n_nationalities = { }
for e in employees :
	_, nationality = e
	n_nationalities [ nationality ] = n_nationalities.get ( nationality, 0 ) + 1
print ( n_nationalities )
#=============================================================
#=============================================================--------------------------------------------------------------Summing up values---------------------------------------------
print ( '\n\n\t\t\t\tSumming up values\n' )
# We have a list, inside the list are tuples with game results.
# Each person can take part in one or more games ( each tuple with person's name represents the different game along with their points )
# Each tuple within the list presents all points that the participants collected:
game_results = [ 
	( 'John', 9 ), ( 'Mike', 8 ), 
	( 'Anne', 5 ), ( 'Anne', 10 ), 
	( 'Kate', 8 ), ( 'Kate', 7 ), 
	( 'John', 3 ), ( 'Anne', 6 )
]
# Task is to sum up the points for each person and present the results as a dictionary
total_game_points = { }
for i in game_results : # collect each individual tuple
	name, points = i # unpack the tuples as they run down the pipe
	total_game_points [ name ] = total_game_points.get ( name, 0 ) + points
print ( total_game_points )
space ( )
#-------------------------------------------------------------------------------------------------------------------------------------
# Three people - Mike, John, and Tom - measured the length of their jumps in centimeters.
# Create a dictionary which will store the names as keys and the average length of their jumps as values
jumps = [
	( 'Mike', 283 ), ( 'Mike', 317 ), ( 'Mike', 302 ),
	( 'John', 305 ), ( 'John', 311 ), ( 'John', 297 ),
	( 'John', 308 ), ( 'Tom', 341 ), ( 'Tom', 256 )
]
sum_distance = { }
number_of_jumps = { }
avg_results = { }

for tup in jumps :# collect each tuple
	name, distance = tup# unpack each tuple, separate the key and put it in the variable 'name', separate the value and put it in the variable 'distance'
	sum_distance [ name ] = sum_distance.get ( name, 0 ) + distance
	number_of_jumps [ name ] = number_of_jumps.get ( name, 0 ) + 1
for i in number_of_jumps :
	avg_results [ i ] = sum_distance [ i ] / number_of_jumps [ i ]
print ( avg_results )
#=============================================================
#=============================================================--------------------------------------------------------------Tuples as dictionary keys---------------------------------------------
print ( '\n\n\t\t\t\tTuples as dictionary keys\n' )
# You have a flowerbed divided into a checkerboard-like field - 5 rows and 5 columns. There may be more than one flower in a given cell. 
# We want to know how many flowers there are in each non-empty cell. 
flowers = [
	( ( 0, 3 ), 'violet' ), 
	( ( 1, 2 ), 'sunflower' ),
	( ( 0, 3 ), 'forget-me-not' ), 
	( ( 3, 4 ), 'violet' ),
	( ( 0, 3 ), 'poppy' ), 
	( ( 1, 2 ), 'forget-me-not' )
]
flower_counts = { }
for f in flowers :# grab each tuple
	position, _ = f
	flower_counts [ position ] = flower_counts.get ( position, 0 ) + 1
print ( flower_counts )
space ( )
#-------------------------------------------------------------------------------------------------------------------------------------
# Count how many times a combo was thrown
dice_throws = [ ( 4, 3 ), ( 5, 6 ), ( 1, 3 ), ( 4, 3 ), ( 5, 5 ), ( 5, 6 ), ( 1, 3 ), ( 4, 3 ) ]
#             ( first_dice = 4, second_dice = 3 )
resulting_throws = { }
for i in dice_throws :
	( first_dice, second_dice ) = i
	resulting_throws [ ( first_dice, second_dice ) ] = resulting_throws.get ( ( first_dice, second_dice ), 0 ) + 1
print ( resulting_throws )
#=============================================================
#=============================================================--------------------------------------------------------------Grouping with dictionaries---------------------------------------------
print ( '\n\n\t\t\t\tGrouping with dictionaries\n' )
# Grouping based on name length. 
names = [ 'John', 'Mary', 'Alice', 'Kate', 'Michael', 'Samantha', 'Adrian', 'Gray' ] 
groups = { }
#-----------------------------------------------without using .get
for i in names :# grab each name from the list
	key = len ( i )
	if key not in groups :# if length is not an existing key in the dictionary,
		groups [ key ] = [ ]# create a key and initialize it with an empty list
	groups [ key ].append ( i )# append the given name to a given key represented as the name's length
print ( groups )
space ( )
#----------------------------------------------using .get
groups.clear ( )
for i in names :
	key = len ( i )
	groups [ key ] = groups.get ( key, [ ] ) + [ i ]
print ( groups )
space ( )
#-------------------------------------------------------------------------------------------------------------------------------------
# Given a list of tuples that store information about airports
# Each tuple consists of the airport's name and number of runways
airport_runways = [
	( 'Warsaw', 2 ),
	( 'Vienna', 2 ),
	( 'Franfurt', 4 ),
	( 'London Heathrow', 2 ),
	( 'Fukuoka', 1 ),
	( 'Madrid', 4 )
]
# create a dictionary which will group all airport names by the number of runways. 
# the keys should represent the number of runways
# the values should store lists of airport names
runways = { }
# -------------------------------------------------------------------------------------------------------without .get
for i in airport_runways :
	name, num_run = i
	if num_run not in runways :
		runways [ num_run ] = [ ]
	runways [ num_run ].append ( name )
print ( runways )
space ( )
# -------------------------------------------------------------------------------------------------------using .get
runways.clear ( )
for i in airport_runways :# collect the tuples in the list
	name, num_run = i# unpack each tuple and assign the key to the variable 'name', assign the value to the variable 'num_run'
	runways [ num_run ] = runways.get ( num_run, [ ] ) + [ name ]
print ( runways )
#=============================================================
#=============================================================--------------------------------------------------------------Grouping with dictionaries - anagrams---------------------------------------------
print ( '\n\n\t\t\t\tGrouping with dictionaries - anagrams\n' )
# Anagrams are words which contain the same letters in a different order ( dear, read, dare, etc )
# write a function which will accept a list of words ( strings ) and return a dictionary with the following properties:
# 1. the keys should store the strings from the input list with their letters sorted alphabetically
# 2. the values of each key should contain a list of words from the input list which are anagrams for the given key
words = [ 
	'jeremy', 'michael', 'marine', 'bembenek', 'gracie', 
	'jynx', 'dagon', 'jaina', 'jasmine', 'read', 
	'dear', 'dare', 'gallery', 'recasts', 'casters', 
	'bird', 'largely', 'actress', 'remain', 'allergy' 
]
def find_anagrams ( word_list ) :
	anagrams = { }
	for i in word_list :
		key = ''.join ( sorted ( i ) )# sort the letters in each word alphabetically
		anagrams [ key ] = anagrams.get ( key, [ ] ) + [ i ]
	return anagrams
print ( find_anagrams ( words ) )
#=============================================================
#=============================================================--------------------------------------------------------------Linking dictionaries---------------------------------------------
print ( '\n\n\t\t\t\tLinking dictionaries\n' )
# Linking dictionaries is creating a new dictionary with the current parameter values based on existing dictionaries which are chained in a specific order.
defaults = { 'weight' : 80.0, 'height' : 1.82, 'age' : 28.0 }
user_profile = defaults.copy ( )# the user_profile is a copy of the dictionary defaults

# You are given a dictionary with salaries 2017
# Create a copy of this salary and name it salaries_2018
# In 2018 everyone got a 10% raise. 
# Update the 2018 dictionary to reflect the rise - each value in salaries_2018 should be an integer 
# Finally, print both dictionaries and observe that the values in the dictionary salaries_2017 were not modified. This confirms salaries_2018 is a separate dictionary

salaries_2017 = { 'Anna' : 4000, 'Mark' : 5000, 'Jane' : 5500, 'John' : 3000 }
salaries_2018 = salaries_2017.copy ( )# make a copy of the above dictionary
for k in salaries_2018.keys ( ) :
	salaries_2018 [ k ] = int ( salaries_2018 [ k ] * 1.1 )
print ( salaries_2017 )
print ( salaries_2018 )
#=============================================================
#=============================================================--------------------------------------------------------------The update ( ) function---------------------------------------------
print ( '\n\n\t\t\t\tThe update ( ) function\n' )
# the next function needed for linking dictionaries
salaries_2018 = { 
	'Anna' :	 4400, 
	'Mark' :	 5500, 
	'Jane' 	:	 6050, 
	'John' :	 3300 
}
salaries_update = { 'Anna' : 5500, 'Mary' : 4000 }
salaries_2018.update ( salaries_update )
print ( salaries_2018 )
#=============================================================
#=============================================================---------------------------------------------------------------Linking with dictionaries---------------------------------------------
print ( '\n\n\t\t\t\tLinking with dictionaries\n' )

default_profile = { 
	'Weight'	: 100.0,
	'Height'	: 69.6,
	'Age'		: 28.0 
}

user_input_dict = { }

for k in default_profile.keys ( ) :# grab the strings weight, height, age
	user_input = input ( 'Enter ' + k + ' or press ENTER for default: ' )
	if user_input != '' :# if user enters a value
		user_input_dict [ k ] = float ( user_input )# store that value in a new dictionary 'user_input_dict'
# Linkin process
user_profile = default_profile.copy ( )# link a copy of the default values to new user_profile dictionary
user_profile.update ( user_input_dict )# update that profile with the values now contained in user_input_dict
print ( user_profile )
user_input_dict.clear ( )
space ( )
#-------------------------------------------------------------------------------------------------------------------------------------
# Create a function that returns a regional settings dictionary for a given user.
# Should contain 3 elements:
# 1. language
# 2. currency
# 3. timezone
# The logic is as follows:
# 1. If there is a value for the given key in user_settings, use that setting
# 2. If there is no value, use the value in computer_settings
# 3. If there is no value in computer_settings, use the default value

c_input = { 
	'language' : 'Polish'
}
u_input = {
	'timezone' : 'UTC'
}

def get_regional_settings ( c_settings, u_settings ) :# 
	defaults = { 
	'language' : 'English',
	'currency' : 'USD',
	'timezone' : 'PST'
	}
	user_input_dict = { }
	for k in defaults.keys ( ) :# grab the keys from the default dictionary
		user_input_dict.update ( c_settings )# update the empty user_input_dict to reflect the key 'language' and corresponding value 'Polish' piped through the variable c_settings
		user_input_dict.update ( u_settings )# update the empty user_input_dict to reflect the key 'timezone' and corresponding value 'UTC' piped through the variable u_settings
	user_profile = defaults.copy ( )# create a copy of the defaults
	user_profile.update ( user_input_dict )
	return ( user_profile )

print ( get_regional_settings ( c_input, u_input ) )
#=============================================================
#=============================================================---------------------------------------------------------------Quiz - Question 1---------------------------------------------
print ( '\n\n\t\t\t\tQuiz - Question 1\n' )
# create a function that accepts any dictionary with string values and returns the averagage length of all the string values
titles = {
	2016 : 'Running To the Moon', 
	2008 : 'When we are naughty', 
	2017 : 'On the Beach' 
}
def get_mean_length ( input_dict ) :
	dic_length = 0
	dic_length_list = [ ]
	for v in input_dict.values ( ) :
		dic_length += len ( v )
		dic_length_list.append ( v )
	return ( round ( dic_length / len ( dic_length_list ), 2 ) )
print ( get_mean_length ( titles ) )
#=============================================================
#=============================================================---------------------------------------------------------------Quiz - Question 2---------------------------------------------
print ( '\n\n\t\t\t\tQuiz - Question 2\n' )
# Create a function that accepts a list of strings and returns a tuple with 2 elements:
# 1. the string which appears most frequently in the list
# 2. the number of appearances of that string 
from b_dic import book_listing

def get_most_frequent_elements ( string_list ) :# book_listing from b_dic.py 
	duplicates = { }
	for i in string_list :# go through each string element in the list
		if i in duplicates :# check duplicates dictionary, if no listing of element currently in the pipe:
			duplicates [ i ] += 1# add the string element to duplicates
		else :
			duplicates [ i ] = 1# if yes add the number to the value section associated with the sting element key
	counter = 0
	most_freq = ( )
	
	for k, v in duplicates.items ( ) :# check the key-value pairs in the duplicates dictionary
		if v > counter :# if the value is greater than 0
			counter = v# set the counter to the number of times it sees the repeated string elements
			most_freq = ( k, counter )# add the key-value set to the most_freq tuple
	return ( most_freq )
print ( get_most_frequent_elements ( book_listing ) )
space ( )

