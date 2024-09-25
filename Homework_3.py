# Homework 3 - Data Types, Functions, Conditionals, and Loops.

# 1 Oski Stole Your Power.
x = 2 
y = 3
def computePower(a,b):
    a_initial= a
    while b > 1: 
        a = a*a_initial
        b -= 1
    return a
print (computePower (x, y))

# 2 What Should I Wear?
readings = [15, 14, 17, 20, 23, 28, 20]
def temeperatureRange(list):
    minTemp = min(list)
    maxTemp = max(list)
    minMax = (minTemp, maxTemp)
    return minMax
print (temeperatureRange(readings))

# 3 Check if it's the Weekend.
day = 6 # Saturday
def isWeekend(d):
    if d >= 6:
        return True
    else:
        return False
print(isWeekend(day))

# 4 Fuel Efficiency Calculator.
distance = 70 # miles
fuel = 21.5 # gallons
def fuel_efficiency(d,f):
    fe = round((d/f),2)
    return fe
print(fuel_efficiency(distance, fuel))

# 5 Secret Code.
n = 12345
def decodeNumbers(number):
    lastDigit = number % 10
    otherDigits = number // 10
    counter = 0
    while number != 0:
        number = number // 10
        counter += 1
    number = lastDigit*10**(counter-1)+otherDigits
    return number 
print(decodeNumbers(n))

# 6 Min & Max but with Loops.
# 6.1 For Loops.
nums = [2024, 98, 131, 2, 3, 72]
def find_min_with_for_loop(list):
    min = list[0]
    for i in range (0, len(list)):
        if list[i] < min:
            min = list[i]
    return min
def find_max_with_for_loop(list):
    max = list[0]
    for i in range (0, len(list)):
        if list[i] > max:
            max = list[i]
    return max
print (find_min_with_for_loop(nums))
print (find_max_with_for_loop(nums))

# 6.2 While Loops.
nums = [2024, 98, 131, 2, 3, 72]
def find_min_with_while_loop(list):
    i = 0
    min = list[0]
    while i < len(list):
        if list[i] < min:
            min = list[i]
        i += 1
    return min
def find_max_with_while_loop(list):
    i = 0
    max = list[0]
    while i < len(list):
        if list[i] > max:
            max = list[i]
        i += 1
    return max
print (find_min_with_while_loop(nums))
print (find_max_with_while_loop(nums))

# 7 Counting Vowels.
text = "UC Berkeley, founded in 1868"
def vowel_and_consonant_count(text):
    vowels = 0 
    consonants = 0 
    vowelsList = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in range (0, len(text)):
        if text[i].isalpha() == True:
            for j in range (0, len(vowelsList)):
                if text[i] == vowelsList[j]:
                    vowels += 1
            consonants += 1
    consonants = consonants - vowels
    return ((vowels, consonants))
print(vowel_and_consonant_count(text))

# 8 Caclulate Digital Root. 
num = 2468
def digital_root(num):
    counter = 0
    numLength = num 
    while numLength != 0:
        numLength = numLength // 10
        counter += 1
    sum = 0
    for i in range (1, counter+1):
        numChange = num
        j = i 
        numChange = numChange // (10**(j-1))
        numChange = numChange % (10)
        sum += numChange
    return sum
print(digital_root(num))