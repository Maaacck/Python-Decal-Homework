import numpy as np
# Homework 5 - Numpy Arrays
# Mackaelan Songco

# 1 The Odd Ones Out.
arr = np.array([[1, 2, 3], [5, 7, 9], [2, 4, 6], [7, 7, 7]])

def onlyOdd(arr):
    oddOnly = []
    for i in arr:
        if np.sum(i)%2 != 0:
            oddOnly.append(i)
    return oddOnly

oddOnesOut = onlyOdd(arr)
print(oddOnesOut)

# 2 Let's Plat Checkers.

# 2.1 
def checkerboard():
    checkerboard = np.array([[0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0]])
    return checkerboard

print(checkerboard())

# 2.2 
def checkerboardTwo():
    checkerboardTwo = checkerboard()
    for i in range (0, 8):
        if i%2 !=0:
            checkerboardTwo[i][:checkerboardTwo.size//1:2] = 1
    return checkerboardTwo

print(checkerboardTwo())

# 2.3
def checkerboardThree():
    checkerboardThree = checkerboard()
    for i in range (0,8):
        if i%2 == 0:
            checkerboardThree[i][:checkerboardThree.size//1:2] = 1
        else:
            checkerboardThree[i] = [1, 1, 1, 1, 1, 1, 1, 1]
            checkerboardThree[i][:checkerboardThree.size//1:2] = 0
    return checkerboardThree

print(checkerboardThree())

# 2.4
def reverse_checkerboard():
    reverse_checkerboard = checkerboard()
    for i in range (0,8):
        if i%2 != 0:
            reverse_checkerboard[i][:reverse_checkerboard.size//1:2] = 1
        else:
            reverse_checkerboard[i] = [1, 1, 1, 1, 1, 1, 1, 1]
            reverse_checkerboard[i][:reverse_checkerboard.size//1:2] = 0
    return reverse_checkerboard

print(reverse_checkerboard())

# 3 The Expanding Universe 
universe = np.array(['galaxy', 'clusters'])

def expansion(universe, expansion):
    for i in range (0, expansion):
        universe = np.char.join(" ", universe)
    return universe

print(expansion(universe, 2))

# 4 
np.random.seed(42)
planets = np.random.randint(100, 1000, (5, 5))

def secondLargest(planets):
    secondLargest = []
    index = np.argsort(planets, axis=0)[-2, :]
    secondLargest = planets[index, np.arange(planets.shape[1])]
    return secondLargest

print(planets)
print(secondLargest(planets))