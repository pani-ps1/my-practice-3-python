Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> win = Tk()
>>> lb = Lable(win,text = 'hi ladys'),pack()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    lb = Lable(win,text = 'hi ladys'),pack()
NameError: name 'Lable' is not defined
>>> lb1 = Lable(win,text ='hi guys')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    lb1 = Lable(win,text ='hi guys')
NameError: name 'Lable' is not defined
>>> lb1 = lable(win,text ='hi')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    lb1 = lable(win,text ='hi')
NameError: name 'lable' is not defined
>>> lb1.pack
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    lb1.pack
NameError: name 'lb1' is not defined
>>> win = Tk()
>>> win.title('hi')
''
>>> lb = Lable(win,text = 'hi')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    lb = Lable(win,text = 'hi')
NameError: name 'Lable' is not defined
>>> from tkinter import *
>>> win = Tk()
>>> win.title('hi')
''
>>> lb = Label(win,text = 'hi')
>>> 
>>> lb.pack()
>>> lb.config()
{'activebackground': ('activebackground', 'activeBackground', 'Foreground', <string object: 'SystemButtonFace'>, 'SystemButtonFace'), 'activeforeground': ('activeforeground', 'activeForeground', 'Background', <string object: 'SystemButtonText'>, 'SystemButtonText'), 'anchor': ('anchor', 'anchor', 'Anchor', <string object: 'center'>, 'center'), 'background': ('background', 'background', 'Background', <string object: 'SystemButtonFace'>, 'SystemButtonFace'), 'bd': ('bd', '-borderwidth'), 'bg': ('bg', '-background'), 'bitmap': ('bitmap', 'bitmap', 'Bitmap', '', ''), 'borderwidth': ('borderwidth', 'borderWidth', 'BorderWidth', <string object: '2'>, <string object: '2'>), 'compound': ('compound', 'compound', 'Compound', <string object: 'none'>, 'none'), 'cursor': ('cursor', 'cursor', 'Cursor', '', ''), 'disabledforeground': ('disabledforeground', 'disabledForeground', 'DisabledForeground', <string object: 'SystemDisabledText'>, 'SystemDisabledText'), 'fg': ('fg', '-foreground'), 'font': ('font', 'font', 'Font', <string object: 'TkDefaultFont'>, 'TkDefaultFont'), 'foreground': ('foreground', 'foreground', 'Foreground', <string object: 'SystemButtonText'>, 'SystemButtonText'), 'height': ('height', 'height', 'Height', 0, 0), 'highlightbackground': ('highlightbackground', 'highlightBackground', 'HighlightBackground', <string object: 'SystemButtonFace'>, 'SystemButtonFace'), 'highlightcolor': ('highlightcolor', 'highlightColor', 'HighlightColor', <string object: 'SystemWindowFrame'>, 'SystemWindowFrame'), 'highlightthickness': ('highlightthickness', 'highlightThickness', 'HighlightThickness', <string object: '0'>, <string object: '0'>), 'image': ('image', 'image', 'Image', '', ''), 'justify': ('justify', 'justify', 'Justify', <string object: 'center'>, 'center'), 'padx': ('padx', 'padX', 'Pad', <string object: '1'>, <string object: '1'>), 'pady': ('pady', 'padY', 'Pad', <string object: '1'>, <string object: '1'>), 'relief': ('relief', 'relief', 'Relief', <string object: 'flat'>, 'flat'), 'state': ('state', 'state', 'State', <string object: 'normal'>, 'normal'), 'takefocus': ('takefocus', 'takeFocus', 'TakeFocus', '0', '0'), 'text': ('text', 'text', 'Text', '', 'hi'), 'textvariable': ('textvariable', 'textVariable', 'Variable', '', ''), 'underline': ('underline', 'underline', 'Underline', -1, -1), 'width': ('width', 'width', 'Width', 0, 0), 'wraplength': ('wraplength', 'wrapLength', 'WrapLength', <string object: '0'>, <string object: '0'>)}
>>> lb.config(font = 'mitra')
>>> lb.config()
{'activebackground': ('activebackground', 'activeBackground', 'Foreground', 'SystemButtonFace', 'SystemButtonFace'), 'activeforeground': ('activeforeground', 'activeForeground', 'Background', 'SystemButtonText', 'SystemButtonText'), 'anchor': ('anchor', 'anchor', 'Anchor', 'center', 'center'), 'background': ('background', 'background', 'Background', 'SystemButtonFace', 'SystemButtonFace'), 'bd': ('bd', '-borderwidth'), 'bg': ('bg', '-background'), 'bitmap': ('bitmap', 'bitmap', 'Bitmap', '', ''), 'borderwidth': ('borderwidth', 'borderWidth', 'BorderWidth', '2', '2'), 'compound': ('compound', 'compound', 'Compound', 'none', 'none'), 'cursor': ('cursor', 'cursor', 'Cursor', '', ''), 'disabledforeground': ('disabledforeground', 'disabledForeground', 'DisabledForeground', 'SystemDisabledText', 'SystemDisabledText'), 'fg': ('fg', '-foreground'), 'font': ('font', 'font', 'Font', 'TkDefaultFont', 'mitra'), 'foreground': ('foreground', 'foreground', 'Foreground', 'SystemButtonText', 'SystemButtonText'), 'height': ('height', 'height', 'Height', 0, 0), 'highlightbackground': ('highlightbackground', 'highlightBackground', 'HighlightBackground', 'SystemButtonFace', 'SystemButtonFace'), 'highlightcolor': ('highlightcolor', 'highlightColor', 'HighlightColor', 'SystemWindowFrame', 'SystemWindowFrame'), 'highlightthickness': ('highlightthickness', 'highlightThickness', 'HighlightThickness', '0', '0'), 'image': ('image', 'image', 'Image', '', ''), 'justify': ('justify', 'justify', 'Justify', 'center', 'center'), 'padx': ('padx', 'padX', 'Pad', '1', '1'), 'pady': ('pady', 'padY', 'Pad', '1', '1'), 'relief': ('relief', 'relief', 'Relief', 'flat', 'flat'), 'state': ('state', 'state', 'State', 'normal', 'normal'), 'takefocus': ('takefocus', 'takeFocus', 'TakeFocus', '0', '0'), 'text': ('text', 'text', 'Text', '', 'hi'), 'textvariable': ('textvariable', 'textVariable', 'Variable', '', ''), 'underline': ('underline', 'underline', 'Underline', -1, -1), 'width': ('width', 'width', 'Width', 0, 0), 'wraplength': ('wraplength', 'wrapLength', 'WrapLength', '0', '0')}
>>> lb.config(font = mitrea)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    lb.config(font = mitrea)
NameError: name 'mitrea' is not defined
>>> 