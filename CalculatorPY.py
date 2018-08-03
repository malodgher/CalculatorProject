import tkinter

class Calculator:
    # Button action when operator or number button is pressed
    def numAndOpButton(self, opChar):
        expr = self.numInput.get()

        if(len(expr) != 0):
            if((opChar == "+") or (opChar == "-") or (opChar == "*") or (opChar == "/")):
                if((expr[len(expr) - 1] == "+") or (expr[len(expr) - 1] == "-") or (expr[len(expr) - 1] == "*") or (expr[len(expr) - 1] == "/")):
                    return None
                else:
                    self.numInput.insert("end", opChar)
            else:
                self.numInput.insert("end", opChar)
        else:
            self.numInput.insert("end", opChar)

    def backspace(self):
        if(len(self.numInput.get()) != 0):
            self.numInput.delete(len(self.numInput.get()) - 1, "end")

    def clearCalc(self):
        self.numInput.delete(0, "end")
        # self.answerLabel['text'] = ""
        self.answerLabel['textvariable'] = tkinter.StringVar(value="")

    def equalButton(self):
        try:
            eval(self.numInput.get())
        except:
            self.clearCalc()
            self.answerLabel['textvariable'] = tkinter.StringVar(value="Invalid Input")
            return None

        self.ans = eval(self.numInput.get())
        if(type(self.ans) == float and (self.ans).is_integer()):
            self.ans = int(self.ans)

        # self.answerLabel['text'] = str(self.ans)
        self.numInput.delete(0, "end")

        if(len(str(self.ans)) > 21):
            self.answerLabel['textvariable'] = tkinter.StringVar(value= ("%.14e" % self.ans))
        else:
            self.answerLabel['textvariable'] = tkinter.StringVar(value=(self.ans))

    def enterAns(self):
        try:
            self.numInput.insert("end", self.ans)
        except:
            return None

    # Main initializer
    def __init__(self, master):
        #Initializing window dimensions
        master.title('Calculator')
        master.minsize(width=320, height=480)
        master.maxsize(width=320, height=480)

        #Initializing input box and answer box
        self.numInput = tkinter.Entry(master, font = "Calibri 21", justify="right", relief="sunken")
        self.numInput.place(x=10, y=20, width=300, height=50)

        self.answerLabel = tkinter.Entry(master, font="Calibri 21", justify="right", relief="sunken", state="readonly")
        self.answerLabel.place(x=10, y=80, width=300, height=50)
        #self.answerLabel = tkinter.Label(master, font="Calibri 21", anchor="e", relief="sunken")

        #Scroll setup
        scrollbar = tkinter.Scrollbar(orient="horizontal")
        self.numInput['xscrollcommand'] = scrollbar.set
        scrollbar.place(x=0, y=0, width=320)
        scrollbar.config(command=self.numInput.xview)

        ansScroll = tkinter.Scrollbar(orient="horizontal")
        self.answerLabel['xscrollcommand'] = ansScroll.set
        ansScroll.place(x=0, y=130, width=320)
        ansScroll.config(command=self.answerLabel.xview)

        self.ans = None

        #Initializing Buttons
        tkinter.Button(master, text=".", font="Calibri 20", command=lambda:self.numAndOpButton('.')).place(x=65, y=400, width=50, height=50)

        tkinter.Button(master, text="+", font="Calibri 20", command=lambda:self.numAndOpButton('+')).place(x=260, y=180, width=50, height=50)
        tkinter.Button(master, text="-", font="Calibri 20", command=lambda:self.numAndOpButton('-')).place(x=260, y=235, width=50, height=50)
        tkinter.Button(master, text="x", font="Calibri 20", command=lambda:self.numAndOpButton('*')).place(x=260, y=290, width=50, height=50)
        tkinter.Button(master, text="÷", font="Calibri 20", command=lambda:self.numAndOpButton('/')).place(x=260, y=345, width=50, height=50)
        tkinter.Button(master, text="(", font="Calibri 20", command=lambda:self.numAndOpButton('(')).place(x=190, y=180, width=50, height=50)
        tkinter.Button(master, text=")", font="Calibri 20", command=lambda:self.numAndOpButton(')')).place(x=190, y=235, width=50, height=50)
        tkinter.Button(master, text="%", font="Calibri 20", command=lambda:self.numAndOpButton('%')).place(x=190, y=290, width=50, height=50)
        #tkinter.Button(master, text="^", font="Calibri 20", command=lambda:self.numAndOpButton('^')).place(x=190, y=345, width=50, height=50)

        tkinter.Button(master, text="=", font="Calibri 20", command=lambda:self.equalButton()).place(x=260, y=400, width=50, height=50)

        tkinter.Button(master, text="<-", font="Calibri 20", command=lambda:self.backspace()).place(x=120, y=180, width=50, height=50)
        tkinter.Button(master, text="CLR", font="Calibri 18", command=lambda:self.clearCalc()).place(x=65, y=180, width=50, height=50)
        tkinter.Button(master, text="ANS", font="Calibri 18", command=lambda:self.enterAns()).place(x=10, y=180, width=50, height=50)

        tkinter.Button(master, text="0", font="Calibri 20", command=lambda:self.numAndOpButton('0')).place(x=10, y=400, width=50, height=50)
        tkinter.Button(master, text="1", font="Calibri 20", command=lambda:self.numAndOpButton('1')).place(x=10, y=345, width=50, height=50)
        tkinter.Button(master, text="2", font="Calibri 20", command=lambda:self.numAndOpButton('2')).place(x=65, y=345, width=50, height=50)
        tkinter.Button(master, text="3", font="Calibri 20", command=lambda:self.numAndOpButton('3')).place(x=120, y=345, width=50, height=50)
        tkinter.Button(master, text="4", font="Calibri 20", command=lambda:self.numAndOpButton('4')).place(x=10, y=290, width=50, height=50)
        tkinter.Button(master, text="5", font="Calibri 20", command=lambda:self.numAndOpButton('5')).place(x=65, y=290, width=50, height=50)
        tkinter.Button(master, text="6", font="Calibri 20", command=lambda:self.numAndOpButton('6')).place(x=120, y=290, width=50, height=50)
        tkinter.Button(master, text="7", font="Calibri 20", command=lambda:self.numAndOpButton('7')).place(x=10, y=235, width=50, height=50)
        tkinter.Button(master, text="8", font="Calibri 20", command=lambda:self.numAndOpButton('8')).place(x=65, y=235, width=50, height=50)
        tkinter.Button(master, text="9", font="Calibri 20", command=lambda:self.numAndOpButton('9')).place(x=120, y=235, width=50, height=50)


root = tkinter.Tk()
cal = Calculator(root)
root.mainloop()

# Division character if you need it:  ÷