import json

def process_json(data: dict, filenmae: str) -> dict:

    # Step 1: Serialize (save) the dictionary to a JSON file
    with open(filename, 'w') as file:
        json.dump(data, file, indent = 4)

    # Step 2: Deserialize (read) the JSON file back into a dictionary
    with open(filename, 'r') as file:
        loaded_data = json.load(file)

    # Step 3: Return the dictionary that was read back
    return loaded_data


# Example usage
data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
filename = 'data.json'  
result = process_json(data, filename)
print(result)


