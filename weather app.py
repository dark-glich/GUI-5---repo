from tkinter import *
import requests
import json

root = Tk()
root.title("weather app")
root.geometry("540x220")
try:
    def show():

        get = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/"
                           "json&zipCode=" + d.get() + "&distance=25&API_KEY=BC46AA5E-2E6C-484D-B518-5BCC9144807D")
        ge = json.loads(get.content)

        region = ge[0]['ReportingArea']
        quality = str(ge[0]['AQI'])
        category = ge[0]['Category']['Name']
        labelf = LabelFrame(root, text="AIR QUALITY", padx=50, pady=50)
        labelf.grid(row=0, column=0)
        color = ""
        if category == 'Good':
            color = "#00e400"
        elif category == "Moderate":
            color = "#ffff00"
        elif category == "Unhealthy for Sensitive Groups":
            color = "#ff7e0"
        elif category == "Unhealthy":
            color = "#ff0000"
        elif category == "Very Unhealthy":
            color = "#99004c"
        elif category == "Hazardous":
            color = "#7e0023"

        label1 = Label(root, text="REGION : " + region, font=('helvetica', 30), bg=color)
        label2 = Label(root, text="AQI : " + quality, font=('helvetica', 30), bg=color)
        label3 = Label(root, text="CONDITION : " + category, font=('helvetica', 30), bg=color)
        label1.grid(row=1, column=0)
        label2.grid(row=2, column=0)
        label3.grid(row=3, column=0)
        root.configure(bg=color)

    d = StringVar(root)
    d.set("90201")
    drop = OptionMenu(root, d, "90201", "90805", "10001", "20001", "88901", "91945", "93301")
    butt = Button(root, text="show", command=show)
    butt.grid(row=6, column=0, ipadx=200)
    drop.grid(row=4, column=0, ipadx=200)
except ConnectionError:
    ge = "error!!!"
    print(ge)
root.mainloop()
