# Calculator by Taehyun Lee
# For unit conversion, click unit button. Converts the number displayed when clicking buttons such
# as Km/Mi, which is km to miles. Shift button would change its order.
# Shift button shows more functions.
# Enjoy

# Import
from tkinter import *
import math
import threading

# Variables
operator = ['round('] # Calculation behind
ans = '0' # Saves last result
text = [''] # What is shown in the interface
Rad = True # Radians or Degrees
Shift = False # Pressed shift or not
Unit = False # Unit mode or normal mode
# Colors
red = '#ff5050'
green = '#00cc00'
lime = '#ccffcc'
cyan = '#009999'
blue = '#99ccff'
purple = '#cc99ff'
orange = '#ff9966'
yellow = '#ffff66'
# Counter
extraBrac = 0 # To add extra bracket for calculations like sin(radians(
nonBrac = 0 # How much non-brackets there are after the first extra bracket
extraBracLoc = [] # Where the extra brackets is located
showResult = False # Is it displaying result (automatically inputs ans when clicking signs)
addMult = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ')', 'e', 'π', 'Ans') # Inputs * when the last text is in this

# Tkinter Setting
cal = Tk()
cal.title('Super Calculator')
cal.configure(background=lime) # Background color = lime
# Displayer
text_Input = StringVar() # Displays text
txtDisplay = Entry(cal, font = ('arial', 20, 'bold'),textvariable = text_Input,
                   bd = 30, insertwidth = 4, bg = 'powder blue',
                   justify = 'right').grid(columnspan = 8)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Functions
# Inputs in the calcualtor
def btnClick(num):
    global operator, ans, text, extraBrac, nonBrac, showResult
    try:
        if nonBrac > 0: # Counts how much non-bracket are there after extra bracket
            nonBrac = nonBrac + 1
        if num in (1, 2, 3, 4, 5, 6, 7, 8, 9, 0): # If clicked number
            if text[-1] in ('Ans', ')', 'π', 'e'): # Inputs * if last text is in this
                operator.append('*')
                text.append('*')
        elif num == '(': # If clicked (
            if text[-1] in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'): # Inputs * if last text is in this
                operator.append('*')
                text.append('*')
        elif num == ')': # If clicked )
            if extraBrac > 0: # If it needs extra bracket, input extra
                operator.append(')')
                extraBrac = extraBrac - 1
                nonBrac = nonBrac + 1
                extraBracLoc.append(nonBrac)
    except:
        pass
    if showResult == True: # When displaying result
        if num not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 0): # When clicked non-number
            operator.append(ans) # Input ans
            text.append('Ans')
            if num == '(': # When clicked (
                operator.append('*') # Input *
                text.append('*')
        showResult = False
    operator.append(str(num)) # Input the clicked button in calculator
    text.append(str(num)) # Input the clicked button in text
    Tinput = ''.join(text)
    text_Input.set(Tinput) # Display the text

# Radians / Degrees mode
def btnClickRadDeg(btn):
    global Rad
    # Change Rad/Deg button
    btn.grid_forget()
    if Rad == True: # When radians mode change to degrees
        Rad = False
        btnRadDeg = Button(cal, padx = 15, pady = 5, width = 1, bd = 8, fg = 'black',
              font = ('arial', 10, 'bold'), text = 'Deg', bg = purple,
              command = lambda:btnClickRadDeg(btnRadDeg))
    else: # When degrees mode change to radians
        Rad = True
        btnRadDeg = Button(cal, padx = 15, pady = 5, width = 1, bd = 8, fg = 'black',
              font = ('arial', 10, 'bold'), text = 'Rad', bg = blue,
              command = lambda:btnClickRadDeg(btnRadDeg))
    btnRadDeg.grid(row=0, column=6) # Place button

# Shift Function (changes buttons or inverts the order of conversion, basically page 2)
def btnClickShift(btn):
    global Shift, btnSin, btnCos, btnTan, btnLog, btnPi, btnOBrac, btnCBrac, btnAbs, btnExp, btnRoot, btnFact
    # Change sin, cos, tan, log, pi buttons
    btn.grid_forget()
    btnSin.grid_forget()
    btnCos.grid_forget()
    btnTan.grid_forget()
    btnLog.grid_forget()
    btnPi.grid_forget()
    if Unit == True: # When unit mode, change the order of conversion
        btnOBrac.grid_forget()
        btnCBrac.grid_forget()
        btnAbs.grid_forget()
        btnExp.grid_forget()
        btnRoot.grid_forget()
        btnFact.grid_forget()
    if Shift == False: # When it was not shift mode
        Shift = True
        btnShift = Button(cal, padx = 15, pady = 5, width = 1, bd = 8, fg = 'black',
              font = ('arial', 10, 'bold'), text = 'Shift', bg = purple,
              command = lambda:btnClickShift(btnShift))
        btnSin = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black', # asinx
              font = ('arial', 20, 'bold'), text = 'asinx', bg = purple,
              command = lambda:btnClickTrig('sinx'))
        btnCos = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black', # acosx
              font = ('arial', 20, 'bold'), text = 'acosx', bg = purple,
              command = lambda:btnClickTrig('cosx'))
        btnTan = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black', # atanx
              font = ('arial', 20, 'bold'), text = 'atanx', bg = purple,
              command = lambda:btnClickTrig('tanx'))
        btnLog = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black', # ln(x)
              font = ('arial', 20, 'bold'), text = 'ln(x)', bg = purple,
              command = lambda:btnClickLog('ln'))
        btnPi = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black', # e
              font = ('arial', 20, 'bold'), text = 'e', bg = purple,
              command = lambda:btnClickIrrat('euler'))
        if Unit == True: # When Unit mode
            btnOBrac = Button(cal, padx = 16, pady = 16, width = 2, bd = 8,
                fg = 'black',font = ('arial', 18, 'bold'), text = 'ft/m', bg = yellow, # ft/m
                command = lambda:btnClickUnit('FtM'))
            btnCBrac = Button(cal, padx = 16, pady = 16, width = 2, bd = 8,
                fg = 'black',font = ('arial', 18, 'bold'), text = 'in/cm', bg = yellow, # in/cm
                command = lambda:btnClickUnit('InCm'))
            btnAbs = Button(cal, padx = 16, pady = 16, width = 2, bd = 8,
                fg = 'black',font = ('arial', 18, 'bold'), text = 'mi/km', bg = yellow, # mi/km
                command = lambda:btnClickUnit('MiKm'))
            btnExp = Button(cal, padx = 16, pady = 16, width = 2, bd = 8,
                fg = 'black',font = ('arial', 18, 'bold'), text = 'lb/kg', bg = yellow, # lb/kg
                command = lambda:btnClickUnit('LbKg'))
            btnRoot = Button(cal, padx = 16, pady = 16, width = 2, bd = 8,
                fg = 'black',font = ('arial', 18, 'bold'), text = 'Gal/L', bg = yellow, # Gal/l
                command = lambda:btnClickUnit('GalL'))
            btnFact = Button(cal, padx = 16, pady = 16, width = 2, bd = 8,
                fg = 'black',font = ('arial', 18, 'bold'), text = 'oz/ml', bg = yellow, # oz/ml
                command = lambda:btnClickUnit('OzMl'))
            btnOBrac.grid(row = 1, column = 5)
            btnCBrac.grid(row = 1, column = 6)
            btnAbs.grid(row = 1, column = 7)
            btnExp.grid(row = 2, column = 5)
            btnRoot.grid(row = 2, column = 6)
            btnFact.grid(row = 2, column = 7)
    else: # When shift mode
        Shift = False
        btnShift = Button(cal, padx = 15, pady = 5, width = 1, bd = 8, fg = 'black',
              font = ('arial', 10, 'bold'), text = 'Shift', bg = blue,
              command = lambda:btnClickShift(btnShift))
        btnSin = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
              font = ('arial', 20, 'bold'), text = 'sinx', bg = blue,
              command = lambda:btnClickTrig('sinx'))
        btnCos = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
              font = ('arial', 20, 'bold'), text = 'cosx', bg = blue,
              command = lambda:btnClickTrig('cosx'))
        btnTan = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
              font = ('arial', 20, 'bold'), text = 'tanx', bg = blue,
              command = lambda:btnClickTrig('tanx'))
        btnLog = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
              font = ('arial', 20, 'bold'), text = 'log(x)', bg = blue,
              command = lambda:btnClickLog('logx'))
        btnPi = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
              font = ('arial', 20, 'bold'), text = 'π', bg = blue,
              command = lambda:btnClickIrrat('pi'))
        if Unit == True: # If Unit mode
            btnOBrac = Button(cal, padx = 16, pady = 16, width = 2, bd = 8,
                fg = 'black',font = ('arial', 18, 'bold'), text = 'm/ft', bg = orange, # m/ft
                command = lambda:btnClickUnit('MFt'))
            btnCBrac = Button(cal, padx = 16, pady = 16, width = 2, bd = 8,
                fg = 'black',font = ('arial', 18, 'bold'), text = 'cm/in', bg = orange, # cm/in
                command = lambda:btnClickUnit('CmIn'))
            btnAbs = Button(cal, padx = 16, pady = 16, width = 2, bd = 8,
                fg = 'black',font = ('arial', 18, 'bold'), text = 'km/mi', bg = orange, # km/mi
                command = lambda:btnClickUnit('KmMi'))
            btnExp = Button(cal, padx = 16, pady = 16, width = 2, bd = 8,
                fg = 'black',font = ('arial', 18, 'bold'), text = 'kg/lb', bg = orange, # kg/lb
                command = lambda:btnClickUnit('KgLb'))
            btnRoot = Button(cal, padx = 16, pady = 16, width = 2, bd = 8,
                fg = 'black',font = ('arial', 18, 'bold'), text = 'L/Gal', bg = orange, # l/gal
                command = lambda:btnClickUnit('LGal'))
            btnFact = Button(cal, padx = 16, pady = 16, width = 2, bd = 8,
                fg = 'black',font = ('arial', 18, 'bold'), text = 'ml/oz', bg = orange, # ml/oz
                command = lambda:btnClickUnit('MlOz'))
            btnOBrac.grid(row = 1, column = 5)
            btnCBrac.grid(row = 1, column = 6)
            btnAbs.grid(row = 1, column = 7)
            btnExp.grid(row = 2, column = 5)
            btnRoot.grid(row = 2, column = 6)
            btnFact.grid(row = 2, column = 7)
    # Place buttons
    btnShift.grid(row=0, column=7)
    btnSin.grid(row=3, column=5)
    btnCos.grid(row=3, column=6)
    btnTan.grid(row=3, column=7)
    btnLog.grid(row = 4, column = 6)
    btnPi.grid(row=4, column=5)

# Unit / Normal mode
def btnClickConvert(btn):
    global Unit, btnCBrac, btnOBrac, btnAbs, btnExp, btnRoot, btnFact
    # Change buttons to unit / normal buttons
    btn.grid_forget()
    btnCBrac.grid_forget()
    btnOBrac.grid_forget()
    btnAbs.grid_forget()
    btnExp.grid_forget()
    btnRoot.grid_forget()
    btnFact.grid_forget()
    if Unit == False: # When it was not unit mode
        btnConvert = Button(cal, padx = 16, pady = 16, width = 2, bd = 8,
            fg = 'black',font = ('arial', 20, 'bold'), text = 'Cal', bg = orange,
            command = lambda:btnClickConvert(btnConvert))
        Unit = True
        if Shift == False: # If shift is not pressed
            btnOBrac = Button(cal, padx = 16, pady = 16, width = 2, bd = 8,
                fg = 'black',font = ('arial', 18, 'bold'), text = 'm/ft', bg = orange, # m/ft
                command = lambda:btnClickUnit('MFt'))
            btnCBrac = Button(cal, padx = 16, pady = 16, width = 2, bd = 8,
                fg = 'black',font = ('arial', 18, 'bold'), text = 'cm/in', bg = orange, # cm/in
                command = lambda:btnClickUnit('CmIn'))
            btnAbs = Button(cal, padx = 16, pady = 16, width = 2, bd = 8,
                fg = 'black',font = ('arial', 18, 'bold'), text = 'km/mi', bg = orange, # km/mi
                command = lambda:btnClickUnit('KmMi'))
            btnExp = Button(cal, padx = 16, pady = 16, width = 2, bd = 8,
                fg = 'black',font = ('arial', 18, 'bold'), text = 'kg/lb', bg = orange, # kg/lb
                command = lambda:btnClickUnit('KgLb'))
            btnRoot = Button(cal, padx = 16, pady = 16, width = 2, bd = 8,
                fg = 'black',font = ('arial', 18, 'bold'), text = 'L/Gal', bg = orange, # l/gal
                command = lambda:btnClickUnit('LGal'))
            btnFact = Button(cal, padx = 16, pady = 16, width = 2, bd = 8,
                fg = 'black',font = ('arial', 18, 'bold'), text = 'ml/oz', bg = orange, # ml/oz
                command = lambda:btnClickUnit('MlOz'))
        else: # If shift is pressed
            btnOBrac = Button(cal, padx = 16, pady = 16, width = 2, bd = 8,
                fg = 'black',font = ('arial', 18, 'bold'), text = 'ft/m', bg = yellow, # ft/m
                command = lambda:btnClickUnit('FtM'))
            btnCBrac = Button(cal, padx = 16, pady = 16, width = 2, bd = 8,
                fg = 'black',font = ('arial', 18, 'bold'), text = 'in/cm', bg = yellow, # in/cm
                command = lambda:btnClickUnit('InCm'))
            btnAbs = Button(cal, padx = 16, pady = 16, width = 2, bd = 8,
                fg = 'black',font = ('arial', 18, 'bold'), text = 'mi/km', bg = yellow, # mi/km
                command = lambda:btnClickUnit('MiKm'))
            btnExp = Button(cal, padx = 16, pady = 16, width = 2, bd = 8,
                fg = 'black',font = ('arial', 18, 'bold'), text = 'lb/kg', bg = yellow, # lb/kg
                command = lambda:btnClickUnit('LbKg'))
            btnRoot = Button(cal, padx = 16, pady = 16, width = 2, bd = 8,
                fg = 'black',font = ('arial', 18, 'bold'), text = 'Gal/L', bg = yellow, # gal/l
                command = lambda:btnClickUnit('GalL'))
            btnFact = Button(cal, padx = 16, pady = 16, width = 2, bd = 8,
                fg = 'black',font = ('arial', 18, 'bold'), text = 'oz/ml', bg = yellow, # oz/ml
                command = lambda:btnClickUnit('OzMl'))
    else: # When it was unit mode, come back
        btnConvert = Button(cal, padx = 16, pady = 16, width = 2, bd = 8,
            fg = 'black',font = ('arial', 20, 'bold'), text = 'Unit', bg = cyan,
            command = lambda:btnClickConvert(btnConvert))
        btnOBrac = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
            font = ('arial', 20, 'bold'), text = '(', bg = cyan,
            command = lambda:btnClick('('))
        btnCBrac = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
            font = ('arial', 20, 'bold'), text = ')', bg = cyan,
            command = lambda:btnClick(')'))
        btnAbs = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
            font = ('arial', 20, 'bold'), text = '|x|', bg = cyan,
            command = lambda:btnClick('abs('))
        btnExp = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
            font = ('arial', 20, 'bold'), text = 'x\u02b8', bg = cyan,
            command = lambda:btnClick('**'))
        btnRoot = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
            font = ('arial', 20, 'bold'), text = '√x', bg = cyan,
            command = lambda:btnClickRoot())
        btnFact = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
            font = ('arial', 20, 'bold'), text = 'x!', bg = cyan,
            command = lambda:btnClickFact())
        Unit = False
    # Place buttons
    btnOBrac.grid(row = 1, column = 5)
    btnCBrac.grid(row = 1, column = 6)
    btnAbs.grid(row = 1, column = 7)
    btnExp.grid(row = 2, column = 5)
    btnRoot.grid(row = 2, column = 6)
    btnFact.grid(row = 2, column = 7)
    btnConvert.grid(row = 4, column = 7)

# Ans
def btnClickAns(num):
    global operator, ans, text, showResult, addMult
    try:
        if text[-1] in addMult: # Input * when last text is in addMult
            operator.append('*')
            text.append('*')
    except:
        pass
    if showResult == True: # Displaying result to false
        showResult = False
    operator.append(str(num)) # Input last result in calculator
    text.append('Ans') # Input ans as text
    Tinput = ''.join(text)
    text_Input.set(Tinput) # Display text

# Root
def btnClickRoot():
    global operator, text, showResult, ans, addMult
    try:
        if text[-1] in addMult: # Input * when last text is in addMult
            operator.append('*')
            text.append('*')
    except:
        pass
    # If displaying result, input ans and *
    if showResult == True:
        operator.append(ans)
        operator.append('*')
        text.append('Ans')
        text.append('*')
        showResult = False
    operator.append('math.sqrt(') # Input sqrt in calculator
    text.append('sqrt(') # input sqrt as text
    Tinput = ''.join(text)
    text_Input.set(Tinput) # Display text

# Factorial
def btnClickFact():
    global operator, text, showResult, ans, addMult
    try:
        if text[-1] in addMult: # Input * when last text is in addMult
            operator.append('*')
            text.append('*')
    except:
        pass
    # If displaying result, input ans and *
    if showResult == True:
        operator.append(ans)
        operator.append('*')
        text.append('Ans')
        text.append('*')
        showResult = False
    operator.append('math.factorial(') # Input factorial in calculator
    text.append('fact(') # Input fact as text
    Tinput = ''.join(text)
    text_Input.set(Tinput) # Display text

# Scientific Notation
def btnClickSciNot():
    global operator, text, showResult, ans, addMult
    try:
        if text[-1] in addMult: # Input * when last text is in add Mult
            operator.append('*10**') # Also input 10^
        else: # If not only input 10^
            operator.append('10**')
    except:
        pass
    # If displaying result, input ans and *
    if showResult == True:
        operator.append(ans)
        operator.append('*10**')
        text.append('Ans')
        showResult = False
    text.append('x10e') # Input x10e as text
    Tinput = ''.join(text)
    text_Input.set(Tinput) # Display text

# Logarithm
def btnClickLog(Ltype):
    global operator, text, showResult, ans, addMult
    try:
        if text[-1] in addMult: # Input * when last text is in addMult
            operator.append('*')
            text.append('*')
    except:
        pass
    # If displaying result, input ans and *
    if showResult == True:
        operator.append(ans)
        operator.append('*')
        text.append('Ans')
        text.append('*')
        showResult = False
    # If clicked log(x) input logx
    if Ltype == 'logx':
        operator.append('math.log10(')
        text.append('log(')
    # If clicked ln(x) input ln
    elif Ltype == 'ln':
        operator.append('math.log(')
        text.append('ln(')
    Tinput = ''.join(text)
    text_Input.set(Tinput) # Display text

# Trignometry
def btnClickTrig(Ttype):
    global operator, text, Rad, extraBrac, showResult, ans, Shift, addMult
    try:
        if text[-1] in addMult: # Input * when last text is in addMult
            operator.append('*')
            text.append('*')
    except:
        pass
    # If displaying result, input ans and *
    if showResult == True:
        operator.append(ans)
        operator.append('*')
        text.append('Ans')
        text.append('*')
        showResult = False
    # Sinx
    if Ttype == 'sinx':
        if Rad == True: # When radians mode
            if Shift == True: # When shift mode
                operator.append('math.asin(') # Input arc sin
                text.append('rasin(') # Radians arc sin
            else: # Not shift mode
                operator.append('math.sin(') # normal sin
                text.append('rsin(') # Radians sin
        else: # When degrees mode
            if Shift == True:
                operator.append('math.degrees(math.asin(')
                text.append('dasin(') # Degrees arc sin
            else:
                operator.append('math.sin(math.radians(')
                text.append('dsin(') # Degrees sin
            extraBrac = extraBrac + 1 # Extra bracket
    # Cosx
    elif Ttype == 'cosx':
        if Rad == True:
            if Shift == True:
                operator.append('math.acos(')
                text.append('racos(') # Radians arc cos
            else:
                operator.append('math.cos(')
                text.append('rcos(') # Radians cos
        else:
            if Shift == True:
                operator.append('math.degrees(math.acos(')
                text.append('dacos(') # Degrees arc cos
            else:
                operator.append('math.cos(math.radians(')
                text.append('dcos(') # Degrees cos
            extraBrac = extraBrac + 1
    # Tan
    elif Ttype == 'tanx':
        if Rad == True:
            if Shift == True:
                operator.append('math.atan(')
                text.append('ratan(') # Radians arc tan
            else:
                operator.append('math.tan(')
                text.append('rtan(') # Radians tan
        else:
            if Shift == True:
                operator.append('math.degrees(math.atan(')
                text.append('datan(') # Degrees arc tan
            else:
                operator.append('math.tan(math.radians(')
                text.append('dtan(') # Degrees tan
            extraBrac = extraBrac + 1
    Tinput = ''.join(text)
    text_Input.set(Tinput) # Display text

# Irrational
def btnClickIrrat(Itype):
    global operator, text, showResult, ans, addMult
    try:
        if text[-1] in addMult: # Input * when last text is in addMult
            operator.append('*')
            text.append('*')
    except:
        pass
    # If displaying result, input ans and *
    if showResult == True:
        operator.append(ans)
        operator.append('*')
        text.append('Ans')
        text.append('*')
        showResult = False
    # Pi
    if Itype == 'pi':
        operator.append('math.pi') # Input pi in calculator
        text.append('π') # Input π as text
    # Euler's number
    elif Itype == 'euler':
        operator.append('math.e') # Input e in calculator
        text.append('e') # Input e as text
    Tinput = ''.join(text)
    text_Input.set(Tinput) # Display text

# Delete function
def btnDelete():
    global operator, text, extraBrac, nonBrac
    # Trig in degrees
    degtrig = ['math.sin(math.radians(', 'math.cos(math.radians(',
               'math.tan(math.radians(', 'math.degrees(math.asin(',
               'math.degrees(math.acos(', 'math.degrees(math.atan(']
    try:
        # If deleting extrabracket
        if nonBrac in extraBracLoc:
            extraBracLoc.pop() # Delete location
            operator.pop() # Delete extra bracket
            nonBrac = nonBrac - 1
            extraBrac = extraBrac + 1 # Give back extra bracket
        # If deleting non-bracket after extra bracket
        elif nonBrac > 1:
            nonBrac = nonBrac - 1 # Number of non-bracket - 1
        # If last value is degrees trig
        if operator[-1] in degtrig:
            extraBrac = extraBrac - 1 # Remove extra bracket
        # When the calculator is not empty
        if operator[-1] != 'round(':
            operator.pop() # Remove the recent value
            text.pop()
            Tinput = ''.join(text)
            text_Input.set(Tinput)
    except:
        pass

# Clear function
def btnClickClear():
    global operator, text, extraBrac, nonBrac, showResult
    # Reset variables
    operator = ['round(']
    text = ['']
    text_Input.set('')
    extraBrac = 0
    nonBrac = 0
    if showResult == True: # Stop displaying results
        showResult = False

# Calculation
def btnClickEquals():
    global operator, ans, text, showResult
    try:
        if operator[-1] == 'round(':# Input ans if there is no ihput
            operator.append(ans)
        # Add closed brackets as many as not closed
        numBrac = 0
        testOp = operator
        calculation = ''.join(testOp)
        for i in calculation: # Check every input
            if i == '(': # Count opened brackets
                numBrac = numBrac + 1
            elif i == ')': # Count closed brackets
                numBrac = numBrac - 1
        for j in range(numBrac): # Input closed brackets
            testOp.append(')')
        testOp.pop()
        testOp.append(', 10)') # Round to 10 decimal
        calculation = ''.join(testOp)
        result = str(eval(calculation)) # Calculate
        text_Input.set(result) # Display result
        ans = result # ans = result
        operator = ['round(']
        text = ['']
        showResult = True # Showing result = True
    # Error
    except:
        timer = threading.Timer(1, textReset) # After 1 second, display text back
        timer.start()
        text_Input.set('ERROR') # Display ERROR

# Unit conversion
def btnClickUnit(unit):
    global operator, ans, text, showResult
    btnClickEquals() # Calcualte first
    ans = float(ans)
    if unit == 'MFt': # m to ft
        result = ans*3.281
    elif unit == 'FtM': # ft to m
        result = ans/3.281
    elif unit == 'CmIn': # cm to in
        result = ans/2.54
    elif unit == 'InCm': # in to cm
        result = ans*2.54
    elif unit == 'KmMi': # km to mi
        result = ans/1.609
    elif unit == 'MiKm': # mi to km
        result = ans*1.609
    elif unit == 'KgLb': # kg to lb
        result = ans*2.205
    elif unit == 'LbKg': # lb to kg
        result = ans/2.205
    elif unit == 'LGal': # l to gal
        result = ans/3.785
    elif unit == 'GalL': # gal to l
        result = ans*3.785
    elif unit == 'MlOz': # ml to oz
        result = ans/29.574
    elif unit == 'OzMl': # oz to ml
        result = ans*29.574
    text_Input.set(str(round(result, 10))) # Display conversion
    ans = str(result) # ans = conversion

# Reset text
def textReset():
    Tinput = ''.join(text)
    text_Input.set(Tinput)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 1st row
# Rad / Deg button
btnRadDeg = Button(cal, padx = 15, pady = 5, width = 1, bd = 8, fg = 'black',
              font = ('arial', 10, 'bold'), text = 'Rad', bg = blue,
              command = lambda:btnClickRadDeg(btnRadDeg))
btnRadDeg.grid(row=0, column=6)

# Shift button
btnShift = Button(cal, padx = 15, pady = 5, width = 1, bd = 8, fg = 'black',
              font = ('arial', 10, 'bold'), text = 'Shift', bg = blue,
              command = lambda:btnClickShift(btnShift))
btnShift.grid(row=0, column=7)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 2nd row
# 7
btn7 = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
              font = ('arial', 20, 'bold'), text = '7', bg = green,
              command = lambda:btnClick(7)).grid(row = 1, column = 0)

# 8
btn8 = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
              font = ('arial', 20, 'bold'), text = '8', bg = green,
              command = lambda:btnClick(8)).grid(row = 1, column = 1)

# 9
btn9 = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
              font = ('arial', 20, 'bold'), text = '9', bg = green,
              command = lambda:btnClick(9)).grid(row = 1, column = 2)

# Delete
btnDel = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
              font = ('arial', 20, 'bold'), text = 'DEL', bg = red,
              command = btnDelete).grid(row = 1, column = 3)

# Clear
btnClear = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
              font = ('arial', 20, 'bold'), text = 'C', bg = red,
              command = btnClickClear).grid(row = 1, column = 4)

# (
btnOBrac = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
              font = ('arial', 20, 'bold'), text = '(', bg = cyan,
              command = lambda:btnClick('('))
btnOBrac.grid(row = 1, column = 5)

# )
btnCBrac = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
              font = ('arial', 20, 'bold'), text = ')', bg = cyan,
              command = lambda:btnClick(')'))
btnCBrac.grid(row = 1, column = 6)

# |x|
btnAbs = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
              font = ('arial', 20, 'bold'), text = '|x|', bg = cyan,
              command = lambda:btnClick('abs('))
btnAbs.grid(row = 1, column = 7)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 3rd row
# 4
btn4 = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
              font = ('arial', 20, 'bold'), text = '4', bg = green,
              command = lambda:btnClick(4)).grid(row = 2, column = 0)

# 5
btn5 = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
              font = ('arial', 20, 'bold'), text = '5', bg = green,
              command = lambda:btnClick(5)).grid(row = 2, column = 1)

# 6
btn6 = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
              font = ('arial', 20, 'bold'), text = '6', bg = green,
              command = lambda:btnClick(6)).grid(row = 2, column = 2)

# X
btnTimes = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
              font = ('arial', 20, 'bold'), text = 'X', bg = cyan,
              command = lambda:btnClick('*')).grid(row = 2, column = 3)

# ÷
btnDivide = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
              font = ('arial', 20, 'bold'), text = '÷', bg = cyan,
              command = lambda:btnClick('/')).grid(row = 2, column = 4)

# x^y
btnExp = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
              font = ('arial', 20, 'bold'), text = 'x\u02b8', bg = cyan,
              command = lambda:btnClick('**'))
btnExp.grid(row = 2, column = 5)

# √x
btnRoot = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
              font = ('arial', 20, 'bold'), text = '√x', bg = cyan,
              command = lambda:btnClickRoot())
btnRoot.grid(row = 2, column = 6)

# x!
btnFact = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
              font = ('arial', 20, 'bold'), text = 'x!', bg = cyan,
              command = lambda:btnClickFact())
btnFact.grid(row = 2, column = 7)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 4th row
# 1
btn1 = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
              font = ('arial', 20, 'bold'), text = '1', bg = green,
              command = lambda:btnClick(1)).grid(row = 3, column = 0)

# 2
btn2 = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
              font = ('arial', 20, 'bold'), text = '2', bg = green,
              command = lambda:btnClick(2)).grid(row = 3, column = 1)

# 3
btn3 = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
              font = ('arial', 20, 'bold'), text = '3', bg = green,
              command = lambda:btnClick(3)).grid(row = 3, column = 2)

# +
btnAdd = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
              font = ('arial', 20, 'bold'), text = '+', bg = cyan,
              command = lambda:btnClick('+')).grid(row = 3, column = 3)

# -
btnSub = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
              font = ('arial', 20, 'bold'), text = '-', bg = cyan,
              command = lambda:btnClick('-')).grid(row = 3, column = 4)

# sinx
btnSin = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
              font = ('arial', 20, 'bold'), text = 'sinx', bg = blue,
              command = lambda:btnClickTrig('sinx'))
btnSin.grid(row=3, column=5)

# cosx
btnCos = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
              font = ('arial', 20, 'bold'), text = 'cosx', bg = blue,
              command = lambda:btnClickTrig('cosx'))
btnCos.grid(row=3, column=6)

# tanx
btnTan = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
              font = ('arial', 20, 'bold'), text = 'tanx', bg = blue,
              command = lambda:btnClickTrig('tanx'))
btnTan.grid(row=3, column=7)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 5th row
# 0
btn0 = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
              font = ('arial', 20, 'bold'), text = '0', bg = green,
              command = lambda:btnClick(0)).grid(row = 4, column = 0)

# .
btnPoint = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
              font = ('arial', 20, 'bold'), text = '.', bg = green,
              command = lambda:btnClick('.')).grid(row = 4, column = 1)

# exp
btnSciNot = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
              font = ('arial', 20, 'bold'), text = 'exp', bg = cyan,
              command = lambda:btnClickSciNot()).grid(row = 4, column = 2)

# ans
btnAns = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
              font = ('arial', 20, 'bold'), text = 'Ans', bg = cyan,
              command = lambda:btnClickAns(ans)).grid(row = 4, column = 3)

# =
btnEquals = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
              font = ('arial', 20, 'bold'), text = '=', bg = red,
              command = btnClickEquals).grid(row = 4, column = 4)

# π
btnPi = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
              font = ('arial', 20, 'bold'), text = 'π', bg = blue,
              command = lambda:btnClickIrrat('pi'))
btnPi.grid(row = 4, column = 5)

# log(x)
btnLog = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
              font = ('arial', 20, 'bold'), text = 'log(x)', bg = blue,
              command = lambda:btnClickLog('logx'))
btnLog.grid(row = 4, column = 6)

# Unit / Cal
btnConvert = Button(cal, padx = 16, pady = 16, width = 2, bd = 8, fg = 'black',
              font = ('arial', 20, 'bold'), text = 'Unit', bg = cyan,
              command = lambda:btnClickConvert(btnConvert))
btnConvert.grid(row = 4, column = 7)

cal.mainloop()
