from user import user_profile

def my_login():
    """Handles user login authentication."""
    logged_in = False

    while not logged_in:
        print("Please Login:")
        un = input("What is your Username: ").strip()
        pw = input("What is your Password: ").strip()

        if un == user_profile.get("username") and pw == user_profile.get("password"):
            logged_in = True
            print(f"Here is your profile:\n{user_profile}")
        else:
            print("False entry.")