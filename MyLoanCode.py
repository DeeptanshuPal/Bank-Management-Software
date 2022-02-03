from tkinter import *

window12 = Tk()
window12.title("Loan Calculator")
window12.geometry('420x420')

#Labels
PLabel12 = Label(window12, text='LOAN AMOUNT          :', font=("ariel", 15, "bold"))
PLabel12.place(x=10,y=5)

RLabel12 = Label(window12, text='INTEREST RATE         :', font=("ariel", 15, "bold"))
RLabel12.place(x=9,y=35)

TLabel4 = Label(window12, text='TERM IN MONTHS      :', font=("ariel", 15, "bold"))
TLabel4.place(x=8,y=65)

#Entry Boxes
loanAmount = IntVar()
loanAmount.set("")
PVal = Entry(window12, font=("ariel", 15, "bold"), width = 16)
PVal.place(x=230,y=5)

loanInterest = IntVar()
loanInterest.set("")
RVal = Entry(window12, font=("ariel", 15, "bold"), width = 16)
RVal.place(x=230,y=35)

loanTerm = IntVar()
loanTerm.set("")
TVal = Entry(window12, font=("ariel", 15, "bold"), width = 16)
TVal.place(x=230,y=65)

##Output
#MonthlyPay Label
paymentLabel = Label(window12, text='Your Monthly Payment is ', font=("ariel", 15, "bold"))
paymentLabel.place(x=10,y=95)
#MPVal Label
Output = StringVar()
Output.set("")
label1 = Label(window12, textvariable=Output, font=("ariel", 15, "bold"))
label1.place(x=255,y=95)

##Buttons
#Calculate Button
def calculate():
    P = PVal.get()
    R = RVal.get()
    T = TVal.get()
    if P.isdigit() and R.isdigit() and T.isdigit():
        if P=='' or R=='' or T=='':
            Invalid_Label = Label(window12,
                                  text="Invalid Input!",
                                  fg="red",
                                  font=("ariel", 15, "bold"))
            Invalid_Label.place(x=135, y=125)
        else:
            p = float(P)
            r = float(R)           #annual interest rate
            mr = (r/100)/12        #monthly interest rate
            t = int(T)
            total = p * (mr/(1-(1+mr) ** (-t)))
            #output
            Output.set("₹" + str(round(total,2)))
            Hide_Invalid_Label = Label(window12,
                                  text="                             ",
                                  font=("ariel", 15, "bold"))
            Hide_Invalid_Label.place(x=135, y=125)
    else:
        Invalid_Label = Label(window12,
                              text="Invalid Input!",
                              fg="red",
                              font=("ariel", 15, "bold"))
        Invalid_Label.place(x=135, y=125)
calculateButton = Button(window12, text="Click to calculate", font=("ariel", 15, "bold"), bg='light grey', command=calculate)
calculateButton.place(x=110,y=155)

#Close Window Button
def closewindow12():
    window12.quit()
closeButton = Button(window12, text="Close", font=("ariel", 15, "bold"), padx=55, bg='light grey', command=closewindow12)
closeButton.place(x=110,y=205)


window12.mainloop()