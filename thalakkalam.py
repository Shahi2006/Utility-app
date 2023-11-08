import tkinter as tk
from PIL import Image,ImageTk
import requests
from datetime import datetime
root =tk.Tk()

root.title("By Shahid, Zeeshan, and Jestin")
root.geometry("600x500")

def prayer():
    prayer_win = tk.Tk()
    prayer_win.title("Prayer Scan")
    prayer_win.geometry("600x500")

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
    prayer_win.mainloop()

def weather():
    weather_win = tk.Tk()
    weather_win.title("Weather Scan")
    weather_win.geometry("600x500")
    
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
        img=ImageTk.PhotoImage(Image.open("project/img/"+icon+".png").resize((size,size)))
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
        
    img=Image.open('project/bg.webp')
    img_photo=ImageTk.PhotoImage(img)

    bg_lbl=tk.Label(root,image=img_photo)
    bg_lbl.place(x=0,y=0,width=600,height=500)


    head=tk.Label(bg_lbl,text="Find the weather for any city you want!",fg="green",bg="silver",font=('times new roman',25,"bold","underline"))
    head.place(x=80,y=18)



    frame_one=tk.Frame(bg_lbl,bg="gold",bd=5)
    frame_one.place(x=80,y=130,width=450,height=50)


    txt_box=tk.Entry(frame_one,bg="silver",font=('times new roman',25,"bold"),width=17)
    txt_box.grid(row=0,column=0,sticky="w")

    btn=tk.Button(frame_one,text="Get weather",fg="green",font=('times new roman',16,"bold"),command=lambda:getweather(txt_box.get()))
    btn.grid(row=0,column=1,padx=20)


    frame_three=tk.Frame(bg_lbl,bg="silver",bd=5)
    frame_three.place(x=80,y=60,width=450,height=50)


    com_box=ttk.Combobox(frame_three,font=('times new roman',15,"bold"),foreground="green",width=50,values=["Imperial","Metric","Standard"])
    com_box.set("Select your preferred unit system")
    com_box['state']="readonly"
    com_box.grid(row=0,column=0,sticky="e")




    frame_two=tk.Frame(bg_lbl,bg="gold",bd=5)
    frame_two.place(x=80,y=190,width=450,height=200)


    result=tk.Label(frame_two,font=("baguet script",20),fg="red",bg="silver",justify="left",anchor="nw")
    result.place(relwidth=1,relheight=1)
    
    


    weather_icon=tk.Canvas(result,bg="silver",bd=0,highlightthickness=0)
    weather_icon.place(relx=0.75,rely=0,relwidth=1,relheight=0.5)
    weather_win.mainloop()

menu_frame = tk.Frame(root)
menu_frame.pack()#expand = True,fill = "both", rely = 0.5, relx = 0.5)

weather_btn = tk.Button(menu_frame, text = "Find Weather" ,command = weather)
weather_btn.pack()
prayer_btn = tk.Button(menu_frame, text ="Find Prayer times",command = prayer)
prayer_btn.pack()