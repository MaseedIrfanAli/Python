number = int(input("Enter the number "))
if number > 0: 
    print('Positive')
else : print('Not Positive')


if number % 2 == 0:
    print('even')
elif number % 2 == 1:
    print('odd')
else : print('not defined')    

if number >=1 and number<= 10:
    print("within the expected range")
else : print("not in the expected range")

if number < 10:
    print('Small')
elif number > 10 and number <= 20:
    print('Medium')
else:
    print('Large')        


k= input("Enter the string ")
if len(k) > 10:
    print('Long string')
else: print('Short string')

find_leapyear = int(input("Enter the year "))
if find_leapyear % 400 == 0 or (find_leapyear % 100 !=0 and find_leapyear % 4 == 0):
        print("leap year")
else: print("not leap year")         


