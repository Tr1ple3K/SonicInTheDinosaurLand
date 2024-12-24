# #Pattanapong Chirabandhu 6310742132
# from tkinter import *
# import tkinter
# from PIL import Image, ImageTk

# #tkinter window settings
# root = Tk()
# root.geometry("1000x680") #window size
# root.configure(bg='white') #set background color
# root.title("Tempereture Converter") # Title of window

# image1 = Image.open("sf210/sonicgame/sonicLogo.png")
# test = ImageTk.PhotoImage(image1)
# label1 = tkinter.Label(image=test, bd=0)
# label1.image = test
# # Position image
# label1.pack(anchor='n', pady=(60, 0))

# def startGame():


# startButton = Button(root, text="Convert to °C", command=convertToCelsius,bd=0, bg="#B35340", fg="white", height=1, width=15,activebackground="#5072A7",activeforeground="white")
# startButton.pack(pady=(40, 0)) # set to middle padding from top 40 units

# #this is for running gui
# root.mainloop() 