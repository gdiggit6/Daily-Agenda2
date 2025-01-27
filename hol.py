#!/bin/python3
#!/usr/bin/env python
#-*- coding: utf-8 -*-
#--------------------------------------------------------------------------------------------------------
from sys import argv
import datetime
#script, names, tofile = argv
#--------------------------------------------------------------------------------------------------------
def space ( ) :
	print ( '\n' )	
#--------------------------------------------------------------------------------------------------------
class Holiday :
	def __init__( self, month, day, year ) :
		self.month = month
		self.day = day
		self.year = year

	def fulldate ( self ) :
		return '{} {}, {}'.format ( self.month, self.day, self.year )


imbolc = Holiday ( 'February', 2, 2023 )
ostara = Holiday ( 'March', 3, 2023 )

space ( )
print ( imbolc.fulldate ( ) )
print ( ostara.fulldate ( ) )
















space ( )
