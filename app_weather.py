import tkinter as tk
import weather as weather
import json

#@TODO: Add open API_KEY from directory navigation

def get_city_data():
    """@TODO: Get data from weather.py
    """
    frm_show_data.grid(row=1, column=0, padx=10)
    city_name = ent_city.get()
    weather.get_weather_data(city_name)

    with open("weather.json","r") as read_file:
        data = json.load(read_file)
        print(type(data))

    #temperature in celcius
    temperature ="{:.2f}".format(data['main']['temp_min'] - 273.15)
    print(temperature)
    lbl_result["text"] = f"{temperature} \N{DEGREE CELSIUS}"

# Set up the window
window = tk.Tk()
window.title("Weather Good For What?")
window.resizable(width=True, height=True)
window.rowconfigure(0,minsize=100)
window.rowconfigure(1,minsize=200)
window.columnconfigure(0,minsize=400)

# Create the City entry frame with an Entry
frm_ent_city = tk.Frame(master=window)
lbl_city = tk.Label(master=frm_ent_city, text="Enter city :")
ent_city = tk.Entry(master=frm_ent_city, width=25)
btn_search = tk.Button(
    master=frm_ent_city,
    text="search",
    command=get_city_data
)
# Layout the temperature Entry and Label in frm_entry
# using the .grid() geometry manager

lbl_city.grid(row=0, column=0,padx=5, sticky="nsw")
ent_city.grid(row=0, column=1,padx=5, sticky="nsw")
btn_search.grid(row=0, column=2, padx=5, sticky="e")




frm_show_data = tk.Frame(master=window)
lbl_result = tk.Label(master=frm_show_data, text="\N{DEGREE CELSIUS}")

# Set up the layout using the .grid() geometry manager
frm_ent_city.grid(row=0, column=0, padx=10)
lbl_result.grid(row=0, column=2, padx=10)

# Run the application
window.mainloop()