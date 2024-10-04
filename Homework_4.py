# Homework #4 - List, Debugging.
# Mackaelan Songco.

# 2 Practicing Sliding & Striding.

# 2.1 Making a List Variable.
forList = []

for i in range (0, 21):
    """
    I encountered the following error: "TypeError: type 'range' is not subscriptable"
    (detected in line 9). This was because I used brackets instead of parentheses.
    Once I switched them, the code printed successfully. 
    """
    forList.append(i)

print(forList)

# 2.2 Working with List Elements.
def squareList(list):
    squaredList = []
    for i in list:
        squaredList.append(i**2)
        """
        I encountered the following error: "TypeError: can only concatenate list (not "int") to list
        (detected in line 23). Originally I used a "for i in range (x, y)," but the "y" was len(list).
        Once I switched to "for i in x," the code printed successfully. 
        """
    return squaredList

result = squareList(forList)
print(result)

# 2.3 Slicing.
def first_fifteen_elements(list):
    fifteenList = []
    for i in range (0, 15):
        fifteenList.append(list[i])
        """
        I encountered tge following error: "AttributeError: 'list' object has no attribute 'appened'. Did you mean: 'append'?"
        (detected in line 38). I spelt "append" wrong. 
        Once I spelnt it right, the code printed successfully.
        """
    return fifteenList

print(first_fifteen_elements(result))

# 2.4 Striding.
def every_fifth_element(list):
    fifthList = list[4::5]
    return fifthList

print(every_fifth_element(result))
"""
I encountered no errors, only figuring out how to get list to desired output. 
"""

# 2.5 Slicing & Striding. 
def fancy_function(list):
    fancyList = list[::-3]
    return fancyList

print(fancy_function(result))
"""
I encountered no issues.
"""

# 3 2D List. 

# 3.1 Creating a 5x5 2D List
def create_2d_list():
    outerList = []
    for i in range (0, 5):
        innerList = [] 
        for j in range (5*i+1, 5*i+6):
            innerList.append(j)
        outerList.append(innerList)
    return outerList

matrix = create_2d_list()
print(matrix)
"""
I encountered no errors, only figuring out how to get list to desired output. 
"""

# 3.2 Replacing 2D List with Multiples of 3
def modified_2d_list(matrix):
    for i in range (0, len(matrix)): 
        """
        I encountered the following error: "NameError: name 'le' is not defined. Did you mean: 'len'?"
        (detected in line 88). I did not finish writing "len."
        Once I properly wrote it, the code printed successfully. 
        """
        for j in range (0, len(matrix[i])):
            """
            I encounted another error but it wasn't listed in the terminal. 
            I used parentheses instead of brackets which led to the program not working.
            Once I switched them, the code printed successfully. 
            """
            if matrix[i][j] % 3 == 0:
                matrix[i][j] = '?'
    return matrix

new_matrix = modified_2d_list(matrix)
print(new_matrix)

# 3.3 Summing None-’ ?’ Elements
def sum_non_question_elements(new_matrix):
    sum = 0
    for i in range (0, len(new_matrix)): 
        for j in range (0, len(new_matrix[i])):
            if new_matrix[i][j] != '?':
                sum += new_matrix[i][j]
                """
                I encountered the error: "TypeError: 'list' object is not callable"
                (detected from line 113). I originally wanted to use "list.pop()" but I could not call it.
                By switching to ignoring '?' instead of removing them, the code printed successfully. 
                """
    return sum

print(sum_non_question_elements(new_matrix))