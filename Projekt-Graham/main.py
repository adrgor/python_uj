import random
from point import Point
import helpFun
from matplotlib import pyplot as plt

points = helpFun.genPoints(0,51,10)
plt.plot([punkt.x for punkt in points], [punkt.y for punkt in points], 'ro')

hull = helpFun.find_hull(points)

plt.fill([punkt.x for punkt in hull], [punkt.y for punkt in hull], fill=False)
plt.show()