from config import Config


config = Config.load_json("config.json")

# Get a single value:
print(config.some_string)  # Returns: "A string"

# Prints all config items, values and the value types
for k, v in config.items():
    print(f"Key: {k}, Value: {v}, Type: {type(v)}")

print(config.missing_value)  # Returns: None
