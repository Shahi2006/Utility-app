import tkinter as tk
from PIL import Image,ImageTk
import requests
from datetime import datetime
from tkinter import ttk
root =tk.Tk()
root.title("Skyspirit")
root.geometry("600x500")

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


menu_frame = tk.Frame(root)
menu_frame.pack()#expand = True,fill = "both", rely = 0.5, relx = 0.5)

weather_btn = tk.Button(menu_frame, text = "Find Weather",font=('times new roman',16,"bold") ,fg="red",command = weather)
weather_btn.configure(height=10,width=20)
weather_btn.pack(side=tk.TOP,padx=20)
prayer_btn = tk.Button(menu_frame, text ="Find Prayer times",font=('times new roman',16,"bold"),fg="blue",command = prayer)
prayer_btn.configure(height=10,width=20)
prayer_btn.pack(side=tk.TOP,padx=20,pady=20)



root.mainloop()
