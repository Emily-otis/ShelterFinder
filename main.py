from gui import main_window, window
from data import points_data, shelters_data
from csv_utils import write_points_to_csv, write_shelters_to_csv, read_points_data, read_shelters_data

#Define function to launch the map window
def launch_map_window(points, shelters):
    window(points, shelters)

if __name__ == "__main__":
    # Write data to CSV files
    write_points_to_csv("points.csv", points_data)
    write_shelters_to_csv("shelters.csv", shelters_data)

    # Read data from CSV files
    points_data_from_csv = read_points_data("points.csv")
    shelters_data_from_csv = read_shelters_data("shelters.csv")

    # Launch the main_window function with data read from CSV files
    main_window(launch_map_window, points_data_from_csv, shelters_data_from_csv)
