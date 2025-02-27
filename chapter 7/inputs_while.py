count = 0  # Initialize the counter
while count < 1:  # Loop runs once as long as count is less than 1
    character = random.choice(characters)  # Pick a random character
    action = random.choice(actions)  # Pick a random action
    place = random.choice(places)  # Pick a random place
    
    print(f"{character} {action} {place}.")  # Print the generated sentence
    
    count += 1  # Increment the counter to end the loop