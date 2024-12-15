# pirmais mājasdarbs
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

# Uzdevums nav pabeigts, vēl būs Dictionary un Set