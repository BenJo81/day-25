import pandas

# data = pandas.read_csv("weather_data2.csv")
# print(data["temp"])
#
# # data_dict = data.to_dict()
# # print(data["temp"].max())
# #
# # # Get Data in Columns
# # print(data.condition)
#
# # Get Data in a Row
# # print(data[data.temp == data.temp.max()])
# #
# # monday = data[data.day == "Monday"]
# # print(int((monday.temp) * (9/5) + 32))
# #
# # # Create a dataframe from scratch
# # data_dict = {
# #     "students": ["Amy", "James", "Angela"],
# #     "scores": [76, 56, 65]
# # }
# # data = pandas.DataFrame(data_dict)
# # data.to_csv("new_data.csv")
#
# print(data[data.temp == data.temp.max()])

gray = 0
cinnamon = 0
black = 0

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240208.csv")
fur_color = data["Primary Fur Color"]

for color in fur_color:
    if color == "Gray":
        gray += 1
    elif color == "Cinnamon":
        cinnamon += 1
    elif color == "Black":
        black += 1

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black]
}

data2 = pandas.DataFrame(data_dict)
data2.to_csv("squirrel_count")