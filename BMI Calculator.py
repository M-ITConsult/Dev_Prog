import customtkinter
from tkinter import *
from tkinter import messagebox

app = customtkinter.CTk()
# App window dimension
app.geometry('300x500')
# App title
app.title('BMI_Calculator')
# App background color
app.config(bg='#020414')
# App icon
# image_icon=PhotoImage(file='')
# app.iconphoto(False,image_icon)


# Label title
top = Label(app,text='BMI CALCULATOR',font=('Arial',18,'bold'),fg='#FFFFFF',bg='#181935',width=28,height=1)
top.pack()

# Label for Height
height_label = Label(app,font=('Arial',18,'bold'),fg='#FFFFFF',bg='#181935',width=17,height=4)
height_label.place(x=20,y=60)

# Text for Height
height_text_label = Label(app,text='HEIGHT CM',font=('Arial',18,'bold'),fg='#FFFFFF',bg='#181935',width=10,height=1)
height_text_label.place(x=76,y=60)

# Label for Weight
weight_label = Label(app,font=('Arial',18,'bold'),fg='#FFFFFF',bg='#181935',width=17,height=4)
weight_label.place(x=20,y=210)

# Text for Weight
weight_text_label = Label(app,text='WEIGHT KG',font=('Arial',18,'bold'),fg='#FFFFFF',bg='#181935',width=10,height=1)
weight_text_label.place(x=75,y=220)

# Values Height, Weight
height = StringVar()
weight = StringVar()

height_value = IntVar()
weight_value = IntVar()

txt = StringVar()

# Definition to get height value
def get_height_value():
    return height_value.get()

def slider1(event):
    return height.set(get_height_value())
    
# Definition to get weight value
def get_weight_value():
    return weight_value.get()

def slider2(event):
    return weight.set(get_weight_value())

height_entry = customtkinter.CTkEntry(app,textvariable=height,bg_color='#181935',fg_color='#181935',border_width=0,font=('Arial',23,'bold'))
height_entry.place(x=127,y=100)

weight_entry = customtkinter.CTkEntry(app,textvariable=weight,bg_color='#181935',fg_color='#181935',border_width=0,font=('Arial',23,'bold'))
weight_entry.place(x=127,y=250)

height_slider = customtkinter.CTkSlider(app,variable=height_value,from_=0,to=300,width=260,bg_color='#181935',fg_color='#FFFFFF',button_hover_color='#2E852E',command=slider1)
height_slider.place(x=20,y=155)

weight_slider = customtkinter.CTkSlider(app,variable=weight_value,from_=0,to=500,width=260,bg_color='#181935',fg_color='#FFFFFF',button_hover_color='#2E852E',command=slider2)
weight_slider.place(x=20,y=300)

# Definition to calculate BMI
def BMI():
    try:
        cm = int(height_entry.get())
        m = (cm/100)*(cm/100)
        w = int(weight_entry.get())
        bmi = float(format(w/m,'.2f'))
        if(bmi <= 18.5):
            txt.set('Underweight')
        elif(bmi <= 24.5):
            txt.set('Normal')
        elif(bmi <= 29.9):
            txt.set('Overweight')
        elif(bmi <= 34.9):
            txt.set('Obese I')
        elif(bmi <= 39.9):
            txt.set('Obese II')
        else:
            txt.set('Obese III')
        result1_label = customtkinter.CTkLabel(app,text=f'BMI: {bmi}',font=('Arial',18,'bold'))
        result1_label.place(x=75,y=410)
        result2_label = customtkinter.CTkLabel(app,textvariable=txt,font=('Arial',18,'bold'))
        result2_label.place(x=73,y=440)
    except:
        # Message Error if the BMI is equal to 0
        messagebox.showerror(title='Error',message='Heigh or weight cannot be equal to 0.')


# Button to calculate
calc_button = customtkinter.CTkButton(app,text='CALCULATE',command=BMI,width=170,height=50,font=('Arial',20,'bold'),fg_color='#2E852E',hover_color='#2E852E')
calc_button.place(x=63,y=350)


app.mainloop()