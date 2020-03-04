#import openpyxl as xl 
#from openpyxl.chart import BarChart, Reference

#def process_workbook(filename):
#    wb = xl.load_workbook(filename)
#    sheet = wb['Sheet1']
#    for row in range(2, sheet.max_row + 1):
#        cell = sheet.cell(row, 3)
#        corrected_price = cell.value * 0.9
#        corrected_price_cell = sheet.cell(row, 4)
#        corrected_price_cell.value = corrected_price
#    values = Reference(sheet, 
#             min_row=2, 
#             max_row=sheet.max_row,
#             min_col=4,
#             max_col=4)
#
#    chart = BarChart()
#    chart.add_data(values)
#    sheet.add_chart(chart, 'e2')
#
#    wb.save(filename)


#from pathlib import Path
#path = Path()
#for file in path.glob('*.py'):
#    print(file)


#import random
#class Dice:
#    def roll(self):
#        first = random.randint(1,6)
#        second = random.randint(1,6)
#        return first, second
#dice = Dice()
#print(dice.roll())


#members = ['John', 'Mary', 'Bob']
#leader = random.choice(members)
#print(leader)


#from ecommerce.shipping import calc_shipping
#calc_shipping()


#import utils
#data = [2, 4, 6, 8, 10, 5, 4, 3, 16]
#print(utils.find_max(data))


#class Person:
#    def __init__(self, name):
#        self.name = name
#        
#    def talk(self):
#        print(f'Hi, I am {self.name}. Nice to meet you.')


#john = Person('John Smith')
#john.talk()

#bob = Person('Bob Smith')
#bob.talk()



#class Point:
#    def __init__(self, x, y):
#        self.x = x
#        self.y = y
#
#    def move(self):
#        print('move')
#    
#    def draw(self):
#        print('draw')


#point = Point(10, 20)
#print(point.x)


#try:
#    age = int(input('Age: '))
#    income = 20000
#    risk = income / age
#    print(age)
#except ZeroDivisionError:
#    print('Age cannot be 0.')
#except ValueError:
#    print('Invalid value')


#def square(number):
#    return number * number
#output = square(3)


#print(output)


#def emoji_converter(text):
#    words = text.split(' ')
#    emojis = {
#        ':)': '😃',
#        ':(': '🙃'
#        }
#    output = ''
#    for word in words:
#        output += emojis.get(word, word) + ' '
#    return output

#message = input('>')
#print(emoji_converter(message))


#phone = input('phone: ')
#mapping = {
#    '0': 'zero',
#    '1': 'one',
#    '2': 'two',
#    '3': 'three',
#    '4': 'four',
#    '6': 'six',
#}
#output = ''
#for ch in phone:
#    output += mapping.get(ch,) + ' '
#
#print(output)


#customer = {
#    'name': 'John Smith', 
#    'age': 30,
#    'is_verfied': True
#}

#customer['name'] = 'Jack smith'
#print(customer['name'])


#numbers = [5, 2, 1, 5, 7, 4]
#uniques = []

#for count in numbers:
#    if numbers not in uniques:
#        uniques.append(numbers)
#print(uniques)

#numbers = [2, 4, 6, 8, 10, 5]
#max = numbers[0]
#for count in numbers:
#    if count > max:
#        max = count
#print(max)

numbers = [1, 1, 1, 1, 5]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

#prices = [10, 20, 30]
#total = 0
#for price in prices:
#    total += price
#print(total)


# Car start and stopp program.

#guess_name = ""
#started = False
#while True:
#    guess_name = input('> ').lower()
#    if guess_name == 'start':
#        if started:
#            print('Car is already started.')
#        else:
#            started = True
#            print('Your car is started... brooom!')
#    elif guess_name == 'stop':
#        if not started:
#            print('Car is not moving.')
#        else:
#            started = False
#            print('Your car has stopped.')
#    elif guess_name == 'help':
#        print(''' 
#start - starts the the car
#stop - stops the car
#quit - to exit ''')
#    elif guess_name == 'quit':
#        break
#    else:
#        print('Sorry, I dont understand.')