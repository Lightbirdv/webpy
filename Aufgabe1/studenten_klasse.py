from datetime import date

class Student(object):

    vorname: str
    nachname: str
    matrikelnummer: int
    geburtsdatum: date
    studiendokumentation: dict


    def __init__(self, vorname, nachname, matrikelnummer, geburtsdatum):
        self.vorname = vorname
        self.nachname = nachname
        self.matrikelnummer = matrikelnummer
        self.geburtsdatum = geburtsdatum
        self.studiendokumentation = []


    def __str__(self):
        return self.vorname + " " + self.nachname + ", " + str(self.matrikelnummer) + ", " + self.geburtsdatum.strftime("%B %d %Y")
    

    def __repr__(self):
        return "Student(" + self.vorname + "," + self.nachname + "," + str(self.matrikelnummer) + "," + self.geburtsdatum.strftime("%B %d %Y") + ")"


    def note_eintragen(self, kurs, note):
        self.studiendokumentation.append({kurs : note})


    def noten_berichten(self):
        for occurence in self.studiendokumentation:
            for k,v in occurence.items():
                print(k, v)


    def noten_schummeln(self):
        counter = 0
        for occurence in self.studiendokumentation:
            for k,v in occurence.items():
                if v > 1.0:
                    occurence.update({k : 1.0})
                    counter = counter+1
        return counter
           