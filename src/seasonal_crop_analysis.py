import pandas as pd

# Load dataset
data = pd.read_csv("data/Crop_recommendation.csv")

# Summer crops
summer = data[
    (data["temperature"] > 30) &
    (data["humidity"] > 50)
]["label"].unique()

# Winter crops
winter = data[
    (data["temperature"] < 20) &
    (data["humidity"] > 30)
]["label"].unique()

# Rainy crops
rainy = data[
    (data["rainfall"] > 200) &
    (data["humidity"] > 50)
]["label"].unique()

print("\n🌞 Summer Crops")
print(summer)

print("\n❄ Winter Crops")
print(winter)

print("\n🌧 Rainy Crops")
print(rainy)

summary = pd.DataFrame({
    "Season": ["Summer", "Winter", "Rainy"],
    "Number of Crops": [
        len(summer),
        len(winter),
        len(rainy)
    ]
})

print("\nSeason Summary")
print(summary)