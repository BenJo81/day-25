import pandas

# data = pandas.read_csv("weather_data2.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data["temp"].max())
#
# # Get Data in Columns
# print(data.condition)

# Get Data in a Row
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(int((monday.temp) * (9/5) + 32))
#
# # Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

