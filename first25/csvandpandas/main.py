#with open("weather_data.csv") as wheater:
#    data = wheater.readlines()
#    print(data)
#import csv
#
#with open("weather_data.csv") as data_file:
#    data = csv.reader(data_file)
#    temperatures = []
#    for row in data:
#        if row[1] != 'temp':
#            temperatures.append(int(row[1]))
#    print(temperatures)
    
#import pandas
#
#data = pandas.read_csv("weather_data.csv")
#print(data["temp"])

#data_dict = data.to_dict()
#print(data_dict)

#temp_list = data["temp"].to_list()

#Get data in columns
#print(data["temp"].mean())
#print(data.temp.max())

#Get data in rows
#print(data[data.day == "Monday"])
#print(data[data.temp == data.temp.max()])

#monday = data[data.day == "Monday"]
#fahrenheit = (monday.temp[0] * 9/5) + 32
#print(fahrenheit)

#Create dataframe from scratch
#data_dict = {
#    "students": ["Amy", "James", "Angela"],
#    "scores": [76, 56, 65]
#}

#Create csv
#data = pandas.DataFrame(data_dict)
#data.to_csv("data.csv")

#DataFrame(all the table) and series[1 column]

import pandas 

data = pandas.read_csv("Squirrels_Central_Park.csv")
squirrels_total = data["Primary Fur Color"]
squirrels_gray = len(data[squirrels_total == "Gray"])  
squirrels_cinnamon = len(data[squirrels_total == "Cinnamon"]) 
squirrels_black = len(data[squirrels_total == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [squirrels_gray, squirrels_cinnamon, squirrels_black]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Squirrels_Count.csv")

