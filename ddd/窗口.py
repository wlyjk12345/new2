from tkinter import *  #第一步是导入Tkinter包的所有内容：
import tkinter.messagebox as messagebox
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')      #标签
        self.helloLabel.pack()
        self.expression = Entry(self)             #单行文本框
        self.expression.pack()
        self.alertButton = Button(self, text='Evaluate it!', command=self.compute)        #按钮
        self.alertButton.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit )
        self.quitButton.pack()
        self.checkbutton = Checkbutton(self, )

    def compute(self):
        expression = self.expression.get() or '0'
        messagebox.showinfo('Result', '%s = %s' % (expression, eval(expression)))
app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()