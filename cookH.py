import time

'''
This is Edward's cooking helper.
This program takes the ingredients used in a dish and keeps track of them.
You can then use this to look up dishes or look at the interactions between ingredients.
'''

def reader(file):
    inF = open(file, 'r')
    dishes = []
    for line in inF:
        line = line.strip()
        line = line.split('---')
        temp = []
        for obj in line:
            try:
                temp.append(obj.upper())
            except:
                temp.append(obj)
        dishes.append(Dish(str(temp[0]), temp[1].split(', '), \
                           int(temp[2]), str(temp[3])))
    inF.close()
    return dishes

def print_loop(strIn):
    temp = ''
    for obj in strIn:
        temp += str(obj)+'\n'
    return temp

class Dish:
    '''
    This is a dish (food)
    Input the ingredients used in the dish, how well the dish turned out, and some notes for the dish.
    '''
    def __init__(self, name, ingred, rating, notes):
        self.name = name
        self.ingred = ingred
        self.rating = rating
        self.notes = notes

    def __str__(self):
        return 'Name: %s\n\n'%self.name+ \
               'Ingredients:\n'+ print_loop(self.ingred)+ '\n'+\
               'Rating: %d \n\n'%self.rating+ \
               'Notes: %s'%self.notes

    def __repr__(self):
        self.ingred = ', '.join(self.ingred)
        return '%s---%s---%d---%s\n'%(self.name.upper(), self.ingred, \
                                    self.rating, self.notes)

def dish_finder(dishes, ingreds):
    print()
    temp = []
    for dish in dishes:
        for ingred in ingreds:
            count = 0
            if ingred.upper() in dish.ingred:
                count += 1
        if count > 0:
            temp.append((dish, count))
        
    rips = 0
    for dish in temp:
        rips += 1
        print('%d. '%rips+dish[0].name+ \
              ' %d common ingredients'%count)

    choice = int(input('\nWhat dish would you like to choose? '))
    print()
    print(temp[choice-1][0])
    time.sleep(15)

def open_book(dishes):
    print("\nHere's the list of "+'"recipes" stored:')
    counter = 0
    for dish in dishes:
        counter += 1
        print('%d. '%counter+dish.name)
    choice = int(input('\nWhich dish would you like to choose? '))
    print()
    print(dishes[choice-1])
    time.sleep(15)

def ing_counter(dishes, ingreds):
    tempL = []
    for dish in dishes:
        inD = True
        for ingred in ingreds:
            if not ingred.upper() in dish.ingred and dish.rating > 5:
                inD = False
        if inD:
            tempL += dish.ingred

    seen = []
    counts = []
    for ingred in tempL:
        if not ingred.upper() in seen:
            seen.append(ingred.upper())
            counts.append((ingred.upper(), tempL.count(ingred.upper())))
    return counts

def maker(dishes):
    name = input('What is the name of the dish? ')
    for dish in dishes:
        if name.upper() == dish.name.upper():
            print('This dish already exists!')
            return dishes

    temp = []
    count = quitter = 0
    while quitter != '':
        count += 1
        quitter = (input('Ingredient %d (no plurals,'%count+ \
                         'press enter when done): ').upper())
        if quitter != '':
            temp.append(quitter)
    rating = int(input('How would you rate the dish (1-10)? '))
    note = input('Any notes for the dish? ')
    try:
        note = note.upper()
        if note == '':
            note = 'NA'
    except:
        note = 'NA'
    dish = Dish(name, temp, rating, note)
    dishes.append(dish)
    return dishes

def printer(dishes, file):
    outF = open(file, 'w')
    for dish in dishes:
        outF.write(repr(dish))
    outF.close()
