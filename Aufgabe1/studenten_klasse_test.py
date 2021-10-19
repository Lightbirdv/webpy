import studenten_klasse as st
from datetime import date

#creation of Student object
s = st.Student("Ralph","Peter", 999999, date(1996,12,24))

#add values to studiendokumentation
s.note_eintragen("Mathe", 3.0)
s.note_eintragen("Informatik", 1.0)
s.note_eintragen("Elektrotechnik", 4.0)

#prints and functions
## print for user
print(s.__str__())
## print for programmer
print(s.__repr__())
## print studiendokumentation as list with dicts
print(s.studiendokumentation)
## print studiendokumentation line by line 
s.noten_berichten()
## change bad notes to 1.0 and print out how many have been changed
print("Number of times cheated: " + str(s.noten_schummeln()))
## print studiendokumentation line by line again
s.noten_berichten()
