from tkinter import *

import mysql.connector as sqltor

con = sqltor.connect(host="localhost", user="root", passwd="R3d23@lnut", database="bank")
if con.is_connected():
    print("Connection Successful...")

def Window1_Function():
    ### (Window1)Welcome window
    window1 = Tk()
    window1.geometry("445x440")
    window1.title("Welcome Page")
    # empty label in window1
    label1 = Label(window1,
                   text="            ",
                   font=("ariel", 30),
                   pady=50)
    label1.grid(row=0, column=0)
    label2 = Label(window1,
                   text="            ",
                   font=("ariel", 15))
    label2.grid(row=2, column=1)
    # window1 icon and image
    icon = PhotoImage(file="Window_Thumbnail.png")
    logo = PhotoImage(file="Bank-Logo.png")
    window1.iconphoto(True, icon)
    bank_img = Label(window1, image=logo, padx=50)
    bank_img.place(x=5, y=15)
    bank_name = Label(window1, text="OLA Bank", font=("Arial Black", 45, 'italic'), fg="#e91c27")
    bank_name.place(x=100, y=10)
    bank_motto = Label(window1, text="We Understand Your World.", font=("Bahnschrift SemiLight", 15, 'italic', 'bold'),
                       fg="gray")
    bank_motto.place(x=108, y=80)

    # Window1 Button Functions
    ## (Window2)Create Account window
    def Window2_Function():
        window2 = Tk()
        window2.title("Create Account")
        window2.geometry("420x420")
        window1.destroy()

        # Name label
        name2 = Label(window2,
                      text=" NAME           :",
                      font=("ariel", 15, "bold"))
        name2.grid(row=0, column=0, sticky='w')
        # Name textbox
        name_box2 = Entry(window2,
                          font=("ariel", 15),
                          width=24)
        name_box2.grid(row=0, column=1)
        # username label
        uname2 = Label(window2,
                       text=" USERNAME  :",
                       font=("ariel", 15, "bold"))
        uname2.grid(row=1, column=0, sticky='w')
        # username textbox
        uname_box2 = Entry(window2,
                           font=("ariel", 15),
                           width=24)
        uname_box2.grid(row=1, column=1, sticky='w')
        # PASSWORD label
        passwd2 = Label(window2,
                        text=" PASSWORD :",
                        font=("ariel", 15, "bold"))
        passwd2.grid(row=2, column=0, sticky='w')
        # PASSWORD textbox
        passwd_box2 = Entry(window2,
                            show=str('*'),
                            font=("ariel", 15),
                            width=24)
        passwd_box2.grid(row=2, column=1)
        # Deposit label
        deposit2 = Label(window2,
                         text=" DEPOSIT      :",
                         font=("ariel", 15, "bold"))
        deposit2.grid(row=3, column=0, sticky='w')
        # Deposit textbox
        deposit_box2 = Entry(window2,
                             font=("ariel", 15),
                             width=24)
        deposit_box2.grid(row=3, column=1)

        # submit button
        def CreateAccSubmit():
            n2 = name_box2.get()
            u2 = uname_box2.get()
            p2 = passwd_box2.get()
            b2 = deposit_box2.get()
            cursor = con.cursor()
            q = "select username from bdetails"
            cursor.execute(q)
            data = cursor.fetchall()
            datalst = [item for t in data for item in t]
            if n2.isalnum() and u2.isalnum() and p2.isalnum() and b2.isdigit():
                if u2 not in datalst:
                    if int(b2) >= 1000:
                        q = "INSERT INTO bdetails(NAME, USERNAME,PASSWD,BALANCE)values('{}','{}','{}',{})".format(n2,u2,p2,b2)
                        cursor2 = con.cursor()
                        cursor2.execute(q)
                        con.commit()
                        window2.destroy()
                        Window1_Function()
                    else:
                        Invalid_Label = Label(window2,
                                              text="Minimum deposit ₹1000!",
                                              fg="red",
                                              font=("ariel", 15, "bold"))
                        Invalid_Label.place(x=10, y=220)
                else:
                    Invalid_Label = Label(window2,
                                          text="Username already exists!",
                                          fg="red",
                                          font=("ariel", 15, "bold"))
                    Invalid_Label.place(x=10, y=220)

            else:
                Invalid_Label = Label(window2,
                                      text="Invalid Values!                               ",
                                      fg="red",
                                      font=("ariel", 15, "bold"))
                Invalid_Label.place(x=10, y=220)

        submit2 = Button(window2,
                         text="SUBMIT",
                         font=("ariel", 15, "bold"),
                         bg="light grey",
                         padx=10,
                         command=CreateAccSubmit)
        submit2.place(x=150, y=140)

    ## (Window3)LogIn window
    def Window3_Function():
        window3 = Tk()
        window3.title("Log In")
        window3.geometry("420x420")
        window1.destroy()

        # username label
        uname3 = Label(window3,
                       text=" USERNAME  :",
                       font=("ariel", 15, "bold"))
        uname3.grid(row=0, column=0)
        # username textbox
        uname_box3 = Entry(window3,
                           font=("ariel", 15),
                           width=24)
        uname_box3.grid(row=0, column=1)
        # Passwd label
        passwd3 = Label(window3,
                        text=" PASSWORD :",
                        font=("ariel", 15, "bold"))
        passwd3.grid(row=1, column=0)
        # Passwd textbox
        passwd_box3 = Entry(window3,
                            show=str('*'),
                            font=("ariel", 15),
                            width=24)
        passwd_box3.grid(row=1, column=1)

        ### submit button
        ##(Window4) Bank Details Window
        def Window4_Function():
            window4 = Tk()
            window4.geometry("420x420")
            window4.title("Bank Details")
            U3 = uname_box3.get()  # used in window4

            window3.destroy()  ### this should not be here
            # Window4 widgets
            # Name label
            name4 = Label(window4,
                          text=" NAME                        :",
                          font=("ariel", 15, "bold"))
            name4.grid(row=0, column=0, sticky='w')
            # username label
            uname4 = Label(window4,
                           text=" USERNAME               :",
                           font=("ariel", 15, "bold"))
            uname4.grid(row=1, column=0, sticky='w')
            # PASSWORD label
            passwd4 = Label(window4,
                            text=" PASSWORD              :",
                            font=("ariel", 15, "bold"))
            passwd4.grid(row=2, column=0, sticky='w')
            # Balance label
            balance4 = Label(window4,
                             text=" ACCOUNT BALANCE :",
                             font=("ariel", 15, "bold"))
            balance4.grid(row=3, column=0, sticky='w')

            # Labels to Display values from SQL
            cursor = con.cursor()
            q = "select NAME,USERNAME,PASSWD,BALANCE from bdetails where USERNAME = '{}'".format(U3)
            cursor.execute(q)
            data = cursor.fetchall()
            for i in data:
                a, b, c, d = i[0], i[1], i[2], i[3]
                # NameValue label
                var1 = StringVar()
                NameVal4 = Label(window4,
                                 textvariable=var1,
                                 font=("ariel", 15, "bold"))
                var1.set(a)
                NameVal4.grid(row=0, column=1, sticky='w')
                # UsernameValue label
                var2 = StringVar()
                UsernameVal4 = Label(window4,
                                     textvariable=var2,
                                     font=("ariel", 15, "bold"))
                var2.set(b)
                UsernameVal4.grid(row=1, column=1, sticky='w')
                # PasswordValue label
                var3 = StringVar()
                PasswdVal4 = Label(window4,
                                   textvariable=var3,
                                   font=("ariel", 15, "bold"))
                var3.set(c)
                PasswdVal4.grid(row=2, column=1, sticky='w')
                # BalanceValue label
                var4 = StringVar()
                PasswdVal4 = Label(window4,
                                   textvariable=var4,
                                   font=("ariel", 15, "bold"))
                var4.set(d)
                PasswdVal4.grid(row=3, column=1, sticky='w')
            print(b)
            print(var2)

            ###Take Loan Button
            ##button func--------
            # (Window5) Loan Choices Window
            def Window5_Function():
                window5 = Tk()
                window5.geometry("420x420")
                window5.title("Loan Choices")

                ### (Window6)Home Loan Window
                def Window6_Function():
                    window6 = Tk()
                    window6.geometry("420x420")
                    window6.title("Home Loan")
                    # h_principal label
                    h_principal6 = Label(window6,
                                         text=" Loan Taken : ",
                                         font=("ariel", 15, "bold"))
                    h_principal6.grid(row=1, column=0, sticky='w')
                    # h_principal display label
                    h_principal_box6 = Entry(window6,
                                             font=("ariel", 15),
                                             width=24)
                    h_principal_box6.grid(row=1, column=1, sticky='w')
                    # h_rate label
                    h_rate6 = Label(window6,
                                    text=" Rate            : ",
                                    font=("ariel", 15, "bold"))
                    h_rate6.grid(row=2, column=0, sticky='w')
                    # h_rate display label
                    h_rate_box6 = Label(window6,
                                        text=" 7%",
                                        font=("ariel", 15, "bold"))
                    h_rate_box6.grid(row=2, column=1, sticky='w')
                    # h_time label
                    h_time6 = Label(window6,
                                    text=" Time           : ",
                                    font=("ariel", 15, "bold"))
                    h_time6.grid(row=3, column=0, sticky='w')
                    # h_time display label
                    h_time_box6 = Entry(window6,
                                        font=("ariel", 15),
                                        width=24)
                    h_time_box6.grid(row=3, column=1, sticky='w')
                    window5.destroy()

                    # submit button
                    def SubmitLoanFunc():
                        p6 = h_principal_box6.get()
                        r6 = 7
                        global t6
                        t6 = h_time_box6.get()
                        if p6.isdigit() and t6.isdigit():
                            if p6 == '' or r6 == '' or t6 == '':
                                Invalid_Label = Label(window6,
                                                      text="Invalid Input!                          ",
                                                      fg="red",
                                                      font=("ariel", 15, "bold"))
                                Invalid_Label.place(x=10, y=220)
                            elif int(t6) > 15:
                                MaxTime_Label = Label(window6,
                                                      text="Max time is 15 years!",
                                                      fg="red",
                                                      font=("ariel", 15, "bold"))
                                MaxTime_Label.place(x=10, y=220)
                            elif int(p6) > 5 * int(d):
                                MaxHLoan_Label = Label(window6,
                                                       text="Loan Criteria not met!",
                                                       fg="red",
                                                       font=("ariel", 15, "bold"))
                                MaxHLoan_Label.place(x=10, y=220)
                                MaxHLoan_Label2 = Label(window6,
                                                        text="*Maximum loan allowance is 5x account balance.",
                                                        fg="black",
                                                        font=("ariel", 10, "bold"))
                                MaxHLoan_Label2.place(x=10, y=250)

                            else:
                                q = "UPDATE bdetails SET h_principal={},h_rate={},h_time={},h_date=curdate() where USERNAME='{}'".format(
                                    p6, r6, t6, U3)
                                cursor6 = con.cursor()
                                cursor6.execute(q)
                                con.commit()
                                window6.destroy()
                                Window1_Function()
                        else:
                            Invalid_Label = Label(window6,
                                                  text="Invalid Input!                             ",
                                                  fg="red",
                                                  font=("ariel", 15, "bold"))
                            Invalid_Label.place(x=10, y=220)

                    submit6 = Button(window6,
                                     text="SUBMIT",
                                     font=("ariel", 15, "bold"),
                                     bg="light grey",
                                     padx=10,
                                     command=SubmitLoanFunc)
                    submit6.place(x=150, y=130)

                ### (Window7)Car Loan Window
                def Window7_Function():
                    window7 = Tk()
                    window7.geometry("420x420")
                    window7.title("Car Loan")
                    # c_principal label
                    c_principal7 = Label(window7,
                                         text=" Loan Taken : ",
                                         font=("ariel", 15, "bold"))
                    c_principal7.grid(row=1, column=0, sticky='w')
                    # c_principal display label
                    c_principal_box7 = Entry(window7,
                                             font=("ariel", 15),
                                             width=24)
                    c_principal_box7.grid(row=1, column=1, sticky='w')
                    # c_rate label
                    c_rate7 = Label(window7,
                                    text=" Rate            : ",
                                    font=("ariel", 15, "bold"))
                    c_rate7.grid(row=2, column=0, sticky='w')
                    # c_rate display label
                    c_rate_box7 = Label(window7,
                                        text=" 6%",
                                        font=("ariel", 15, "bold"))
                    c_rate_box7.grid(row=2, column=1, sticky='w')
                    # c_time label
                    c_time7 = Label(window7,
                                    text=" Time           : ",
                                    font=("ariel", 15, "bold"))
                    c_time7.grid(row=3, column=0, sticky='w')
                    # c_time display label
                    c_time_box7 = Entry(window7,
                                        font=("ariel", 15),
                                        width=24)
                    c_time_box7.grid(row=3, column=1, sticky='w')
                    window5.destroy()

                    # submit button
                    def SubmitLoanFunc():
                        p7 = c_principal_box7.get()
                        r7 = 6
                        t7 = c_time_box7.get()
                        if p7.isdigit() and t7.isdigit():
                            if p7 == '' or r7 == '' or t7 == '':
                                Invalid_Label = Label(window7,
                                                      text="Invalid Input!                       ",
                                                      fg="red",
                                                      font=("ariel", 15, "bold"))
                                Invalid_Label.place(x=10, y=220)
                            elif int(t7) > 10:
                                MaxTime_Label = Label(window7,
                                                      text="Max time is 10 years!",
                                                      fg="red",
                                                      font=("ariel", 15, "bold"))
                                MaxTime_Label.place(x=10, y=220)
                            elif int(p7) > 5 * int(d):
                                MaxHLoan_Label = Label(window7,
                                                       text="Loan Criteria not met!",
                                                       fg="red",
                                                       font=("ariel", 15, "bold"))
                                MaxHLoan_Label.place(x=10, y=220)
                                MaxHLoan_Label2 = Label(window7,
                                                        text="*Maximum loan allowance is 5x account balance.",
                                                        fg="black",
                                                        font=("ariel", 10, "bold"))
                                MaxHLoan_Label2.place(x=10, y=250)
                            else:
                                q = "UPDATE bdetails SET c_principal={},c_rate={},c_time={},c_date=curdate() where USERNAME='{}'".format(
                                    p7, r7, t7, U3)
                                cursor6 = con.cursor()
                                cursor6.execute(q)
                                con.commit()
                                window7.destroy()
                                Window1_Function()
                        else:
                            Invalid_Label = Label(window7,
                                                  text="Invalid Input!                      ",
                                                  fg="red",
                                                  font=("ariel", 15, "bold"))
                            Invalid_Label.place(x=10, y=220)

                    submit7 = Button(window7,
                                     text="SUBMIT",
                                     font=("ariel", 15, "bold"),
                                     bg="light grey",
                                     padx=10,
                                     command=SubmitLoanFunc)
                    submit7.place(x=150, y=130)

                ### (Window8)Personal Loan Window
                def Window8_Function():
                    window8 = Tk()
                    window8.geometry("420x420")
                    window8.title("Personal Loan")
                    # p_principal label
                    p_principal8 = Label(window8,
                                         text=" Loan Taken : ",
                                         font=("ariel", 15, "bold"))
                    p_principal8.grid(row=1, column=0, sticky='w')
                    # p_principal display label
                    p_principal_box8 = Entry(window8,
                                             font=("ariel", 15),
                                             width=24)
                    p_principal_box8.grid(row=1, column=1, sticky='w')
                    # p_rate label
                    p_rate8 = Label(window8,
                                    text=" Rate            : ",
                                    font=("ariel", 15, "bold"))
                    p_rate8.grid(row=2, column=0, sticky='w')
                    # p_rate display label
                    p_rate_box8 = Label(window8,
                                        text=" 5%",
                                        font=("ariel", 15, "bold"))
                    p_rate_box8.grid(row=2, column=1, sticky='w')
                    # p_time label
                    p_time8 = Label(window8,
                                    text=" Time           : ",
                                    font=("ariel", 15, "bold"))
                    p_time8.grid(row=3, column=0, sticky='w')
                    # p_time display label
                    p_time_box8 = Entry(window8,
                                        font=("ariel", 15),
                                        width=24)
                    p_time_box8.grid(row=3, column=1, sticky='w')
                    window5.destroy()

                    # submit button
                    def SubmitLoanFunc():
                        p8 = p_principal_box8.get()
                        r8 = 5
                        t8 = p_time_box8.get()
                        if p8.isdigit() and t8.isdigit():
                            if p8 == '' or r8 == '' or t8 == '':
                                Invalid_Label = Label(window8,
                                                      text="Invalid Input!                   ",
                                                      fg="red",
                                                      font=("ariel", 15, "bold"))
                                Invalid_Label.place(x=10, y=220)
                            elif int(t8) > 8:
                                MaxTime_Label = Label(window8,
                                                      text="Max time is 8 years!",
                                                      fg="red",
                                                      font=("ariel", 15, "bold"))
                                MaxTime_Label.place(x=10, y=220)
                            elif int(p8) > 5 * int(d):
                                MaxHLoan_Label = Label(window8,
                                                       text="Loan Criteria not met!",
                                                       fg="red",
                                                       font=("ariel", 15, "bold"))
                                MaxHLoan_Label.place(x=10, y=220)
                                MaxHLoan_Label2 = Label(window8,
                                                        text="*Maximum loan allowance is 5x account balance.",
                                                        fg="black",
                                                        font=("ariel", 10, "bold"))
                                MaxHLoan_Label2.place(x=10, y=250)
                            else:
                                q = "UPDATE bdetails SET p_principal={},p_rate={},p_time={},p_date=curdate() where USERNAME='{}'".format(
                                    p8, r8, t8, U3)
                                cursor6 = con.cursor()
                                cursor6.execute(q)
                                con.commit()
                                window8.destroy()
                                Window1_Function()
                        else:
                            Invalid_Label = Label(window8,
                                                  text="Invalid Input!                           ",
                                                  fg="red",
                                                  font=("ariel", 15, "bold"))
                            Invalid_Label.place(x=10, y=220)

                    submit8 = Button(window8,
                                     text="SUBMIT",
                                     font=("ariel", 15, "bold"),
                                     bg="light grey",
                                     padx=10,
                                     command=SubmitLoanFunc)
                    submit8.place(x=150, y=130)

                ##Home Loan Button
                HomeLoanButton = Button(window5,
                                        text="HOME LOAN",
                                        font=("Arial", 12, "bold"),
                                        bg="light grey",
                                        padx=30,
                                        command=Window6_Function)
                HomeLoanButton.place(x=120, y=80)
                ##Car Loan Button
                CarLoanButton = Button(window5,
                                       text="CAR LOAN",
                                       font=("Arial", 12, "bold"),
                                       bg="light grey",
                                       padx=36,
                                       command=Window7_Function)
                CarLoanButton.place(x=120, y=150)
                ##Personal Loan Button
                PersonalLoanButton = Button(window5,
                                            text="PERSONAL LOAN",
                                            font=("Arial", 12, "bold"),
                                            bg="light grey",
                                            padx=10,
                                            command=Window8_Function)
                PersonalLoanButton.place(x=120, y=220)

                window4.destroy()

            # Button Code
            TakeLoanButton = Button(window4,
                                    text="TAKE LOANS",
                                    font=("Arial", 12, "bold"),
                                    bg="light grey",
                                    padx=35,
                                    command=Window5_Function)
            TakeLoanButton.place(x=115, y=220)

            # Log out & Go Back to Home Screen Button
            def LogOutFunc():
                window4.destroy()
                Window1_Function()

            LogOutButton = Button(window4,
                                  text="LOG OUT",
                                  font=("Arial", 12, "bold"),
                                  bg="light grey",
                                  padx=50,
                                  command=LogOutFunc)
            LogOutButton.place(x=115, y=370)

            ### (Window9)Deposit Balance Window
            def Window9_Function():
                window9 = Tk()
                window9.geometry("423x423")
                window9.title("Deposit Balance")
                window4.destroy()
                # Deposit Amount label
                Deposit_Amt = Label(window9,
                                    text=" Deposit Amount : ",
                                    font=("ariel", 15, "bold"))
                Deposit_Amt.grid(row=0, column=0, sticky='w')
                # Deposit amt display label
                DepositAmt_box9 = Entry(window9,
                                        font=("ariel", 15),
                                        width=21)
                DepositAmt_box9.grid(row=0, column=1, sticky='w')

                # submit button
                def DepositFunc():
                    d9 = str(DepositAmt_box9.get())
                    if d9.isdigit() and int(d9) > 0 and int(d9) < 100000:
                        q = "update bdetails set balance=balance+'{}' where username = '{}'".format(d9, U3)
                        cursor9 = con.cursor()
                        cursor9.execute(q)
                        con.commit()
                        window9.destroy()
                        Window1_Function()
                    elif int(d9) > 100000:
                        Limit_Label = Label(window9,
                                            text="Max deposit ₹100000!",
                                            fg="red",
                                            font=("ariel", 15, "bold"))
                        Limit_Label.place(x=10, y=220)


                    else:
                        Invalid_Label = Label(window9,
                                              text="Invalid Input!                   ",
                                              fg="red",
                                              font=("ariel", 15, "bold"))
                        Invalid_Label.place(x=10, y=220)

                submit9 = Button(window9,
                                 text="DEPOSIT & EXIT",
                                 font=("ariel", 15, "bold"),
                                 bg="light grey",
                                 padx=10,
                                 command=DepositFunc)
                submit9.place(x=110, y=70)

            # Button Code
            DepositAmtButton = Button(window4,
                                      text="DEPOSIT MONEY",
                                      font=("Arial", 12, "bold"),
                                      bg="light grey",
                                      padx=20,
                                      command=Window9_Function)
            DepositAmtButton.place(x=115, y=270)

            ### (Window10)Withdraw Balance Window
            def Window10_Function():
                window10 = Tk()
                window10.geometry("420x420")
                window10.title("Withdraw Balance")
                window4.destroy()
                # Withdraw Amount label
                Withdraw_Amt = Label(window10,
                                     text=" Withdraw Amount : ",
                                     font=("ariel", 15, "bold"))
                Withdraw_Amt.grid(row=1, column=0, sticky='w')
                # Withdraw amt display label
                WithdrawAmt_box10 = Entry(window10,
                                          font=("ariel", 15),
                                          width=19)
                WithdrawAmt_box10.grid(row=1, column=1, sticky='w')

                # submit button
                def WithdrawFunc():
                    w10 = str(WithdrawAmt_box10.get())
                    if w10.isdigit() and int(w10) > 0:
                        m = "select balance from bdetails where username='{}'".format(U3)
                        cursor11 = con.cursor()
                        cursor11.execute(m)
                        data10 = cursor11.fetchall()
                        print(data10)
                        if int(w10) > data10[0][0]:
                            Invalid_Label = Label(window10,
                                                  text="Insufficient balance!             ",
                                                  fg="red",
                                                  font=("ariel", 15, "bold"))
                            Invalid_Label.place(x=10, y=120)

                        else:
                            q = "update bdetails set balance=balance-{} where username='{}' and balance >= '{}'".format(
                                w10, U3, w10)
                            cursor10 = con.cursor()
                            cursor10.execute(q)
                            con.commit()
                            window10.destroy()
                            Window1_Function()

                    else:

                        Invalid_Label = Label(window10,
                                              text="Invalid Input!",
                                              fg="red",
                                              font=("ariel", 15, "bold"))
                        Invalid_Label.place(x=10, y=120)

                submit10 = Button(window10,
                                  text="WITHDRAW & EXIT",
                                  font=("ariel", 15, "bold"),
                                  bg="light grey",
                                  padx=10,
                                  command=WithdrawFunc)
                submit10.place(x=102, y=70)

            # Button Code
            WithdrawAmtButton = Button(window4,
                                       text="WITHDRAW MONEY",
                                       font=("Arial", 12, "bold"),
                                       bg="light grey",
                                       padx=10,
                                       command=Window10_Function)
            WithdrawAmtButton.place(x=115, y=320)

            ##(Window11)Loan Details Window
            def Window11_Function():
                window11 = Tk()
                window11.geometry("423x423")
                window11.title("Loan Details")
                window4.destroy()
                # h_principal label
                H_LoanTakenLabel11 = Label(window11,
                                           text=" HOME LOAN             : ",
                                           font=("ariel", 15, "bold"))
                H_LoanTakenLabel11.grid(row=0, column=0, sticky='w')
                # c_principal label
                C_LoanTakenLabel11 = Label(window11,
                                           text=" CAR LOAN                : ",
                                           font=("ariel", 15, "bold"))
                C_LoanTakenLabel11.grid(row=1, column=0, sticky='w')
                # p_principal label
                P_LoanTakenLabel11 = Label(window11,
                                           text=" PERSONAL LOAN     : ",
                                           font=("ariel", 15, "bold"))
                P_LoanTakenLabel11.grid(row=2, column=0, sticky='w')

                # Labels to Display values from SQL
                cursor = con.cursor()

                def HomeLoanDetails():
                    window12 = Tk()
                    window12.title("Home Loan Details")
                    window12.geometry('420x420')
                    window11.destroy()

                    # Labels
                    PLabel12 = Label(window12, text='LOAN TAKEN         :₹', font=("ariel", 15, "bold"))
                    PLabel12.place(x=10, y=5)

                    RLabel12 = Label(window12, text='INTEREST RATE         :', font=("ariel", 15, "bold"))
                    RLabel12.place(x=9, y=35)

                    TLabel2 = Label(window12, text='TIME IN YEAR              :', font=("ariel", 15, "bold"))
                    TLabel2.place(x=8, y=65)

                    SdLabel12 = Label(window12, text='START DATE                :', font=("ariel", 15, "bold"))
                    SdLabel12.place(x=9, y=95)

                    SdLabel12 = Label(window12, text='END DATE                  :', font=("ariel", 15, "bold"))
                    SdLabel12.place(x=9, y=125)

                    #GETTING VALUES FROM SQL
                    q1="select h_time from bdetails"
                    cursor.execute(q1)
                    data1=cursor.fetchall()
                    for i in data1:
                        Ht=i[0]

                    q2="select H_principal,H_rate,H_time,h_date,date_add(h_date,interval '{}' year) from bdetails where username='{}'".format(Ht,U3)
                    cursor.execute(q2)
                    data2=cursor.fetchall()
                    for i in data2:
                        p,r,t,sd,ed=i[0],i[1],i[2],i[3],i[4]
                    print(p,r,t,sd,ed)

                    # Labels
                    PvalLabel12 = Label(window12, text=str(p),font=("ariel", 15, "bold"))
                    PvalLabel12.place(x=250, y=5)

                    RvalLabel12 = Label(window12, text=str(r), font=("ariel", 15, "bold"))
                    RvalLabel12.place(x=250, y=35)

                    TvalLabel12 = Label(window12, text=str(t), font=("ariel", 15, "bold"))
                    TvalLabel12.place(x=250, y=65)

                    SDvalLabel12 = Label(window12, text=str(sd), font=("ariel", 15, "bold"))
                    SDvalLabel12.place(x=250, y=95)

                    EDvalLabel12 = Label(window12, text=str(ed), font=("ariel", 15, "bold"))
                    EDvalLabel12.place(x=250, y=125)

                    ##Output
                    # MonthlyPay Label
                    tpaymentLabel = Label(window12, text='TOTAL AMOUNT:', font=("ariel", 15, "bold"))
                    tpaymentLabel.place(x=10, y=155)
                    mpaymentLabel = Label(window12, text='MONTHLY PAYEMNT:', font=("ariel", 15, "bold"))
                    mpaymentLabel.place(x=10, y=185)
                    # MPVal Label
                    Output1 = StringVar()
                    Output2=StringVar()
                    p = float(p)
                    r = float(r)  
                    t = float(t)
                    total = p*((1+(r/100))**t)
                    mtotal=total/(t*12)
                    # output
                    Output1.set("₹" + str(round(total, 2)))
                    label1 = Label(window12, textvariable=Output1, font=("ariel", 15, "bold"))
                    label1.place(x=255, y=155)
                    Output2.set("₹" + str(round(mtotal, 2)))
                    label2 = Label(window12, textvariable=Output2, font=("ariel", 15, "bold"))
                    label2.place(x=255, y=185)
        
                    # Close Window Button
                    def closewindow12():
                        window12.destroy()
                        Window1_Function()

                    closeButton = Button(window12, text="Close", font=("ariel", 15, "bold"), padx=55, bg='light grey',
                                         command=closewindow12)
                    closeButton.place(x=110, y=235)



                 #Home Loan Button
                HomeLoanButton11 = Button(window11,
                                          text="HOME LOAN DETAILS",
                                          font=("Arial", 12, "bold"),
                                          bg="light grey",
                                          padx=30,
                                          command=HomeLoanDetails)
                HomeLoanButton11.place(x=90, y=150)
                ##Car Loan Button
                CarLoanButton11 = Button(window11,
                                         text="CAR LOAN DETAILS",
                                         font=("Arial", 12, "bold"),
                                         bg="light grey",
                                         padx=36,
                                         )
                CarLoanButton11.place(x=90, y=220)
                ##Personal Loan Button
                PersonalLoanButton11 = Button(window11,
                                              text="PERSONAL LOAN DETAILS",
                                              font=("Arial", 12, "bold"),
                                              bg="light grey",
                                              padx=10,
                                              )
                PersonalLoanButton11.place(x=90, y=290)

                q = "select h_principal,c_principal,p_principal from bdetails where USERNAME = '{}'".format(b)
                cursor.execute(q)
                data = cursor.fetchall()
                for i in data:
                    e, f, g = i[0], i[1], i[2]
                    e = str(e)
                    f = str(f)
                    g = str(g)
                    # h_principalValue label
                    h_principalVal11 = Label(window11,
                                             text=e,
                                             font=("ariel", 15, "bold"))

                    h_principalVal11.grid(row=0, column=1, sticky='w')

                    # c_principalValue label

                    c_principalVal11 = Label(window11,
                                             text=f,
                                             font=("ariel", 15, "bold"))
                    c_principalVal11.grid(row=1, column=1, sticky='w')

                    # p_principalValue label

                    p_principalVal11 = Label(window11,
                                             text=g,
                                             font=("ariel", 15, "bold"))
                    p_principalVal11.grid(row=2, column=1, sticky='w')

            # Button Code
            LoanDetailsButton = Button(window4,
                                       text="LOAN DETAILS",
                                       font=("Arial", 12, "bold"),
                                       bg="light grey",
                                       padx=10,
                                       command=Window11_Function)
            LoanDetailsButton.place(x=115, y=120)

        ## Checking function
        def LogInCheck():
            u3 = uname_box3.get()
            p3 = passwd_box3.get()
            cursor3 = con.cursor()
            qry = ('select * from bdetails')
            cursor3.execute(qry)
            data = cursor3.fetchall()
            for i in data:
                if u3 == i[1] and p3 == i[2]:
                    Window4_Function()
                    break
                else:
                    Invalid_Label = Label(window3,
                                          text="Invalid Username / Password!",
                                          fg="red",
                                          font=("ariel", 15, "bold"))
                    Invalid_Label.place(x=10, y=120)

        submit3 = Button(window3,
                         text="SUBMIT",
                         font=("ariel", 15, "bold"),
                         bg="light grey",
                         padx=10,
                         command=LogInCheck)
        submit3.place(x=150, y=70)

    # Window1 Buttons
    CreateAccButton = Button(window1,
                             text="Create Account",
                             font=("ariel", 15, "bold"),
                             bg="light gray",
                             command=Window2_Function)
    CreateAccButton.grid(row=1, column=1)
    LogInButton = Button(window1,
                         text="Log In",
                         font=("ariel", 15, "bold"),
                         bg="light gray",
                         padx=45,
                         command=Window3_Function)
    LogInButton.grid(row=3, column=1)

    window1.mainloop()


Window1_Function()
