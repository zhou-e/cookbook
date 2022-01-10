import cookH
import os
import operator
import time

print("Welcome to Edward's cooking tool!")

keepUp = True
while keepUp:
    try:
        filename = input('What is the name of the text file of your ingredients? ')+'.txt'
        dishes = cookH.reader(filename)
        keepUp = False
    except FileNotFoundError:
        print('Try agane!')

rekt = 'T'
while rekt == 'T':
    os.system('cls')

    print('\nYou can:')
    print('(F)ind dishes with your current ingredients,')
    print('(O)pen cookbook,')
    print('(S)earch for collaboration of ingredients,')
    print('(M)ake a new dish,')
    print('or (E)xit.\n')
    choice = input('What would you like to do? ')

    if choice.lower() == 'f':
        os.system('cls')

        user = count = 0
        ingreds = []
        print('\nWhat ingredients pairs are you searching for?')
        while user != '':
            count += 1
            user = input('Ingredient %d (press enter '%count+ \
                         'again when finished): ')
            if user != '':
                ingreds.append(user)
        
        cookH.dish_finder(dishes, ingreds)

    elif choice.lower() == 's':
        os.system('cls')
        
        user = count = 0
        print('\nWhat ingredients pairs are you searching with?')
        ingreds = []
        while user != '':
            count += 1
            user = input('Ingredient %d (press enter '%count+ \
                         'again when finished): ')
            if user != '':
                ingreds.append(user)
                
        counts = cookH.ing_counter(dishes, ingreds)
        print()
        counts.sort(key = operator.itemgetter(1), reverse = True)
        for count in counts:
            print(count[0].upper()+': '+str(count[1]))
        time.sleep(15)

    elif choice.lower() == 'o':
        cookH.open_book(dishes)

    elif choice.lower() == 'm':
        os.system('cls')
        cookH.maker(dishes)

    elif choice.lower() == 'e':
        rekt = 'F'
        cookH.printer(dishes, filename)
            
    else:
        print('Please type a correct input.')
