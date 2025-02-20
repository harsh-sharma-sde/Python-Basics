# Matplotlib module Python : useful for making plots

# importing matplotlib library
import matplotlib.pyplot as plt

# import numpy to get data for our plots
import numpy as np

x = np.linspace(0,10,100)
y = np.sin(x)
z = np.cos(x)

print(x)
print(y)

# sine wave
plt.plot(x,y)
plt.show()

# cosine wave
plt.plot(x,z)
plt.show()

# adding title, x-axis & y-axis labels
plt.plot(x,y)
plt.xlabel('angle')
plt.ylabel('sine value')
plt.title('sine wave')
plt.show()

# parabola
x = np.linspace(-10,10,20)
y = x**2
plt.plot(x,y)
plt.show()

plt.plot(x, y, 'r+')
plt.show()

plt.plot(x, y, 'g.')
plt.show()

plt.plot(x, y, 'rx')
plt.show()

x = np.linspace(-5,5,50)
plt.plot(x, np.sin(x), 'g-')
plt.plot(x, np.cos(x), 'r--')
plt.show()


#Bar Plot
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
languages = ['English','French','Spanish','Latin','German']
people = [100, 50, 150, 40, 70]
ax.bar(languages, people)
plt.xlabel('LANGUAGES')
plt.ylabel('NUMBER OF PEOPLE')
plt.show()


# Pie chart
fig1 = plt.figure()
ax = fig1.add_axes([0,0,1,1])
languages = ['English','French','Spanish','Latin','German']
people = [100, 50, 150, 40, 70]
ax.pie(people, labels=languages, autopct='%1.1f%%')
plt.show()


# scatter plot
x = np.linspace(0,10,30)
y = np.sin(x)
z = np.cos(x)
fig2 = plt.figure()
ax = fig2.add_axes([0,0,1,1])
ax.scatter(x,y,color='g')
ax.scatter(x,z,color='b')
plt.show()


# 3d scatter plot
fig3 = plt.figure()
ax = plt.axes(projection='3d')
z = 20 * np.random.random(100)
x = np.sin(z)
y = np.cos(z)
ax.scatter(x,y,z,c=z,cmap='Blues')
plt.show()

