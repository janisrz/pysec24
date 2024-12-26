# MD_1

print('\n\nMājas darbs Nr.1')

# Uzd. samainīt versijas:
# 1. terminālī: py -0 būs redzamas pieejamās versijas
# 1.1. ar * esošā būs noklusējuma. Man ir -V:3.13*; -V:3.11; -V3.10
# 1.2. izvēloties py -3.11 būs Python 3.11.9
# 1.3. izvēloties py -3.10 būs Python 3.10.11
# 2.VSCode: apakšējā labajā stūrī redzama versija;
# 2.1. uz tās uzklikšķinot augšā pa vidu parādīsies Select Interpreter
# 2.2. izvēlas attiecīgi versiju
# 2.3. uzspiež augšējā labajā stūrī Run Python File
# 2.4. redzu, ka var atkārtot līdzīgas darbības kā pirmajā punktā.

# MD_2

print('\n\nMājas darbs Nr.2')

# pip install virtualenv
# python.exe -m pip install --upgrade pip
# python -m venv myenv2
# myenv2\Scripts\Activate.ps1
# Set-ExecutionPolicy Unrestricted
# rezultāts (myenv2)
#  in (myenv2) pip install virtualenv
# python.exe -m pip install --upgrade pip
# Sagatavoju arī myenv3 un komanda deactivate
# rm -r myenv3 lai noņemt myenv3
# myenv2\Scripts\Activate.ps1 lai atkal nokļūtu myenv2
# pip list
# pip install numpy
# pip freeze
# pip freeze > requirements.txt

# MD_3

print('\n\nMājas darbs Nr.3')

# 3.1. Lists
# funkcija len() 
my_list = [1, 2, 3, 4, 5]
print(len(my_list))

# funkcija Concatenate
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print(concatenated_list)

# funkcija append()
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

# funkcija extend()
my_list = [1, 2, 3]
my_list.extend([4, 5, 6, 7, 8, 9])
print(my_list)

# funkcija reverse()
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list.reverse()
print(my_list)

# funkcija pop()
my_list = [1, 2, 3, 4, 5]
popped_item = my_list.pop()
print(popped_item) # Output: 5
print(my_list) #Output: [1, 2, 3, 4]

popped_item = my_list.pop(1) #Removes the item at index 1 (dators sāk skaitīt ar 0)
print(popped_item) # Output: 2
print(my_list) # Output: [1, 3, 4]

# funkcija insert()
my_list = [1, 2, 4, 5] # Nav 3
my_list.insert(2, 3) # Inserts 3 at index 2
print(my_list)

# funkcija delete
my_list = [1, 2, 3, 4, 5]
del my_list[2] # Deletes the item at index 2
print(my_list)
del my_list[1:3]
print(my_list) # Output: [1, 5]

# 3.2 Tuple
my_tuple = ("abols", "kirsis", "datele", "banans") # Creating a tuple
print(my_tuple)
# Accessing elements using indexing
first_element = my_tuple[0]
print(first_element) # Output: abols
second_element = my_tuple[1]
print(second_element) # Output: kirsis

tuple_lengt = len(my_tuple) #Getting the lenght of the tuple
print(len(my_tuple))

my_list = list(my_tuple) # Converting the tuple to a list
print(my_list)

my_set = set(my_tuple) # Converting the tuple to a set
print(my_set) # List un Set atšķiras iekavas [List] un {Set}

# 3.3 Set
my_list = ["Janis", "Karlis", "Peteris", "Uldis"] # Creating a list
my_set = set(my_list) # Converting the list to a set
print(my_set)

my_set = {"Linda", "Laura", "Vilma", "Jolita"} # Creating a set
my_list = list(my_set) # Converting the set to a list
print(my_list)

set_a = {"Valmiera", "Bauska", "Skrunda"}
set_b = {"Saldus", "Ogre", "Salaspils"}
union_set = set_a | set_b # Union of set_a and set_b
print(union_set)

set_a = {"Valmiera", "Bauska", "Alsunga", "Skrunda"} #added Alsunga
set_b = {"Alsunga", "Saldus", "Ogre", "Salaspils"} #added Alsunga
intersection_set = set_a & set_b # Intersection of set_a and set_b
print(intersection_set) # Output {'Alsunga'}

set_a = {"Valmiera", "Alsunga", "Bauska"}
set_b = {"Alsunga", "Bauska", "Ogre"}
difference_set = set_a - set_b
print(difference_set) # Output {'Valmiera'}

# 3.4 Dictionary

# Creating a dictionary
my_dict = {
    "vards": "Aldis",
    "vecums": 50,
    "pilseta": "Valmiera",
    "amats": "Direktors"
}
items = my_dict.items() # Get Tuple of items
print(items)

keys = my_dict.keys() # Get List of keys
print(keys)

values = my_dict.values() # Get List of values
print(values)

vards = my_dict.get("vards") # Get a particular item
print(vards) # Output Aldis

del my_dict["vecums"] # Deleting one item
print(my_dict) # Output - nav vecums

my_dict.clear() # All items
print(my_dict) # Output {}

# MD_4

print('\n\nMājas darbs Nr.4')

# 4.1 If Statement

vecums = 26 # Define the variable
if vecums == 6: # False
    print("Tu esi 6 gadus jauns.")
    print("Tu esi bērns.")
elif vecums == 26: # True
    print("Tu esi 26 gadus jauns.")
    print("Tu esi jaunietis.")
elif vecums == 96: # False
    print("Jūs esat 96 gadus vecs.")
    print("Jūs esat seniors.")
else:
    print("Tavs vecums neatbilst nosacījumiem.") # Else condition neizpildās, jo vecums ir 26, kas ir True.

print(vecums == 6) # Output False
print(vecums == 26) # Output True
print(vecums == 96) # Output False

vecums = 50 # Lai izpildītos else condition, vecums samainīts uz 50
if vecums == 6: # False
    print("Tu esi 6 gadus jauns.")
    print("Tu esi bērns.")
elif vecums == 26: # True
    print("Tu esi 26 gadus jauns.")
    print("Tu esi jaunietis.")
elif vecums == 96: # False
    print("Jūs esat 96 gadus vecs.")
    print("Jūs esat seniors.")
else:
    print("Tavs vecums neatbilst nosacījumiem.")

print(vecums == 50) # Output: Tavs vecums neatbilst nosacījumiem. True

# 4.2 While Loops

egles = 0 # Variable

while egles < 10:
    print(f"Egles ir {egles}")

    if egles == 3:
        print("Egles ir 3, laid tālāk")
        pass

    if egles == 5:
        print("Egles ir 5, turpini")
        egles += 1
        continue

    if egles == 8:
        print("Egles ir 8, stop")
        break

    egles += 1

else:
    print("Egles skaits 10, aplis noslēgts")

print("Aplis noslēgts")

# 4.3 For loops

for saraksts in [1, 'a', 'Janis']:
    print(saraksts)

for saraksts in [('Pitons', 'programma'), ('drošības', 'testētājiem')]:
    print(saraksts)

for saraksts in [1, 2, 3]:
    print(saraksts)
else:
    print("Aizpildīts")

# 4.4 Emulating C style FOR Loops

for R in range(1,12, 1):
    print(R) # Output no 1 līdz 11

for R in range(12, 0, -2):
    print(R) # Output samazinās pa 2 sākot no 12

# MD_5

print('\n\nMājas darbs Nr.5')

class Auto:
    def __init__(self, marka, modelis, gads): # Attributes for car
        self.marka = marka
        self.modelis = modelis
        self.gads = gads
    
    def display_info(self): # To display Auto info
        return f"Auto: {self.marka} {self.modelis} {self.gads}"
    
class Persona:
    def __init__(self, vards, vecums, dzimums, auto): # Attributes for Persona
        self.vards = vards
        self.vecums = vecums
        self.dzimums = dzimums
        self.auto = auto
    
    def greet(self): # To display a greeting
        return f"Sveiciens, mans vards ir {self.vards}!"
    
    def dzimsanas_gads(self, gads_tagad):
        return gads_tagad - self.vecums
    
    def display_info(self):
        return f"vards: {self.vards}\nvecums: {self.vecums}\ndzimums: {self.dzimums}\n{self.auto.display_info()}"

my_auto = Auto("Toyota", "Corolla", 2021)

persona1 = Persona("Jānis", 50, "Vīrietis", my_auto)

print(persona1.greet()) # Output: Sveiciens, mans vards ir Janis!
print(f"Dzimsanas gads: {persona1.dzimsanas_gads(2024)}") # Output: Dzimsanas gads: 1974
print(persona1.display_info())

# MD_6

print('\n\nMājas darbs Nr.6')

from connections_MD_6 import wifi
import pip   # Output: Connections package is being initialised! 
wifi.connect_with_wifi()            # Output: Connected through wifi!

from connections_MD_6 import mobile
mobile.connect_with_mobile_data()   # Output: Connected through mobile data!

from matematika_MD_6_1 import dati  #Output: Piemēri ar saskaitīšanu, atņemšanu, reizināšanu un dalīšanu

print(dati.add(5, 3))               # Output: 8
print(dati.subtract(5, 3))          # Output: 2
print(dati.multiply(5, 3))          # Output: 15
print(dati.divide(5, 3))            # Output: 1.6666666666666667
print(dati.divide(5, 0))            # Output: Ar nulli nedala

# MD_7

print('\n\nMājas darbs Nr.7')

# Izņēmuma piemēri Pitonā (iebūvēto ir daudz vairāk). Te norādu: IndexError, KeyError, NameError un ValueError

list = [1, 2, 3]
try:
    print(list[10])                 # Output: IndexError
except IndexError:
    print("IndexError: list index out of range")


d = {'a': 1}
try:
    print(d['a'])                   # Output: 1 (strādā)
    print(d['b'])                   # Output: KeyError
except KeyError:
    print("KeyError")


try:
    pritn('Janis') # type: ignore # Output: NameError
except NameError:
    print("NameError: Vai domāji 'print'?")

try:
    koki = 50                       # Output: būs "Kopumā ir 50", jo norādītā vērtība iekļaujas
    if koki < 1 or koki > 100:
        raise ValueError("Kokiem jābūt no 1 līdz 100.")
    print(f"Kopumā ir {koki}")
except ValueError as e:
    print(f"Nepareizi norādīts koku skaits: {e}")


try:
    koki = 122                      # Output: būs "Nepareizi norādīts koku skaits: Kokiem jābūt no 1 līdz 100."
    if koki < 1 or koki > 100:
        raise ValueError("Kokiem jābūt no 1 līdz 100.")
    print(f"Kopumā ir {koki}")
except ValueError as e:
    print(f"Nepareizi norādīts koku skaits: {e}")

# MD_8

print('\n\nMājas darbs Nr.8')

print("Skatīt failu: read_usb_logs.py")

# MD_9

print('\n\nMājas darbs Nr.9')

print("Skatit failu MD_9.py")

# MD_10

print('\n\nMājas darbs Nr.10')

print("Skatit failu MD_10.py")

# MD_11

print('\n\nMājas darbs Nr.11')

print("Skatit failu MD_11.py")

# MD_12

print('\n\nMājas darbs Nr.12')

print("Skatit failu MD_12.py")
print('\nKā arī skatīt failu MD_12_1.py, kas ir papildinājums MD_12.py" ar papildus informāciju.')
print('\nKā arī skatīt failu MD_12_2.py, kas ir papildinājums MD_12.py"\n'
      'ar mēģinājumu faila lejupielādei, bet nesekmīgi,\n'
      'proti: HTTP Error 403: Forbiden.')