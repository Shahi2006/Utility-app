import tkinter as tk
from PIL import Image,ImageTk
import requests
from tkinter import ttk
from datetime import datetime



root=tk.Tk()

root.title("Weather App")
root.geometry("600x500")

def form(pray):
    d=pray["data"]["timings"]
    s=""
    for i in d:
        s+=f"{i}:"
        j=d[i]
        s+=f"{j} \n"
    return s
        


def convert_to_12_hour_format(time_24_hour):
    time_24_hour = time_24_hour.split()[0]
    time_object = datetime.strptime(time_24_hour, '%H:%M')
    time_12_hour = time_object.strftime('%I:%M %p')
    return time_12_hour

current_date = datetime.now().strftime("%D-%m-%Y")
def prayertime(city,country):
    city_name=city
    country_name=country
    api_url = f"http://api.aladhan.com/v1/calendarByCity/{current_date.split('-')[2]}/{current_date.split('-')[1]}?city={city_name}&country={country_name}&method=2"
    response = requests.get(api_url)
    pray=response.json()
    #print(pray)
    result["text"]=form(pray)
def prayertime1(city,country):
    cit=city
    con=country
    url = f"https://api.aladhan.com/v1/timingsByCity?city={city}&country={con}"
    response = requests.get(url)
    pray=response.json()
    result["text"]=form(pray)
    

        
        
img=Image.open('mosque.webp')
img_photo=ImageTk.PhotoImage(img)

bg_lbl=tk.Label(root,image=img_photo)
bg_lbl.place(x=0,y=0,width=600,height=500)


head=tk.Label(bg_lbl,text="Find the Prayer times for any city you want!",fg="green",bg="silver",font=('times new roman',25,"bold","underline"))
head.place(x=80,y=18)



frame_one=tk.Frame(bg_lbl,bg="silver",bd=5)
frame_one.place(x=80,y=130,width=450,height=50)

txt_box=tk.Entry(frame_one,bg="gray",font=('times new roman',16,"bold"),width=17)
txt_box.grid(row=0,column=0,sticky="w")
txt_box2=tk.Entry(frame_one,bg="gray",font=('times new roman',16,"bold"),width=17)
txt_box2.grid(row=0,column=1,sticky="w")

btn=tk.Button(frame_one,text="Get weather",fg="green",font=('times new roman',16,"bold"),command=lambda:prayertime1(txt_box.get(),txt_box.get()),)
btn.grid(row=0,column=3,padx=20)

frame_two=tk.Frame(bg_lbl,bg="silver",bd=5)
frame_two.place(x=80,y=190,width=450,height=300)


result=tk.Label(frame_two,font=("baguet script",20),fg="gold",bg="gray",justify="left",anchor="nw")
result.place(relwidth=1,relheight=1)




root.mainloop()
