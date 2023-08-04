from tkinter import *
import requests

root = Tk()
root.title("Weather App")
root.geometry("600x500")
root.config(bg="skyblue")


def format_response(weather):
    try:
        city = weather['name']
        condition = weather['weather'][0]['description']
        temp = weather['main']['temp']
        final_str = 'City: %s\nCondition: %s\nTemperature: %s' % (
            city, condition, temp)
    except:
        final_str = 'There was a problem retreiving that information'
    return final_str


def get_weather(city):
    weather_key = 'c4e7f0e0f01b33c4cc35bdbde80a68eb'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params)
    weather = response.json()
    result['text'] = format_response(weather)


label1 = Label(root, text="Aditya's Weather Forecasting Application", font=(
    "Ultra", 20, 'bold'), background="skyblue", fg="red")
label1.place(x=25, y=30)
frame1 = Frame(root, width=400, height=100, background="palegreen")
frame1.place(x=100, y=100)

entry1 = Entry(frame1, font=("Oswald", 20), width=15)
entry1.grid(row=0, column=0, sticky='w')

btn1 = Button(frame1, text="Get Weather", font=("times new roman", 15, 'bold'),
              fg="Blue", background="pink", command=lambda: get_weather(entry1.get()))
btn1.grid(row=0, column=1, padx=15)

frame2 = Frame(root, width=400, height=200, background="palegreen")
frame2.place(x=100, y=150)

result = Label(frame2, font=("Ultra",
               20, 'bold'), background="Palegreen", foreground="Red")
result.place(relheight=1, relwidth=1)

label2 = Label(root, text="Thankyou! for visiting the application :) ", font=(
    'Lobster', 20, 'italic', 'bold'), foreground="purple", background="skyblue")
label2.place(x=55, y=400)
root.mainloop()
