# List of available rental cars
available_cars = ['Subaru', 'Toyota', 'Ford', 'BMW', 'Honda']

# Display the list of available cars to the user
print("Here are the available rental cars:")
for car in available_cars:
    print(f"- {car}")

# Ask the user which car they would like to rent
car = input("Which car would you like to rent? ")

# Check if the chosen car is in the list of available cars
if car.title() in available_cars:
    print(f"Let me see if I can find you a {car.title()}.")
else:
    print("Sorry, that car is not available.")