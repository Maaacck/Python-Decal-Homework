
import numpy as np
import matplotlib.pyplot as plt
import random

# Mackaelan Songco
# October 31, 2024
# Homework #6: Plotting with NumPy

# 1 How many plots?

# 1
def sinGraph(A, x, w):
    return A*np.sin(w*x)

# 2
x = np.linspace(0, 2 * np.pi, 1000)

# 3
# Amplitude
A = np.array([1, 2, 3, 4, 5])
w = np.array([5, 4, 3, 2, 1])

# 4 
def sineFunctions(A, w):
    y = sinGraph(A, x, w)
    plt.plot(x, y)

# 5
plt.figure()
for i in range(5):
    sineFunctions(A[i], w[i])
plt.title("5 Different Sine Functions")
plt.xlabel("x")        
plt.ylabel("y")
plt.legend(loc="upper right")
plt.show()

# 2 Randomness
listOne = []
for i in range(40):
    listOne.append(random.randint(0, 100))
listTwo = []
for i in range(40):
    listTwo.append(random.randint(0, 100))

colorOne = color="orange"
colorTwo = color="red"
lineWidth = linewidth=10
lineStyle = linestyle="dashed"

plt.figure()
plt.plot(range(40), listOne, color="orange", linewidth=10)
plt.plot(range(40), listTwo, color="red", linestyle="dashed") 
plt.title("Random Graphs")
plt.xlabel("x")        
plt.ylabel("y")
plt.legend(loc="upper right")
plt.show()