import yaml

# Load YAML file
with open("user_config.yaml", "r") as file:
    data = yaml.safe_load(file)

# Display data
print("User Info:")
print(f"Name: {data['user']['name']}")
print(f"Level: {data['user']['level']}")
print(f"Mission: {data['user']['mission']}")
print("Interests:")
for interest in data['user']['interests']:
    print(f" - {interest}")