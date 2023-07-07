#
# with open("weather_data.csv") as file:
#     data = file.readlines()
#
# for row in data:
#     print(row.strip())
import pandas
# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#
#     print(data.temp)
#
#     temperatures = []
#
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# print(temperatures)


import pandas as pd

data = pd.read_csv("weather_data.csv")

monday_temp = data[data.day == "Monday"].temp
monday_temp_f = (monday_temp * 9/5) + 32


print(monday_temp_f)

# temp_list = data.temp.to_list()


# print(data[data.temp == max_temp].day)

data_dict = {
    "students": ["Amy", "Jesse", "Steven"],
    "scores": ["94", "92", "93"]
}

students_df = pandas.DataFrame(data_dict)
students_df.to_csv("students.csv")
