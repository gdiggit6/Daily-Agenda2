#!/bin/python3
#!/usr/bin/env python
#-*- coding: utf-8 -*-

#-----------------------Linux to Host------------------------
#	cp -r /home/dflex/python/ /media/sf_newpython

#-----------------------copy from host to virtual OS------------------------
#	mv /media/sf_Python/manipura_rosewood.PNG /home/dflex/Pictures/Rounds/; chmod 777 /home/dflex/Pictures/ -R; chown dflex /home/dflex/Pictures/ -R; chgrp dflex /home/dflexPictures/ -R

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
def begin ( ) :
	while True :
		import random
		now = datetime.datetime.today ( )
		print ( '\n\t\t\t\t\t\t\tDaily Agenda' )
		print ( '\t\t\t\t\t\t' + now.strftime ( '%A, %B %e, %Y' ) )

# Sabbat datetimes
		imbolc = datetime.datetime ( 2024, 2, 2 )#			1
		ostara = datetime.datetime ( 2024, 3, 19 )#			2
		beltane = datetime.datetime ( 2024, 5, 6 )#		3
		litha = datetime.datetime ( 2024, 6, 20 )#			4
		lammas = datetime.datetime ( 2024, 8, 1 )#			5
		hecatesDay = datetime.datetime ( 2024, 8, 13 )
		mabon = datetime.datetime ( 2024, 9, 22 )#		6
		samhain = datetime.datetime ( 2024, 11, 7 )#		7
		yule_2024 = datetime.datetime ( 2024, 12, 21 )
		
		yule_2023 = datetime.datetime ( 2023, 12, 21 )

# US Holiday datetimes
		martinday = datetime.datetime ( 2024, 1, 15 )
		daylightSavings = datetime.datetime ( 2024, 3, 10 )	
		eclipse = datetime.datetime ( 2024, 3, 24 )
		easterSunday = datetime.datetime ( 2024, 3, 31 )
		solar_eclipse = datetime.datetime ( 2024, 4, 8 )
		mayday = datetime.datetime ( 2024, 5, 1 )
		motherDay = datetime.datetime ( 2024, 5, 12 )
		memorialDay = datetime.datetime ( 2024, 5, 27 )
		independenceDay = datetime.datetime ( 2024, 7, 4 )
		laborDay = datetime.datetime ( 2024, 9, 2 )
		eclipse2 = datetime.datetime ( 2024, 9, 18 )
		allhollows = datetime.datetime ( 2024, 10, 31 )
		daylightSavingsEnds = datetime.datetime ( 2024, 11, 3 )
		veteranDay = datetime.datetime ( 2024, 11, 11 )
		thanksgiving = datetime.datetime ( 2024, 11, 28 )
		christmas = datetime.datetime ( 2023, 12, 25 )
		newYear = datetime.datetime ( 2024, 1, 1 )
		
		christmas24 = datetime.datetime ( 2024, 12, 25 )
		newYear25 = datetime.datetime ( 2025, 1, 1 )

# New Moon datetimes 
		new_moon_jan = datetime.datetime ( 2024, 1, 11 ) 
		new_moon_feb = datetime.datetime ( 2024, 2, 9 )
		new_moon_march = datetime.datetime ( 2024, 3, 10 ) 
		new_moon_april = datetime.datetime ( 2024, 4, 8 ) 
		new_moon_may = datetime.datetime ( 2024, 5, 7 ) 
		new_moon_jun = datetime.datetime ( 2024, 6, 6 ) 
		new_moon_july = datetime.datetime ( 2024, 7, 5 ) 
		new_moon_august = datetime.datetime ( 2024, 8, 4 ) 
		new_moon_sep = datetime.datetime ( 2024, 9, 2 ) 
		new_moon_oct = datetime.datetime ( 2024, 10, 2 ) 
		new_moon_nov = datetime.datetime ( 2024, 11, 1 ) 
		new_moon_dec1 = datetime.datetime ( 2024, 12, 1 )
		new_moon_dec2 = datetime.datetime ( 2024, 12, 30 )
		
		new_moon_jan_2025 = datetime.datetime ( 2025, 1, 11 )

# Full Moon datetimes
		full_moon_jan = datetime.datetime ( 2024, 1, 25 ) #5:48am
		full_moon_feb = datetime.datetime ( 2024, 2, 24 ) #10:56am
		full_moon_march = datetime.datetime ( 2024, 3, 25 ) #2:17pm
		full_moon_april = datetime.datetime ( 2024, 4, 23 ) #1:55pm
		full_moon_may = datetime.datetime ( 2024, 5, 23 ) #11:14am
		full_moon_june = datetime.datetime ( 2024, 6, 21 ) #6:51pm
		full_moon_july = datetime.datetime ( 2024, 7, 21 ) #1:37pm
		full_moon_august = datetime.datetime ( 2024, 8, 19 ) #8:35pm
		full_moon_sep = datetime.datetime ( 2024, 9, 17 ) #4:59am
		full_moon_oct = datetime.datetime ( 2024, 10, 17 ) #3:54pm
		full_moon_nov = datetime.datetime ( 2024, 11, 15 ) 
		full_moon_deca = datetime.datetime ( 2024, 12, 15 )		
		
		
# Sabbats and U.S. Holidays block--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]

# Sabbats block-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]
# yule_last_year
#		print ( '\n\n\t\t\tSabbat Observances' )

# yule_2022 
		if yule_2023 > now :
			next = yule_2023 - now
			
			print ( '\n\t\t\tWinter Solstice: ' + str ( next ) + ' on ' + yule_2023.strftime  ( '%A, %B %e, %Y' ) )
# imbolc
		elif imbolc > now and yule_2023 < now :
			next = imbolc - now	
			print ( '\n\t\t\tImbolc, Snow Drop Festival: ' + str ( next ) + ' on ' + imbolc.strftime ( '%A, %B %e, %Y' ) )
# ostara
		elif ostara > now and imbolc < now :
			next = ostara - now	
			print ( '\n\t\t\tEostra\'s Day, Spring Equinox: ' + str ( next ) + ' on ' + ostara.strftime ( '%A, %B %e, %Y' ) )
# beltane
		elif beltane > now and ostara < now :
			next = beltane - now	
			print ( '\n\t\t\tBeltane ( May Eve ): ' + str ( next ) + ' on ' + beltane.strftime ( '%A, %B %e, %Y' ) )
# litha
		elif litha > now and beltane < now :
			next = litha - now	
			print ( '\n\t\t\tSummer Solstice: ' + str ( next ) + ' on ' + litha.strftime ( '%A, %B %e, %Y' ) )
# lammas
		elif lammas > now and litha < now :
			next = lammas - now	
			print ( '\n\t\t\tAugust Eve, First Harvest begins: ' + str ( next ) + ' on ' + lammas.strftime ( '%A, %B %e, %Y' ) )
# hecatesDay
		elif hecatesDay > now and lammas < now :
			next = hecatesDay - now
			print ( '\n\t\t\tHecate\'s Day: ' + str ( next ) + ' on ' + hecatesDay.strftime ( '%A, %B %e, %Y' ) )
# mabon
		elif mabon > now and lammas < now :
			next = mabon - now
			print ( '\n\t\t\tMabon ' + str ( next ) + ' on ' + mabon.strftime ( '%A, %B %e, %Y' ) )
# samhain
		elif samhain > now and mabon < now :
			next = samhain - now	
			print ( '\n\t\t\tSamhain ' + str ( next ) + ' on ' + samhain.strftime ( '%A, %B %e, %Y' ) )
#yule_this_year
		elif yule_2024 > now and samhain < now :
			next = yule_2024 - now
			print ( '\n\t\t\tWinter Solstice ' + str ( next ) + ' on ' + yule_2024.strftime ( '%A, %B %e, %Y' ) )
# end Sabbats block-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]
# start US holidays block--------------------------------------------------------------------------------------------------------------------------------------------------------------------------]
#christmas
		if christmas > now :
			n = christmas - now 
			n2 = newYear - now 
			
			print ( '\t\t\tChristmas: ' + str ( n ) + ' on ' + christmas.strftime ( '%A, %B %e, %Y' ) )
			print ( '\t\t\tNew Year: ' + str ( n2 ) + ' on ' + newYear.strftime ( '%A, %B %e, %Y' ) )
			
#new year
		elif newYear > now and christmas < now :
			n = newYear - now
			n2 = martinday - now
			
			print ( '\t\t\tNew Year: ' + str ( n ) + ' on ' + newYear.strftime ( '%A, %B %e, %Y' ) )
			print ( '\t\t\tMartin Luther King Jr Day: ' + str ( n2 ) + ' on ' + martinday.strftime ( '%A, %B %e, %Y' ) )
			
#martin Luther 
		elif martinday > now and newYear < now :
			n = martinday - now
			n2 = daylightSavings - now
			
			print ( '\t\t\tMartin Luther King Jr Day: ' + str ( n ) + ' on ' + martinday.strftime ( '%A, %B %e, %Y' ) )
			print ( '\t\t\tSpring ahead: ' + str ( n2 ) + ' on ' + daylightSavings.strftime ( '%A, %B %e, %Y' ) )

#daylightSavings
		elif daylightSavings > now and martinday < now :
			n = daylightSavings - now
			n2 = eclipse - now

			print ( '\t\t\tSpring ahead: ' + str ( n ) + ' on ' + daylightSavings.strftime ( '%A, %B %e, %Y' ) )
			print ( '\t\t\tPenumbral Lunar Eclipse: ' + str ( n2 ) + ' on ' + eclipse.strftime ( '%A, %B %e, %Y' ) )
			
#eclipse
		elif eclipse > now and daylightSavings < now :
			n = eclipse - now
			n2 = easterSunday - now
			print ( '\t\t\tPenumbral Lunar Eclipse: ' + str ( n ) + ' on ' + eclipse.strftime ( '%A, %B %e, %Y' ) )
			print ( '\t\t\tEaster Sunday: ' + str ( n2 ) + ' on ' + easterSunday.strftime ( '%A, %B %e, %Y' ) )
			
#easterSunday
		elif easterSunday > now and eclipse < now :
			n = easterSunday - now
			n2 = solar_eclipse - now

			print ( '\t\t\tEaster Sunday: ' + str ( n ) + ' on ' + easterSunday.strftime ( '%A, %B %e, %Y' ) )
			print ( '\t\t\tPartial Solar Eclipse: ' + str ( n2 ) + ' on ' + solar_eclipse.strftime ( '%A, %B %e, %Y' ) )
			
#solarEclipse
		elif solar_eclipse > now and easterSunday < now :
			n = solar_eclipse - now
			n2 = motherDay - now
			
			print ( '\t\t\tPartial Solar Eclipse: ' + str ( n ) + ' on ' + solar_eclipse.strftime ( '%A, %B %e, %Y' ) )
			print ( '\t\t\tMother\'s Day: ' + str ( n2 ) + ' on ' + motherDay.strftime ( '%A, %B %e, %Y' ) )
			
#motherDay
		elif motherDay > now and easterSunday < now :
			n = motherDay - now
			n2 = memorialDay - now

			print ( '\t\t\tMother\'s Day: ' + str ( n ) + ' on ' + motherDay.strftime ( '%A, %B %e, %Y' ) )
			print ( '\t\t\tMemorial Day: ' + str ( n2 ) + ' on ' + memorialDay.strftime ( '%A, %B %e, %Y' ) )

#memorialDay
		elif memorialDay > now and motherDay < now :
			n = memorialDay - now
			n2 = independenceDay - now

			print ( '\t\t\tMemorial Day: ' + str ( n ) + ' on ' + memorialDay.strftime ( '%A, %B %e, %Y' ) )
			print ( '\t\t\tIndependence Day: ' + str ( n2 ) + ' on ' + independenceDay.strftime ( '%A, %B %e, %Y' ) )

#independenceDay
		elif independenceDay > now and memorialDay < now :
			n = independenceDay - now
			n2 = laborDay - now

			print ( '\t\t\tIndependence Day: ' + str ( n ) + ' on ' + independenceDay.strftime ( '%A, %B %e, %Y' ) )
			print ( '\t\t\tLabor Day: ' + str ( n2 ) + ' on ' + laborDay.strftime ( '%A, %B %e, %Y' ) )
#laborDay (9/2/2024)
		elif laborDay > now and independenceDay < now :
			n = laborDay - now
			n2 = eclipse2 - now

			print ( '\t\t\tLabor Day: ' + str ( n ) + ' on ' + laborDay.strftime ( '%A, %B %e, %Y' ) )
			print ( '\t\t\tPartial Lunar Eclipse: ' + str ( n2 ) + ' on ' + eclipse2.strftime ( '%A, %B %e, %Y' ) )

#eclipse2 (9/18/2024)
		elif eclipse2 > now and laborDay < now :
			n = eclipse2 - now
			n2 = allhollows - now
			
			print ( '\t\t\tPartial Lunar Eclipse: ' + str ( n ) + ' on ' + eclipse2.strftime ( '%A, %B %e, %Y' ) )
			print ( '\t\t\tHalloween: ' + str ( n2 ) + ' on ' + allhollows.strftime ( '%A, %B %e, %Y' ) )

#halloween 10/31/24
		elif allhollows > now and eclipse2 < now :
			n = allhollows - now
			n2 = daylightSavingsEnds - now
	
			print ( '\t\t\tHalloween: ' + str ( n ) + ' on ' + allhollows.strftime ( '%A, %B %e, %Y' ) )
			print ( '\t\t\tTurn clocks back: ' + str ( n2 ) + ' on ' + daylightSavingsEnds.strftime ( '%A, %B %e, %Y' ) ) 
		
#daylightSavingsEnds 11/3/24
		elif daylightSavingsEnds > now and allhollows < now :
			n = daylightSavingsEnds - now
			n2 = veteranDay - now
		
			print ( '\t\t\tTurn clocks back: ' + str ( n ) + ' on ' + daylightSavingsEnds.strftime ( '%A, %B %e, %Y' ) )
			print ( '\t\t\tVeteran\'s Day: ' + str ( n2 ) + ' on ' + veteranDay.strftime ( '%A, %B %e, %Y' ) )
	
#veteranDay 11/11/24
		elif veteranDay > now and laborDay < now :
			n = veteranDay - now
			n2 = thanksgiving - now

			print ( '\t\t\tVeteran\'s Day: ' + str ( n ) + ' on ' + veteranDay.strftime ( '%A, %B %e, %Y' ) )
			print ( '\t\t\tThanksgiving: ' + str ( n2 ) + ' on ' + thanksgiving.strftime ( '%A, %B %e, %Y' ) )
			
#thanksgiving
		elif thanksgiving > now and daylightSavingsEnds < now :
			n = thanksgiving - now
			n2 = christmas24 - now

			print ( '\t\t\tThanksgiving: ' + str ( n ) + ' on ' + thanksgiving.strftime ( '%A, %B %e, %Y' ) )
			print ( '\t\t\tChristmas: ' + str ( n2 ) + ' on ' + christmas24.strftime ( '%A, %B %e, %Y' ) )			
#christmas
		elif christmas24 > now and thanksgiving < now :
			n = christmas24 - now
			n2 = newYear25 - now

			print ( '\t\t\tChristmas: ' + str ( n ) + ' on ' + christmas24.strftime ( '%A, %B %e, %Y' ) )
			print ( '\t\t\tNew Year\'s Eve: ' + str ( n2 ) + ' on ' + newYear25.strftime ( '%A, %B %e, %Y' ) )			
#newYearseve
		elif newYear25 > now and christmas24 < now :
			n = newYear25 - now
			print ( '\t\t\tEve of the New Year: ' + str ( n ) + ' on ' + newYear25.strftime ( '%A, %B %e, %Y' ) )
		else :
			print ( '\t\t\tEnd of 2022\n' )
# end US Holidays block-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]

#new moon block-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]
		print ( '\n\t\t\t\t\t\t', '*' * 24 )
		
#		if new_moon_dec > now :
#			new_moon = new_moon_dec - now
#			print ( '\n\t\t\tLast New Moon: ' + str ( new_moon ) + ' on ' + new_moon_dec.strftime ( '%A, %B %e, %Y' ) )

#		elif new_moon_jan > now and new_moon_dec < now :
#			new_moon = new_moon_jan - now
#			print ( '\n\t\t\tNew Moon: ' + str ( new_moon ) + ' on ' + new_moon_jan.strftime ( '%A, %B %e, %Y' ) )
			
		if new_moon_feb > now and new_moon_jan < now :
			new_moon = new_moon_feb - now
			print ( '\n\t\t\tSuper New Moon: ' + str ( new_moon ) + ' on ' + new_moon_feb.strftime ( '%A, %B %e, %Y' ) )

		elif new_moon_march > now and new_moon_feb < now :
			new_moon = new_moon_march - now
			print ( '\n\t\t\tSuper New Moon: ' + str ( new_moon ) + ' on ' + new_moon_march.strftime ( '%A, %B %e, %Y' ) )

		elif new_moon_april > now and new_moon_march < now :
			new_moon = new_moon_april - now
			print ( '\n\t\t\tSuper New Moon: ' + str ( new_moon ) + ' on ' + new_moon_april.strftime ( '%A, %B %e, %Y' ) )

		elif new_moon_may > now and new_moon_april < now :
			new_moon = new_moon_may - now
			print ( '\n\t\t\tNew Moon: ' + str ( new_moon ) + ' on ' + new_moon_may.strftime ( '%A, %B %e, %Y' ) )

		elif new_moon_jun > now and new_moon_may < now :
			new_moon = new_moon_jun - now
			print ( '\n\t\t\tNew Moon: ' + str ( new_moon ) + ' on ' + new_moon_jun.strftime ( '%A, %B %e, %Y' ) )

		elif new_moon_july > now and new_moon_jun < now :
			new_moon = new_moon_july - now
			print ( '\n\t\t\tNew Moon: ' + str ( new_moon ) + ' on ' + new_moon_july.strftime ( '%A, %B %e, %Y' ) )

		elif new_moon_august > now and new_moon_july < now :
			new_moon = new_moon_august - now
			print ( '\n\t\t\tMicro New Moon: ' + str ( new_moon ) + ' on ' + new_moon_august.strftime ( '%A, %B %e, %Y' ) )

		elif new_moon_sep > now and new_moon_august < now :
			new_moon = new_moon_sep - now
			print ( '\n\t\t\tNew Moon: ' + str ( new_moon ) + ' on ' + new_moon_sep.strftime ( '%A, %B %e, %Y' ) )

		elif new_moon_oct > now and new_moon_sep < now :
			new_moon = new_moon_oct - now
			print ( '\n\t\t\tMicro New Moon: ' + str ( new_moon ) + ' on ' + new_moon_oct.strftime ( '%A, %B %e, %Y' ) )

		elif new_moon_nov > now and new_moon_oct < now :
			new_moon = new_moon_nov - now
			print ( '\n\t\t\tNew Moon: ' + str ( new_moon ) + ' on ' + new_moon_nov.strftime ( '%A, %B %e, %Y' ) )
			
		elif new_moon_dec1 > now and new_moon_nov < now :
			new_moon = new_moon_dec1 - now 
			print ( '\n\t\t\tNew Moon: ' + str ( new_moon ) + ' on ' + new_moon_dec1.strftime ( '%A, %B %e, %Y' ) )
			
		elif new_moon_dec2 > now and new_moon_dec1 < now :
			new_moon = new_moon_dec2 - now 
			print ( '\n\t\t\tNew Moon: ' + str ( new_moon ) + ' on ' + new_moon_dec2.strftime ( '%A, %B %e, %Y' ) )	
			
		elif new_moon_jan_2025 > now and new_moon_dec2 < now :
			new_moon = new_moon_jan_2025 - now 
			print ( '\n\t\t\tNew Moon: ' + str ( new_moon ) + ' on ' + new_moon_jan_2025.strftime ( '%A, %B %e, %Y' ) )
		else :
			print ( '' )
#end new moon block--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]

# full moon block--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]
		if full_moon_deca > now :
			full_moon = full_moon_deca - now 
			print ( '\t\t\tCold Moon: ' + str ( full_moon ) + ' on ' + full_moon_deca.strftime ( '%A, %B %e, %Y' ) ) #( '%A, %B %e, %Y, %-I:%-M %p \n' ) )

		elif full_moon_jan > now and full_moon_dec < now :
			full_moon = full_moon_jan - now
			print ( '\n\t\t\tWolf Moon: ' + str ( full_moon ) + ' on ' + full_moon_jan.strftime ( '%A, %B %e, %Y' ) )

		elif full_moon_feb > now and full_moon_jan < now :
			full_moon = full_moon_feb - now
			print ( '\n\t\t\tMicro Snow Moon: ' + str ( full_moon ) + ' on ' + full_moon_feb.strftime ( '%A, %B %e, %Y' ) )

		elif full_moon_march > now and full_moon_feb < now :
			full_moon = full_moon_march - now
			print ( '\n\t\t\tMicro Crow Moon: ' + str ( full_moon ) + ' on ' + full_moon_march.strftime ( '%A, %B %e, %Y' ) )

		elif full_moon_april > now and full_moon_march < now :
			full_moon = full_moon_april - now
			print ( '\n\t\t\tAwakening Moon: ' + str ( full_moon ) + ' on ' + full_moon_april.strftime ( '%A, %B %e, %Y' ) )

		elif full_moon_may > now and full_moon_april < now :
			full_moon = full_moon_may - now
			print ( '\n\t\t\tMother\'s Moon: ' + str ( full_moon ) + ' on ' + full_moon_may.strftime ( '%A, %B %e, %Y' ) )

		elif full_moon_june > now and full_moon_may < now :
			full_moon = full_moon_june - now
			print ( '\n\t\t\tRose Moon: ' + str ( full_moon ) + ' on ' + full_moon_june.strftime ( '%A, %B %e, %Y' ) )

		elif full_moon_july > now and full_moon_june < now :
			full_moon = full_moon_july - now
			print ( '\n\t\t\tBuck Moon: ' + str ( full_moon ) + ' on ' + full_moon_july.strftime ( '%A, %B %e, %Y' ) )

		elif full_moon_august > now and full_moon_july < now :	
			full_moon = full_moon_august - now
			print ( '\n\t\t\tBlue Sturgeon Moon: ' + str ( full_moon ) + ' on ' + full_moon_august.strftime ( '%A, %B %e, %Y' ) )

		elif full_moon_sep > now and full_moon_august < now :
			full_moon = full_moon_sep - now
			print ( '\n\t\t\tSuper Harvest Moon: ' + str ( full_moon ) + ' on ' + full_moon_sep.strftime ( '%A, %B %e, %Y' ) )

		elif full_moon_oct > now and full_moon_sep < now :
			full_moon = full_moon_oct - now
			print ( '\n\t\t\tSuper Hunter\'s Moon: ' + str ( full_moon ) + ' on ' + full_moon_oct.strftime ( '%A, %B %e, %Y' ) )

		elif full_moon_nov > now and full_moon_oct < now :
			full_moon = full_moon_nov - now
			print ( '\n\t\t\tFull Moon: ' + str ( full_moon ) + ' on ' + full_moon_nov.strftime ( '%A, %B %e, %Y' ) )

		elif full_moon_deca > now and full_moon_nov < now :
			full_moon = full_moon_deca - now
			print ( '\n\t\t\tCold Moon' + str ( full_moon ) + ' on ' + full_moon_deca.strftime ( '%A, %B %e, %Y' ) )
		else :
			print ( '' )
#end full moon block-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]

#begin choice block-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]
		choice = input (
		'\n\n\t\t\tSpiritual Influence:				\'i\'\
		\n\n\t\t\tSchedual:					\'s\'\
		\n\n\t\t\tMeditation:					\'m\'\
		\n\n\t\t\tAmbiance:					\'a\'\
		\n\n\t\t\tRunes:						\'r\'\
		\n\n\t\t\tGems:						\'g\'\
		\n\n\t\t\tTo Do:						\'d\'\
		\n\n\t\t\tSignificant Events:				\'e\'\
		\n\n\t\t\tBooks:						\'b\'\
		\n\n\t\t\tMath Tools:					\'n\'\
		\n\n\t\t\tQuit:						\'q\'\
		\n\n\t\t\t' )
	
		if 'i' in choice :
			spirit ( )	
		elif 'm' in choice :
			meditations ( )
		elif 'a' in choice :
			ambiance ( )
		elif 'r' in choice :
			rune ( )
		elif 'g' in choice :
			stones ( )
		elif 'd' in choice :
			todo ( )
		elif 'b' in choice :
			books ( )
		elif 's' in choice :
			schedule ( )
		elif 'e' in choice :
			sig_events ( )
		elif 'n' in choice :
			math_tools ( )
		elif 'q' in choice :
			space ( ) , exit ( 0 )
		else :
			begin ( )
#=============================================================
#=============================================================		

def spirit ( ) :
	import random

	wheel = [ 'muladhara', 'svadhishana', 'manipura', 'anahata', 'vissudha', 'ajna', 'sahassrara' ]
	color = {
			'red' : 'ff0000', 'crimson' : 'dc143c', 'venetian red' : 'c80815', 'dark red' : '8b0000', 'maroon' : '800000', 'red2' : 'fe2712',
			'rose madder' : 'e32636', 'red3' : 'ed1c24', 'red brown' : 'a52a2a', 'cadmium red' : 'e30022', 'lava' : 'cf1020', 'cardinal' : 'c41e3a',
			'crimson glory' : 'be0032', 'ruby red' : '9b111e', 'claret' : '7f1734', 'sangria' : '92000a', 'carmine' : '960018', 'burgundy' : '800020',
			'rosewood' : '65000b', 'dark scarlet' : '560319', 'orange red' : 'ff4500', 'suset orange' : 'fd5e53', 'red orange' : 'ff5349', 'orange' : 'ffa500',
			'coral' : 'ff7f50', 'flame' : 'e25822', 'orange2' : 'fb9902', 'willpower orange' : 'fd5800', 'amber' : 'ff7e00', 'orange3' : 'ff7f00', 'gold' : 'ffd700',
			'golden yellow' : 'ffdf00', 'yellow' : 'ffff00', 'yellow2' : 'fefe33', 'cadmium yellow' : 'fff600', 'teal' : '008080', 'turquoise' : '40e0d0',
			'jade' : '00a86b', 'teal green' : '00827f', 'midnight green' : '004953', 'blue' : '0000ff', 'deep sky blue' : '00bfff', 'medium blue' : '0000cd',
			'ultramarine blue' : '4166f5', 'crayola blue' : '1f75fe', 'blue bonnet' : '1c1cf0', 'vivid sky blue' : '00ccff', 'blue2' : '0247fe', 'blue pigment' : '333399',
			'royal blue' : '041690', 'phthalo blue' : '000f89', 'indigo' : '4b0082', 'purple heart' : '69359c', 'regalia' : '522d80', 'spanish violet' : '4c2882',
			'persian indigo' : '32127a', 'russian violet' : '32174d', 'purple' : '800080', 'dark violet' : '9400d3', 'veronica' : 'a020f0', 'violet' : '7f00ff',
			'violet2' : '8f00ff', 'vivid violet' : '9f00ff', 'medium red violet' : 'bb3385', 'violet3' : '8601af', 'dark magenta' : '8b008b', 'magenta' : 'ff00ff',
			'medium violet red' : 'c71585', 'vivid orchid' : 'cc00ff', 'magenta2' : 'ca1f7b', 'red violet' : 'c71585',
			'green' : '008000', 'light green' : '90ee90', 'green yellow' : 'adff2f', 'lime' : '00ff00', 'spring green' : '00ff7f', 'lime green' : '32cd32',
			'medium sea green' : '32b371', 'sea green' : '2e8b57', 'forest green' : '228b22', 'dark green' : '006400', 'nyanza' : 'e9ffdb', 'tea green' : 'd0f0c0',
			'light moss green' : 'addfad', 'pastel green' : '77dd77', 'dark sea green' : '8fbc8f', 'malachite' : '0bda51', 'fern green' : '4f7942', 'spanish viridian' : '007f5c',
			'cadmium green' : '006b3c', 'pink' : 'ffc0cb', 'misty rose' : 'ffe4e1', 'classic rose' : 'fbcce7', 'cherry blossom pink' : 'ffb7c5', 'light fuchsia pink' : 'f984ef' 
	}
		
	meditations = [ 
		'Count down', 'Unifying the Three Selves', 'Treasure chest for solutions', 'Chakra'
	]

	random_wheel = ( random.choice ( wheel ) )
	res = key, val = random.choice ( list ( color.items ( ) ) )
	random_meditation = ( random.choice ( meditations ) )

	print ( '\n\t\t\t\t\t\t' + random_wheel + ', ' + str ( ' - '.join ( res ) ) + '\n\t\t\t\t\t\t' + random_meditation )	
	begin ( )
#=============================================================
#=============================================================
# schedule block-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]
def schedule ( ) :
	while True :
		import random
		user_input = input ( '\nHow would you like your schedule?\nSingle output 		= 1\nWork day 		= 3\nWeekend / day off 	= 5\n' )

		today_agenda = [ ]

		if '1' in user_input :
			counter = 0
			while counter < 1 :
				agenda = [ 'Information Technology', 'Hearth' ]
				randomAgenda = ( random.choice ( agenda ) )
				today_agenda.append ( randomAgenda )
				counter += 1

		elif '3' in user_input :
			counter = 0
			while counter < 3 :
				agenda = [ 'Information Technology', 'Hearth'  ]
				randomAgenda = ( random.choice ( agenda ) )
				today_agenda.append ( randomAgenda )
				counter += 1

		elif '5' in user_input :
			counter = 0
			while counter < 5 :
				agenda = [ 'Information Technology', 'Hearth'  ]
				randomAgenda = ( random.choice ( agenda ) )
				today_agenda.append ( randomAgenda )
				counter += 1			
		else :
			begin ( )			
		space ( )				

		for i in today_agenda :
			i_counter = 0
			while i_counter < counter :											
#-------------------------------------------------------------------------------------------------------------------------------------------------------------begin information technology condition block
				if 'Information Technology' in today_agenda :
					i_counter += 1
					study = [ 'OSINT Techniques', 'Extreme Privacy', 'GRC' ]
					random_study = ( random.choice ( study ) )
					print ( '\t\t\t\tInformation Technology: ' + random_study + '\n' )
					today_agenda.remove ( 'Information Technology' )
#---------------------------------------------------------------------------------------------------------------------------------------------------------begin Hearth condition block
				elif 'Hearth' in today_agenda :
					i_counter += 1
					home = [ 'Home', 'Escoteric' ]
					h = ( random.choice ( home ) )
					if 'Escoteric' in h :
						shadow = [ 'Guy on YouTuble', 'Secret Teachings', 'Wheels of Life', 'Psychic Witch', 'Keeping Her Keys', 'Slavic' ]
						t = ( random.choice ( shadow ) )
						print ( '\t\t\t\tEscotericism: ' + t + '\n' )
						today_agenda.remove ( 'Hearth' )
					elif 'Home' in h :
						s = [ 'Home', 'Polish', 'Reading', 'Writing' ]
						t = ( random.choice ( s ) )
						print ( '\t\t\t\tHearth: ' + t + '\n' )
						today_agenda.remove ( 'Hearth' )
				else :
					break# today_agenda = { }, break out of for loop 
					
#		forback = [ 'Up', 'Down' ]
#		listen = [ 'Later', 'Current Reads', 'Educational', 'Esoteric' ]
#		fb = ( random.choice ( forback ) )	
#		ls = ( random.choice ( listen ) )
#		space ( )
#		print ( '\t\t\t\t\t' + fb + ', ' + ls + '\n' )
		
		c = input ( '\nContinue or go back to main menu?	c / m		' )
#-----------------------------------------------------------------------		
		if 'c' in c :
			continue	
		else :
			begin ( )
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
def stones ( ) :
	while True :
		import random 
		gems = [
			'black obsidian', 'bloodstone', 'jade', 'lapis lazuli', 'lava stone', 'red jasper', 'selenite', 'carnelian', 
			'amethyst', 'quartz', 'rose quartz', 'citrine', 'moonstone', 'tiger\'s eye', 'green jasper', 'hematite',
			'labradorite', 'malachite', 'silver', 'sodalite', 'blue apatite', 'black tourmaline', 'Bone'
	]
		random_gem = ( random.choice ( gems ) )
		print ( '\n\t\t\t\t\t' + random_gem )
		
		c = input ( '\nContinue or go back to main menu?	c / m		' )
#-----------------------------------------------------------------------		
		if 'c' in c :
			continue
		else :
			begin ( )
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
def ambiance ( ) :
	while True :
		choice = input ( 
		'\n\n\t\t\tIncense:				\'i\'\
		\n\n\t\t\tWax:					\'w\'\
		\n\n\t\t\t' )
	
		if 'i' in choice :
			incense ( )
		elif 'w' in choice :
			wax ( )
		elif 'm' in choice :
			begin ( )
		elif 'q' in choice :
			space ( ) , exit ( 0 )
		else :
			begin ( )
			
		c = input ( '\nContinue or go back to main menu?	c / m		' )
#-----------------------------------------------------------------------		
		if 'c' in c :
			continue
		else :
			begin ( )
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
def rune ( ) :
	while True :
		import random 
		runes = [
			'fehu', 'uruz', 'thurisaz', 'ansuz', 'raidho', 'kenaz', 'gebo', 'wunjo', 'naudhiz', 'isa', 'jera', 'hagalaz',
			'eiwaz', 'perthro', 'elhaz', 'sowilo', 'tiwaz', 'berkano', 'ehwaz', 'mannaz', 'laguz', 'ingwaz', 'dagaz', 'othala'
		]	
		random_rune = ( random.choice ( runes ) )
		print ( '\n\t\t\t\t\t' + random_rune )
		
		c = input ( '\nContinue or go back to main menu?	c / m		' )
#-----------------------------------------------------------------------		
		if 'c' in c :
			continue
		else :
			begin ( )
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
def incense ( ) :
	while True:
		import random
		incenseChoice = [ 
			'Lavender', 'Black Cherry', 'myrrh', 'Frankincense', 'Cedar', 'Gardenia', 'Sage', 'Sage & Citrus'
		]
		i_choice = ( random.choice ( incenseChoice ) )
		print ( '\n\t\t\t\t\t' + i_choice )
		
		c = input ( '\nContinue or go back to main menu?	c / m		' )
#-----------------------------------------------------------------------		
		if 'c' in c :
			continue
		else :
			begin ( )
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
def wax ( ) :
	while True :	
		import random
		wax_choice = [ 
			'Cedar, Musk & Mystery', 'Fresh Cut Frasier', 'Balsam Pine', 'Snickerdoodle', 'Apple Pie',
			'Autumn Wrealth', 'Cinnamon', 'Candy Corn', 'Spiced Cider'
			]
		r = ( random.choice ( wax_choice ) )
		print ( '\n\t\t\t' + r + '\n' )
	
		c = input ( '\nContinue or go back to main menu?	c / m		' )
#-----------------------------------------------------------------------		
		if 'c' in c :
			continue
		else :
			begin ( )
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
def todo ( ) :
	while True :
		choice = input ( 
		'\n\n\t\t\tList:			\'l\'\
		\n\n\t\t\tRandomized:		\'r\'\
		\n\n\t\t\tMain:			\'m\'\
		\n\n\t\t\tQuite:			\'q\'\
		\n\n\t\t\t' )
	
		if 'l' in choice :
			todolist ( )
		elif 'r' in choice :
			todolistRandom ( )
		elif 'm' in choice :
			begin ( )
		elif 'q' in choice :
			space ( ) , exit ( 0 )
		else :
			begin ( )
			
		c = input ( '\nContinue or go back to main menu?	c / m		' )
#-----------------------------------------------------------------------		
		if 'c' in c :
			continue
		else :
			begin ( )
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
def todolist ( ) :
	while True :
		from b_dic import todolist
		for i in todolist :
			print ( i )

		c = input ( '\nContinue or go back to main menu?	c / m		' )
#-----------------------------------------------------------------------		
		if 'c' in c :
			continue
		else :
			begin ( )
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
def todolistRandom ( ) :
	while True :
		import random
		from b_dic import todolist
		r = ( random.choice ( todolist ) )
		print ( '\n' + r )

		c = input ( '\nContinue or go back to main menu?	c / m		' )
#-----------------------------------------------------------------------		
		if 'c' in c :
			continue
		else :
			begin ( )
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
def tarot_reading ( ) :
	while True :
		from supertarot import title_only
		import random

		card_collection = [ ]
		ask = input ( '\nWould you care for the one, three, or thirteen-spread reading ( a / b / c )?	' )

		if 'b' in ask :
			counter = 0		
			while counter < 3 :
				random_selection = ( random.choice ( title_only ) )
				card_collection.append ( random_selection )			
				counter += 1

		elif 'c' in ask :
			counter = 0
			while counter < 13 :
				random_selection = ( random.choice ( title_only ) )	
				card_collection.append ( random_selection )	
				counter += 1

		else :			
			random_selection = ( random.choice ( title_only ) )			
			card_collection.append ( random_selection )

		space ( )
		for i in card_collection :
			print ( i )

		c = input ( '\nContinue or go back to main menu?	c / m		' )
#-----------------------------------------------------------------------		
		if 'c' in c :
			continue	
		else :
			begin ( )
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
def meditations ( ) :
	while True :
		import random	
		meditations = [ 
			'Count down', 'Unifying the Three Selves', 'Treasure chest for solutions', 'Chakra'
		]
		randomMeditation = ( random.choice ( meditations ) )
		print ( '\n\t\t\t\t' + randomMeditation )

		c = input ( '\nContinue or go back to main menu?	c / m		' )
#-----------------------------------------------------------------------		
		if 'c' in c :
			continue
		else :
			begin ( )
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
def books_craft ( ) :
	while True :
		import random 
		book = [ 'Anatomy of the Spirit', 'goldenbough', 'hermetica', 'kybalion', 'white goddess', 'Ancient Mirrors' ]
		randombook = ( random.choice(book ) )
		print ( '\n\t\t\t\t\t\t\t' + randombook )

		c = input ( '\nContinue or go back to main menu?	c / m		' )
#-----------------------------------------------------------------------		
		if 'c' in c :
			continue
		else :
			begin ( )
#=============================================================
#=============================================================

def br_event ( ) :
	while True :
		breakup_event = datetime.datetime ( 2021, 3, 14 )
		now = datetime.datetime.today ( )
		timedelta = now - breakup_event

		print ( breakup_event.strftime ( '\n%A, %B %d, %Y\n' ) )
		print ( timedelta )

		c = input ( '\nContinue or go back to main menu?	c / m		' )
#-----------------------------------------------------------------------		
		if 'c' in c :
			continue
		else :
			begin ( )
#=============================================================
#=============================================================

def sig_events ( ) :
	while True :
		choice = input ( 
		'\nKitten birthday:			\'k\'\
		\nBreak Event:				\'b\'\
		\nLeap Year:				\'l\'\
		\nGracie\'s approximate age:		\'g\'\
		\nPassing:				\'p\'\
		\n\nMain Menu:				\'m\'\
		\n\n' )

		if 'k' in choice :
			kitten ( )
		elif 'b' in choice :
			br_event ( )
		elif 'l' in choice :
			leap_year ( )
		elif 'g' in choice :
			gracie ( )
		elif 'p' in choice :
			passing ( )
		elif 'm' in choice :
			begin ( )
		else :
			c = input ( '\nContinue or go back to main menu?	c / m		' )
#-----------------------------------------------------------------------		
			if 'c' in c :
				continue
			else :
				begin ( )
#=============================================================
#=============================================================	

def gracie ( ) :
	while True :
		born = datetime.datetime ( 2010, 3, 1 )
		now = datetime.datetime.today ( )
		timedelta = now - born

		print ( born.strftime ( '\nGracie should be about ' + str ( timedelta ) + ' old.' ) )

		c = input ( '\nContinue or go back to main menu?	c / m		' )
#-----------------------------------------------------------------------		
		if 'c' in c :
			continue
		else :
			begin ( )
#=============================================================
#=============================================================

def kitten ( ) :
	while True :
		k_born = datetime.datetime ( 2021, 9, 3 )
		now = datetime.datetime.today ( )
		timedelta = now - k_born

		print ( k_born.strftime ( '\nKitten birth date: %A, %B %d, %Y - ' + str ( timedelta ) ) )
 
		c = input ( '\nContinue or go back to main menu?	c / m		' )
#-----------------------------------------------------------------------		
		if 'c' in c :
			continue
		else :
			begin ( )
#=============================================================
#=============================================================
def books ( ) :
	while True :
		choice = input (
		'\n\n\t\t\tBook Generator - General:		\'1\'\
		\n\n\t\t\tBook Generator - Craft:			\'2\'\
		\n\n\t\t\tReturn Duplicate Titles:		\'3\'\
		\n\n\t\t\tSearch:					\'4\'\
		\n\n\t\t\tQuit:					\'q\'\
		\n\n\t\t\t')

		if '1' in choice :
			book_gen ( )
		elif '2' in choice :
			book_craft ( )
		elif '3' in choice :
			duplicates ( )
		elif '4' in choice :
			book_search ( )
		elif 'm' in choice :
			begin ( )
		else :
			c = input ( '\nContinue or go back to main menu?	c / m		' )
#-----------------------------------------------------------------------		
			if 'c' in c :
				continue
			else :
				begin ( )
#=============================================================
#=============================================================	

def book_gen ( ) :
	while True :
		import random
		from b_dic import book_listing	
		random_gen = random.choice ( book_listing )

		print ( '\n' + random_gen )

		c = input ( '\nContinue or go back to main menu?	c / m		' )
#-----------------------------------------------------------------------		
		if 'c' in c :
			continue
		else :
			begin ( )
#=============================================================
#=============================================================

def book_search ( ) :
	while True :
		from b_dic import book_listing
		collection = [ ]
		phrase = input ( '\nEnter author, book title, phrase, etc.\n' )
		space ( )
		for i in zip ( book_listing, book_listing [ : ] ) :
			if phrase in i [ 0 ] :		
				collection.append ( i [ 0 ] )
			else :
				continue
		if collection != [ ] :
			for i in collection :
				print ( i )
		else :
			print ( '\nNothing found' )
		return ''

		c = input ( '\nContinue or go back to main menu?	c / m		' )
#-----------------------------------------------------------------------		
		if 'c' in c :
			continue
		else :
			begin ( )
#=============================================================
#=============================================================

def duplicates ( ) :
	while True :
		from b_dic import book_listing

		duplicates = { }
		for i in book_listing :
			if i in duplicates :
				duplicates [ i ] += 1
			else :
				duplicates [ i ] = 1
		max = 0
		most_freq = { }

		for key, value in duplicates.items ( ) :
			if value > max :
				max = value
				most_freq = { key : max }

		print ( '\n' + str ( most_freq ) )

		c = input ( '\nContinue or go back to main menu?	c / m		' )
#-----------------------------------------------------------------------		
		if 'c' in c :
			continue
		else :
			begin ( )
#=============================================================
#=============================================================
def book_craft ( ) :
	while True :
		import random
		from b_dic import craft_books	
		random_gen = random.choice ( craft_books )

		print ( '\n' + random_gen )

		c = input ( '\nContinue or go back to main menu?	c / m		' )
#-----------------------------------------------------------------------		
		if 'c' in c :
			continue
		else :
			begin ( )
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
def passing ( ) :
	while True :
		p_day = datetime.datetime ( 2018, 9, 16 )
		now = datetime.datetime.today ( )
		timedelta = now - p_day

		print ( p_day.strftime ( '\n\t\t\tThat was %A, %B %d, %Y.\n\t\t\t' + str ( timedelta ) + ' ago.' ) )

		c = input ( '\nContinue or go back to main menu?	c / m		' )
#-----------------------------------------------------------------------		
		if 'c' in c :
			continue
		else :
			begin ( )
#=============================================================
#=============================================================

def math_tools ( ) :
	while True :
		user_input = input (
		'\n\n\t\t\tRandom Numbers:				\'1\'\
		\n\n\t\t\tFactorial:				\'2\'\
		\n\n\t\t\tPrimes:					\'3\'\
		\n\n\t\t\tDivisors:				\'4\'\
		\n\n\t\t\tPowers of 2:				\'5\'\
		\n\n\t\t\tPowers:					\'6\'\
		\n\n\t\t\tPowers defined by user:			\'7\'\
		\n\n\t\t\tMultiplication Table:			\'8\'\
		\n\n\t\t\tMage Number:				\'9\'\
		\n\n\t\t\tStart Page:				\'s\'\
		\n\n\t\t\t' )

		if '1' in user_input :
			rand_nums ( )
		elif '2' in user_input :
			factorial ( )
		elif '3' in user_input :
			primes ( )
		elif '4' in user_input :
			divisors ( )
		elif '5' in user_input :
			powers_of_two ( )
		elif '6' in user_input :
			powers ( )
		elif '7' in user_input :
			user_def_power ( )
		elif '8' in user_input :
			mult_table ( )
		elif '9' in user_input :
			mage_number ( )
		else :
			begin ( )

		c = input ( '\nContinue or go back to main menu?	c / m		' )
#-----------------------------------------------------------------------		
		if 'c' in c :
			continue
		else :
			begin ( )
#=============================================================
#=============================================================

def powers ( ) :
	while True :
		user_input = int ( input ( '\nEnter a number to output its powers:	' ) )
		space ( )
		counter = user_input
		while counter <= user_input ** 10 :
			print ( counter )
			counter *= user_input

		c = input ( '\nContinue or go back to main menu?	c / m		' )
#-----------------------------------------------------------------------		
		if 'c' in c :
			continue
		else :
			begin ( )
#=============================================================
#=============================================================

def user_def_power ( ) :
	while True :
		user_input1 = int ( input ( '\nEnter your number:	' ) )
		user_input2 = int ( input ( '\nTo what power?	' ) )
		space ( )
		print ( user_input1 ** user_input2 )

		c = input ( '\nContinue or go back to main menu?	c / m		' )
#-----------------------------------------------------------------------		
		if 'c' in c :
			continue
		else :
			begin ( )
#=============================================================
#=============================================================

def mult_table ( ) :
	while True :
		user_input = int ( input ( '\nEnter a number:	' ) )
		for i in range ( 1, user_input + 1 ) :
			for j in range ( 1, 11 ) :
				print ( i, 'x', j, ' = ' , i * j )

		c = input ( '\nContinue or go back to main menu?	c / m		' )
#-----------------------------------------------------------------------		
		if 'c' in c :
			continue
		else :
			begin ( )
#=============================================================
#=============================================================

def rand_nums ( ) :
	while True :
		import random
		from random import randint

		user_input = input (
			'\n\n\t\t\tRange between two numbers:		\'1\'\
			\n\n\t\t\tRange between two numbers with step:	\'2\'\
			\n\n\t\t\tSecure random number:			\'3\'\
			\n\n\t\t\t' )

		if '1' in user_input :
			rand2nums ( )
		elif '2' in user_input :
			two_nums_step ( )
		elif '3' in user_input :
			secure_rand ( )
		else :
			begin ( )

		c = input ( '\nContinue or go back to main menu?	c / m		' )
#-----------------------------------------------------------------------		
		if 'c' in c :
			continue
		else :
			begin ( )
#=============================================================
def rand2nums ( ) :
	while True :
		import random
		from random import randint
		a = int ( input ( '\nEnter a positive whole number to start from:	' ) )
		b = int ( input ( 'Enter positive whole number to end with:	' ) )
		r = random.randint ( a, b )
		print ( r )
		
		c = input ( '\nContinue or go back to main menu?	c / m		' )
#-----------------------------------------------------------------------		
		if 'c' in c :
			continue
		else :
			begin ( )
#=============================================================
def secure_rand ( ) :
	while True :
		import random 
		import secrets
		s = secrets.randbelow ( 100 )
		print ( s )
		
		c = input ( '\nContinue or go back to main menu?	c / m		' )
#-----------------------------------------------------------------------		
		if 'c' in c :
			continue
		else :
			begin ( )
#=============================================================
def factorial ( ) :
	while True :
		user_input = int ( input ( '\nEnter a positive whole:	' ) )
		user_input = range ( 1, ( user_input + 1 ) )
		counter = 1

		for i in user_input :
			counter *= i
		space ( )
		print ( '\t\t\t\t\t', counter )

		c = input ( '\nContinue or go back to main menu?	c / m		' )
#-----------------------------------------------------------------------		
		if 'c' in c :
			continue
		else :
			begin ( )
#=============================================================
#=============================================================

def primes ( ) :
	while True :
		user_input = int ( input ( '\nEnter a positive whole number to determine its primality:	' ) )
		prime_numbers = [ ] 
		collection = [ 1 ]
		collection2 = user_input
		space ( )

		if user_input <= 1 :
			print ( '\n\t\t\t\tAny value less than or equal to one is not prime.\n' )
		elif user_input > 1 and user_input <= 3 :
			print ( '\n\t\t\t\tPrime number!\n' )
		else :
			for i in range ( 2, user_input - 1 ) :#between 2 and ( user_input - 1 )
				analyzing = ( user_input % i )# user_input divided by every number leading up to it
				prime_numbers.append ( analyzing )
				if user_input % i == 0 :
					collection.append ( i )
			collection.append ( collection2 )# append the number user entered to end of list to include 

			for i in prime_numbers :
				if 0 in prime_numbers :# if the original prime_numbers set is still empty
					res = str ( collection ) [ 1 : -1 ]
					print ( '\n\t\t\t\tNot prime' + '  -->  ' + res )
					break
				else :
					print ( '\n\t\t\t\t\tPrime number!\n' )
					break

		c = input ( '\nContinue or go back to main menu?	c / m		' )
#-----------------------------------------------------------------------		
		if 'c' in c :
			continue
		else :
			begin ( )
#=============================================================
#=============================================================

def divisors ( ) :
	while True :
		user_input = int ( input ( '\nEnter a whole number to obtain its factors:	' ) )
		collection = [ 1 ]
		collection2 = user_input
		space ( )

		for i in range ( 2, user_input - 1 ) :
			if user_input % i == 0 :
				collection.append ( i )
		collection.append ( collection2 )# append the number user entered to end of list to include 

		if len ( collection ) > 2 :# if the list has more numbers than 1 or the number user entered:
			res = str ( collection ) [ 1 : -1 ]
			print ( '\t\t\t\t' + res )
		else :
			print ( '\t\t\t\t', 'This number is prime' )

		c = input ( '\nContinue or go back to main menu?	c / m		' )
#-----------------------------------------------------------------------		
		if 'c' in c :
			continue
		else :
			begin ( )
#=============================================================
#=============================================================

def leap_year ( ) :
	while True :
		year = int ( input ( '\nProvide a year:		' ) )
		if ( year % 4 == 0 and year % 100 != 0 ) or ( year % 400 == 0 )  :#if it is divisible by 4 but NOT 100 or if it is divisible by 400
			print ( '\n' + str ( year ) + ' is a leap year.' )	
		else :
			print ( '\n' + str ( year ) + ' is not leap year.' )	

		c = input ( '\nContinue or go back to main menu?	c / m		' )
#-----------------------------------------------------------------------		
		if 'c' in c :
			continue
		else :
			begin ( )
#=============================================================
#=============================================================

def mage_number ( ) :
	while True :
		witches_diction = {
					'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8, 'i' : 9, 'j' : 1,
					'k' : 2, 'l' : 3, 'm' : 4, 'n' : 5, 'o' : 6, 'p' : 7, 'q' : 8, 'r' : 9, 's' : 1,
					't' : 2, 'u' : 3, 'v' : 4, 'w' : 5, 'x' : 6, 'y' : 7, 'z' : 8
		}

		user_input = input ( '\nInput your name to view the number assocated with it:	' )
		user_input2 = int ( input ( '\nEnter your date of birth in xxyyzzzz format:	' ) )

		x = user_input.lower ( )
		collection = [ ]
		alpha_collection = [ ]
		num_collection = [ ]

		counter = 0
		counter2 = 0
		counter3 = 0
		counter4 = 0

		for a in x :
			alpha_collection.append ( a )
		for b in alpha_collection :
			if b in witches_diction :		
				num_collection.append ( witches_diction [ b ] )
		for c in num_collection :
			counter += ( c - 1 ) % 9 + 1 if c > 0 else 0
	
		num_collection.clear ( )
		num_collection.append ( counter )

		for d in num_collection :
			counter2 += ( d - 1 ) % 9 + 1 if d > 0 else 0

		for i in str ( user_input2 ) :
			i = int ( i )
			collection.append ( i )

		for j in collection :
			counter3 += ( j - 1 ) % 9 + 1 if j > 0 else 0

		collection.clear ( )
		collection.append ( counter3 )

		for k in collection :
			counter4 += ( k - 1 ) % 9 + 1 if k > 0 else 0

		if counter4 == counter2 :
			print ( '\n\t\t\t\tYour birth number and the number associated with your name match, which is ' + str ( counter4 ) )
		else :
			print ( '\n\t\t\t\tYour sacred birth number is ' + str ( counter4 ) )
			print ( '\n\t\t\t\tThe number associated with your name is ' + str ( counter2 ) ) 

		c = input ( '\nContinue or go back to main menu?	c / m		' )
#-----------------------------------------------------------------------		
		if 'c' in c :
			continue
		else :
			begin ( )
#=============================================================
#=============================================================

def powers_of_two ( ) :
	while True :
		print ( '\nPowers of 2:\n' )
		counter_collection = [ ]
		counter = 2
		while counter <= 2 ** 16 :
			counter_collection.append ( str ( counter ) )# change to string type so that I can use 'join' method to get rid of brackets
			counter *= 2
		print ( '\t\t\t\t', '  '.join ( counter_collection ) )# comma separates each number. If space separation without comma exclude comma and just use space: ' '.join ( counter_collection )

		c = input ( '\nContinue or go back to main menu?	c / m		' )
#-----------------------------------------------------------------------		
		if 'c' in c :
			continue
		else :
			begin ( )
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
begin ( )
