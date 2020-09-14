from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import process
import api_interactions
import data_interactions

root = Tk()

root.title("5 Day Weather Forcast")
#add lightning icon


top_label = Label(root, text='5 day forcast')
top_label.grid(row=0, column=0)

def images(code):

    return ImageTk.PhotoImage(Image.open(f'icons/{code}.ico'))


notebook = ttk.Notebook(root)
notebook.grid(row=2, column=0)

w=400
h=400

frame1 = Frame(notebook, width=w, height=h)
frame2 = Frame(notebook, width=w, height=h)
frame3 = Frame(notebook, width=w, height=h)
frame4 = Frame(notebook, width=w, height=h)
frame5 = Frame(notebook, width=w, height=h)

frame1.grid(row=2, column=0)
frame2.grid(row=2, column=0)
frame3.grid(row=2, column=0)
frame4.grid(row=2, column=0)
frame5.grid(row=2, column=0)

notebook.add(frame1, text=process.tabs()[0])
notebook.add(frame2, text=process.tabs()[1])
notebook.add(frame3, text=process.tabs()[2])
notebook.add(frame4, text=process.tabs()[3])
notebook.add(frame5, text=process.tabs()[4])



def template(icon, temp, time, frame): 

    
    time_lab1 = Label(frame, text=time[0])
    time_lab2 = Label(frame, text=time[1])
    time_lab3 = Label(frame, text=time[2])
    time_lab4 = Label(frame, text=time[3])
    time_lab5 = Label(frame, text=time[4])
    time_lab6 = Label(frame, text=time[5])
    time_lab7 = Label(frame, text=time[6])
    time_lab8 = Label(frame, text=time[7])
    
    temp_lab1 = Label(frame, text=temp[0])
    temp_lab2 = Label(frame, text=temp[1])
    temp_lab3 = Label(frame, text=temp[2])
    temp_lab4 = Label(frame, text=temp[3])
    temp_lab5 = Label(frame, text=temp[4])
    temp_lab6 = Label(frame, text=temp[5])
    temp_lab7 = Label(frame, text=temp[6])
    temp_lab8 = Label(frame, text=temp[7])
        
    weath_lab1 = Label(frame, image=icon[0])
    weath_lab2 = Label(frame, image=icon[1])
    weath_lab3 = Label(frame, image=icon[2])
    weath_lab4 = Label(frame, image=icon[3])
    weath_lab5 = Label(frame, image=icon[4])
    weath_lab6 = Label(frame, image=icon[5])
    weath_lab7 = Label(frame, image=icon[6])
    weath_lab8 = Label(frame, image=icon[7])
    # Refrence to image in Tkinter object.
    weath_lab1.image = icon[0]
    weath_lab2.image = icon[1]
    weath_lab3.image = icon[2]
    weath_lab4.image = icon[3]
    weath_lab5.image = icon[4]
    weath_lab6.image = icon[5]
    weath_lab7.image = icon[6]
    weath_lab8.image = icon[7]

    time_lab1.grid(row=0, column=0)
    time_lab2.grid(row=0, column=1)
    time_lab3.grid(row=0, column=2)
    time_lab4.grid(row=0, column=3)
    time_lab5.grid(row=0, column=4)
    time_lab6.grid(row=0, column=5)
    time_lab7.grid(row=0, column=6)
    time_lab8.grid(row=0, column=7)
    
    weath_lab1.grid(row=1, column=0)
    weath_lab2.grid(row=1, column=1)
    weath_lab3.grid(row=1, column=2)
    weath_lab4.grid(row=1, column=3)
    weath_lab5.grid(row=1, column=4)
    weath_lab6.grid(row=1, column=5)
    weath_lab7.grid(row=1, column=6)
    weath_lab8.grid(row=1, column=7)
    
    temp_lab1.grid(row=2, column=0)
    temp_lab2.grid(row=2, column=1)
    temp_lab3.grid(row=2, column=2)
    temp_lab4.grid(row=2, column=3)
    temp_lab5.grid(row=2, column=4)
    temp_lab6.grid(row=2, column=5)
    temp_lab7.grid(row=2, column=6)
    temp_lab8.grid(row=2, column=7)
    

def day1(data, timeslots):
    
    time = timeslots[8-len(data[1]):]
    day1_time = Label(frame1, text=process.time_intervals(len(data[1])))
    img_lst = [images(data[2][i]) for i in range(len(data[1]))]
    temp_list = data[1]
    
    try:
        time_lab1 = Label(frame1, text=time[0])      
        time_lab2 = Label(frame1, text=time[1])    
        time_lab3 = Label(frame1, text=time[2])                  
        time_lab4 = Label(frame1, text=time[3])
        time_lab5 = Label(frame1, text=time[4])
        time_lab6 = Label(frame1, text=time[5])
        time_lab7 = Label(frame1, text=time[6])       
        time_lab8 = Label(frame1, text=time[7])
    except:
        pass
    
    try:
        weath_lab1 = Label(frame1, image=img_lst[0])
        weath_lab2 = Label(frame1, image=img_lst[1])
        weath_lab3 = Label(frame1, image=img_lst[2])
        weath_lab4 = Label(frame1, image=img_lst[3])
        weath_lab5 = Label(frame1, image=img_lst[4])
        weath_lab6 = Label(frame1, image=img_lst[5])
        weath_lab7 = Label(frame1, image=img_lst[6])
        weath_lab8 = Label(frame1, image=img_lst[7])
    except:
        pass
    
    try:
        # Refrence to image in Tkinter object.
        weath_lab1.image = img_lst[0]
        weath_lab2.image = img_lst[1]
        weath_lab3.image = img_lst[2]
        weath_lab4.image = img_lst[3]
        weath_lab5.image = img_lst[4]
        weath_lab6.image = img_lst[5]
        weath_lab7.image = img_lst[6]
        weath_lab8.image = img_lst[7]
    except:
        pass
    
    try:
        temp_lab1 = Label(frame1, text=temp_list[0])
        temp_lab2 = Label(frame1, text=temp_list[1])
        temp_lab3 = Label(frame1, text=temp_list[2])
        temp_lab4 = Label(frame1, text=temp_list[3])
        temp_lab5 = Label(frame1, text=temp_list[4])
        temp_lab6 = Label(frame1, text=temp_list[5])
        temp_lab7 = Label(frame1, text=temp_list[6])
        temp_lab8 = Label(frame1, text=temp_list[7])
    except:
        pass

    try:
        time_lab1.grid(row=0, column=0)
        time_lab2.grid(row=0, column=1)
        time_lab3.grid(row=0, column=2)
        time_lab4.grid(row=0, column=3)
        time_lab5.grid(row=0, column=4)
        time_lab6.grid(row=0, column=5)
        time_lab7.grid(row=0, column=6)        
        time_lab8.grid(row=0, column=7)        
    except:
        pass
    
    try:    
        weath_lab1.grid(row=1, column=0)
        weath_lab2.grid(row=1, column=1)
        weath_lab3.grid(row=1, column=2)
        weath_lab4.grid(row=1, column=3)
        weath_lab5.grid(row=1, column=4)
        weath_lab6.grid(row=1, column=5)
        weath_lab7.grid(row=1, column=6)
        weath_lab8.grid(row=1, column=7) 
    except:
        pass
    
    try:   
        temp_lab1.grid(row=2, column=0)
        temp_lab2.grid(row=2, column=1)
        temp_lab3.grid(row=2, column=2)
        temp_lab4.grid(row=2, column=3)
        temp_lab5.grid(row=2, column=4)
        temp_lab6.grid(row=2, column=5)
        temp_lab7.grid(row=2, column=6)
        temp_lab8.grid(row=2, column=7)
    except:
        pass
    

def click():

    
    timeslots = 8
    
    time = process.time_intervals(timeslots)
    data = api_interactions.api_data(user_input.get()) 



    day5_image = [images(data[14][i]) for i in range(timeslots)] 
    day5_temp = data[13]
    day4_image = [images(data[11][i]) for i in range(timeslots)]
    day4_temp = data[10]
    day3_image = [images(data[8][i]) for i in range(timeslots)]
    day3_temp = data[7]
    day2_image = [images(data[5][i]) for i in range(timeslots)]
    day2_temp = data[4]
    
    template(day5_image, day5_temp, time, frame5)
    template(day4_image, day4_temp, time, frame4)
    template(day3_image, day3_temp, time, frame3)
    template(day2_image, day2_temp, time, frame2)

    day1(data, time)    

user_input = Entry(root, width=60)
user_input.grid(row=1, column=0)

search = Button(root, text='search', command=click)
search.grid(row=1, column=1)

root.mainloop()

