import tkinter as tk
from tkinter import messagebox
import requests
import  geopy
import folium



def find_location():
    address = entry.get()
    if address:
        try:
            url = f"https://nominatim.openstreetmap.org/search?q={address}&format=json"
            response = requests.get(url)
            data = response.json()
            if data:
                latitude = float(data[0]["lat"])
                longitude = float(data[0]["lon"])
                
                map = folium.Map(location=[latitude, longitude], zoom_start=15)
                
                folium.Marker([latitude, longitude], popup=address).add_to(map)
                
                map.save('location_map.html')
                messagebox.showinfo("Location Found", f"Latitude: {latitude}\nLongitude: {longitude}")
            else:
                messagebox.showerror("Error", "Location not found")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        messagebox.showwarning("Warning", "Please enter an address")
root = tk.Tk()
root.title("Location Finder")
label = tk.Label(root, text="Enter an address:")
label.pack()
entry = tk.Entry(root, width=50)
entry.pack()
button = tk.Button(root, text="Find Location", command=find_location)
button.pack()
root.mainloop()
