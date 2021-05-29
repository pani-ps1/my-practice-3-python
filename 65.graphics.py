Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from graphics import *
>>> win = GraphWin('test',300,300)
>>> c1 = circle(point(80,80),30)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    c1 = circle(point(80,80),30)
NameError: name 'circle' is not defined
>>> c1 = Circle(point(80,80),30)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    c1 = Circle(point(80,80),30)
NameError: name 'point' is not defined
>>> c1 = Circle(Point(80,80),30)
>>> c1.draw(win)
Circle(Point(80.0, 80.0), 30)
>>> c1.setFill('red')
>>> c1.setFill('yellow')
>>> c1.setFill('green')
>>> c1.setFill('light green')
>>> c1.setFill('light pink')
>>> c1.setOutline('yellow')
>>> c2 = c1.clone()
>>> c2.move(30,0)
>>> c2.draw(win)
Circle(Point(110.0, 80.0), 30)
>>> c2.setFill('pink')
>>> from time import sleep
>>> for i in range(15):
	c2.move(2,3)
	sleep(0.5)

	
>>> 