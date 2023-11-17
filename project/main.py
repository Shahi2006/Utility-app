import tkinter as tk
from PIL import Image,ImageTk
import requests
from datetime import datetime
from datetime import date
from tkinter import ttk
import csv
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
root =tk.Tk()
root.title("Skyspirit")
root.geometry("600x500")
root.resizable(0,0)
def ping_pong():
    import turtle

    #Game Screen
    gs = turtle.Screen()
    gs.title('Ping Pong Game')
    gs.bgcolor('black')
    gs.setup(width=800, height=600)
    gs.tracer()

    #paddle a
    paddle_a = turtle.Turtle()
    paddle_a.speed(0)
    paddle_a.color('white')
    paddle_a.shape('square')
    paddle_a.shapesize(stretch_wid=5, stretch_len=1)
    paddle_a.penup()
    paddle_a.goto(-350,0)

    #paddle b
    paddle_b = turtle.Turtle()
    paddle_b.speed(0)
    paddle_b.penup()
    paddle_b.color('white')
    paddle_b.goto(350,0)
    paddle_b.shape('square')
    paddle_b.shapesize(stretch_wid=5, stretch_len=1)

    #ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape('circle')
    ball.color('white')
    ball.penup()
    ball.goto(0,0)
    ball.dx = 5
    ball.dy = 5

    #score
    score_A = 0
    score_B = 0

    #pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color('white')
    pen.penup()
    pen.hideturtle()
    pen.goto(0,260)
    pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "bold"))

    #Function
    def paddle_a_up():
        y = paddle_a.ycor()
        y += 20
        paddle_a.sety(y)

    def paddle_a_down():
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)

    def paddle_b_up():
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)

    def paddle_b_down():
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)

    #Keyboard
    gs.listen()
    gs.onkeypress(paddle_a_up, "w")
    gs.onkeypress(paddle_a_down, "s")
    gs.onkeypress(paddle_b_up, "Up")
    gs.onkeypress(paddle_b_down, "Down")

    #Game Loop
    while True:
        gs.update()

        #move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        #border
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() > 390:
            ball.goto(0,0)
            ball.dx *= -1
            score_A += 1
            pen.clear()
            pen.write("Player A: {} Player B: {}".format(score_A, score_B), align="center", font=("Courier", 24, "bold"))

        if ball.xcor() < -390:
            ball.goto(0,0)
            ball.dx *= -1
            score_B += 1
            pen.clear()
            pen.write("Player A: {} Player B: {}".format(score_A, score_B), align="center", font=("Courier", 24, "bold"))

        #Collisions
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
            ball.setx(340)
            ball.dx *= -1

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
            ball.setx(-340)
            ball.dx *= -1
    
calculation=""  
def calculator():
    
    
    def add_to_calculation(symbol):
        global calculation
        calculation+=str(symbol)
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    
    def evaluate_calculation():
        global calculation
        try:
            result=str(eval(calculation))
            entry=calculation+"="+result
            l=[entry]
            f=open("calculatorhistory.csv","a",newline="")
            d=csv.writer(f,delimiter=",")
            d.writerow(l)
            print(l)
            f.close()
            text_result.delete(1.0,"end")
            text_result.insert(1.0,result)
        except:
            clear_field()
            text_result.insert(1.0,"Error")
            
    
    def clear_field():
        global calculation
        calculation=""
        text_result.delete(1.0,"end")
    
    def exit():
        roots.destroy()
    
    roots=tk.Tk()
    roots.geometry("300x270")
    
    text_result= tk.Text(roots,height=2,width=16,font=("Ariel",24))
    text_result.grid(columnspan=5)
    
    
    btn1=tk.Button(roots,text="1",command=lambda:add_to_calculation(1),width=4,font=("Ariel",14))
    btn1.grid(row=2,column=1)
    
    btn2=tk.Button(roots,text="2",command=lambda:add_to_calculation(2),width=4,font=("Ariel",14))
    btn2.grid(row=2,column=2)
    
    btn3=tk.Button(roots,text="3",command=lambda:add_to_calculation(3),width=4,font=("Ariel",14))
    btn3.grid(row=2,column=3)
    
    btn4=tk.Button(roots,text="4",command=lambda:add_to_calculation(4),width=4,font=("Ariel",14))
    btn4.grid(row=3,column=1)
    
    btn5=tk.Button(roots,text="5",command=lambda:add_to_calculation(5),width=4,font=("Ariel",14))
    btn5.grid(row=3,column=2)
    
    btn6=tk.Button(roots,text="6",command=lambda:add_to_calculation(6),width=4,font=("Ariel",14))
    btn6.grid(row=3,column=3)
    
    btn7=tk.Button(roots,text="7",command=lambda:add_to_calculation(7),width=4,font=("Ariel",14))
    btn7.grid(row=4,column=1)
    
    btn8=tk.Button(roots,text="8",command=lambda:add_to_calculation(8),width=4,font=("Ariel",14))
    btn8.grid(row=4,column=2)
    
    btn9=tk.Button(roots,text="9",command=lambda:add_to_calculation(9),width=4,font=("Ariel",14))
    btn9.grid(row=4,column=3)
    
    btn0=tk.Button(roots,text="0",command=lambda:add_to_calculation(0),width=4,font=("Ariel",14))
    btn0.grid(row=5,column=2)
    
    btnplus=tk.Button(roots,text="+",command=lambda:add_to_calculation("+"),width=4,font=("Ariel",14))
    btnplus.grid(row=2,column=4)
    
    btnminus=tk.Button(roots,text="-",command=lambda:add_to_calculation("-"),width=4,font=("Ariel",14))
    btnminus.grid(row=3,column=4)
    
    btnx=tk.Button(roots,text="X",command=lambda:add_to_calculation("*"),width=4,font=("Ariel",14))
    btnx.grid(row=4,column=4)
    
    btndiv=tk.Button(roots,text="/",command=lambda:add_to_calculation("/"),width=4,font=("Ariel",14))
    btndiv.grid(row=5,column=4)
    
    btnopen=tk.Button(roots,text="(",command=lambda:add_to_calculation("("),width=4,font=("Ariel",14))
    btnopen.grid(row=5,column=1)
    
    btnclose=tk.Button(roots,text=")",command=lambda:add_to_calculation(")"),width=4,font=("Ariel",14))
    btnclose.grid(row=5,column=3)
    
    btnclear=tk.Button(roots,text="C",command= clear_field,width=7,font=("Ariel",14))
    btnclear.grid(row=6,column=1,columnspan=2)
    
    btnequal=tk.Button(roots,text="=",command= evaluate_calculation,width=7,font=("Ariel",14))
    btnequal.grid(row=6,column=3,columnspan=2)
    
    btnexit=tk.Button(roots,text="Go Back",command= exit,width=7,font=("Ariel",14),fg="orange")
    btnexit.place(x=175,y=235)
    
    
    

    roots.mainloop()

def calchistory():
    roots=tk.Tk()
    roots.geometry("600x600")
    def exit():
        roots.destroy()
    f=open("calculatorhistory.csv","r",newline="")
    text_result= tk.Label(roots,font=("Ariel",24))
    text_result.place(relheight=1,relwidth=1)
    l=""
    d=csv.reader(f)
    for i in d:
        i=str(i)
        l=l+i+"\n"
    text_result["text"]=l
    btnexit=tk.Button(text_result,text="Go Back",command= exit,width=7,font=("Ariel",14),fg="orange")
    btnexit.place(x=500,y=500)
    




def prayer():
    prayer_win = tk.Tk()
    prayer_win.title("Prayer Scan")
    prayer_win.geometry("600x500")
    prayer_win.destroy()
    def exit():
         bg_lbl.destroy()

    def form(pray):
        d=pray["data"]["timings"]
        s=""
        for i in d:
            s+=f"{i}:"
            j=d[i]
            s+=f"{j} \n"
        return s
            
    def prayertime1(city,country):
        cit=city
        con=country
        url = f"https://api.aladhan.com/v1/timingsByCity?city={city}&country={con}"
        response = requests.get(url)
        pray=response.json()
        if pray["code"]==200:
            result["text"]=form(pray)
        else:
            result["text"]="An Error Occured"
    
    
    img=Image.open('mosque.webp')
    img_photo=ImageTk.PhotoImage(img)

    bg_lbl=tk.Label(root,image=img_photo)
    bg_lbl.place(x=0,y=0,width=600,height=500)
    
    head=tk.Label(bg_lbl,text="Find the Prayer times for any city you want!",fg="green",bg="silver",font=('times new roman',25,"bold","underline"))
    head.pack(pady=90)
    
    frame_one=tk.Frame(bg_lbl,bg="silver",bd=5)
    frame_one.place(x=80,y=130,width=450,height=50)

    txt_box=tk.Entry(frame_one,bg="gray",font=('times new roman',16,"bold"),width=17)
    txt_box.grid(row=0,column=0,sticky="w")
    
    txt_box2=tk.Entry(frame_one,bg="gray",font=('times new roman',16,"bold"),width=17)
    txt_box2.grid(row=0,column=1,sticky="w")

    btn=tk.Button(frame_one,text="Get prayer time",fg="green",font=('times new roman',14,"bold"),command=lambda:prayertime1(txt_box.get(),txt_box.get()),)
    btn.grid(row=0,column=3,padx=10)

    frame_two=tk.Frame(bg_lbl,bg="silver",bd=5)
    frame_two.place(x=80,y=190,width=450,height=300)


    result=tk.Label(frame_two,font=("baguet script",20),fg="gold",bg="gray",justify="left",anchor="nw")
    result.place(relwidth=1,relheight=1)
    
    back=tk.Button(bg_lbl,text="Go Back",bg="orange",fg="green",font=('times new roman',16,"bold"),command=lambda:exit())
    back.place(x=370,y=460)
    
    prayer_win.mainloop()

def weather():
    def exit():
       bg_lbl.destroy()
    
    weather_win = tk.Tk()
    weather_win.title("weather Scan")
    weather_win.geometry("600x500")
    weather_win.destroy()

    def format_response(weathe):
        try:
            city=weathe['name']
            condition=weathe['weather'][0]["description"]
            temp=weathe["main"]["temp"]
            feels=weathe["main"]["feels_like"]
            humi=weathe["main"]["humidity"]
            wind=weathe['wind']['speed']
            sting="City:%s\nCondition:%s\nTemperature:%s\nFeels like:%s\nHumidity:%s\nWind speed:%s"%(city,condition,temp,feels,humi,wind)
        except:
            sting="an error occured"
        return sting
    def open_image(icon):
        size=int(frame_two.winfo_height()*0.5)
        img=ImageTk.PhotoImage(Image.open("img/"+icon+".png").resize((size,size)))
        weather_icon.delete("all")
        weather_icon.create_image(0,0,anchor="nw",image=img)
        weather_icon.image=img

    def getweather(city):
        ke="dd45f0966e256666ece18c1e4380a7aa"
        url="https://api.openweathermap.org/data/2.5/weather"
        unit=com_box.get()
        param={"APPID":ke,"q":city,"units":unit}
        response=requests.get(url,param)
        weathe=response.json()
        #print(weathe)
        result["text"]=format_response(weathe)
        
        ico=weathe['weather'][0]['icon']
        open_image(ico)
        
    img=Image.open('bg.webp')
    img_photo=ImageTk.PhotoImage(img)

    bg_lbl=tk.Label(root,image=img_photo)
    bg_lbl.place(x=0,y=0,width=600,height=500)
    
    head=tk.Label(bg_lbl,text="Find the weather for any city you want!",fg="green",bg="silver",font=('times new roman',25,"bold","underline"))
    head.place(x=80,y=18)

    frame_one=tk.Frame(bg_lbl,bg="silver",bd=5)
    frame_one.place(x=80,y=130,width=450,height=50)

    txt_box=tk.Entry(frame_one,bg="gray",font=('times new roman',25,"bold"),width=17)
    txt_box.grid(row=0,column=0,sticky="w")

    btn=tk.Button(frame_one,text="Get weather",fg="green",font=('times new roman',16,"bold"),command=lambda:getweather(txt_box.get()))
    btn.grid(row=0,column=1,padx=20)

    frame_three=tk.Frame(bg_lbl,bg="silver",bd=5)
    frame_three.place(x=80,y=60,width=450,height=50)

    com_box=ttk.Combobox(frame_three,background='silver',font=('times new roman',15,"bold"),foreground="green",width=50,values=["Imperial","Metric","Standard"])
    com_box.set("Select your preferred unit system")
    com_box['state']="readonly"
    com_box.grid(row=0,column=0,sticky="e")

    frame_two=tk.Frame(bg_lbl,bg="silver",bd=5)
    frame_two.place(x=80,y=190,width=450,height=200)

    result=tk.Label(frame_two,font=("baguet script",20),fg="gold",bg="gray",justify="left",anchor="nw")
    result.place(relwidth=1,relheight=1)
    
    weather_icon=tk.Canvas(result,bg="gray",bd=0,highlightthickness=0)
    weather_icon.place(relx=0.75,rely=0,relwidth=1,relheight=0.5)

    back=tk.Button(bg_lbl,text="Go Back",bg="orange",fg="green",font=('times new roman',16,"bold"),command=lambda:exit())
    back.place(x=300,y=400)
    
    weather_win.mainloop()

def calculation_main():
    roots=tk.Tk()
    roots.geometry("300x300")
    
    menu=tk.Frame(roots)
    menu.pack()
    
    def exit():
        roots.destroy()
    
    calculator_btn=tk.Button(menu, text ="Use Calculator",font=('times new roman',16,"bold"),fg="blue",command = calculator)
    calculator_btn.configure(height=1,width=22)
    calculator_btn.grid(row=1,column=1,rowspan=2)
    
    calchistory_btn=tk.Button(menu, text ="Get Calculation History",font=('times new roman',16,"bold"),fg="brown",command = calchistory)
    calchistory_btn.configure(height=1,width=22)
    calchistory_btn.grid(row=3,column=1,rowspan=2)
    
    exit_btn=tk.Button(menu, text ="Go Back",font=('times new roman',16,"bold"),fg="orange",command = exit)
    exit_btn.configure(height=1,width=22)
    exit_btn.grid(row=9,column=1,rowspan=2)

def fitness():
    pass
dae=date.today()
print(dae)
    
    

menu_frame = tk.Frame(root)
menu_frame.pack()#expand = True,fill = "both", rely = 0.5, relx = 0.5)

weather_btn = tk.Button(menu_frame, text = "Find Weather",font=('times new roman',16,"bold") ,fg="red",command = weather)
weather_btn.configure(height=1,width=22)
weather_btn.pack(side=tk.TOP,padx=20,pady=20)

prayer_btn = tk.Button(menu_frame, text ="Find Prayer times",font=('times new roman',16,"bold"),fg="blue",command = prayer)
prayer_btn.configure(height=1,width=22)
prayer_btn.pack(side=tk.TOP,padx=20,pady=20)



calculator_btn=tk.Button(menu_frame, text ="Use Calculator",font=('times new roman',16,"bold"),fg="orange",command = calculation_main)
calculator_btn.configure(height=1,width=22)
calculator_btn.pack(side=tk.TOP,padx=20,pady=20)


ping_btn=tk.Button(menu_frame, text ="Play Ping-Pong",font=('times new roman',16,"bold"),fg="purple",command = ping_pong)
ping_btn.configure(height=1,width=22)
ping_btn.pack(side=tk.TOP,padx=20,pady=20)



root.mainloop()
