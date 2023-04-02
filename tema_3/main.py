import json
# import random
import csv
import os

# generate a folder output_data with multiple .json files
output_folder = "output_folder"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


if __name__ == '__main__':

    # read the data from file input.csv
    with open("input.csv") as f:
        dict_reader = csv.DictReader(f)
        cars = list(dict_reader)
        slow_cars = []
        fast_cars = []
        sport_cars = []
        cheap_cars = []
        medium_cars = []
        expensive_cars = []
        for car in cars:
            if int(car["hp"]) < 120:
                slow_cars.append(car)
            elif 120 <= int(car["hp"]) < 180:
                fast_cars.append(car)
            else:
                sport_cars.append(car)
            if int(car["price"]) < 1000:
                cheap_cars.append(car)
            elif 1000 <= int(car["price"]) < 5000:
                medium_cars.append(car)
            else:
                expensive_cars.append(car)
            with open(os.path.join(output_folder, f'{car["brand"]}.json'), "a") as f:
                json.dump(car, f)
    with open(os.path.join(output_folder, "slow_cars.json"), "w") as f:
        for slow_car in slow_cars:
            json.dump(slow_car, f)
            f.write("\n")
    with open(os.path.join(output_folder, "fast_cars.json"), "w") as f:
        for fast_car in fast_cars:
            json.dump(fast_car, f)
            f.write("\n")
    with open(os.path.join(output_folder, "sport_cars.json"), "w") as f:
        for sport_car in sport_cars:
            json.dump(sport_car, f)
            f.write("\n")
    with open(os.path.join(output_folder, "cheap_cars.json"), "w") as f:
        for cheap_car in cheap_cars:
            json.dump(cheap_car, f)
            f.write("\n")
    with open(os.path.join(output_folder, "medium_cars.json"), "w") as f:
        for medium_car in medium_cars:
            json.dump(medium_car, f)
            f.write("\n")
    with open(os.path.join(output_folder, "expensive_cars.json"), "w") as f:
        for expensive_car in expensive_cars:
            json.dump(expensive_car, f)
            f.write("\n")

    # deleting the empty files
    output_dir_path = os.path.abspath(output_folder)
    for file_name in os.listdir(output_dir_path):
        if file_name.endswith(".json"):
            file_path = os.path.join(output_dir_path, file_name)
            if os.path.getsize(file_path) == 0:
                os.remove(file_path)
