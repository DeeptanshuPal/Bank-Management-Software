from tkinter import *

import mysql.connector as sqltor

con = sqltor.connect(host="localhost", user="root", passwd="123456", database="bank")
if con.is_connected():
    print("Connection Successful...")


def Window1_Function():
    ### (Window1)Welcome window
    window1 = Tk()
    window1.geometry("495x800+0+0")  #####BG Image = 491x790
    window1.title("Welcome Page")
    # window1 icon and image
    icon = PhotoImage(file="Window_Thumbnail.png")
    logo = PhotoImage(file="Bank-Logo.png")
    BG = PhotoImage(file="MS_Background6.png")
    BackgroundImg = Label(window1, image=BG)
    BackgroundImg.place(x=0, y=0)
    window1.iconphoto(True, icon)
    bank_img = Label(window1, image=logo, padx=50)
    bank_img.place(x=40, y=145)
    bank_name = Label(window1, text="OLA Bank", font=("Arial Black", 45, 'italic'), fg="#e91c27")
    bank_name.place(x=130, y=140)
    bank_motto = Label(window1, text="We Understand Your World.", font=("Bahnschrift SemiLight", 15, 'italic', 'bold'),
                       fg="gray")
    bank_motto.place(x=133, y=210)
    #Display Current Time
    QTime = "Select hour(curtime()),minute(curtime())"
    cursorT = con.cursor()
    cursorT.execute(QTime)
    dataT = cursorT.fetchall()
    for i in dataT:
        hCurTime = i[0]
        mCurTime = i[1]
    TimeVal1=str(hCurTime)+":"+str(mCurTime)
    timeLabel = Label(window1, text=TimeVal1, font=('arial black', 14,'bold'), bg='#a6a8a5',pady=0) # font size =15 for my big screen
    timeLabel.place(x=48,y=72)    #y=85 for my big screen

    # Window1 Button Functions
    ## (Window2)Create Account window
    def Window2_Function():
        window2 = Toplevel()
        window2.title("Create Account")
        window2.geometry("495x800+0+0")
        '''window1.destroy()'''
        BackgroundImg = Label(window2, image=BG)
        BackgroundImg.place(x=0, y=0)
        BackgroundImg.image = BG
        WindowPic = PhotoImage(file="CreateAccPic.png")
        WindowImg = Label(window2, image=WindowPic)
        WindowImg.place(x=200, y=120)  ######WindowImg size = 96x96
        WindowImg.image = WindowPic
        # Display Current Time
        QTime = "Select hour(curtime()),minute(curtime())"
        cursorT = con.cursor()
        cursorT.execute(QTime)
        dataT = cursorT.fetchall()
        for i in dataT:
            hCurTime = i[0]
            mCurTime = i[1]
        TimeVal1 = str(hCurTime) + ":" + str(mCurTime)
        timeLabel = Label(window2, text=TimeVal1, font=('arial black', 14, 'bold'), bg='#a6a8a5',
                          pady=0)  # font size =15 for my big screen
        timeLabel.place(x=48, y=72)  # y=85 for my big screen

        # Name label
        name2 = Label(window2,
                      text="NAME                  :",
                      font=("ariel", 15, "bold"))
        name2.place(x=43, y=235)
        # Name textbox
        name_box2 = Entry(window2,
                          font=("ariel", 15),
                          width=20)
        name_box2.place(x=230, y=235)
        # username label
        uname2 = Label(window2,
                       text="USERNAME         :",
                       font=("ariel", 15, "bold"))
        uname2.place(x=43, y=265)
        # username textbox
        uname_box2 = Entry(window2,
                           font=("ariel", 15),
                           width=20)
        uname_box2.place(x=230, y=265)
        # PASSWORD label
        passwd2 = Label(window2,
                        text="PASSWORD        :",
                        font=("ariel", 15, "bold"))
        passwd2.place(x=44, y=295)
        # PASSWORD textbox
        passwd_box2 = Entry(window2,
                            show=str('*'),
                            font=("ariel", 15),
                            width=20)
        passwd_box2.place(x=230, y=295)
        # Deposit label
        deposit2 = Label(window2,
                         text="INITIAL DEPOSIT :",
                         font=("ariel", 15, "bold"))
        deposit2.place(x=43, y=325)
        # Deposit textbox
        deposit_box2 = Entry(window2,
                             font=("ariel", 15),
                             width=20)
        deposit_box2.place(x=230, y=325)

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
                    if int(b2)<1000:
                        Invalid_Label = Label(window2,
                                              text="Minimum deposit ₹1000!         ",
                                              fg="red",
                                              font=("ariel", 15, "bold"))
                        Invalid_Label.place(x=45, y=450)                        
                    elif int(b2)>1000000:
                        Invalid_Label = Label(window2,
                                              text="Maximum deposit ₹1000000!",
                                              fg="red",
                                              font=("ariel", 15, "bold"))
                        Invalid_Label.place(x=45, y=450)
                    else:
                        q = "INSERT INTO bdetails(NAME, USERNAME,PASSWD,BALANCE)values('{}','{}','{}',{})".format(n2,u2,p2,b2)                                                                                                                  
                        cursor2 = con.cursor()
                        cursor2.execute(q)
                        con.commit()
                        window2.destroy()                    
                                            
                else:
                    Invalid_Label = Label(window2,
                                          text="Username already exists!",
                                          fg="red",
                                          font=("ariel", 15, "bold"))
                    Invalid_Label.place(x=45, y=450)

            else:
                Invalid_Label = Label(window2,
                                      text="Invalid Values!                               ",
                                      fg="red",
                                      font=("ariel", 15, "bold"))
                Invalid_Label.place(x=45, y=450)

        submit2 = Button(window2,
                         text="SUBMIT",
                         font=("ariel", 15, "bold"),
                         bg="light grey",
                         padx=10,
                         command=CreateAccSubmit)
        submit2.place(x=185, y=370)

    ## (Window3)LogIn window
    def Window3_Function():
        window3 = Toplevel()
        window3.title("Log In")
        window3.geometry("495x800+0+0")
        '''window1.destroy()'''
        BackgroundImg = Label(window3, image=BG)
        BackgroundImg.place(x=0, y=0)
        BackgroundImg.image = BG
        WindowPic = PhotoImage(file="LogInPic.png")
        WindowImg = Label(window3, image=WindowPic)
        WindowImg.place(x=200, y=120)  ######WindowImg size = 96x96
        WindowImg.image = WindowPic
        # Display Current Time
        QTime = "Select hour(curtime()),minute(curtime())"
        cursorT = con.cursor()
        cursorT.execute(QTime)
        dataT = cursorT.fetchall()
        for i in dataT:
            hCurTime = i[0]
            mCurTime = i[1]
        TimeVal1 = str(hCurTime) + ":" + str(mCurTime)
        timeLabel = Label(window3, text=TimeVal1, font=('arial black', 14, 'bold'), bg='#a6a8a5',
                          pady=0)  # font size =15 for my big screen
        timeLabel.place(x=48, y=72)  # y=85 for my big screen

        # username label
        uname3 = Label(window3,
                       text="USERNAME  :",
                       font=("ariel", 15, "bold"))
        uname3.place(x=43, y=235)
        # username textbox
        uname_box3 = Entry(window3,
                           font=("ariel", 15),
                           width=24)
        uname_box3.place(x=180, y=235)
        # Passwd label
        passwd3 = Label(window3,
                        text="PASSWORD :",
                        font=("ariel", 15, "bold"))
        passwd3.place(x=43, y=265)
        # Passwd textbox
        passwd_box3 = Entry(window3,
                            show=str('*'),
                            font=("ariel", 15),
                            width=24)
        passwd_box3.place(x=180, y=265)

        ### submit button
        ##(Window4) Bank Details Window
        def Window4_Function():
            window4 = Toplevel()
            window4.geometry("495x800+0+0")
            window4.title("Bank Details")
            U3 = uname_box3.get()  # used in window4

            window3.destroy()  ### this should not be here
            BackgroundImg = Label(window4, image=BG)
            BackgroundImg.place(x=0, y=0)
            BackgroundImg.image = BG
            WindowPic = PhotoImage(file="ProfilePic.png")
            WindowImg = Label(window4, image=WindowPic)
            WindowImg.place(x=200, y=120)  ######WindowImg size = 96x96
            WindowImg.image = WindowPic
            # Display Current Time
            QTime = "Select hour(curtime()),minute(curtime())"
            cursorT = con.cursor()
            cursorT.execute(QTime)
            dataT = cursorT.fetchall()
            for i in dataT:
                hCurTime = i[0]
                mCurTime = i[1]
            TimeVal1 = str(hCurTime) + ":" + str(mCurTime)
            timeLabel = Label(window4, text=TimeVal1, font=('arial black', 14, 'bold'), bg='#a6a8a5',
                              pady=0)  # font size =15 for my big screen
            timeLabel.place(x=48, y=72)  # y=85 for my big screen

            # Window4 widgets
            # Name label
            name4 = Label(window4,
                          text="NAME                           :",
                          font=("ariel", 15, "bold"))
            name4.place(x=44, y=235)
            # username label
            uname4 = Label(window4,
                           text="USERNAME                  :",
                           font=("ariel", 15, "bold"))
            uname4.place(x=44, y=265)
            # PASSWORD label
            passwd4 = Label(window4,
                            text="PASSWORD                 :",
                            font=("ariel", 15, "bold"))
            passwd4.place(x=44, y=295)
            # Balance label
            balance4 = Label(window4,
                             text="ACCOUNT BALANCE   :",
                             font=("ariel", 15, "bold"))
            balance4.place(x=45, y=325)

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
                NameVal4.place(x=295, y=235)
                # UsernameValue label
                var2 = StringVar()
                UsernameVal4 = Label(window4,
                                     textvariable=var2,
                                     font=("ariel", 15, "bold"))
                var2.set(b)
                UsernameVal4.place(x=295, y=265)
                # PasswordValue label                
                k=len(c)
                kl = k*'*'
                PasswdVal4 = Label(window4,
                                   text=kl,
                                   font=("ariel", 15, "bold"))                                
                PasswdVal4.place(x=295, y=295)
                # BalanceValue label
                var4 = StringVar()
                PasswdVal4 = Label(window4,
                                   textvariable=var4,
                                   font=("ariel", 15, "bold"))
                var4.set(d)
                PasswdVal4.place(x=295, y=325)
            print(b)
            print(var2)

            ###Take Loan Button
            ##button func--------
            # (Window5) Loan Choices Window
            def Window5_Function():
                window5 = Toplevel()
                window5.geometry("495x800+0+0")
                window5.title("Loan Choices")
                BackgroundImg = Label(window5, image=BG)
                BackgroundImg.place(x=0, y=0)
                BackgroundImg.image = BG
                WindowPic = PhotoImage(file="LoanChoicesPic.png")
                WindowImg = Label(window5, image=WindowPic)
                WindowImg.place(x=200, y=120)  ######WindowImg size = 96x96
                WindowImg.image = WindowPic
                # Display Current Time
                QTime = "Select hour(curtime()),minute(curtime())"
                cursorT = con.cursor()
                cursorT.execute(QTime)
                dataT = cursorT.fetchall()
                for i in dataT:
                    hCurTime = i[0]
                    mCurTime = i[1]
                TimeVal1 = str(hCurTime) + ":" + str(mCurTime)
                timeLabel = Label(window5, text=TimeVal1, font=('arial black', 14, 'bold'), bg='#a6a8a5',
                                  pady=0)  # font size =15 for my big screen
                timeLabel.place(x=48, y=72)  # y=85 for my big screen


                ### (Window6)Home Loan Window
                def Window6_Function():
                    window6 = Toplevel()
                    window6.geometry("495x800+0+0")
                    window6.title("Home Loan")
                    BackgroundImg = Label(window6, image=BG)
                    BackgroundImg.place(x=0, y=0)
                    BackgroundImg.image = BG
                    WindowPic = PhotoImage(file="HomePic.png")
                    WindowImg = Label(window6, image=WindowPic)
                    WindowImg.place(x=200, y=120)  ######WindowImg size = 96x96
                    WindowImg.image = WindowPic
                    # Display Current Time
                    QTime = "Select hour(curtime()),minute(curtime())"
                    cursorT = con.cursor()
                    cursorT.execute(QTime)
                    dataT = cursorT.fetchall()
                    for i in dataT:
                        hCurTime = i[0]
                        mCurTime = i[1]
                    TimeVal1 = str(hCurTime) + ":" + str(mCurTime)
                    timeLabel = Label(window6, text=TimeVal1, font=('arial black', 14, 'bold'), bg='#a6a8a5',
                                      pady=0)  # font size =15 for my big screen
                    timeLabel.place(x=48, y=72)  # y=85 for my big screen

                    # h_principal label
                    h_principal6 = Label(window6,
                                         text=" Loan Taken : ",
                                         font=("ariel", 15, "bold"))
                    h_principal6.place(x=43, y=235)
                    # h_principal display label
                    h_principal_box6 = Entry(window6,
                                             font=("ariel", 15),
                                             width=24)
                    h_principal_box6.place(x=180, y=235)
                    # h_rate label
                    h_rate6 = Label(window6,
                                    text=" Rate            : ",
                                    font=("ariel", 15, "bold"))
                    h_rate6.place(x=43, y=265)
                    # h_rate display label
                    h_rate_box6 = Label(window6,
                                        text=" 7%",
                                        font=("ariel", 15, "bold"))
                    h_rate_box6.place(x=180, y=265)
                    # h_time label
                    h_time6 = Label(window6,
                                    text=" Time           : ",
                                    font=("ariel", 15, "bold"))
                    h_time6.place(x=43, y=295)
                    # h_time display label
                    h_time_box6 = Entry(window6,
                                        font=("ariel", 15),
                                        width=24)
                    h_time_box6.place(x=180, y=295)
                    window5.destroy()

                    # submit button
                    def SubmitLoanFunc():
                        p6 = h_principal_box6.get()
                        r6 = 7
                        global t6
                        t6 = h_time_box6.get()
                        if p6.isdigit() and t6.isdigit():
                            if p6 == '' or r6 == '' or t6 == '' or int(p6) == 0 or int(t6) == 0:
                                Invalid_Label = Label(window6,
                                                      text="Invalid Input!                          ",
                                                      fg="red",
                                                      font=("ariel", 15, "bold"))
                                Invalid_Label.place(x=45, y=450)
                                Blank = Label(window6,
                                                  text="                                                                           ",
                                                  fg="black",
                                                  font=("ariel", 10, "bold"))
                                Blank.place(x=45, y=480)
                            elif int(t6) > 15:
                                MaxTime_Label = Label(window6,
                                                      text="Max time is 15 years! ",
                                                      fg="red",
                                                      font=("ariel", 15, "bold"))
                                MaxTime_Label.place(x=45, y=450)
                                TimeBlank = Label(window6,
                                                  text="                                                                              ",
                                                  fg="black",
                                                  font=("ariel", 10, "bold"))
                                TimeBlank.place(x=45, y=480)
                            elif int(p6) > 5 * int(d):
                                MaxHLoan_Label = Label(window6,
                                                       text="Loan Criteria not met!",
                                                       fg="red",
                                                       font=("ariel", 15, "bold"))
                                MaxHLoan_Label.place(x=45, y=450)
                                MaxHLoan_Label2 = Label(window6,
                                                        text="*Maximum loan allowance is 5x account balance.",
                                                        fg="black",
                                                        font=("ariel", 10, "bold"))
                                MaxHLoan_Label2.place(x=45, y=480)

                            else:
                                q = "UPDATE bdetails SET h_principal={},h_rate={},h_time={},h_date=curdate() where USERNAME='{}'".format(
                                    p6, r6, t6, U3)
                                cursor6 = con.cursor()
                                cursor6.execute(q)
                                con.commit()
                                window6.destroy()
                        else:
                            Invalid_Label = Label(window6,
                                                  text="Invalid Input!                             ",
                                                  fg="red",
                                                  font=("ariel", 15, "bold"))
                            Invalid_Label.place(x=45, y=450)

                    submit6 = Button(window6,
                                     text="SUBMIT",
                                     font=("ariel", 15, "bold"),
                                     bg="light grey",
                                     padx=10,
                                     command=SubmitLoanFunc)
                    submit6.place(x=185, y=360)

                ### (Window7)Car Loan Window
                def Window7_Function():
                    window7 = Toplevel()
                    window7.geometry("495x800+0+0")
                    window7.title("Car Loan")
                    BackgroundImg = Label(window7, image=BG)
                    BackgroundImg.place(x=0, y=0)
                    BackgroundImg.image = BG
                    WindowPic = PhotoImage(file="CarPic.png")
                    WindowImg = Label(window7, image=WindowPic)
                    WindowImg.place(x=182, y=115)  ######WindowImg size = 96x96
                    WindowImg.image = WindowPic
                    # Display Current Time
                    QTime = "Select hour(curtime()),minute(curtime())"
                    cursorT = con.cursor()
                    cursorT.execute(QTime)
                    dataT = cursorT.fetchall()
                    for i in dataT:
                        hCurTime = i[0]
                        mCurTime = i[1]
                    TimeVal1 = str(hCurTime) + ":" + str(mCurTime)
                    timeLabel = Label(window7, text=TimeVal1, font=('arial black', 14, 'bold'), bg='#a6a8a5',
                                      pady=0)  # font size =15 for my big screen
                    timeLabel.place(x=48, y=72)  # y=85 for my big screen

                    # c_principal label
                    c_principal7 = Label(window7,
                                         text=" Loan Taken : ",
                                         font=("ariel", 15, "bold"))
                    c_principal7.place(x=43, y=235)
                    # c_principal display label
                    c_principal_box7 = Entry(window7,
                                             font=("ariel", 15),
                                             width=24)
                    c_principal_box7.place(x=180, y=235)
                    # c_rate label
                    c_rate7 = Label(window7,
                                    text=" Rate            : ",
                                    font=("ariel", 15, "bold"))
                    c_rate7.place(x=43, y=265)
                    # c_rate display label
                    c_rate_box7 = Label(window7,
                                        text=" 6%",
                                        font=("ariel", 15, "bold"))
                    c_rate_box7.place(x=180, y=265)
                    # c_time label
                    c_time7 = Label(window7,
                                    text=" Time           : ",
                                    font=("ariel", 15, "bold"))
                    c_time7.place(x=43, y=295)
                    # c_time display label
                    c_time_box7 = Entry(window7,
                                        font=("ariel", 15),
                                        width=24)
                    c_time_box7.place(x=180, y=295)
                    window5.destroy()

                    # submit button
                    def SubmitLoanFunc():
                        p7 = c_principal_box7.get()
                        r7 = 6
                        t7 = c_time_box7.get()
                        if p7.isdigit() and t7.isdigit():
                            if p7 == '' or r7 == '' or t7 == '' or int(p7) == 0 or int(t7) == 0:
                                Invalid_Label = Label(window7,
                                                      text="Invalid Input!                       ",
                                                      fg="red",
                                                      font=("ariel", 15, "bold"))
                                Invalid_Label.place(x=45, y=450)
                                Blank = Label(window7,
                                                  text="                                                                               ",
                                                  fg="black",
                                                  font=("ariel", 10, "bold"))
                                Blank.place(x=45, y=480)
                            elif int(t7) > 10:
                                MaxTime_Label = Label(window7,
                                                      text="Max time is 10 years! ",
                                                      fg="red",
                                                      font=("ariel", 15, "bold"))
                                MaxTime_Label.place(x=45, y=450)
                                Blank = Label(window7,
                                                  text="                                                                                   ",
                                                  fg="black",
                                                  font=("ariel", 10, "bold"))
                                Blank.place(x=45, y=480)
                            elif int(p7) > 5 * int(d):
                                MaxHLoan_Label = Label(window7,
                                                       text="Loan Criteria not met!",
                                                       fg="red",
                                                       font=("ariel", 15, "bold"))
                                MaxHLoan_Label.place(x=45, y=450)
                                MaxHLoan_Label2 = Label(window7,
                                                        text="*Maximum loan allowance is 5x account balance.",
                                                        fg="black",
                                                        font=("ariel", 10, "bold"))
                                MaxHLoan_Label2.place(x=45, y=480)
                            else:
                                q = "UPDATE bdetails SET c_principal={},c_rate={},c_time={},c_date=curdate() where USERNAME='{}'".format(
                                    p7, r7, t7, U3)
                                cursor6 = con.cursor()
                                cursor6.execute(q)
                                con.commit()
                                window7.destroy()
                        else:
                            Invalid_Label = Label(window7,
                                                  text="Invalid Input!                      ",
                                                  fg="red",
                                                  font=("ariel", 15, "bold"))
                            Invalid_Label.place(x=45, y=450)

                    submit7 = Button(window7,
                                     text="SUBMIT",
                                     font=("ariel", 15, "bold"),
                                     bg="light grey",
                                     padx=10,
                                     command=SubmitLoanFunc)
                    submit7.place(x=185, y=360)

                ### (Window8)Personal Loan Window
                def Window8_Function():
                    window8 = Toplevel()
                    window8.geometry("495x800+0+0")
                    window8.title("Personal Loan")
                    BackgroundImg = Label(window8, image=BG)
                    BackgroundImg.place(x=0, y=0)
                    BackgroundImg.image = BG
                    WindowPic = PhotoImage(file="PersonalLoanPic.png")
                    WindowImg = Label(window8, image=WindowPic)
                    WindowImg.place(x=200, y=120)  ######WindowImg size = 96x96
                    WindowImg.image = WindowPic
                    # Display Current Time
                    QTime = "Select hour(curtime()),minute(curtime())"
                    cursorT = con.cursor()
                    cursorT.execute(QTime)
                    dataT = cursorT.fetchall()
                    for i in dataT:
                        hCurTime = i[0]
                        mCurTime = i[1]
                    TimeVal1 = str(hCurTime) + ":" + str(mCurTime)
                    timeLabel = Label(window8, text=TimeVal1, font=('arial black', 14, 'bold'), bg='#a6a8a5',
                                      pady=0)  # font size =15 for my big screen
                    timeLabel.place(x=48, y=72)  # y=85 for my big screen

                    # p_principal label
                    p_principal8 = Label(window8,
                                         text=" Loan Taken : ",
                                         font=("ariel", 15, "bold"))
                    p_principal8.place(x=43, y=235)
                    # p_principal display label
                    p_principal_box8 = Entry(window8,
                                             font=("ariel", 15),
                                             width=24)
                    p_principal_box8.place(x=180, y=235)
                    # p_rate label
                    p_rate8 = Label(window8,
                                    text=" Rate            : ",
                                    font=("ariel", 15, "bold"))
                    p_rate8.place(x=43, y=265)
                    # p_rate display label
                    p_rate_box8 = Label(window8,
                                        text=" 5%",
                                        font=("ariel", 15, "bold"))
                    p_rate_box8.place(x=180, y=265)
                    # p_time label
                    p_time8 = Label(window8,
                                    text=" Time           : ",
                                    font=("ariel", 15, "bold"))
                    p_time8.place(x=43, y=295)
                    # p_time display label
                    p_time_box8 = Entry(window8,
                                        font=("ariel", 15),
                                        width=24)
                    p_time_box8.place(x=180, y=295)
                    window5.destroy()

                    # submit button
                    def SubmitLoanFunc():
                        p8 = p_principal_box8.get()
                        r8 = 5
                        t8 = p_time_box8.get()
                        if p8.isdigit() and t8.isdigit():
                            if p8 == '' or r8 == '' or t8 == '' or int(p8) == 0 or int(t8) == 0:
                                Invalid_Label = Label(window8,
                                                      text="Invalid Input!                   ",
                                                      fg="red",
                                                      font=("ariel", 15, "bold"))
                                Invalid_Label.place(x=45, y=450)
                                Blank = Label(window8,
                                                  text="                                                                        ",
                                                  fg="black",
                                                  font=("ariel", 10, "bold"))
                                Blank.place(x=45, y=480)
                            elif int(t8) > 8:
                                MaxTime_Label = Label(window8,
                                                      text="Max time is 8 years! ",
                                                      fg="red",
                                                      font=("ariel", 15, "bold"))
                                MaxTime_Label.place(x=45, y=450)
                                Blank = Label(window8,
                                                  text="                                                                        ",
                                                  fg="black",
                                                  font=("ariel", 10, "bold"))
                                Blank.place(x=45, y=480)
                            elif int(p8) > 5 * int(d):
                                MaxHLoan_Label = Label(window8,
                                                       text="Loan Criteria not met!",
                                                       fg="red",
                                                       font=("ariel", 15, "bold"))
                                MaxHLoan_Label.place(x=45, y=450)
                                MaxHLoan_Label2 = Label(window8,
                                                        text="*Maximum loan allowance is 5x account balance.",
                                                        fg="black",
                                                        font=("ariel", 10, "bold"))
                                MaxHLoan_Label2.place(x=45, y=480)
                            else:
                                q = "UPDATE bdetails SET p_principal={},p_rate={},p_time={},p_date=curdate() where USERNAME='{}'".format(p8, r8, t8, U3)
                                cursor6 = con.cursor()
                                cursor6.execute(q)
                                con.commit()
                                window8.destroy()
                        else:
                            Invalid_Label = Label(window8,
                                                  text="Invalid Input!                           ",
                                                  fg="red",
                                                  font=("ariel", 15, "bold"))
                            Invalid_Label.place(x=45, y=450)

                    submit8 = Button(window8,
                                     text="SUBMIT",
                                     font=("ariel", 15, "bold"),
                                     bg="light grey",
                                     padx=10,
                                     command=SubmitLoanFunc)
                    submit8.place(x=185, y=360)

                ##Home Loan Button
                HomeLoanButton = Button(window5,
                                        text="HOME LOAN",
                                        font=("Arial", 12, "bold"),
                                        bg="light grey",
                                        padx=30,
                                        command=Window6_Function)
                HomeLoanButton.place(x=155, y=310)
                ##Car Loan Button
                CarLoanButton = Button(window5,
                                       text="CAR LOAN",
                                       font=("Arial", 12, "bold"),
                                       bg="light grey",
                                       padx=36,
                                       command=Window7_Function)
                CarLoanButton.place(x=155, y=380)
                ##Personal Loan Button
                PersonalLoanButton = Button(window5,
                                            text="PERSONAL LOAN",
                                            font=("Arial", 12, "bold"),
                                            bg="light grey",
                                            padx=10,
                                            command=Window8_Function)
                PersonalLoanButton.place(x=155, y=450)

                window4.destroy()

            # Button Code
            TakeLoanButton = Button(window4,
                                    text="TAKE LOANS",
                                    font=("Arial", 12, "bold"),
                                    bg="light grey",
                                    padx=35,
                                    command=Window5_Function)
            TakeLoanButton.place(x=150, y=410)

            # Log out & Go Back to Home Screen Button
            def LogOutFunc():
                window4.destroy()

            LogOutButton = Button(window4,
                                  text="LOG OUT",
                                  font=("Arial", 12, "bold"),
                                  bg="light grey",
                                  padx=50,
                                  command=LogOutFunc)
            LogOutButton.place(x=150, y=560)

            ### (Window9)Deposit Balance Window
            def Window9_Function():
                window9 = Toplevel()
                window9.geometry("495x800+0+0")
                window9.title("Deposit Balance")
                window4.destroy()
                BackgroundImg = Label(window9, image=BG)
                BackgroundImg.place(x=0, y=0)
                BackgroundImg.image = BG
                WindowPic = PhotoImage(file="MoneyPic.png")
                WindowImg = Label(window9, image=WindowPic)
                WindowImg.place(x=200, y=120)  ######WindowImg size = 96x96
                WindowImg.image = WindowPic
                # Display Current Time
                QTime = "Select hour(curtime()),minute(curtime())"
                cursorT = con.cursor()
                cursorT.execute(QTime)
                dataT = cursorT.fetchall()
                for i in dataT:
                    hCurTime = i[0]
                    mCurTime = i[1]
                TimeVal1 = str(hCurTime) + ":" + str(mCurTime)
                timeLabel = Label(window9, text=TimeVal1, font=('arial black', 14, 'bold'), bg='#a6a8a5',
                                  pady=0)  # font size =15 for my big screen
                timeLabel.place(x=48, y=72)  # y=85 for my big screen

                # Deposit Amount label
                Deposit_Amt = Label(window9,
                                    text=" Deposit Amount : ",
                                    font=("ariel", 15, "bold"))
                Deposit_Amt.place(x=43, y=235)
                # Deposit amt display label
                DepositAmt_box9 = Entry(window9,
                                        font=("ariel", 15),
                                        width=21)
                DepositAmt_box9.place(x=220, y=235)

                # submit button
                def DepositFunc():
                    d9 = str(DepositAmt_box9.get())
                    if d9.isdigit():
                        if int(d9) > 0 and int(d9) <= 100000:
                            q = "update bdetails set balance=balance+'{}' where username = '{}'".format(d9, U3)
                            cursor9 = con.cursor()
                            cursor9.execute(q)
                            con.commit()
                            window9.destroy()
                        elif int(d9) > 100000:
                            Limit_Label = Label(window9,
                                                text="Max deposit ₹100000!",
                                                fg="red",
                                                font=("ariel", 15, "bold"))
                            Limit_Label.place(x=45, y=450)
                        else:
                            Invalid_Label = Label(window9,
                                                  text="Invalid Input!                   ",
                                                  fg="red",
                                                  font=("ariel", 15, "bold"))
                            Invalid_Label.place(x=45, y=450)
                    
                    else:
                        Invalid_Label = Label(window9,
                                              text="Invalid Input!                   ",
                                              fg="red",
                                              font=("ariel", 15, "bold"))
                        Invalid_Label.place(x=45, y=450)

                submit9 = Button(window9,
                                 text="DEPOSIT & EXIT",
                                 font=("ariel", 15, "bold"),
                                 bg="light grey",
                                 padx=10,
                                 command=DepositFunc)
                submit9.place(x=145, y=300)

            # Button Code
            DepositAmtButton = Button(window4,
                                      text="DEPOSIT MONEY",
                                      font=("Arial", 12, "bold"),
                                      bg="light grey",
                                      padx=20,
                                      command=Window9_Function)
            DepositAmtButton.place(x=150, y=460)

            ### (Window10)Withdraw Balance Window
            def Window10_Function():
                window10 = Toplevel()
                window10.geometry("495x800+0+0")
                window10.title("Withdraw Balance")
                window4.destroy()
                BackgroundImg = Label(window10, image=BG)
                BackgroundImg.place(x=0, y=0)
                BackgroundImg.image = BG
                WindowPic = PhotoImage(file="MoneyPic.png")
                WindowImg = Label(window10, image=WindowPic)
                WindowImg.place(x=200, y=120)  ######WindowImg size = 96x96
                WindowImg.image = WindowPic
                # Display Current Time
                QTime = "Select hour(curtime()),minute(curtime())"
                cursorT = con.cursor()
                cursorT.execute(QTime)
                dataT = cursorT.fetchall()
                for i in dataT:
                    hCurTime = i[0]
                    mCurTime = i[1]
                TimeVal1 = str(hCurTime) + ":" + str(mCurTime)
                timeLabel = Label(window10, text=TimeVal1, font=('arial black', 14, 'bold'), bg='#a6a8a5',
                                  pady=0)  # font size =15 for my big screen
                timeLabel.place(x=48, y=72)  # y=85 for my big screen

                # Withdraw Amount label
                Withdraw_Amt = Label(window10,
                                     text=" Withdraw Amount : ",
                                     font=("ariel", 15, "bold"))
                Withdraw_Amt.place(x=43, y=235)
                # Withdraw amt display label
                WithdrawAmt_box10 = Entry(window10,
                                          font=("ariel", 15),
                                          width=19)
                WithdrawAmt_box10.place(x=240, y=235)

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
                            Invalid_Label.place(x=45, y=350)

                        else:
                            q = "update bdetails set balance=balance-{} where username='{}' and balance >= '{}'".format(
                                w10, U3, w10)
                            cursor10 = con.cursor()
                            cursor10.execute(q)
                            con.commit()
                            window10.destroy()
                    else:
                        Invalid_Label = Label(window10,
                                              text="Invalid Input!                        ",
                                              fg="red",
                                              font=("ariel", 15, "bold"))
                        Invalid_Label.place(x=45, y=350)

                submit10 = Button(window10,
                                  text="WITHDRAW & EXIT",
                                  font=("ariel", 15, "bold"),
                                  bg="light grey",
                                  padx=10,
                                  command=WithdrawFunc)
                submit10.place(x=137, y=300)

            # Button Code
            WithdrawAmtButton = Button(window4,
                                       text="WITHDRAW MONEY",
                                       font=("Arial", 12, "bold"),
                                       bg="light grey",
                                       padx=10,
                                       command=Window10_Function)
            WithdrawAmtButton.place(x=150, y=510)

            ##(Window11)Loan Details Window
            def Window11_Function():
                window11 = Toplevel()
                window11.geometry("495x800+0+0")
                window11.title("Loan Details")
                window4.destroy()
                BackgroundImg = Label(window11, image=BG)
                BackgroundImg.place(x=0, y=0)
                BackgroundImg.image = BG
                WindowPic = PhotoImage(file="LoanDetailsPic.png")
                WindowImg = Label(window11, image=WindowPic)
                WindowImg.place(x=200, y=120)  ######WindowImg size = 96x96
                WindowImg.image = WindowPic
                # Display Current Time
                QTime = "Select hour(curtime()),minute(curtime())"
                cursorT = con.cursor()
                cursorT.execute(QTime)
                dataT = cursorT.fetchall()
                for i in dataT:
                    hCurTime = i[0]
                    mCurTime = i[1]
                TimeVal1 = str(hCurTime) + ":" + str(mCurTime)
                timeLabel = Label(window11, text=TimeVal1, font=('arial black', 14, 'bold'), bg='#a6a8a5',
                                  pady=0)  # font size =15 for my big screen
                timeLabel.place(x=48, y=72)  # y=85 for my big screen

                # h_principal label
                H_LoanTakenLabel11 = Label(window11,
                                           text=" HOME LOAN             : ",
                                           font=("ariel", 15, "bold"))
                H_LoanTakenLabel11.place(x=43, y=235)
                # c_principal label
                C_LoanTakenLabel11 = Label(window11,
                                           text=" CAR LOAN                : ",
                                           font=("ariel", 15, "bold"))
                C_LoanTakenLabel11.place(x=43, y=265)
                # p_principal label
                P_LoanTakenLabel11 = Label(window11,
                                           text=" PERSONAL LOAN     : ",
                                           font=("ariel", 15, "bold"))
                P_LoanTakenLabel11.place(x=43, y=295)

                # Labels to Display values from SQL
                cursor = con.cursor()

                # home loan function
                def HomeLoanDetails():
                    window12 = Toplevel()
                    window12.title("Home Loan Details")
                    window12.geometry("495x800+0+0")
                    window11.destroy()
                    BackgroundImg = Label(window12, image=BG)
                    BackgroundImg.place(x=0, y=0)
                    BackgroundImg.image = BG
                    WindowPic = PhotoImage(file="HomePic.png")
                    WindowImg = Label(window12, image=WindowPic)
                    WindowImg.place(x=200, y=120)  ######WindowImg size = 96x96
                    WindowImg.image = WindowPic
                    # Display Current Time
                    QTime = "Select hour(curtime()),minute(curtime())"
                    cursorT = con.cursor()
                    cursorT.execute(QTime)
                    dataT = cursorT.fetchall()
                    for i in dataT:
                        hCurTime = i[0]
                        mCurTime = i[1]
                    TimeVal1 = str(hCurTime) + ":" + str(mCurTime)
                    timeLabel = Label(window12, text=TimeVal1, font=('arial black', 14, 'bold'), bg='#a6a8a5',
                                      pady=0)  # font size =15 for my big screen
                    timeLabel.place(x=48, y=72)  # y=85 for my big screen

                    # Labels
                    PLabel12 = Label(window12, text='LOAN TAKEN               :   ₹', font=("ariel", 15, "bold"))
                    PLabel12.place(x=45, y=235)

                    RLabel12 = Label(window12, text='INTEREST RATE          :', font=("ariel", 15, "bold"))
                    RLabel12.place(x=44, y=265)

                    TLabel2 = Label(window12, text='TIME IN YEAR              :', font=("ariel", 15, "bold"))
                    TLabel2.place(x=43, y=295)

                    SdLabel12 = Label(window12, text='START DATE               :', font=("ariel", 15, "bold"))
                    SdLabel12.place(x=44, y=325)

                    EdLabel12 = Label(window12, text='END DATE                   :', font=("ariel", 15, "bold"))
                    EdLabel12.place(x=44, y=355)

                    # GETTING VALUES FROM SQL
                    q1 = "select H_principal,H_rate,H_time,h_date from bdetails where username='{}'".format(U3)
                    cursor.execute(q1)
                    data1 = cursor.fetchall()
                    for i in data1:
                        p, r, t, sd = i[0], i[1], i[2], i[3]

                    q2 = "select date_add(h_date,interval '{}' year) from bdetails where username = '{}'".format(t, U3)
                    cursor.execute(q2)
                    data2 = cursor.fetchall()
                    for i in data2:
                        ed = i[0]
                    print(p, r, t, sd, ed)

                    # Labels
                    PvalLabel12 = Label(window12, text=str(p), font=("ariel", 15, "bold"))
                    PvalLabel12.place(x=303, y=235)

                    RvalLabel12 = Label(window12, text=str(r), font=("ariel", 15, "bold"))
                    RvalLabel12.place(x=285, y=265)

                    TvalLabel12 = Label(window12, text=str(t), font=("ariel", 15, "bold"))
                    TvalLabel12.place(x=285, y=295)

                    SDvalLabel12 = Label(window12, text=str(sd), font=("ariel", 15, "bold"))
                    SDvalLabel12.place(x=285, y=325)

                    EDvalLabel12 = Label(window12, text=str(ed), font=("ariel", 15, "bold"))
                    EDvalLabel12.place(x=285, y=355)

                    ##Output
                    # MonthlyPay Label
                    tpaymentLabel = Label(window12, text='TOTAL AMOUNT       :', font=("ariel", 15, "bold"))#THIS WAS AMOUNT TO BE PAID
                    tpaymentLabel.place(x=45, y=385)
                    mpaymentLabel = Label(window12, text='MONTHLY PAYMENT  :', font=("ariel", 15, "bold"))
                    mpaymentLabel.place(x=45, y=415)
                    # MPVal Label
                    if p!=None and r!=None and t!=None:                        
                        Output1 = StringVar()
                        Output2 = StringVar()
                        p = float(p)
                        r = float(r)
                        t = float(t)
                        total = p * ((1 + (r / 100)) ** t)
                        mtotal = total / (t * 12)
                        qhtotal = "update bdetails set h_total = {} where username = '{}'".format(total,U3)
                        '''qhtc = "select h_totcalc from bdetails where username = '{}'".format(U3)
                        cursor.execute(qhtc)                        
                        datahtc = cursor.fetchall()
                        for i in datahtc:
                            hhtc = i[0]
                        vcheck = hhtc
                        if vcheck==None: #or int(vcheck)<0
                            qhtotcalc = "update bdetails set h_totcalc = {} where username = '{}'".format(total,U3)
                            cursor.execute(qhtotcalc)
                            con.commit()'''                            
                            # output
                        Output1.set("₹ " + str(round(total, 2)))
                        label1 = Label(window12, textvariable=Output1, font=("ariel", 15, "bold"))
                        label1.place(x=285, y=385)
                        Output2.set("₹ " + str(round(mtotal, 2)))
                        label2 = Label(window12, textvariable=Output2, font=("ariel", 15, "bold"))
                        label2.place(x=285, y=415)
                                                    
                        '''else:                                              
                            # output
                            Output1.set("₹ " + str(round(hhtc, 2)))
                            label1 = Label(window12, textvariable=Output1, font=("ariel", 15, "bold"))
                            label1.place(x=285, y=385)
                            Output2.set("₹ " + str(round(mtotal, 2)))
                            label2 = Label(window12, textvariable=Output2, font=("ariel", 15, "bold"))
                            label2.place(x=285, y=415)'''
                                            
                    # Close Window Button
                    def closewindow12():
                        window12.destroy()

                    closeButton = Button(window12, text="Close", font=("ariel", 15, "bold"), padx=120, bg='light grey',
                                         command=closewindow12)
                    closeButton.place(x=89, y=510)

                    '''##pay loan
                    def HLoanPay():
                        qHPay = "select Balance,h_total,h_totcalc,h_time from bdetails where username='{}'".format(U3)
                        cursor.execute(qHPay)
                        data = cursor.fetchall()
                        for i in data:
                            bal,ht,htc,hti = i[0],i[1],i[2],i[3]
                        mtotal=int(float(ht)/(int(hti)*12))
                        print(bal,mtotal)    
                        DecBal = float(bal) - float(mtotal)
                        DecBal=int(DecBal)
                        DecLoan = float(htc) - float(mtotal)
                        DecLoan = int(DecLoan)
                        print(bal,ht,htc,hti,mtotal,DecBal,DecLoan)
                        qNewDetails1 = "update bdetails set balance={} where username='{}'".format(DecBal,U3)
                        qNewDetails2="update bdetails set h_totcalc = {} where username='{}'".format(DecLoan,U3)
                        cursor.execute(qNewDetails1)
                        cursor.execute(qNewDetails2)
                        con.commit()
                        window12.destroy()

                    HPay = Button(window12, text='Pay Monthly Installment', font=("ariel", 15, "bold"), bg='light grey',
                                  command=HLoanPay)
                    HPay.place(x=90, y=450)'''

                # Home Loan Button
                HomeLoanButton11 = Button(window11,
                                          text="HOME LOAN DETAILS",
                                          font=("Arial", 12, "bold"),
                                          bg="light grey",
                                          padx=30,
                                          command=HomeLoanDetails)
                HomeLoanButton11.place(x=125, y=380)

                # car loan function
                def CarLoanDetails():
                    window13 = Toplevel()
                    window13.title("Car Loan Details")
                    window13.geometry("495x800+0+0")
                    window11.destroy()
                    BackgroundImg = Label(window13, image=BG)
                    BackgroundImg.place(x=0, y=0)
                    BackgroundImg.image = BG
                    WindowPic = PhotoImage(file="CarPic.png")
                    WindowImg = Label(window13, image=WindowPic)
                    WindowImg.place(x=182, y=115)  ######WindowImg size = 96x96
                    WindowImg.image = WindowPic
                    # Display Current Time
                    QTime = "Select hour(curtime()),minute(curtime())"
                    cursorT = con.cursor()
                    cursorT.execute(QTime)
                    dataT = cursorT.fetchall()
                    for i in dataT:
                        hCurTime = i[0]
                        mCurTime = i[1]
                    TimeVal1 = str(hCurTime) + ":" + str(mCurTime)
                    timeLabel = Label(window13, text=TimeVal1, font=('arial black', 14, 'bold'), bg='#a6a8a5',
                                      pady=0)  # font size =15 for my big screen
                    timeLabel.place(x=48, y=72)  # y=85 for my big screen

                    # Labels
                    PLabel13 = Label(window13, text='LOAN TAKEN               :   ₹', font=("ariel", 15, "bold"))
                    PLabel13.place(x=45, y=235)

                    RLabel13 = Label(window13, text='INTEREST RATE          :', font=("ariel", 15, "bold"))
                    RLabel13.place(x=44, y=265)

                    TLabel2 = Label(window13, text='TIME IN YEAR              :', font=("ariel", 15, "bold"))
                    TLabel2.place(x=43, y=295)

                    SdLabel13 = Label(window13, text='START DATE               :', font=("ariel", 15, "bold"))
                    SdLabel13.place(x=44, y=325)

                    EdLabel13 = Label(window13, text='END DATE                   :', font=("ariel", 15, "bold"))
                    EdLabel13.place(x=44, y=355)

                    # GETTING VALUES FROM SQL
                    q1 = "select c_principal,c_rate,c_time,c_date from bdetails where username='{}'".format(U3)
                    cursor.execute(q1)
                    data1 = cursor.fetchall()
                    for i in data1:
                        p, r, t, sd = i[0], i[1], i[2], i[3]

                    q2 = "select date_add(c_date,interval '{}' year) from bdetails where username = '{}'".format(t, U3)
                    cursor.execute(q2)
                    data2 = cursor.fetchall()
                    for i in data2:
                        ed = i[0]
                    print(p, r, t, sd, ed)

                    # Labels
                    PvalLabel13 = Label(window13, text=str(p), font=("ariel", 15, "bold"))
                    PvalLabel13.place(x=303, y=235)

                    RvalLabel13 = Label(window13, text=str(r), font=("ariel", 15, "bold"))
                    RvalLabel13.place(x=285, y=265)

                    TvalLabel13 = Label(window13, text=str(t), font=("ariel", 15, "bold"))
                    TvalLabel13.place(x=285, y=295)

                    SDvalLabel13 = Label(window13, text=str(sd), font=("ariel", 15, "bold"))
                    SDvalLabel13.place(x=285, y=325)

                    EDvalLabel13 = Label(window13, text=str(ed), font=("ariel", 15, "bold"))
                    EDvalLabel13.place(x=285, y=355)

                    ##Output
                    # MonthlyPay Label
                    tpaymentLabel = Label(window13, text='TOTAL AMOUNT         :', font=("ariel", 15, "bold"))
                    tpaymentLabel.place(x=45, y=385)
                    mpaymentLabel = Label(window13, text='MONTHLY PAYMENT  :', font=("ariel", 15, "bold"))
                    mpaymentLabel.place(x=45, y=415)
                    # MPVal Label
                    if p!=None and r!=None and t!=None:                        
                        Output1 = StringVar()
                        Output2 = StringVar()
                        p = float(p)
                        r = float(r)
                        t = float(t)
                        total = p * ((1 + (r / 100)) ** t)
                        mtotal = total / (t * 13)
                        # output
                        Output1.set("₹ " + str(round(total, 2)))
                        label1 = Label(window13, textvariable=Output1, font=("ariel", 15, "bold"))
                        label1.place(x=285, y=385)
                        Output2.set("₹ " + str(round(mtotal, 2)))
                        label2 = Label(window13, textvariable=Output2, font=("ariel", 15, "bold"))
                        label2.place(x=285, y=415)

                    # Close Window Button
                    def closewindow13():
                        window13.destroy()

                    closeButton = Button(window13, text="Close", font=("ariel", 15, "bold"), padx=120, bg='light grey',
                                         command=closewindow13)
                    closeButton.place(x=89, y=510)

                ##Car Loan Button
                CarLoanButton11 = Button(window11,
                                         text="CAR LOAN DETAILS",
                                         font=("Arial", 12, "bold"),
                                         bg="light grey",
                                         padx=36,
                                         command=CarLoanDetails)
                CarLoanButton11.place(x=125, y=450)

                # personal loan function
                def PersonalLoanDetails():
                    window14 = Toplevel()
                    window14.title("Personal Loan Details")
                    window14.geometry("495x800+0+0")
                    window11.destroy()
                    BackgroundImg = Label(window14, image=BG)
                    BackgroundImg.place(x=0, y=0)
                    BackgroundImg.image = BG
                    WindowPic = PhotoImage(file="PersonalLoanPic.png")
                    WindowImg = Label(window14, image=WindowPic)
                    WindowImg.place(x=200, y=120)  ######WindowImg size = 96x96
                    WindowImg.image = WindowPic
                    # Display Current Time
                    QTime = "Select hour(curtime()),minute(curtime())"
                    cursorT = con.cursor()
                    cursorT.execute(QTime)
                    dataT = cursorT.fetchall()
                    for i in dataT:
                        hCurTime = i[0]
                        mCurTime = i[1]
                    TimeVal1 = str(hCurTime) + ":" + str(mCurTime)
                    timeLabel = Label(window14, text=TimeVal1, font=('arial black', 14, 'bold'), bg='#a6a8a5',
                                      pady=0)  # font size =15 for my big screen
                    timeLabel.place(x=48, y=72)  # y=85 for my big screen

                    # Labels
                    PLabel14 = Label(window14, text='LOAN TAKEN               :   ₹', font=("ariel", 15, "bold"))
                    PLabel14.place(x=45, y=235)

                    RLabel14 = Label(window14, text='INTEREST RATE          :', font=("ariel", 15, "bold"))
                    RLabel14.place(x=44, y=265)

                    TLabel2 = Label(window14, text='TIME IN YEAR              :', font=("ariel", 15, "bold"))
                    TLabel2.place(x=43, y=295)

                    SdLabel14 = Label(window14, text='START DATE               :', font=("ariel", 15, "bold"))
                    SdLabel14.place(x=44, y=325)

                    EdLabel14 = Label(window14, text='END DATE                   :', font=("ariel", 15, "bold"))
                    EdLabel14.place(x=44, y=355)

                    # GETTING VALUES FROM SQL
                    q1 = "select p_principal,p_rate,p_time,p_date from bdetails where username='{}'".format(U3)
                    cursor.execute(q1)
                    data1 = cursor.fetchall()
                    for i in data1:
                        p, r, t, sd = i[0], i[1], i[2], i[3]

                    q2 = "select date_add(p_date,interval '{}' year) from bdetails where username = '{}'".format(t, U3)
                    cursor.execute(q2)
                    data2 = cursor.fetchall()
                    for i in data2:
                        ed = i[0]
                    print(p, r, t, sd, ed)

                    # Labels
                    PvalLabel14 = Label(window14, text=str(p), font=("ariel", 15, "bold"))
                    PvalLabel14.place(x=303, y=235)

                    RvalLabel14 = Label(window14, text=str(r), font=("ariel", 15, "bold"))
                    RvalLabel14.place(x=285, y=265)

                    TvalLabel14 = Label(window14, text=str(t), font=("ariel", 15, "bold"))
                    TvalLabel14.place(x=285, y=295)

                    SDvalLabel14 = Label(window14, text=str(sd), font=("ariel", 15, "bold"))
                    SDvalLabel14.place(x=285, y=325)

                    EDvalLabel14 = Label(window14, text=str(ed), font=("ariel", 15, "bold"))
                    EDvalLabel14.place(x=285, y=355)

                    ##Output
                    # MonthlyPay Label
                    tpaymentLabel = Label(window14, text='TOTAL AMOUNT         :', font=("ariel", 15, "bold"))
                    tpaymentLabel.place(x=45, y=385)
                    mpaymentLabel = Label(window14, text='MONTHLY PAYMENT  :', font=("ariel", 15, "bold"))
                    mpaymentLabel.place(x=45, y=415)
                    # MPVal Label
                    if p!=None and r!=None and t!=None:                        
                        Output1 = StringVar()
                        Output2 = StringVar()
                        p = float(p)
                        r = float(r)
                        t = float(t)
                        total = p * ((1 + (r / 100)) ** t)
                        mtotal = total / (t * 12)
                        # output
                        Output1.set("₹ " + str(round(total, 2)))
                        label1 = Label(window14, textvariable=Output1, font=("ariel", 15, "bold"))
                        label1.place(x=285, y=385)
                        Output2.set("₹ " + str(round(mtotal, 2)))
                        label2 = Label(window14, textvariable=Output2, font=("ariel", 15, "bold"))
                        label2.place(x=285, y=415)

                    # Close Window Button
                    def closewindow14():
                        window14.destroy()

                    closeButton = Button(window14, text="Close", font=("ariel", 15, "bold"), padx=120, bg='light grey',
                                         command=closewindow14)
                    closeButton.place(x=89, y=510)

                ##Personal Loan Button
                PersonalLoanButton11 = Button(window11,
                                              text="PERSONAL LOAN DETAILS",
                                              font=("Arial", 12, "bold"),
                                              bg="light grey",
                                              padx=10,
                                              command=PersonalLoanDetails)
                PersonalLoanButton11.place(x=125, y=525)

                # window11 details from SQL
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

                    h_principalVal11.place(x=290, y=235)

                    # c_principalValue label

                    c_principalVal11 = Label(window11,
                                             text=f,
                                             font=("ariel", 15, "bold"))
                    c_principalVal11.place(x=290, y=265)

                    # p_principalValue label

                    p_principalVal11 = Label(window11,
                                             text=g,
                                             font=("ariel", 15, "bold"))
                    p_principalVal11.place(x=290, y=295)

            # Button Code
            LoanDetailsButton = Button(window4,
                                       text="LOAN DETAILS",
                                       font=("Arial", 12, "bold"),
                                       bg="light grey",
                                       padx=28,
                                       command=Window11_Function)
            LoanDetailsButton.place(x=150, y=355)

        ## Checking function
        def LogInCheck():
            u3 = uname_box3.get()
            p3 = passwd_box3.get()
            cursor3 = con.cursor()
            qry = ('select * from bdetails')
            cursor3.execute(qry)
            data = cursor3.fetchall()
            if data!=[]:
                for i in data:
                    if u3 == i[1] and p3 == i[2]:
                        Window4_Function()
                        break  
                    else:
                        Invalid_Label = Label(window3,
                                              text="Invalid Username / Password!",
                                              fg="red",
                                              font=("ariel", 15, "bold"))
                        Invalid_Label.place(x=45, y=350)
            else:
                Invalid_Label = Label(window3,
                                      text="Invalid Username / Password!",
                                      fg="red",
                                      font=("ariel", 15, "bold"))
                Invalid_Label.place(x=45, y=350)

        submit3 = Button(window3,
                         text="SUBMIT",
                         font=("ariel", 15, "bold"),
                         bg="light grey",
                         padx=10,
                         command=LogInCheck)
        submit3.place(x=185, y=300)

    # Window1 Buttons
    CreateAccButton = Button(window1,
                             text="Create Account",
                             font=("ariel", 15, "bold"),
                             bg="light gray",
                             command=Window2_Function)
    CreateAccButton.place(x=170, y=280)
    LogInButton = Button(window1,
                         text="Log In",
                         font=("ariel", 15, "bold"),
                         bg="light gray",
                         padx=45,
                         command=Window3_Function)
    LogInButton.place(x=170, y=360)

    window1.mainloop()


Window1_Function()

####Loan details None error
####Change PAY MONTHLY INSTALLMENT to small
