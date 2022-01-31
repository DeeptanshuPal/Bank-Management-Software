from tkinter import *

import mysql.connector as sqltor

con = sqltor.connect(host="localhost", user="root", passwd="123456", database="bank")
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
            if n2 == '' or p2 == '' or u2 == '' or b2 == '':
                Invalid_Label = Label(window2,
                                      text="Invalid Values!",
                                      fg="red",
                                      font=("ariel", 15, "bold"))
                Invalid_Label.place(x=10, y=220)
            else:
                q = "INSERT INTO bdetails(NAME, USERNAME,PASSWD,BALANCE)values('{}','{}','{}',{})".format(n2, u2, p2,
                                                                                                          b2)
                cursor2 = con.cursor()
                cursor2.execute(q)
                con.commit()
                window2.destroy()
                Window1_Function()

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
                    # Username label
                    uname6 = Label(window6,
                                   text=" Username : ",
                                   font=("ariel", 15, "bold"))
                    uname6.grid(row=0, column=0, sticky='w')
                    # Username display label
                    uname_box6 = Entry(window6,
                                       font=("ariel", 15),
                                       width=24)
                    uname_box6.grid(row=0, column=1, sticky='w')
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
                        u6 = uname_box6.get()
                        p6 = h_principal_box6.get()
                        r6 = 7
                        t6 = h_time_box6.get()
                        if u6 == '' or p6 == '' or r6 == '' or t6 == '':
                            Invalid_Label = Label(window6,
                                                  text="Invalid Input!",
                                                  fg="red",
                                                  font=("ariel", 15, "bold"))
                            Invalid_Label.place(x=10, y=220)
                        else:
                            Q = "select username from bdetails"
                            cursor.execute(Q)
                            datas = cursor.fetchall()
                            for k in range(len(datas)):
                                if u6 != datas[k][0]:
                                    Invalid_Label = Label(window6,
                                                          text="Invalid Username!",
                                                          fg="red",
                                                          font=("ariel", 15, "bold"))
                                    Invalid_Label.place(x=10, y=220)
                                else:
                                    q = "UPDATE bdetails SET h_principal={},h_rate={},h_time={} where USERNAME='{}'".format(
                                        p6, r6, t6, u6)
                                    cursor6 = con.cursor()
                                    cursor6.execute(q)
                                    con.commit()
                                    window6.destroy()
                                    Window1_Function()

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
                    # Username label
                    uname7 = Label(window7,
                                   text=" Username : ",
                                   font=("ariel", 15, "bold"))
                    uname7.grid(row=0, column=0, sticky='w')
                    # Username display label
                    uname_box7 = Entry(window7,
                                       font=("ariel", 15),
                                       width=24)
                    uname_box7.grid(row=0, column=1, sticky='w')
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
                        u7 = uname_box7.get()
                        p7 = c_principal_box7.get()
                        r7 = 6
                        t7 = c_time_box7.get()
                        if u7 == '' or p7 == '' or r7 == '' or t7 == '':
                            Invalid_Label = Label(window7,
                                                  text="Invalid Input!",
                                                  fg="red",
                                                  font=("ariel", 15, "bold"))
                            Invalid_Label.place(x=10, y=220)
                        else:
                            Q = "select username from bdetails"
                            cursor.execute(Q)
                            datas = cursor.fetchall()
                            for k in range(len(datas)):
                                if u7 != datas[k][0]:
                                    Invalid_Label = Label(window7,
                                                          text="Invalid Username!",
                                                          fg="red",
                                                          font=("ariel", 15, "bold"))
                                    Invalid_Label.place(x=10, y=220)
                                else:
                                    q = "UPDATE bdetails SET c_principal={},c_rate={},c_time={} where USERNAME='{}'".format(
                                        p7, r7, t7, u7)
                                    cursor6 = con.cursor()
                                    cursor6.execute(q)
                                    con.commit()
                                    window7.destroy()
                                    Window1_Function()

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
                    # Username label
                    uname8 = Label(window8,
                                   text=" Username : ",
                                   font=("ariel", 15, "bold"))
                    uname8.grid(row=0, column=0, sticky='w')
                    # Username display label
                    uname_box8 = Entry(window8,
                                       font=("ariel", 15),
                                       width=24)
                    uname_box8.grid(row=0, column=1, sticky='w')
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
                        u8 = uname_box8.get()
                        p8 = p_principal_box8.get()
                        r8 = 5
                        t8 = p_time_box8.get()
                        if u8 == '' or p8 == '' or r8 == '' or t8 == '':
                            Invalid_Label = Label(window8,
                                                  text="Invalid Input!",
                                                  fg="red",
                                                  font=("ariel", 15, "bold"))
                            Invalid_Label.place(x=10, y=220)
                        else:
                            Q = "select username from bdetails"
                            cursor.execute(Q)
                            datas = cursor.fetchall()
                            for k in range(len(datas)):
                                if u8 != datas[k][0]:
                                    Invalid_Label = Label(window8,
                                                          text="Invalid Username!",
                                                          fg="red",
                                                          font=("ariel", 15, "bold"))
                                    Invalid_Label.place(x=10, y=220)
                                else:
                                    q = "UPDATE bdetails SET p_principal={},p_rate={},p_time={} where USERNAME='{}'".format(
                                        p8, r8, t8, u8)
                                    cursor6 = con.cursor()
                                    cursor6.execute(q)
                                    con.commit()
                                    window8.destroy()
                                    Window1_Function()

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
                # Username label
                uname9 = Label(window9,
                               text=" Username          : ",
                               font=("ariel", 15, "bold"))
                uname9.grid(row=0, column=0, sticky='w')
                # Username display label
                uname_box9 = Entry(window9,
                                   font=("ariel", 15),
                                   width=21)
                uname_box9.grid(row=0, column=1, sticky='w')
                # Deposit Amount label
                Deposit_Amt = Label(window9,
                                    text=" Deposit Amount : ",
                                    font=("ariel", 15, "bold"))
                Deposit_Amt.grid(row=1, column=0, sticky='w')
                # Deposit amt display label
                DepositAmt_box9 = Entry(window9,
                                        font=("ariel", 15),
                                        width=21)
                DepositAmt_box9.grid(row=1, column=1, sticky='w')

                # submit button
                def DepositFunc():
                    u9 = uname_box9.get()
                    d9 = DepositAmt_box9.get()
                    if u9 == '' or d9 == '':
                        Invalid_Label = Label(window9,
                                              text="Invalid Input!",
                                              fg="red",
                                              font=("ariel", 15, "bold"))
                        Invalid_Label.place(x=10, y=220)
                    else:
                        Q = "select username from bdetails"
                        cursor.execute(Q)
                        datas = cursor.fetchall()
                        for k in range(len(datas)):
                            if u9 != datas[k][0]:
                                Invalid_Label = Label(window9,
                                                      text="Invalid Username!",
                                                      fg="red",
                                                      font=("ariel", 15, "bold"))
                                Invalid_Label.place(x=10, y=220)
                            else:
                                q = "update bdetails set balance=balance+'{}' where username = '{}'".format(d9, u9)
                                cursor9 = con.cursor()
                                cursor9.execute(q)
                                con.commit()
                                window9.destroy()
                                Window1_Function()

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
                # Username label
                uname10 = Label(window10,
                                text=" Username             : ",
                                font=("ariel", 15, "bold"))
                uname10.grid(row=0, column=0, sticky='w')
                # Username display label
                uname_box10 = Entry(window10,
                                    font=("ariel", 15),
                                    width=19)
                uname_box10.grid(row=0, column=1, sticky='w')
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
                    u10 = uname_box10.get()
                    w10 = WithdrawAmt_box10.get()
                    if u10 == '' or w10 == '':
                        Invalid_Label = Label(window10,
                                              text="Invalid Input!",
                                              fg="red",
                                              font=("ariel", 15, "bold"))
                        Invalid_Label.place(x=10, y=120)
                    else:
                        Q = "select username from bdetails"
                        cursor.execute(Q)
                        datas = cursor.fetchall()
                        for k in range(len(datas)):
                            if u10 != datas[k][0]:
                                Invalid_Label = Label(window10,
                                                      text="Invalid Username!                ",
                                                      fg="red",
                                                      font=("ariel", 15, "bold"))
                                Invalid_Label.place(x=10, y=120)
                            else:
                                m = "select balance from bdetails where username='{}'".format(u10)
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
                                    break
                                else:
                                    q = "update bdetails set balance=balance-{} where username='{}' and balance >= '{}'".format(
                                        w10, u10, w10)
                                    cursor10 = con.cursor()
                                    cursor10.execute(q)
                                    con.commit()
                                    window10.destroy()
                                    Window1_Function()

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

            ##(Window11)Loan Window
            def Window11_Function():
                window11 = Tk()
                window11.geometry("423x423")
                window11.title("Loan Details")
                window4.destroy()
                # h_principal label
                H_LoanTakenLabel4 = Label(window11,
                                          text=" HOME LOAN             : ",
                                          font=("ariel", 15, "bold"))
                H_LoanTakenLabel4.grid(row=4, column=0, sticky='w')
                # c_principal label
                C_LoanTakenLabel4 = Label(window11,
                                          text=" CAR LOAN                : ",
                                          font=("ariel", 15, "bold"))
                C_LoanTakenLabel4.grid(row=5, column=0, sticky='w')
                # p_principal label
                P_LoanTakenLabel4 = Label(window11,
                                          text=" PERSONAL LOAN     : ",
                                          font=("ariel", 15, "bold"))
                P_LoanTakenLabel4.grid(row=6, column=0, sticky='w')

                # Labels to Display values from SQL
                cursor = con.cursor()

                q = "select h_principal,c_principal,p_principal from bdetails where USERNAME = '{}'".format(b)
                cursor.execute(q)
                data = cursor.fetchall()
                for i in data:
                    e, f, g = i[0], i[1], i[2]
                    print(type(e))
                    # h_principalValue label
                    var5 = IntVar()
                    var5.set(e)
                    h_principalVal11 = Label(window11,
                                            textvariable=var5,
                                            font=("ariel", 15, "bold"))
                    h_principalVal11.grid(row=4, column=1, sticky='w')

                    # c_principalValue label
                    var6 = IntVar()
                    var6.set(f)
                    c_principalVal11 = Label(window11,
                                            textvariable=var6,
                                            font=("ariel", 15, "bold"))
                    c_principalVal11.grid(row=5, column=1, sticky='w')

                    # p_principalValue label
                    var7 = IntVar()
                    var7.set(g)
                    p_principalVal11 = Label(window11,
                                            textvariable=var7,
                                            font=("ariel", 15, "bold"))
                    p_principalVal11.grid(row=6, column=1, sticky='w')

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
