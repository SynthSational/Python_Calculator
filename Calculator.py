from tkinter import *
from math import *

cal = Tk()
cal.title("Calculator")
operator=""
text_input=StringVar()

#Function enables button clicks
def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_input.set(operator)
    operator =operator

#Function enables 'C' button to clear display
def btnClearDisplay():
    global operator
    operator=""
    text_input.set("")

#Function enables completion of calculations
def btnEqualsInput():
    global operator
    sumof=str(eval(operator))
    text_input.set(sumof)
    operator=sumof

def btnOppositeInput():
    global operator
    opp =str(eval(operator)*-1)
    text_input.set(opp)
    operator=opp

#Function enables square root calculations
def btnSquareRoot():
    global operator
    sqrt=math.sqrt()
    text_input.set("")
    operator=""
    
def keyKlick(event=None):
    #print('3 is pressed')
    global operator
    operator=operator+str(event.char)
    text_input.set(operator)
    operator =operator
    
def btnEqualsKeyboard(event=None):
    global operator
    sumof=str(eval(operator))
    text_input.set(sumof)
    operator=sumof

 
#Decides size, colour, etc. of display and font
txtdisplay=Entry(cal,font=('arial',20,'bold'),textvariable=text_input,bd=30,
                insertwidth=4,bg="powder blue",justify='right').grid(columnspan=3)
 
#Clear Button
#btnClear=Button(cal,padx=10,bd=8,fg="black",font=('arial',20,'bold'),
               #text="C",bg="Honeydew3",command=btnClearDisplay).grid(row=0,column=3)
btn = []
vats = [7,8,9,4,5,6,1,2,3,0]
positionx = [4,4,4,5,5,5,6,6,6,7]
positiony = [0,1,2,0,1,2,0,1,2,0]
btnClear=Button(cal,padx=10,bd=8,fg="black",font=('arial',20,'bold'),
               text="C",bg="Honeydew3",command=btnClearDisplay).grid(row=0,column=3)

btnEquals=Button(cal,padx=16, bd=8,fg="black",font=('arial',20,'bold'),
               text="=",bg="tomato",command=btnEqualsInput).grid(row=7,column=2)
cal.bind('<Return>',btnEqualsKeyboard)


## Number 0-9
for i in range(0,len(vats)):
    btn.append(Button(cal, text = str(vats[i]),  width = 10, height = 3, font=('arial',10,'bold'),  command=lambda i=i:btnClick(vats[i])).grid(row=positionx[i],column=positiony[i])) 
    cal.bind("<KeyPress-" + str(i) + ">", keyKlick)

    
## Basic maths: +,-,/,*
btnAddition=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
               text="+",bg="Honeydew3",command=lambda:btnClick("+")).grid(row=1,column=0)
cal.bind('<KeyPress-+>',keyKlick)


btnSubtract=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
               text="-",bg="Honeydew3",command=lambda:btnClick("-")).grid(row=1,column=1)
cal.bind('<KeyPress-->',keyKlick)

btnMulti=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
               text="*",bg="Honeydew3",command=lambda:btnClick("*")).grid(row=1,column=2)
cal.bind('<KeyPress-*>',keyKlick)
btnDivision=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
               text="/",bg="Honeydew3",command=lambda:btnClick("/")).grid(row=1,column=3)
cal.bind('<KeyPress-/>',keyKlick)


#Math symbols: ., pi, sqrt, %
btnDot=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
               text=".",bg="Honeydew3",command=lambda:btnClick(".")).grid(row=7,column=1)
cal.bind('<KeyPress-.>',keyKlick)
btnPi=Button(cal,padx=13,bd=8,fg="black",font=('arial',20,'bold'), #Pi button was too big when padx=16
               text="π",bg="Honeydew3",command=lambda:btnClick("3.14159")).grid(row=2,column=3), #Lambda command produces requested symbol/number in display when corresponding button is clicked
 
btnSquareRoot=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
               text="√",bg="Honeydew3",command=lambda:btnClick("sqrt")) .grid(row=2,column=3)
 
btnPercentage=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
               text="%",bg="Honeydew3",command=lambda:btnClick("/100*")).grid(row=4,column=3)

## Parenthesies and positive/negative
btnBrackets=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
               text="(",command=lambda:btnClick("(")).grid(row=2,column=0)
cal.bind('<KeyPress-(>',keyKlick)
btnBrackets=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
               text=")",command=lambda:btnClick(")")).grid(row=2,column=1)
cal.bind('<KeyPress-)>',keyKlick)
btnOpposite=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
               text="+/-",command=btnOppositeInput).grid(row=2,column=2)

#Causes calculator to stay open
cal.mainloop()
