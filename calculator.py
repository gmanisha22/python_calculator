from tkinter import *


############################################################################################################################################################
window = Tk()
window.title("CALCULATOR-gmanisha22")
operator =''
text_Input = StringVar()

def btnclicl(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


def btnequals():
     try:
          global operator
          sumup = str(eval(operator))
          text_Input.set(sumup)
          operator = '' 
     except:
          text_Input.set("Error")
          operator = ''

def btnclears():
    global operator
    operator = ""
    text_Input.set("") 

##########################################################################################################################################################

txtDisplay = Entry(window , font=('arial' , 20 , 'bold') , bg='#000033' , fg='white' ,bd = 7 ,textvar =text_Input , insertwidth = 4, justify = 'right' ) 
txtDisplay. grid(columnspan=4 )
############################################################################################################################################################

button7 = Button(window , padx = 15 ,pady = 15 , font=('arial' , 25 , 'bold') , bg='white' , fg='black',bd = 0 , text = "7" , command = lambda:btnclicl(7))
button7.grid(row = 1 , column=0)

button8 = Button(window , padx = 15 ,pady = 15 , font=('arial' , 25 , 'bold') , bg='white' , fg='black',bd = 0 , text = "8"  ,  command = lambda:btnclicl(8))
button8.grid(row = 1 , column=1)

button9 = Button(window , padx = 15 ,pady = 15 , font=('arial' , 25 , 'bold') , bg='white' , fg='black',bd = 0 , text = "9"  , command = lambda:btnclicl(9))
button9.grid(row = 1 , column=2)

buttonadd = Button(window , padx = 14 ,pady = 13 , font=('arial' , 25 , 'bold') , bg='#993399' , fg='white',bd = 0 , text = "+"  , command = lambda:btnclicl("+"))
buttonadd.grid(row = 1 , column=3)

#############################################################################################################################################################

button4 = Button(window , padx = 15 ,pady = 15 , font=('arial' , 25 , 'bold') , bg='white' , fg='black',bd = 0 , text = "4"  , command = lambda:btnclicl(4))
button4.grid(row = 2 , column=0)

button5 = Button(window , padx = 15 ,pady = 15 , font=('arial' , 25 , 'bold') , bg='white' , fg='black',bd = 0 , text = "5"  , command = lambda:btnclicl(5))
button5.grid(row = 2 , column=1)

button6 = Button(window , padx = 15 ,pady = 15 , font=('arial' , 25 , 'bold') , bg='white' , fg='black',bd = 0 , text = "6" , command = lambda:btnclicl(6) )
button6.grid(row = 2 , column=2)

buttonsub = Button(window , padx = 18 ,pady = 13 , font=('arial' , 25 , 'bold') , bg='#993399' , fg='white',bd = 0 , text = "-" ,command = lambda:btnclicl("-"))
buttonsub.grid(row = 2 , column=3)

#############################################################################################################################################################

button1 = Button(window , padx = 15 ,pady = 15 , font=('arial' , 25 , 'bold') , bg='white' , fg='black',bd = 0 , text = "1" , command = lambda:btnclicl(1))
button1.grid(row = 3 , column=0)

button2 = Button(window , padx = 15 ,pady = 15 , font=('arial' , 25 , 'bold') , bg='white' , fg='black',bd = 0 , text = "2" , command = lambda:btnclicl(2) )
button2.grid(row = 3 , column=1)

button3 = Button(window , padx = 15 ,pady = 15 , font=('arial' , 25 , 'bold') , bg='white' , fg='black',bd = 0 , text = "3" , command = lambda:btnclicl(3))
button3.grid(row = 3 , column=2)

buttonmul = Button(window , padx = 17 ,pady = 12 , font=('arial' , 25 , 'bold') , bg='#993399' , fg='white',bd = 0 , text = "*" , command = lambda:btnclicl("*") )
buttonmul.grid(row = 3 , column=3)

#############################################################################################################################################################

button0 = Button(window , padx = 15 ,pady = 11 , font=('arial' , 25 , 'bold') , bg='#993399' , fg='white',bd = 0 , text = "0" , command = lambda:btnclicl(0) )
button0.grid(row = 4 , column=0)

buttonclr = Button(window , padx = 13 ,pady = 11, font=('arial' , 25 , 'bold') , bg='#993399' , fg='white',bd = 0 , text = "C" , command = lambda:btnclears())
buttonclr.grid(row = 4 , column=1)

buttonequ = Button(window , padx = 14 ,pady = 11 , font=('arial' , 25 , 'bold') , bg='#993399' , fg='white',bd = 0 , text = "=" , command = lambda:btnequals())
buttonequ.grid(row = 4 , column=2)

buttondiv = Button(window , padx = 19 ,pady = 11 , font=('arial' , 25 , 'bold') , bg='#993399' , fg='white',bd = 0 , text = "/" , command = lambda:btnclicl("/") )
buttondiv.grid(row = 4 , column=3)

window.mainloop()