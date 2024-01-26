# deluser.py

def delete_user(username, passwd_file):
    """
    Deletes a user from the password file.

    This function takes a username and the path to the password file as parameters.
    It reads all lines from the password file, excluding the specified user.
    It then writes back the modified content to the password file, effectively deleting the user.

    Parameters:
    - username (str): The username of the user to be deleted.
    - passwd_file (str): The path to the password file.

    Returns:
    None
    """
    # Read all lines from the password file
    with open(passwd_file, 'r') as file:
        lines = file.readlines()
        
    # Write back to the password file, excluding the specified user
    with open(passwd_file, 'w') as file:
        for line in lines:
            # Skip the line if it starts with the specified username
            if not line.startswith(username + ":"):
                file.write(line)

if __name__ == "__main__":
    # Get user input for the username to be deleted
    username = input("Enter username: ")
    # Define the path to the password file
    passwd_file = "passwd.txt"
    
    # Call the delete_user function
    delete_user(username, passwd_file)
    # Print a message indicating that the user has been deleted
    print("User Deleted.")
