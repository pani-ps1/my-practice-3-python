Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from ghraphics import *
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    from ghraphics import *
ModuleNotFoundError: No module named 'ghraphics'
>>> from graphics import *
>>> win = GraphWin('emoji')
>>> head = Circle(point(40,100),25)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    head = Circle(point(40,100),25)
NameError: name 'point' is not defined
>>> head = Circle(Point(40,100),25)
>>> head.draw(win)
Circle(Point(40.0, 100.0), 25)
>>> head.setFill('yellow')
>>> eye1 = Circle(Point(30,105),5)
>>> eye1.setFill('blue')
>>> eye1.draw(win)
Circle(Point(30.0, 105.0), 5)
>>> eye2 = Line(Point(45,105), Point(55,105))
>>> eye2.setWidth(3)
>>> eye2.draw(win)
Line(Point(45.0, 105.0), Point(55.0, 105.0))
>>> mouth = oval(Point(30,90),Point(50,85))
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    mouth = oval(Point(30,90),Point(50,85))
NameError: name 'oval' is not defined
>>> mouth = Oval(Point(30,90), Point(50,85))
>>> mouth.setFill('red')
>>> mouth.draw(win)
Oval(Point(30.0, 90.0), Point(50.0, 85.0))
>>> lb = Text(Point(100,120), 'EMOJI')
>>> lb.draw(win)
Text(Point(100.0, 120.0), 'EMOJI')
>>> ms = Text(Point(win.getWidth()/2,20), 'Click to quit')
>>> ms.draw(win)
Text(Point(100.0, 20.0), 'Click to quit')
>>> win.getmouse()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    win.getmouse()
AttributeError: 'GraphWin' object has no attribute 'getmouse'
>>> win.getMouse()
Point(127.0, 95.0)
>>> win.close()
>>> 