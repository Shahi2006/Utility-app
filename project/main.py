import tkinter as tk
from PIL import Image,ImageTk
import requests
from tkinter import ttk
root=tk.Tk()

root.title("Weather App")
root.geometry("600x500")


# key dd45f0966e256666ece18c1e4380a7aa
# url; https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
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
    img=ImageTk.PhotoImage(Image.open("./img/"+icon+".png").resize((size,size)))
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
    
img=Image.open('./bg.webp')
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








root.mainloop()
