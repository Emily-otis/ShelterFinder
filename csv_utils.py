import csv

# Writes points data to a CSV file
def write_points_to_csv(filename, points_data):
    # Open the CSV file in write mode with UTF-8 encoding
    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        # Define the fieldnames for the CSV file
        fieldnames = ['id', 'x', 'y', 'distance_m', 'distance_ft', 'walking_time', 'closest_shelters']
        # Create a CSV writer object with the defined fieldnames
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # Write the header row
        writer.writeheader()
        # Write each row of point data
        for point in points_data:
            writer.writerow(point)

# Writes shelters data to a CSV file
def write_shelters_to_csv(filename, shelters_data):
    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'x', 'y', 'name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for shelter in shelters_data:
            writer.writerow(shelter)

# Reads points data from a CSV file and returns it as a list of dictionaries
def read_points_data(filename):
    points_data = []
    # Open the CSV file in read mode
    with open(filename, newline='') as csvfile:
        # Create a CSV reader object
        reader = csv.DictReader(csvfile)
        # Read each row of data as a dictionary and append it to the list of points data
        for row in reader:
            points_data.append(row)

    # Convert string values to appropriate data types
    for point in points_data:
        point["id"] = int(point["id"])
        point["x"] = int(point["x"])
        point["y"] = int(point["y"])
        point["distance_m"] = float(point["distance_m"])
        point["distance_ft"] = int(point["distance_ft"])

    return points_data

# Reads shelters data from a CSV file and returns it as a list of dictionaries
def read_shelters_data(filename):
    shelters_data = []

    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            shelters_data.append(row)

    for shelter in shelters_data:
        shelter["id"] = int(shelter["id"])
        shelter["x"] = int(shelter["x"])
        shelter["y"] = int(shelter["y"])

    return shelters_data
