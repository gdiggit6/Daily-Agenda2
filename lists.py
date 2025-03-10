#!/usr/bin/env python
#-*- coding: utf-8 -*-

#	alias l='python /home/dbustaflexitlap/Python/sf_Python/lists.py'
#	alias l='python lists.py names, tofile'
#	grep -r 'phrase' /home/dbustaflexitlap/Python/sf_Python/
#	cp -ruv /home/dbustaflex666/Python/ /media/sf_Python/
#       grep -r --exclude-from=b_dic.py [ 'phrase' ] /home/dbustaflex666/Python/

#	12!!#8FG
# 	#&x9$g!JeV65VQAp
#       PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
from sys import argv
import datetime
#script, names, tofile = argv
#=============================================================
def space ( ) :
	print ( '\n' )	
#=============================================================
print ( '\n\t\t\t\tLists warm-up\n' )
#remove the UAE from list
#Add Japan to the list
#for each country in the modified list, print: { country } contains { len ( country ) } letters!
countries = [ 'Thailand', 'Vietnam', 'Malaysia', 'UAE' ]
print ( ', '.join ( countries ),'\n' )
countries.remove ( 'UAE' )
countries.append ( 'Japan' )
print ( ', '.join ( countries ), '\n' )
for i in countries :
	print ( i + ' contains ' + str ( len ( i ) ) + ' letters!\n' )
#=============================================================
#=============================================================-------------------------------Iterating over list elements--------------------------------------------------------------
print ( '\n\t\t\t\tIterating over list elements\n' )
#Track the amount of time I studied each day. Each element in the list represents n minutes studied in a day.
#to find the average study duration value:
minutes = [ 368, 690, 426, 494, 445, 690, 426, 494, 445, 690, 423, 534, 606, 390 ] 
t_minutes = 0 # added elements from the list
counter = 0 # this number will be used in the avg formula

for element in minutes :
	counter += 1 # element 1, 2, 3...
	t_minutes += element # e1, e1 + e2, ( e1 + e2 ) + e3...
t_avg = round ( ( t_minutes / counter ) / 60, 2 )# 60 turns the total avg from minutes to hours 
print ( 'In a', len ( minutes ), 'day period, I studied for', t_avg, 'hours.\n' )
#=============================================================

monthly_spendings = [ 2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45, 3000.00, 2000.00 ]
# My spending for n months falls into 3 categories:
low = 0 # below 2000.0
medium = 0 # between 2000.0 and 3000.0
high = 0 # above 3000.0

for i in monthly_spendings :
	if i < 2000.0 : # take n and compare it to i, ie. is 2689.58 < 2000.0? If True, then:
		low += 1
	elif i >= 2000.0 and i <= 3000.0 :
		medium += 1
	else :
		high += 1
#---------------------------------------------------------------------------------------------------------------
print ( 'My spending was low for ' + str ( low ) + ' months, ' + 'medium for ' + str ( medium ) + ' months and high for ' + str ( high ) + ' months.\n' )
#=============================================================
#=============================================================-------------------------------Iterating over list elements with enumerate ( )--------------------------------------------------------------
print ( '\n\t\t\t\tIterating over lists elements with enumerate ( )\n' )
minutes = [ 368, 690, 426, 494, 445, 690, 426, 494, 445, 690, 423, 534, 606, 390 ] 
t_minutes = 0 # added elements from the list
counter = 0 # this number will be used in the avg formula

for index, element in enumerate ( minutes ) : # index = 0, 1, 2...  |  element = 368, 690....
#                                         mon - sun              mon - sun      mon - fri ( 1st week )   mon - fri ( 2nd week )
#	if 0 <= index % 7 and index % 7 <= 4 : this is the same as the statement below excluding the 'and'
	if 0 <= index % 7 <= 4 : # 0, 1, 2, 3, 4, 5, 6,   |   0, 1, 2, 3, 4, 5, 6   -->  0, 1, 2, 3, 4  |  0, 1, 2, 3, 4
#                                           0 - 6                    7 - 14                 0 - 4           7 - 11
		counter += 1
		t_minutes += element
t_avg = round ( ( t_minutes / counter ) / 60, 2 )# 60 turns the total avg from minutes to hours 
#---------------------------------------------------------------------------------------------------------------
print ( 'In a', len ( minutes ), 'day period, I studied for', t_avg, 'hours.\n' )# avg will reflect two five-day periods rather than two 7-day periods as above
#=============================================================

# I'm interested in knowing avg expenses in each half of year.
# Compute avg expenses for 1st half ( jan - Jun )
# Compute avg expenses for 2nd half ( Jul - Dec )
# i = index;  e = element
sum_expenses = [ 0, 0 ]
for i, e in enumerate ( monthly_spendings ) :
	if i < 6 :
		sum_expenses [ 0 ] += e # element
	else :
		sum_expenses [ 1 ] += e
#---------------------------------------------------------------------------------------------------------------
print ( '\nAverage expense Jan-June: {}'.format ( round ( sum_expenses [ 0 ] / 6, 2 ) ) )
print ( 'Average expense July-Dec: {}'.format ( round ( sum_expenses [ 1 ] / 6, 2 ) ) )
#=============================================================
#=============================================================-------------------------------Updating list elements--------------------------------------------------------------
print ( '\n\n\t\t\t\tUpdating list elements\n' )
# In a previous exercise, I forgot to include phone bills in the monthly spending totals. 
# Add 20.50 to each element in the monthly_spendings list and print the output.
print ( 'Before monthly update:', monthly_spendings )
monthly_spendings = [ 2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45, 3000.00, 2000.00 ]
for e in range ( len ( monthly_spendings ) ) :
	monthly_spendings [ e ] += 20.50
#---------------------------------------------------------------------------------------------------------------
print ( '\nAfter monthly update:', monthly_spendings )
#print ( monthly_spendings )
#=============================================================
#=============================================================-------------------------------Changing the order of list elements--------------------------------------------------------------
print ( '\n\n\t\t\t\tChanging the order of list elements\n' )
ls_elements = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ]
print ( 'Before swap:', ls_elements )
for e in range ( len ( ls_elements ) ) :
	if e % 2 == 0 :
		temp_v = ls_elements [ e + 1 ]
		ls_elements [ e + 1 ] = ls_elements [ e ]
		ls_elements [ e ] = temp_v
#---------------------------------------------------------------------------------------------------------------
print ( '\nAfter swap:', ls_elements )
#=============================================================
#=============================================================-------------------------------Changing the order of elements without using a temp variable--------------------------------------------------------------
print ( '\n\n\t\t\t\tChanging the order of elements without using a temp variable\n' )
ls_elements = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ]
print ( 'Before swap:', ls_elements )
for e in range ( len ( ls_elements ) ) :
	if e % 2 == 0 :
		ls_elements [ e + 1 ], ls_elements [ e ] = ls_elements [ e ], ls_elements [ e + 1 ]
#---------------------------------------------------------------------------------------------------------------
print ( '\nAfter swap:', ls_elements )
#=============================================================
#=============================================================-------------------------------Deleting list elements - Creating a temporary copy of list elements--------------------------------------------------------------
print ( '\n\n\t\t\t\tDeleting list elements - Creating a temporary copy of list elements\n' )
# Some erroneous data must be removed from the monthly spendings list. 
# Remove all values less than 100
monthly_spendings = [ 2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 34.89, 52.67, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45, 3000.00, 2000.00 ]
#                                                                      erroneous values
for i in monthly_spendings [ : ] :
	if i < 100 :
		monthly_spendings.remove ( i )
#---------------------------------------------------------------------------------------------------------------
print ( monthly_spendings )
#=============================================================
#=============================================================-------------------------------Creating new lists based on existing ones--------------------------------------------------------------
print ( '\n\n\t\t\t\tCreating new lists based on existing ones\n' )
celsius_temp = [ -10, -7.78, -5, -2.78, 0, 1.67 ]
fahrenheit_temp = [ ]
for i in celsius_temp :
	fahrenheit_temp.append ( round ( i * 1.8 + 32 ) )
#---------------------------------------------------------------------------------------------------------------
print ( 'Celsius:', celsius_temp )
print ( 'Fahrenheit:', fahrenheit_temp, '\n' )
#=============================================================

# convert monthly spendings from U.S. dollars to Euros
monthly_spendings = [ 2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45 ]
monthly_spendings_eur = [ ]
for i in monthly_spendings :
	monthly_spendings_eur.append ( round ( i * 0.88, 2 ) )
#---------------------------------------------------------------------------------------------------------------
print ( 'Dollars:', monthly_spendings )
print ( 'Euros:', monthly_spendings_eur )
#=============================================================
#=============================================================-------------------------------Comparing two lists of the same size--------------------------------------------------------------
print ( '\n\n\t\t\t\tComparing two lists of the same size\n' )
mark_study_min = [ 340, 520, 378, 494, 445, 623, 432, 534, 606, 390 ] 
kate_study_min = [ 546, 462, 474, 440, 299, 541, 399, 547, 471, 388 ] 
counter = 0

for i in range ( len ( mark_study_min ) ) : # 0, 1, 2, 3, 4...
	if mark_study_min [ i ] > kate_study_min [ i ] : # compare elements in each list
		counter += 1
#---------------------------------------------------------------------------------------------------------------
print ( '\n', counter, '\n' )
#=============================================================

# Create a new list named household_monthly_spendings containing the total monthly expenses ( defined as the sum of mark and kate's expenses )
mark_monthly_spendings = [ 2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45 ]
kate_monthly_spendings = [ 1969.62, 3939.37, 2241.59, 3968.27, 3068.80, 1755.02, 3885.66, 2491.67, 3828.49, 3171.32, 2771.32, 3380.37 ]
household_monthly_spendings = [ ]

for i in range ( 0, len ( kate_monthly_spendings ) ) :
	household_monthly_spendings.append ( round ( kate_monthly_spendings [ i ] + mark_monthly_spendings [ i ] ) )
#---------------------------------------------------------------------------------------------------------------
print ( household_monthly_spendings )
#=============================================================
#=============================================================-------------------------------Comparing two lists of different sizes--------------------------------------------------------------
print ( '\n\n\t\t\t\tComparing two lists of different sizes\n' )
#In 2017, Martha had two credit cards: one that she used during the whole year, and another she used for the first six months
#Create a new list containing total monthly spendings for the entirety of 2017. 
#Round the sums to integers
card1 = [ 3231.22, 3039.49, 2813.55, 2271.80, 1922.53, 2335.07 ]
#            0         1        2         3         4        5
card2 = [ 3883.04, 3073.93, 3727.18, 2340.49, 1651.91, 1585.41, 2025.84, 3367.66, 2442.75, 2395.70, 3328.55, 3453.42 ]
#            0          1        2         3         4        5
total_spendings = [ ]

for e, v in enumerate ( card2 ) :
	if 0 <= e % 12 and e % 12 < 6 :
		total_spendings.append ( round ( card2 [ e ] + card1 [ e ] ) )

for e, v in enumerate ( card2 ) :
	if not ( 0 <= e % 12 and e % 12 < 6 ) :
		total_spendings.append ( round ( card2 [ e ] ) )
#---------------------------------------------------------------------------------------------------------------
print ( total_spendings )
#=============================================================
#=============================================================-------------------------------Merging two sorted lists--------------------------------------------------------------
print ( '\n\n\t\t\t\tMerging two sorted lists\n' )
# Suppose we have study times for two weeks in two separate, sorted lists:
week1 = [ 301, 346, 378, 410, 420 ]
week2 = [ 289, 317, 367, 414, 454 ]
# Create a common list containing all values from week1 and week2, sorted by amount:
i, j = 0, 0 # temp variables
sorted_weeks = [ ]

while i < len ( week1 ) and j < len ( week2 ) : # temp variables representing current indices. Loop continues until the end of either the two lists
	if week1 [ i ] < week2 [ j ] :
		sorted_weeks.append ( week1 [ i ] )
		i += 1
	else :
		sorted_weeks.append ( week2 [ j ] )
		j += 1
# at some point, either i or j will point to the end of its list, but other variagble will still point to some remaining values in the other list.
# that's why we need to add those remaining elements after the while loop terminates:
sorted_weeks += week1 [ i : ]
sorted_weeks += week2 [ j : ]
#---------------------------------------------------------------------------------------------------------------
print ( '\n' + str ( sorted_weeks ) ) # using + str rather than ',' will prevent tab space when printing out
#=============================================================

# Given two lists: one showing monthly spending in 2017
# The other 2018 monthly spending
# However, both lists are sorted in descending order. Merge these lists into a new list named all_sorted_spendings
# New list should be sorted in descending order

ms_2017 = [ 3890.45, 3328.2, 3267.12, 3182.2, 3147.3, 2770.38, 2689.56, 2545.72, 2462.61, 2394.04, 2099.91, 1746.83 ]
ms_2018 = [ 3883.04, 3727.18, 3453.42, 3367.66, 3328.55, 3073.93, 2442.75, 2395.7, 2340.49, 2025.84, 1651.91, 1585.41 ]

i, j = 0, 0
all_sorted_spendings = [ ]

while i < len ( ms_2017 ) and j < len ( ms_2018 ) :
	if ms_2017 [ i ] > ms_2018 [ j ] :
		all_sorted_spendings.append ( ms_2017 [ i ] )
		i += 1
	else :
		all_sorted_spendings.append ( ms_2018 [ j ] )
		j += 1

all_sorted_spendings += ms_2017 [ i : ]
all_sorted_spendings += ms_2018 [ j : ]
#---------------------------------------------------------------------------------------------------------------
print ( '\n' + str ( all_sorted_spendings ) )
#=============================================================
#=============================================================-------------------------------Intersection of two sorted lists--------------------------------------------------------------
print ( '\n\n\t\t\t\tIntersection of two sorted lists\n' )
# Finding common elements in two sorted lists
# Create a new sorted list named common_study_times
# List must contain elements common to both lists

my_study_times = [ 268, 290, 323, 326, 345, 394, 434, 506, 590, 590 ]
kate_study_times = [ 268, 299, 323, 440, 474, 546, 562, 590 ]

i, j = 0, 0
common_study_times = [ ]

while i < len ( my_study_times ) and j < len ( kate_study_times ) :
	if my_study_times [ i ] < kate_study_times [ j ] :
		i += 1
	elif my_study_times [ i ] > kate_study_times [ j ] :
		j += 1
	else :
		common_study_times.append ( kate_study_times [ j ] )
		i += 1
		j += 1
#---------------------------------------------------------------------------------------------------------------
print ( common_study_times )
#=============================================================
#=============================================================-------------------------------Working with Book LIsting--------------------------------------------------------------
print ( '\n\n\t\t\t\tWorking with Book Listing\n' )
from b_dic import book_listing, craft_books
import random

def books ( x ) :
	book_list = [ ]
	for i in sorted ( set ( x ) ) :
		book_list.append ( i )
	for i in book_list :
		print ( i )
	space ( )
	return len ( book_list )
#---------------------------------------------------------------------------------------------------------------
#print ( books ( book_listing ) )
#=============================================================
#=============================================================-------------------------------List summary questions--------------------------------------------------------------
print ( '\n\n\t\t\t\tList summary questions - Question 1\n' )
#function accepts a list of strings and returns new list containing only words at least as long as the minimum length provided as the second argument
def get_long_title_entries ( in_list, minimum_len ) :
	new_list = [ ]
	for i, values in enumerate ( sorted ( set ( in_list ) ) ) :
		if len ( values ) >= minimum_len :
			new_list.append ( values )
	for i in new_list :
		print ( i )
	return len ( new_list ) 
#---------------------------------------------------------------------------------------------------------------
print ( get_long_title_entries ( book_listing, 65 ) )
#---------------------------------------------------------------------------------------------------------------
print ( '\n\n\t\t\t\tList summary questions - Question 2\n' )
#write a function named get_sorted_union ( list1, list2 ) that accepts two sorted integer lists and returns a new sorted list containing unique values from both lists.
#function 'without repetition'
def get_sorted_union ( list1, list2 ) :
	new_sorted_list = list ( set ( list1 ) | set ( list2 ) )
	return sorted ( new_sorted_list )
#---------------------------------------------------------------------------------------------------------------
#print ( get_sorted_union ( book_listing, craft_books ) )
print ( get_sorted_union ( my_study_times, kate_study_times ) )
space ( )
#---------------------------------------------------------------------------------------------------------------
print ( '\n\t\t\t\tMaintained repetition\n' )

list1 = [ 1, 3, 5, 7, 9 ]
list2 = [ 1, 2, 3, 6, 8, 9, 10 ]

def union ( x, y ) :
	new_list = x + y
	return new_list
#---------------------------------------------------------------------------------------------------------------
print ( union ( list1, list2 ) )
#---------------------------------------------------------------------------------------------------------------
print ( '\n\t\t\t\tMaintained repetition and order\n' )
def union2 ( x, y ) :
	new_list = sorted ( x + y )
	return new_list
#---------------------------------------------------------------------------------------------------------------
print ( union2 ( list1, list2 ) )
#---------------------------------------------------------------------------------------------------------------
print ( '\n\t\t\t\tWithout repetition\n' )
def union3 ( x, y ) :
	new_list = list ( set ( x ) | set ( y ) )
	return new_list
#---------------------------------------------------------------------------------------------------------------
print ( union3 ( list1, list2 ) )
space ( )


