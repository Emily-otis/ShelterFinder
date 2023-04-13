import tkinter as tk
from tkinter import Canvas
from tkinter import PhotoImage
from tkinter import messagebox
import data

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
def show_info(data, shelters_data):
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
def create_point_button(canvas, point_data, shelters_data):
    button = tk.Button(canvas, text=str(point_data['id']), command=lambda: show_info(point_data, shelters_data), bg="DarkOrange1" ) # Anonymous functions are used to avoid immediate execution of the program.
    button.place(x=point_data['x'], y=point_data['y'], anchor=tk.CENTER)
    return button

# Creates a button for a shelter on the canvas with the given shelter data
def create_shelter_button(canvas, shelter_data, shelters_data):
    button = tk.Button(canvas, text=shelter_data['name'], command=lambda: show_info(shelter_data, shelters_data), bg="blue", fg="white" )
    button.place(x=shelter_data['x'], y=shelter_data['y'], anchor=tk.CENTER)
    return button

# Main function that initializes the window, loads the background image, and creates buttons for points and shelters
def window(points_data, shelters_data):
    # Initialize the root window
    root = tk.Tk()
    root.geometry("900x900")
    root.title("Shelter")

    # Load the background image
    bg = PhotoImage(file="CampusStormShelters900.png")
    label1 = tk.Label(root, image=bg)
    label1.place(x=0, y=0)

    global current_line_id
    current_line_id = None

    # Clears the information in the info label
    def clear_info():
        info_var.set("")

    # Create the canvas for the map
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

    # Creates a button to clear the info label
    clear_info_button = tk.Button(root, text="Clear Info", command=clear_info)
    clear_info_button.place(x=500, y=840)

    for point_data in points_data:
        create_point_button(canvas, point_data, shelters_data)

    for shelter_data in shelters_data:
        create_shelter_button(canvas, shelter_data, shelters_data)

    root.mainloop()




# Defines the main_window function that creates a new window to launch the map application
# The function takes three arguments: launch_callback, points_data, and shelters_data
def main_window(launch_callback, points_data, shelters_data):
    # Creates a new window with the specified size and title

    main_win = tk.Tk()
    main_win.geometry("1280x914")

    bgMain = PhotoImage(file="TitleSreenFrontPage2.png")
    label2 = tk.Label(main_win, image=bgMain)
    label2.place(x=0, y=0)

    main_win.title("main")
    # Creates a label with a welcome message and places it on the main window
    description_label = tk.Label(main_win, text="Welcome to the map application. \nThis app provides the nearest storm shelter when you encounter a storm. \n"
                                                "There are multiple locations and three storm shelters available. \nWhen you click on a location, the distance and other related information "
                                                "will be displayed in the bottom left corner. \nClick the options below to get started.", font=("Arial", 10), fg="blue")
    description_label.place(x=500, y=42)
    # Creates a button for visitors and assigns a lambda function that calls the launch_callback function with the points and shelters data as arguments
    visitor_button = tk.Button(main_win, text="Find Shelter", command=lambda: [main_win.destroy(), launch_callback(points_data, shelters_data)],  bg="red", fg="white", font=("Arial", 8))
    visitor_button.place(x=800, y=150)
    # Starts the main loop of the main window
    main_win.mainloop()