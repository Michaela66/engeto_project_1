registrovani = {
    'USER': 'PASSWORD',
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123',
}
oddelovac = '----------------------------------------'

TEXTS = {
    '1': """Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. """,

    '2': """At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.""",

    '3': """The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present."""
}

username = input('username:')
password = input('password:')

if username not in registrovani:
    print('unregistered user, terminating the program..')
    quit()
elif username in registrovani and registrovani.get(username) != password:
    print('wrong password, terminating the program..')
    quit()
else:
    print(f"""{oddelovac}
Welcome to the app, {username}
We have 3 texts to be analyzed.
{oddelovac}""")

# vycistit text
vycisteny_text_1 = []
text_1 = TEXTS.get('1')

for slovo in text_1.split():
    vycisteny_text_1.append(slovo.strip(".:;,-"))

vycisteny_text_2 = []
text_2 = TEXTS.get('2')

for slovo in text_2.split():
    vycisteny_text_2.append(slovo.strip(".:;,-"))

vycisteny_text_3 = []
text_3 = TEXTS.get('3')

for slovo in text_3.split():
    vycisteny_text_3.append(slovo.strip(".:;,-"))

# celkovy pocet slov
celkem_1 = len(vycisteny_text_1)
celkem_2 = len(vycisteny_text_2)
celkem_3 = len(vycisteny_text_3)

# titlecase words
title_1 = 0
for word in vycisteny_text_1:
    if word.istitle():
        title_1 += 1

title_2 = 0
for word in vycisteny_text_2:
    if word.istitle():
        title_2 += 1

title_3 = 0
for word in vycisteny_text_3:
    if word.istitle():
        title_3 += 1

# uppercase words
uppercase_1 = 0
for word in vycisteny_text_1:
    if word.isupper() and word.isalpha():
        uppercase_1 += 1

uppercase_2 = 0
for word in vycisteny_text_2:
    if word.isupper() and word.isalpha():
        uppercase_2 += 1

uppercase_3 = 0
for word in vycisteny_text_3:
    if word.isupper() and word.isalpha():
        uppercase_3 += 1

# lowercase words
lowercase_1 = 0
for word in vycisteny_text_1:
    if word.islower() and word.isalpha():
        lowercase_1 += 1

lowercase_2 = 0
for word in vycisteny_text_2:
    if word.islower() and word.isalpha():
        lowercase_2 += 1

lowercase_3 = 0
for word in vycisteny_text_3:
    if word.islower() and word.isalpha():
        lowercase_3 += 1

# numeric strings
numeric_1 = 0
for word in vycisteny_text_1:
    if word.isnumeric():
        numeric_1 += 1

numeric_2 = 0
for word in vycisteny_text_2:
    if word.isnumeric():
        numeric_2 += 1

numeric_3 = 0
for word in vycisteny_text_3:
    if word.isnumeric():
        numeric_3 += 1

# all numbers
all_numbers_1 = []
for number in vycisteny_text_1:
    if number.isnumeric():
        all_numbers_1.append(int(number))
sum_numbers_1 = sum(all_numbers_1)

all_numbers_2 = []
for number in vycisteny_text_2:
    if number.isnumeric():
        all_numbers_2.append(int(number))
sum_numbers_2 = sum(all_numbers_2)

all_numbers_3 = []
for number in vycisteny_text_3:
    if number.isnumeric():
        all_numbers_3.append(int(number))
sum_numbers_3 = sum(all_numbers_3)

# delka slov
delky_slov_1 = [len(slovo) for slovo in vycisteny_text_1]
delky_slov_2 = [len(slovo) for slovo in vycisteny_text_2]
delky_slov_3 = [len(slovo) for slovo in vycisteny_text_3]

# cetnost delek
cetnosti_delek_1 = {}
for delka in delky_slov_1:
    if delka in cetnosti_delek_1:
        cetnosti_delek_1[delka] += 1
    else:
        cetnosti_delek_1[delka] = 1

cetnosti_delek_2 = {}
for delka in delky_slov_2:
    if delka in cetnosti_delek_2:
        cetnosti_delek_2[delka] += 1
    else:
        cetnosti_delek_2[delka] = 1

cetnosti_delek_3 = {}
for delka in delky_slov_3:
    if delka in cetnosti_delek_3:
        cetnosti_delek_3[delka] += 1
    else:
        cetnosti_delek_3[delka] = 1

vyber_cisla = input('Enter a number btw. 1 and 3 to select:')
if vyber_cisla.isnumeric() == True and vyber_cisla not in TEXTS.keys():
    print('Toto číslo není v rozmezí 1-3')
    quit()
elif vyber_cisla.isnumeric() == False:
    print('Zadaná hodnota není číslo')
    quit()
elif vyber_cisla == '1':
    print(oddelovac)
    print(f"There are {celkem_1} words in the selected text.")
    print(f"There are {title_1} titlecase words.")
    print(f"There are {uppercase_1} uppercase words.")
    print(f"There are {lowercase_1} lowercase words.")
    print(f"There are {numeric_1} numeric strings.")
    print(f"The sum of all the numbers {sum_numbers_1}.")
    print(oddelovac)
    print(f"LEN| OCCURENCES  |NR.")
    print(oddelovac)
    # poradi
    if vyber_cisla == '1':
        poradi_1 = sorted(cetnosti_delek_1.items())

        for cislo in poradi_1:
            pocet_hvezda_1 = cislo[1] * '*'
            pocet_cislo_1 = cislo[1]
            print(f"{cislo[0]: >3}|{pocet_hvezda_1: <13}|{pocet_cislo_1}")
elif vyber_cisla == '2':
    print(oddelovac)
    print(f"There are {celkem_2} words in the selected text.")
    print(f"There are {title_2} titlecase words.")
    print(f"There are {uppercase_2} uppercase words.")
    print(f"There are {lowercase_2} lowercase words.")
    print(f"There are {numeric_2} numeric strings.")
    print(f"The sum of all the numbers {sum_numbers_2}.")
    print(oddelovac)
    print(f"LEN| OCCURENCES       |NR.")
    print(oddelovac)
    # poradi
    if vyber_cisla == '2':
        poradi_2 = sorted(cetnosti_delek_2.items())

        for cislo in poradi_2:
            pocet_hvezda_2 = cislo[1] * '*'
            pocet_cislo_2 = cislo[1]
            print(f"{cislo[0]: >3}|{pocet_hvezda_2: <18}|{pocet_cislo_2}")
elif vyber_cisla == '3':
    print(oddelovac)
    print(f"There are {celkem_3} words in the selected text.")
    print(f"There are {title_3} titlecase words.")
    print(f"There are {uppercase_3} uppercase words.")
    print(f"There are {lowercase_3} lowercase words.")
    print(f"There are {numeric_3} numeric strings.")
    print(f"The sum of all the numbers {sum_numbers_3}.")
    print(oddelovac)
    print(f"LEN| OCCURENCES     |NR.")
    print(oddelovac)
    # poradi
    if vyber_cisla == '3':
        poradi_3 = sorted(cetnosti_delek_3.items())

        for cislo in poradi_3:
            pocet_hvezda_3 = cislo[1] * '*'
            pocet_cislo_3 = cislo[1]
            print(f"{cislo[0]: >3}|{pocet_hvezda_3: <16}|{pocet_cislo_3}")

