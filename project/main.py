import tkinter as tk
from PIL import Image,ImageTk
import requests
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
        sting="City:%s\nCondition:%s\nTemperature:%s\nFeels like:%s\nHumidity:%s"%(city,condition,temp,feels,humi)
    except:
"%(city,condition,temp,)
    except:
        sting="an error occured"
    return sting





def open_image(icon):
    size=int(frame_two.winfo_height()*0.25)
    img=ImageTk.PhotoImage(Image.open("./img/"+icon+".png").resize((size,size)))
    weather_icon.delete("all")
    weather_icon.create_image(0,0,anchor="nw",image=img)
    weather_icon.image=img

def getweather(city):
    ke="dd45f0966e256666ece18c1e4380a7aa"
    url="https://api.openweathermap.org/data/2.5/weather"
    param={"APPID":ke,"q":city,"units":"imperial"}
    response=requests.get(url,param)
    weathe=response.json()
    print(weathe['name'])
    print(weathe['weather'][0]["description"])
    print(weathe["main"]["temp"])
    
    result["text"]=format_response(weathe)
    
    ico=weathe['weather'][0]['icon']
    open_image(ico)
    
img=Image.open('./bg.webp')
img_photo=ImageTk.PhotoImage(img)

bg_lbl=tk.Label(root,image=img_photo)
bg_lbl.place(x=0,y=0,width=600,height=500)


head=tk.Label(bg_lbl,text="Find the weather for any city you want!",fg="yellow",bg="purple",font=('times new roman',25,"bold"))
head.place(x=80,y=18)



frame_one=tk.Frame(bg_lbl,bg="yellow",bd=5)
frame_one.place(x=80,y=60,width=450,height=50)


txt_box=tk.Entry(frame_one,bg="light blue",font=('times new roman',25,"bold"),width=17)
txt_box.grid(row=0,column=0,sticky="w")

btn=tk.Button(frame_one,text="Get weather",fg="green",font=('times new roman',16,"bold"),command=lambda:getweather(txt_box.get()))
btn.grid(row=0,column=1,padx=20)


frame_two=tk.Frame(bg_lbl,bg="yellow",bd=5)
frame_two.place(x=80,y=130,width=450,height=300)


result=tk.Label(frame_two,font=40,bg="silver",justify="left",anchor="nw")
result.place(relwidth=1,relheight=1)
  
  


weather_icon=tk.Canvas(result,bg="silver",bd=0,highlightthickness=0)
weather_icon.place(relx=0.75,rely=0,relwidth=1,relheight=0.5)








root.mainloop()
