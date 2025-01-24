def space():
	print('\n')
space()
import datetime
now = datetime.datetime.today()
print("\n\t\t\t\t\tDaily Agenda")
print("\t\t\t\t\t" + now.strftime("%A, %B %e, %Y"))
space()

#Sabbat datetimes (month, day). Notice how the year isn't listed, this is because we are going to keep this going year to year
sabbats = [
	("Imbolc, Snow Drop Festival", (2, 2)),#february
	("Spring Equinox", (3, 20)),#march
	("Beltane", (5, 1)),#may
	("Summer Solstice", (6, 20)),#june
 	("First Harvest", (8, 1)),#august
	("Autumn Equinox", (9, 21)),#september
    	("Samhain", (10, 31)),#october
    	("Yule", (12, 21))#december
]

newmoons = [
	("New Moon", (1, 29)),#january
	("New Moon", (2, 27)),#february
	("Super New Moon", (3, 29)),#march
	("Super New Moon", (4, 27)),#april
	("New Moon", (5, 26)),#may
	("New Moon", (6, 25)),#june
	("New Moon", (7, 24)),#july
	("Black Moon", (8, 23)),#august
	("New Moon", (9, 21)),#september
	("New Moon", (10, 21)),#october
	("Micro New Moon", (11, 20)),#november
	("New Moon", (12, 19))#december
]
	
fullmoons = [
	("Wolf Moon", (1, 13)),#january
	("Snow Moon", (2, 12)),#february
	("Worm Moon", (3, 14)),#march
	("Pink Moon, Micro Full Moon", (4, 12)),#april
	("Flower Moon",(5, 12)),#may
	("Strawberry Moon", (6, 11)),#june
	("Buck Moon", (7, 10)),#july
	("Sturgeon Moon", (8, 9)),#august
	("Corn Moon", (9, 7 )),#september
	("Hunter\'s Moon", (10, 6)),#october 
	("Beaver Moon, Super Full Moon", (11, 5)),#november
	("Cold Moon, Super Full Moon", (12, 4))#december
]

eclipses = [
	("Total Lunar Eclipse in Virgo", (3, 14)),#march 14, embrace analytical abilities
	("Partial Solar Eclipse in Aries", (3, 29)),#march 29, carnal impulses
	("Total Lunar Eclipse in Pisces", (9, 7)),#september 7, chase our fantasies and romance
	("Partial Solar Eclipse in Virgo", (9, 21)),#september 21, let go of fears in practical ways
]


# Calculate the event dates for the current year
year = now.year
sabbat_calculate = [(name, datetime.datetime(year, month, day)) for name, (month, day) in sabbats]
fullmoon_calculate = [(name, datetime.datetime(year, month, day)) for name, (month, day) in fullmoons]
eclipse_calculate = [(name, datetime.datetime(year, month, day)) for name, (month, day) in eclipses]
#formatted_date_time = now.strftime('%A, %B %d, %Y %I:%M:%S %p')

# Find the next event
for event_name, event_date in sabbat_calculate:
	if event_date > now:
        # Calculate the difference in days
	        next_event = event_date - now
	        days_left = next_event.days
        # Format the event date and time
	        formatted_event_date = event_date.strftime('%A, %B %d, %Y')
	        print(f'\t\t\t{event_name}: {days_left} days, {formatted_event_date}')
	        break

# Find full moon
for event_name, event_date in fullmoon_calculate:
	if event_date > now:
		next_event = event_date - now
		days_left = next_event.days 
		formatted_event_date = event_date.strftime('%A, %B %d, %Y')
		print(f'\n\t\t\t{event_name}: {days_left} days, {formatted_event_date}')
		break         
		
# Find next eclipse
for event_name, event_date in eclipse_calculate:
	if event_date > now:
		next_event = event_date - now
		days_left = next_event.days 
		formatted_event_date = event_date.strftime('%A, %B %d, %Y')
		print(f'\n\t\t\t{event_name}: {days_left} days, {formatted_event_date}')
		break         
        



space()
