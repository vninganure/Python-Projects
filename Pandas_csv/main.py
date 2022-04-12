import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_furr_sqr = len(data[data["Primary Fur Color"] == "Gray"])
red_furr_sqr = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_furr_sqr = len(data[data["Primary Fur Color"] == "Black"])

data_dic = {
    "Fur color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_furr_sqr, red_furr_sqr, black_furr_sqr]
}

df = pandas.DataFrame(data_dic)
df.to_csv("squirrel_count.csv")
