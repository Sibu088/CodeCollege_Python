# Define a variable 'car' and assign it the string 'Peugeot'
car = 'Peugeot'

# Print a prediction about comparing 'car' to 'Peugeot' (case-sensitive)
print("\nIs car == 'Peugeot'? I predict False.")
# Check if 'car' is equal to 'peugeot' (incorrect case)
print(car == 'peugeot')  # Expected: False

# Print a prediction about comparing 'car' to 'Peugeot' (case-insensitive check)
print("\nIs car == 'Peugeot'? I predict True.")
# Check if 'car' in lowercase is equal to 'peugeot'
print(car.lower() == 'peugeot')  # Expected: True

print('\n')  # Print a newline for separation

# Set age to 21
age = 21
# Check if age is exactly 22
if age == 22:
    print('You can come in!')  # This will not execute
else:
    print("You can't come in!")  # This will execute since age is not 22

print('\n')  # Print a newline for separation

# Set age to 25
age = 25
# Check if age is greater than or equal to 22
if age >= 22:
    print('You can come in!')  # This will execute since age is 25
else:
    print("You can't come in!")  # This will not execute

print('\n')  # Print a newline for separation

# Set age to 25
age = 25
# Check if age is both greater than or equal to 22 and 27 (this condition can't be true)
if age >= 22 and age >= 27:
    print('You can come in!')  # This will not execute
else:
    print("You can't come in!")  # This will execute since both conditions are not met

print('\n')  # Print a newline for separation

# Define a list of dog breeds
dogs = ['shepard', 'chow chow', 'york']
# Check if 'shepard' is in the list of dogs
print('shepard' in dogs)  # Expected: True
# Check if 'york' is in the list of dogs
print('york' in dogs)  # Expected: True
# Check if 'amstaf' is in the list of dogs
print('amstaf' in dogs)  # Expected: False

print('\n')  # Print a newline for separation

# Define a list of dog breeds
dogs = ['shepard', 'chow chow', 'york']
# Set name_dog to 'amstaf'
name_dog = 'amstaf'
# Check if name_dog is not in the list of dogs
if name_dog not in dogs:
    print("it isn't")  # This will execute since 'amstaf' is not in dogs
else:
    print("it is")  # This will not execute
