import matplotlib.pyplot as plt

#made input number for x and y from user input
print("Put Number For Graph 1")
input_x1 = int(input('Input 4 number for x1 axis '))
input_x2 = int(input('Input 4 number for x1 axis ')) 
input_x3 = int(input('Input 4 number for x1 axis '))
input_x4 = int(input('Input 4 number for x1 axis '))
input_y1 = int(input('Input 4 number for y1 axis '))
input_y2 = int(input('Input 4 number for y1 axis '))
input_y3 = int(input('Input 4 number for y1 axis '))
input_y4 = int(input('Input 4 number for y1 axis '))

x1 = []
y1 = []

#add number to list
x1.append(input_x1)
x1.append(input_x2)
x1.append(input_x3)
x1.append(input_x4)
y1.append(input_y1)
y1.append(input_y2)
y1.append(input_y3)
y1.append(input_y4)

tick_label = ['one', 'two', 'three', 'four']

plt.bar(x1, y1, tick_label = tick_label, width=0.8, color=['blue', 'orange'])

#plt.plot(x1,y1, color='green', linestyle='dashed', linewidth=3, marker='o', markerfacecolor='blue', markersize=12, label = 'Line 1')

#plt.ylim(1,8)
#plt.xlim(1,8)

print("Put Number For Graph 2")
input_x1 = int(input('Input 4 number for x2 axis '))
input_x2 = int(input('Input 4 number for x2 axis ')) 
input_x3 = int(input('Input 4 number for x2 axis '))
input_x4 = int(input('Input 4 number for x2 axis '))
input_y1 = int(input('Input 4 number for y2 axis '))
input_y2 = int(input('Input 4 number for y2 axis '))
input_y3 = int(input('Input 4 number for y2 axis '))
input_y4 = int(input('Input 4 number for y2 axis '))

x2 = []
y2 = []

x2.append(input_x1)
x2.append(input_x2)
x2.append(input_x3)
x2.append(input_x4)
y2.append(input_y1)
y2.append(input_y2)
y2.append(input_y3)
y2.append(input_y4)


plt.plot(x2,y2, label = 'Line 2')

plt.xlabel('X Axis')

plt.ylabel('Y Axis')

plt.title('Demo Graph - Bar Chart')

plt.legend()


plt.show()
