# Weather Recommendation Program

# Prompt user for weather input
weather = input("What's the weather like today? (sunny/rainy/cold): ")

# Convert input to lowercase for case-insensitive comparison
weather = weather.lower()

# Provide clothing recommendations based on weather condition
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")