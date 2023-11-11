import tkinter as tk
from PIL import Image,ImageTk
import requests
from datetime import datetime
from tkinter import ttk
root =tk.Tk()
root.title("Skyspirit")
root.geometry("600x500")
root.resizable(0,0)
def calculator():

    LARGE_FONT_STYLE = ("Arial", 40, "bold")
    SMALL_FONT_STYLE = ("Arial", 16)
    DIGITS_FONT_STYLE = ("Arial", 24, "bold")
    DEFAULT_FONT_STYLE = ("Arial", 20)

    OFF_WHITE = "#F8FAFF"
    WHITE = "#FFFFFF"
    LIGHT_BLUE = "#CCEDFF"
    LIGHT_GRAY = "#F5F5F5"
    LABEL_COLOR = "#25265E"


    class Calculator:
        def __init__(self):
            self.window = tk.Tk()
            self.window.geometry("375x667")
            self.window.resizable(0, 0)
            self.window.title("Calculator")
            

            self.total_expression = ""
            self.current_expression = ""
            self.display_frame = self.create_display_frame()

            self.total_label, self.label = self.create_display_labels()

            self.digits = {
                7: (1, 1), 8: (1, 2), 9: (1, 3),
                4: (2, 1), 5: (2, 2), 6: (2, 3),
                1: (3, 1), 2: (3, 2), 3: (3, 3),
                0: (4, 2), '.': (4, 1)
            }
            self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
            self.buttons_frame = self.create_buttons_frame()

            self.buttons_frame.rowconfigure(0, weight=1)
            for x in range(1, 5):
                self.buttons_frame.rowconfigure(x, weight=1)
                self.buttons_frame.columnconfigure(x, weight=1)
            self.create_digit_buttons()
            self.create_operator_buttons()
            self.create_special_buttons()
            self.bind_keys()
            

        def bind_keys(self):
            self.window.bind("<Return>", lambda event: self.evaluate())
            for key in self.digits:
                self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

            for key in self.operations:
                self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

        def create_special_buttons(self):
            self.create_clear_button()
            self.create_equals_button()
            self.create_square_button()
            self.create_sqrt_button()

        def create_display_labels(self):
            total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY,
                                fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
            total_label.pack(expand=True, fill='both')

            label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY,
                            fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
            label.pack(expand=True, fill='both')

            return total_label, label

        def create_display_frame(self):
            frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
            frame.pack(expand=True, fill="both")
            return frame

        def add_to_expression(self, value):
            self.current_expression += str(value)
            self.update_label()

        def create_digit_buttons(self):
            for digit, grid_value in self.digits.items():
                button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
                                borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
                button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

        def append_operator(self, operator):
            self.current_expression += operator
            self.total_expression += self.current_expression
            self.current_expression = ""
            self.update_total_label()
            self.update_label()

        def create_operator_buttons(self):
            i = 0
            for operator, symbol in self.operations.items():
                button = tk.Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                                borderwidth=0, command=lambda x=operator: self.append_operator(x))
                button.grid(row=i, column=4, sticky=tk.NSEW)
                i += 1

        def clear(self):
            self.current_expression = ""
            self.total_expression = ""
            self.update_label()
            self.update_total_label()

        def create_clear_button(self):
            button = tk.Button(self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                            borderwidth=0, command=self.clear)
            button.grid(row=0, column=1, sticky=tk.NSEW)

        def square(self):
            self.current_expression = str(eval(f"{self.current_expression}**2"))
            self.update_label()

        def create_square_button(self):
            button = tk.Button(self.buttons_frame, text="x\u00b2", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                            borderwidth=0, command=self.square)
            button.grid(row=0, column=2, sticky=tk.NSEW)

        def sqrt(self):
            self.current_expression = str(eval(f"{self.current_expression}**0.5"))
            self.update_label()

        def create_sqrt_button(self):
            button = tk.Button(self.buttons_frame, text="\u221ax", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                            borderwidth=0, command=self.sqrt)
            button.grid(row=0, column=3, sticky=tk.NSEW)

        def evaluate(self):
            self.total_expression += self.current_expression
            self.update_total_label()
            try:
                self.current_expression = str(eval(self.total_expression))

                self.total_expression = ""
            except Exception as e:
                self.current_expression = "Error"
            finally:
                self.update_label()

        def create_equals_button(self):
            button = tk.Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                            borderwidth=0, command=self.evaluate)
            button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

        def create_buttons_frame(self):
            frame = tk.Frame(self.window)
            frame.pack(expand=True, fill="both")
            return frame

        def update_total_label(self):
            expression = self.total_expression
            for operator, symbol in self.operations.items():
                expression = expression.replace(operator, f' {symbol} ')
            self.total_label.config(text=expression)

        def update_label(self):
            self.label.config(text=self.current_expression[:11])

        def run(self):
            self.window.mainloop()
        
    
    if __name__ == "__main__":
        calc = Calculator()
        calc.run()
    

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
weather_btn.configure(height=1,width=22)
weather_btn.pack(side=tk.TOP,padx=20,pady=20)

prayer_btn = tk.Button(menu_frame, text ="Find Prayer times",font=('times new roman',16,"bold"),fg="blue",command = prayer)
prayer_btn.configure(height=1,width=22)
prayer_btn.pack(side=tk.TOP,padx=20,pady=20)



calculator_btn=tk.Button(menu_frame, text ="Use Calculator",font=('times new roman',16,"bold"),fg="blue",command = calculator)
calculator_btn.configure(height=1,width=22)
calculator_btn.pack(side=tk.TOP,padx=20,pady=20)



root.mainloop()
