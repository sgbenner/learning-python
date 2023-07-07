
import pandas as pd

squirrels_df = pd.read_csv("squirrel_data.csv")


gray = squirrels_df[squirrels_df["Primary Fur Color"] == "Gray"]
cinnamon = squirrels_df[squirrels_df["Primary Fur Color"] == "Cinnamon"]
black = squirrels_df[squirrels_df["Primary Fur Color"] == "Black"]

results = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [len(gray), len(cinnamon), len(black)]
}

results_df = pd.DataFrame(results)
results_df.to_csv("squirrel_count.csv")

print(results_df)
