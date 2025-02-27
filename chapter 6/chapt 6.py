#making a dict with names for keys and programming langs for values
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'Javascript',
 }

#making a for loop that itterates ofver the values of 
#the favorite_languages dict using the .value() dict method
for name in favorite_languages.values():
    #every value will be checked to see if it says js, and when it is it will print forbidden
    if name == "Javascript":
        print("Forbidden...")
    #else it will print the name and noice
    else:
        print(f"{name}, noice")