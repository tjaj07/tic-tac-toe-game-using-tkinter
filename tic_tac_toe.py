from tkinter import *

#main class
class tic:

    #variable used to enter alternate X and 0
    count = 0


    #function to enter value in the box which is clicked
    def clr(self,button,event = None):

        #to print alternate X and 0
        if self.count % 2 == 0:
            button["text"] = "0"
        else:
            button["text"] = "X"

        #incrementing value to count for alternate X and 0
        self.count = self.count + 1

    #function to restart the game
    def cls(self,event = None):

        #set count to 0 and all boxs emppty
        self.count = 0;
        self.button1["text"] = ""
        self.button2["text"] = ""
        self.button3["text"] = ""
        self.button4["text"] = ""
        self.button5["text"] = ""
        self.button6["text"] = ""
        self.button7["text"] = ""
        self.button8["text"] = ""
        self.button9["text"] = ""


    #main initilization function
    def __init__(self,root):

        #assiging size to the game
        root.geometry("176x288")

        #setting title to the game
        root.title("Game")

        #to be displayed on screen
        Label(root, text = "Tic Tac Toe Game").grid(row = 0 ,column = 4, columnspan = 4,pady = 10)

        #button to restart the game
        Button(root,text = "Restart",font = "Arial 10 bold" ,bg = "Red", fg = "black",height = 2,width = 6, border = 1,   command = self.cls).grid(row = 1,column = 6,pady = 10)

        #various boxes to fill them with values
        self.button1 = Button(root,text = "",font = "Arial 10 bold", bg = "black", fg = "white", height = 3,width = 6 ,command = lambda : self.clr(self.button1))
        self.button1.grid(row = 5, column = 5)
        self.button2 = Button(root,text = "",font = "Arial 10 bold", bg = "black", fg = "white", height = 3,width = 6 ,command = lambda : self.clr(self.button2))
        self.button2.grid(row = 5, column = 6)
        self.button3 = Button(root,text = "",font = "Arial 10 bold", bg = "black", fg = "white", height = 3,width = 6 ,command = lambda : self.clr(self.button3))
        self.button3.grid(row = 5, column = 7)
        self.button4 = Button(root,text = "",font = "Arial 10 bold", bg = "black", fg = "white", height = 3,width = 6 ,command = lambda : self.clr(self.button4))
        self.button4.grid(row = 6, column = 5)
        self.button5 = Button(root,text = "",font = "Arial 10 bold", bg = "black", fg = "white", height = 3,width = 6 ,command = lambda : self.clr(self.button5))
        self.button5.grid(row = 6, column = 6)
        self.button6 = Button(root,text = "",font = "Arial 10 bold", bg = "black", fg = "white", height = 3,width = 6 ,command = lambda : self.clr(self.button6))
        self.button6.grid(row = 6, column = 7)
        self.button7 = Button(root,text = "",font = "Arial 10 bold", bg = "black", fg = "white", height = 3,width = 6 ,command = lambda : self.clr(self.button7))
        self.button7.grid(row = 7, column = 5)
        self.button8 = Button(root,text = "",font = "Arial 10 bold", bg = "black", fg = "white", height = 3,width = 6 ,command = lambda : self.clr(self.button8))
        self.button8.grid(row = 7, column = 6)
        self.button9 = Button(root,text = "",font = "Arial 10 bold", bg = "black", fg = "white", height = 3,width = 6 ,command = lambda : self.clr(self.button9))
        self.button9.grid(row = 7, column = 7)


#main window
root = Tk()

#creating class object
tac = tic(root)

#tp continously display the game on the screen
root.mainloop()
