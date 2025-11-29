import pandas as pd

bios = pd.read_csv("./data/bios.csv")
print(bios.loc[(bios["height_cm"] > 210) & (
    bios["born_country"] == "GBR"), ["name", "born_country", "height_cm"]])
