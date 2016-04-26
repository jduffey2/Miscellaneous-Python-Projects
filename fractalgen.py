# fractalgen.py
# Author: Jason Duffey
# Date: 12/2015
# Creates a dynamically generated line to look like a mountainous background
import tkinter
import random

top = tkinter.Tk()
canvas = tkinter.Canvas(top, bg='#7ec0ee', height='400',width='1600')
pointList = [(0,200),(1600,200)]

def midPoint(point1, point2):
	x = (point1[0] + point2[0]) / 2
	y = (point1[1] + point2[1]) / 2

	return (x,y)

def midDisplacement(points, reps, rangeReduction):
	cur_range = 200
	for y in range(reps):
		for x in range(len(points) - 1,0,-1):
			mid = midPoint(points[x],points[x - 1])
			adjustment = random.randint(-cur_range,cur_range)
			adjMid = (mid[0], mid[1] + adjustment)
			points.insert(x,adjMid)
		cur_range = round(cur_range * rangeReduction,-1)

def graphPoints(points):
	for x in range(len(points) - 1):
		canvas.create_line(points[x][0],points[x][1],points[x+1][0],points[x+1][1], fill='brown')

midDisplacement(pointList,10,.5)
graphPoints(pointList)

# canvas.create_line(x1,y1,x2,y2,options)

canvas.pack()
top.mainloop()
