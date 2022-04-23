from tkinter import *
import tkinter.messagebox as msg



app = Tk()
app.title("Form")
#for set the size of window
app.geometry("600x400")
app.configure(bg ="#1D5C63" )

#resizable meqans your is not resized by your user it take two att first is width and height
app.resizable(False, False)

#make varibles for entry box

name_entry = StringVar()
age_entry = IntVar()

#deine button you have to define your btn logic here what will work after pressing your btn...
def submit():
    #.get fun use to retive our data from entry box
    name = name_entry.get()
    age = age_entry.get()
    #you can simply print your data in terminal with this line
    print(f"Your name is {name} and your age is {age}")

    #this is file for file saving method 
    with open('D:\\Python_DEV\\Advanced_python_harry\\1.txt', 'a') as f :
        f.write(f"Your name is {name}\n")
        f.write(f"your age is {age}\n")
        f.write("\n")
        msg.showinfo("Sucess", f"Your data has been Saved {name}")





#label for name 
#place is used to place our label with x and y coordinares 
name_lb = Label(app, text= "Name :", font= "Verdana 15 bold", bg= "#1D5C63", fg = "white" )
name_lb.place(x = 70, y = 60)

#entry box can help can to fill our response
#entry box take textvarible for store our data and retirve to btn 
name_entry_box = Entry(app, textvariable= name_entry, font= "Verdana 10 bold")
name_entry_box.place(x = 190, y = 64, width= 190, height= 25)


age_lb = Label(app, text= "Age :", font= "Verdana 15 bold", bg= "#1D5C63", fg = "white" )
age_lb.place(x = 70, y = 130)

age_entry_box = Entry(app, textvariable= age_entry, font= "Verdana 10 bold")
age_entry_box.place(x = 190, y = 130, width= 190, height= 27)


#you can define your btn and set command 
submit_btn = Button(app, text= "Submit", font= "verdana 10 bold", command= submit)
submit_btn.place(x = 250, y = 230)






app.mainloop()