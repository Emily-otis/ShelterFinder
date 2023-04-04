import tkinter as tk
from tkinter import Canvas
from tkinter import PhotoImage



# A list of point data, including information about the distance, walking time, and closest shelter
points_data = [
    # Add each point as a dictionary with the relevant information
    {"id": 1, "x": 406, "y": 278, "distance_m": 0.5, "distance_ft": 2640, "walking_time": "10 mins", "closest_shelters": "Haley Center"},
    {"id": 2, "x": 520, "y": 244, "distance_m": 0.4, "distance_ft": 2112, "walking_time": "7 mins", "closest_shelters": "Haley Center"},
    {"id": 3, "x": 621, "y": 231, "distance_m": 0.2, "distance_ft": 1056, "walking_time": "4 mins", "closest_shelters": "Brown-Kopel"},
    {"id": 4, "x": 811, "y": 178, "distance_m": 0.2, "distance_ft": 1056, "walking_time": "4 mins", "closest_shelters": "Draughon Library"},
    {"id": 5, "x": 691, "y": 278, "distance_m": 0.1, "distance_ft": 528, "walking_time": "3 mins", "closest_shelters": "Haley Center"},
    {"id": 6, "x": 694, "y": 352, "distance_m": 0.1, "distance_ft": 528, "walking_time": "3 mins", "closest_shelters": "Haley Center"},
    {"id": 7, "x": 808, "y": 384, "distance_m": 0.1, "distance_ft": 528, "walking_time": "3 mins", "closest_shelters": "Draughon Library"},
    {"id": 8, "x": 624, "y": 390, "distance_m": 0.1, "distance_ft": 528, "walking_time": "3 min", "closest_shelters": "Haley Center"},
    {"id": 9, "x": 453, "y": 376, "distance_m": 0.4, "distance_ft": 2112, "walking_time": "8 min", "closest_shelters": "Haley Center"},
    {"id": 10, "x": 741, "y": 513, "distance_m": 0.4, "distance_ft": 2112, "walking_time": "8 min", "closest_shelters": "Draughon Library"},
    {"id": 11, "x": 523, "y": 542, "distance_m": 0.5, "distance_ft": 2640, "walking_time": "11 min", "closest_shelters": "Haley Center"},
    {"id": 12, "x": 681, "y": 457, "distance_m": 0.3, "distance_ft": 1584, "walking_time": "6 min", "closest_shelters": "Draughon Library"},
    {"id": 13, "x": 617, "y": 609, "distance_m": 0.6, "distance_ft": 3168, "walking_time": "12 min", "closest_shelters": "Haley Center"},
    #{"id": 14, "x": 0, "y": 0, "distance_m": 0.4, "distance_ft": 2112, "walking_time": "7 min", "closest_shelters": "Greene Hall"},
    #{"id": 15, "x": 0, "y": 0, "distance_m": 0.1, "distance_ft": 528, "walking_time": "2 min", "closest_shelters": "Greene Hall"},
    #{"id": 16, "x": 0, "y": 0, "distance_m": 0.5, "distance_ft": 2640, "walking_time": "11 min", "closest_shelters": "Greene Hall"},
]


# A list of shelter data, including their coordinates and name
shelters_data = [
    # Add each shelter as a dictionary with the relevant information
    {"id": 1, "x": 641, "y": 293, "name": "Haley Center"},
    {"id": 2, "x": 700, "y": 231, "name": "Brown-Kopel"},
    {"id": 3, "x": 782, "y": 316, "name": "Draughon Library"},
    #{"id": 4, "x": 0, "y": 0, "name": "Greene Hall"},

]
# Clears the currently displayed path on the canvas
def clear_path():
    global current_line_id
    if current_line_id:
        delete_path(current_line_id)
        current_line_id = None
# Draws a path on the canvas between the given start and end coordinates
def draw_path(start_x, start_y, end_x, end_y):
    line_id = canvas.create_line(start_x, start_y, end_x, end_y, fill="red", width=4)
    return line_id  # Add this line to return the line_id
# Deletes a path with the given line_id from the canvas
def delete_path(line_id):
    canvas.delete(line_id)
# Shows the information related to the clicked point or shelter and draws the path if needed
def show_info(data):
    global current_line_id
    if current_line_id:
        delete_path(current_line_id)

    if 'distance_m' in data:
        info_var.set(
            f"Distance (M): {data['distance_m']}\nDistance (ft): {data['distance_ft']}\nWalking Time: {data['walking_time']}\nClosest Shelters: {data['closest_shelters']}")
        shelter_data = next((shelter for shelter in shelters_data if shelter['name'] == data['closest_shelters']), None) # Finds the nearest shelter to the geographic point and assigns the found shelter data to the shelter_data variable. If no shelter is found, the value of the shelter_data variable will be None.
        if shelter_data:
            current_line_id = draw_path(data['x'], data['y'], shelter_data['x'], shelter_data['y'])  # Update the current_line_id variable with the returned line_id
    else:
        info_var.set(f"Shelter Name: {data['name']}")
        current_line_id = None

# Creates a button for a point on the canvas with the given point data
def create_point_button(canvas, point_data):
    button = tk.Button(canvas, text=str(point_data['id']), command=lambda: show_info(point_data), bg="DarkOrange1" ) # Anonymous functions are used to avoid immediate execution of the program.
    button.place(x=point_data['x'], y=point_data['y'], anchor=tk.CENTER)
    return button

# Creates a button for a shelter on the canvas with the given shelter data
def create_shelter_button(canvas, shelter_data):
    button = tk.Button(canvas, text=shelter_data['name'], command=lambda: show_info(shelter_data), bg="blue", fg="white" )
    button.place(x=shelter_data['x'], y=shelter_data['y'], anchor=tk.CENTER)
    return button

# Main function that initializes the window, loads the background image, and creates buttons for points and shelters
def window():

    root = tk.Tk()
    root.geometry("900x900")
    root.title("Shelter")



    bg = PhotoImage(file="CampusStormShelters900.png")
    label1 = tk.Label(root, image=bg)
    label1.place(x=0, y=0)

    global current_line_id
    current_line_id = None

    global canvas
    canvas = Canvas(root, width=900, height=900)
    canvas.pack()
    canvas.create_image(0, 0, anchor=tk.NW, image=bg)
    clear_path_button = tk.Button(root, text="Clear Path", command=clear_path)
    clear_path_button.place(x=420, y=840)

    global info_var
    info_var = tk.StringVar()
    font1 = ("Arial", 15)
    info_label = tk.Label(root, textvariable=info_var, anchor=tk.W, justify=tk.LEFT, font=font1)
    info_label.place(x=17, y=610, width=320, height=150)

    for point_data in points_data:
        create_point_button(canvas, point_data)

    for shelter_data in shelters_data:
        create_shelter_button(canvas, shelter_data)

    root.mainloop()




if __name__ == "__main__":
    window()
