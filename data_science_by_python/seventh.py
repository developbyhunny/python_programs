from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x = [5, 8, 10]
y = [12,16,6]

x2 = [6,9,10]
y2 = [5,6,3]

plt.bar(x, y, align='center')
plt.bar(x2, y2, color='g', align='center')

plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()

