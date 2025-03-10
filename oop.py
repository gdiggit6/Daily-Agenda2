#!/bin/python3
#!/usr/bin/env python
#-*- coding: utf-8 -*-
#--------------------------------------------------------------------------------------------------------
from sys import argv
#script, names, tofile = argv
#--------------------------------------------------------------------------------------------------------
def space ( ) :
	print ( '\n' )	
#--------------------------------------------------------------------------------------------------------
# Classes allow us to logically group our data and functions in a way that's easy to reuse and build upon
# Data and functions associated with a specific Class are called attributes and methods of that Class	
# A Class is a blueprint for creating instances
space ( )
class Employee :
	#When accessing Class variables, we need to access them through the Class itself or an instance of the Class (instance variables)
	num_of_emps = 0
	raise_amt = 1.06# Class variable saying 'raise amount by 6 percent'

	def __init__( self, first, last, pay ) :# special init method or "constructor". This receives the instance as the first argument
	# within the init method we set all the instance variables
		self.first = first# instance variable set for each instance of the Employee
		self.last = last# instance variable
		self.pay = pay# instance variable
		self.email = first + '.' + last + '@rockwellautomation.com'
		
		Employee.num_of_emps += 1

	def fullname ( self ) :# <-- Methods automatically take in the instances created above
		return '{} {}'.format ( self.first, self.last )
		
	def apply_raise ( self ) :# <-- Method /The Method automatically takes in the 'instance' we will call 'self'
		self.pay = int ( self.pay * self.raise_amt )# Subclasses can change this amount any time
		
	@classmethod# decorator. Here you are working with the class instead of the instances
	def set_raise_amt ( cls, amount ) :# by convention when using a class variable name, use 'cls' since the word "class" such as above has a different meaning 
		cls.raise_amt = amount
		
	# Using a classmethod as an alternative constructor
	@classmethod
	def from_string ( cls, emp_str ) :
		first, last, pay = emp_str.split ( '-' )
		return cls ( first, last, pay )# this line is what will create the new employee
		
	# Additional constructors
	@classmethod
	def fromtimestamp ( cls, t ) :
		"Construct a date from a PSIX timestamp ( like time.time ( ) ). "
		y, m, d, hh, ss, weekday, jday, dst = _time.localtime ( t )
		return cls ( y, m, d )
		
	@classmethod
	def today ( cls ) :
		"Construct a date from time.time ( )."
		t = _time.time ( )
		return cls.fromtimestamp ( t )
		
	@classmethod
	def fromordinal ( cls, n ) :
		"""Construct a date from a proleptic Gregorian ordinal.		
		January 1 of year 1 is day 1. Only the year, month and day are non-zero in the result.
		"""
		pass
		
	@staticmethod
	def is_workday ( day ) :# static methods don't take in the instance or the class as the first argument, so we can just pass in the arguments we want to work with 
		if day.weekday ( ) == 5 or day.weekday ( ) == 6 :# Saturday or Sunday
			return False# if it doesn't hit this conditional, that means it's a workday
		return True
#---------------------------------------------------------------------------------------------------------------------------------------------
class Developer ( Employee ) :# inherit from the Employee class. By doing this you inherit all its functionality
	pass



#---------------------------------------------------------------------------------------------------------------------------------------------
emp_1 = Developer ( 'Jeremy', 'Marine', 17.65 )
emp_2 = Employee ( 'Liki', 'Johnson', 18.65 )# both of these instances are objects that have their own postitions in memory
emp_3 = Employee ( 'Sarah', 'Emmerson', 15.80 )

import datetime
my_date = datetime.date ( 2023, 11, 21 )

print ( Employee.is_workday ( my_date ) )# prints whether the above date resides on Monday - Friday ( True ), or Saturday or Sunday ( False )

#parcing through strings using the @classmethod when new employees are added that have a different format than above
emp_str_1 = 'John-Doe-19.85'
emp_str_2 = 'Steven-Smith-20.00'
emp_str_3 = 'Jane-Doe-13.75'

new_emp_1 = Employee.from_string ( emp_str_1 )
print ( new_emp_1.email )
print ( new_emp_1.pay )
space ( )
#-------------------------------------------------------------------------------------------------------------------
print ( 'emp_1 pay and applied raise class instance ' )
print ( emp_1.pay )
emp_1.apply_raise ( )
print ( emp_1.pay )
#-------------------------------------------------------------------------------------------------------------------
space ( )

#-------------------------------------------------------------------------------------------------------------------
print ( 'emp_1 pay and raise through classmethod decorator' )
Employee.set_raise_amt ( 1.20 )# automatically accepts the class 

print ( emp_1.pay )
emp_1.apply_raise ( )
print ( emp_1.pay )
#-------------------------------------------------------------------------------------------------------------------
space ( )

print ( Employee.raise_amt )
print ( emp_2.raise_amt )
print ( emp_3.raise_amt )

# -------------------------------------------Instance variables - contain data that is unique to each instance--------------------------------------------------------------------------------
space ( )
print ( emp_1.email )
print ( emp_2.email )
print ( emp_3.email )
space ( )
# manually printing out full name of employee outside the Class
#print ( '{} {}'.format ( emp_1.first, emp_1.last ) )
# print out fullname as defined within the Class structure
print ( emp_1.fullname ( ) )
# --------------------------------------------------------------------Class variables----------------------------------------------------------------------------------------------------
space ( )
'''
print ( emp_1.__dict__ )
emp_1.raise_amount = 1.30# Setting an individual init/instance variable as apposed to an enitre Class method 
space ( )
#Accessing through instance variable
print ( emp_1.raise_amount, 'Set through instance variable' )
print ( emp_2.raise_amount, 'Set through Class variable' )
#Accessing through Class variable
print ( Employee.raise_amount )
space ( )
print ( emp_1.pay, 'emp_1 original pay' )
emp_1.apply_raise ( )
print ( emp_1.pay, 'em_1 After applied instance variable' )
space ( )
'''
space ( )
print ( emp_2.pay, 'emp_2 original pay' )
emp_2.apply_raise ( )
print ( emp_2.pay, 'em_2 After Class instance' )

print ( Employee.num_of_emps )
space ( )
#---------------------------------------------------------------------------------------------Regular, Static & Class Methods---------------------------------------------------------------
	

























space ( )
