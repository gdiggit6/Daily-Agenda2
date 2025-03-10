


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

dictionary_values = {
		'key1' : 23,
		'key2' : 54,
		'key3' : 2,
		'key4' : 99,
		'key5' : 32
}
space ( )

def keyvaluepairs ( x ) :
	for key, value in x.items ( ) :
		print ( key, '=', value )
	return x
print ( keyvaluepairs ( dictionary_values ) )
space ( )
#=============================================================
#=============================================================

def max_value ( x ) :
	max_dictionary_value = [ ]
	for i in x.values ( ) :
		max_dictionary_value.append ( i )
	return max ( max_dictionary_value )
space ( )
print ( 'The largest value in this dictionary is', max_value ( dictionary_values ), '\b.' )
space ( )
#=============================================================
#=============================================================

def add_ten ( x ) :
	print ( '\nAdding 10 to the even values of a dictionary...\n' )	
	for value in x.values ( ) :
		if value % 2 == 0 :
			value2 = value + 10			
			print ( value2, ' <-- added 10' )
		else :
			print ( value )

	for key in x :
		if x [ key ] % 2 == 0 :
			x [ key ] += 10
	space ( )
	return x

print ( add_ten ( dictionary_values ) )
space ( )
#=============================================================
#=============================================================

def add_ten_more ( x ) :
	new_x = x.copy ( )
	for i in new_x :#for every key in new_x
		if new_x [ i ] % 2 == 0 :#if the value is divided by 2 and the result ihas no remainder (an even number)
			new_x [ i ] += 10# add 10 to this
	space ( )
	return new_x

print ( add_ten_more ( dictionary_values ) )
space ( )
#=============================================================
#=============================================================

base_prices = {
	'shoes' : 235,
	't-shirt' : 49,
	'pullover' : 109
}

discounts = {
	'shoes' : 40,
	'pullover' : 9
}

def calculate_discount ( b, d ) :
	new_value = b.copy ( )
	for i in new_value.keys ( ) :
#		print ( i, ' <-- key for base_prices' )
		for j in d.keys ( ) :
#			print ( j, ' <-- key for discounts' )
			if i == j :
				print ( i, j, ' <-- match!' )

	return new_value

print ( calculate_discount ( base_prices, discounts ) )
space ( )
#=============================================================
#=============================================================

def calculate_discount2 ( x, y ) :#holders for 2 dictionarys for forthcoming opertion
	space ( )
	z = x.copy ( )
	for i in z :
		for j in y :
			if i == j :
				discount = ( ( z [ i ] ) - ( y [ j ] ) )
				z [ i ] = discount
	space ( )
	return z
print ( calculate_discount2 ( base_prices, discounts ) )
space ( )
for i in base_prices :
	print ( base_prices [ i ], ' <--original price' )
space ( )
#=============================================================
#=============================================================

en_de = {
	'cat' : 'Katze',
	'dog' : 'Hund',
	'pig' : 'Schweine'
}

en_de [ 'pig' ] = 'Schwein'
en_de [ 'guinea pig' ] = 'Meerschweinchen'

for i in en_de :
	print ( i, ':', en_de [ i ] )

space ( )
#=============================================================
#=============================================================

morse = { 
       		 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
	         'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
	         'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
	         'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
	         'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
        	 '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        	 '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--'
}

def translate_into_morse ( x ) :
	text = input ( '\nEnter a string for translation into morse code:	' )
	text = text.upper ( )

	for i in text :#iterate through each element in user input
		for key, value in x.items ( ) :#iterate through both the keys and associated values of the  morse dictionary 
			if i == key :#if i matches up with the key 
				print ( i, ' -> ', value )#print the associated value of the morse dictionary
	return key

print ( translate_into_morse ( morse ) )

space ( )
#=============================================================
#=============================================================

#text = input ( '\nEnter a string for translation into morse code:	' )

def translate_into_morse ( x, y ) :
	x = x.upper ( )
	code = [ ] 

	for i in x :
		for key, value in y.items ( ) :
			if i == key :
				code.append ( value )
			#	print ( i, ' -> ', value )
			else :
				pass
		if i not in y :
			code.append ( i )
	data = ''
	print ( data )
	return ''.join ( code )

#print ( translate_into_morse ( text, morse ) )
space ( )
#=============================================================
#=============================================================
print ( 'Calculate costomer order\n' )
costomer_order = {
	'cheese' : 3,
	'coke' : 2,
	'ass juice' : 1,
	'bread' : 2,
	'butter' : 1
}

def calculate_price ( x ) :# < temporary holder for the 'y' dictionary - also acts as a gateway for the 'y' value
	pricelist = { 'bread' : 2.37, 'ham' : 3.48, 'cheese' : 3.09, 'water' : 1.19, 'coke' : 2.58, 'juice' : 4.18, 'butter' : 5.18 }		
	space ( )
	total_cost = [ ]
	for a, b in x.items ( ) :
		for c, d in pricelist.items ( ) :
			if a == c :
				t = ( b * d )
				total_cost.append ( t )
	return ( sum ( total_cost ) )

print ( calculate_price ( costomer_order ) )
space ( )
#=============================================================
#=============================================================
print ( 'Calculate costomer order different way\n' )
pricelist = { 
	'bread' : 2.37, 
	'ham' : 3.48, 
	'cheese' : 3.09, 
	'water' : 1.19, 
	'coke' : 2.58, 
	'juice' : 4.18, 
	'butter' : 5.18 
}		

def calculate_price ( order ) :
	amount = 0.0
	for key, value in order.items ( ) :
		if key in pricelist :
			amount += value * pricelist [ key ]
	return amount

#print ( calculate_price ( costomer_order ) )
space ( )
#=============================================================----------------------------------------------------------------Handling Files
#=============================================================

file = open ( 'daily_sales.txt', 'r' )
print ( file.read ( ) )
file.close ( )
space ( )
#Text file modes:
#'r' - read: file can only be read
#'w' - write: a file with the given name is created ( or overwritten if it already exists) for writing only
#'a' - append: a file with the given name is opened for adding new info at the end.
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

with open ( 'user_data.txt', 'w' ) as file :#<--open the file for editing
	nickname = input ( 'What is your nickname?	' )#<--get user input
	age = input ( 'What is your age?	' )#<--get user input
	file.writelines ( 'Nickname: ' + nickname + '\n' + 'Age: ' + age )#<--file automaticaliy closes when using the 'with' function after operations
space ()
file = open ( 'user_data.txt', 'r' )
print ( file.read ( ) )
file.close ( )
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#file = open ( 'daily_sales.txt', 'a' )
#file.write ( '\nDay 8 (Monday): 19432.19' + '\n' )
#file.write ( 'Day 9 (Tuesday): 18233.76' + '\n' )
#file.write ( 'Day 10 (Wednesday): 23432.43' + '\n' )
#file.close ( )

#file = open ( 'random_numbers.txt', 'r' )
#numbers = [ ]
#for i in file :
#	i = int ( i )
#	numbers.append ( i )
	
#print ( max ( numbers ) )
#print ( min ( numbers ) )
#file.close ( )

space ( )
#=============================================================
#=============================================================

subjects = [ 'math', 'biology', 'chemistry', 'physics' ]
file = open ( 'urls.txt', 'w' )#<--file open for editing

for i in subjects :#<--iterate through each element in the subjects list
	for year in range ( 2010, 2019 ) :#<--literate through each year starting with 2010 and ending at 2019
		file.writelines ( 'http://imaginary-site.com/download/'+( i )+'-'+str ( year )+'\n' )
file.close ( )#<--close the file

file = open ( 'urls.txt', 'r' )#<--open the file in read-only mode to verify results
print ( file.read ( ) )#<--present the contents of the file onscreen
file.close ( )#<--close the file	

space ( )
#=============================================================----------------------------------------------------------Exceptions and IOError handling
#=============================================================

file_name = input ( 'Provide a file name:	' )
try :
	with open ( file_name, 'r' ) as file :
		print ( 'Read the file successfully!' )
		print ( file.read ( ) )
except IOError :
	print ( '\nThe file does not exist!' )

space ( )
#=============================================================
#=============================================================

while True :
	try :
		file_name = input ( '\nProvide a file name:	' )
		space ( )
		with open ( file_name, 'r' ) as file :
			print ( file.read ( ) )
			break
	except IOError :
		print  ( '\nCould not read the file. Try another one.\n' )
space ( )
#=============================================================
#=============================================================

username = input ( '\nWhat is your name?	' )
with open ( 'question_1.txt', 'w' ) as file :
	file.writelines ( 'Question 1' + '\n' + username )

file = open ( 'question_1.txt', 'r' )
print ( file.read ( ) )
file.close ( )

space ( )
#=============================================================
#=============================================================

with open ( 'question_2.txt', 'a' ) as file :
#		print ( file.read ( ) )
	for i in file :	
#			print ( '\n|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||Begin|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n' )
		file.writelines ( '\n|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||Begin|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n' )

#			print ( i, '^---for i', type ( i ) )
		file.writelines ( i + '^---for i' + type ( i ) )
		space ( )
		j = str ( i )
#		print ( j, '^----------------------------------------------------------------this is str ( i )', type ( j ) )
#		file.writelines ( j, '^----------------------------------------------------------------this is str ( i )', type ( j ) )
		space ( )			
			
			print ( i + '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^--------------this is int ( i )' )
#		file.writelines ( k, '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^--------------this is int ( k )' )
			print ( '\nEnd..............................................................................................................................................................................................end' )
#		file.writelines ( '\nEnd..............................................................................................................................................................................................end' )			
#except ValueError :	
	print ( 'An error occured^____!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!value of i' )
#	file.writelines ( type ( i ) + '^____!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!value of i' )

space ( )
#=============================================================
#=============================================================
counter = 0
with open ( 'question_2.txt', 'r' ) as file :
	for i in file :
		try :
			current_num = int ( i )
			if current_num > 0 :
				counter += 1
		except ValueError :
			print ( 'Problem...' )			
			continue
print ( counter )
space ( )
#=============================================================
#=============================================================

palindrome = input ( '\nEnter a word:	' )
def is_palindrome ( x ) :
	str = ''
	for i in x :
		str = i + str
	if x == str :
		return True
	else :
		return False
print ( is_palindrome ( palindrome ) )
space ( )
#=============================================================
#=============================================================

word = input ( '\nName the word:	' )

def count_word ( file_name, x ) :
	x = x.lower ( )
	count = 0
	with open ( file_name, 'r' ) as f :
		for i in f :
			i = i.strip ( )
			i = i.lower ( )
			words = i.split ( ' ' )
			
			for j in words :
				if j == x :
					count += 1
				else :
					count += 0
	return count

print ( '\nThis word occurs ', count_word ( 'word_capture.txt', word ), 'times.' )
space ( )
#=============================================================
#=============================================================
'''
number = int ( input ( '\nInput a number:	' ) )

def second_powers ( x ) :#<--x represents an argument that will be called outside the function	
	square_dictionary = { }#<--empty dictionary 
	for i in range ( 2, x + 1 ) :
		if i % 2 == 0 :#<--if i divided by 2 has no remainder (an even number)
			square_dictionary [ i ] = i * i#<--add the key with its associated second power to dictionary_even
		else :
			continue#<--continue through the next iteration if i is other than that specified above
	return ( square_dictionary )
	
print ( '\nAll even keys from 2 to user input with their respective second powers values:\n\n', second_powers ( number ) )#<--call number, ie, pass the variable number through the function and print the returned dictionary within the function

space ( )
#=============================================================
#=============================================================


train_connection = [
	( 'Paris', 'Lyon', 393, 45.00 ),
	( 'Marseille', 'Nice', 200, 24.00 ),
	( 'Nantes', 'Montepellier', 811, 91.00 ),
	( 'Paris', 'Grenoble', 580, 67.00 )
]
