# passwd.py

def change_password(username, current_password, new_password, passwd_file):
    """
    Changes the password for a user in the password file.

    This function takes a username, the current password, the new password, and the path to
    the password file as parameters. It reads all lines from the password file, updates
    the password if the specified conditions are met, and writes the modified content back to the file.

    Parameters:
    - username (str): The username of the user whose password needs to be changed.
    - current_password (str): The current password of the user.
    - new_password (str): The new password to be set for the user.
    - passwd_file (str): The path to the password file.

    Returns:
    None
    """
    # Read all lines from the password file
    with open(passwd_file, 'r') as file:
        lines = file.readlines()

    # Write back to the password file, updating the password if conditions are met
    with open(passwd_file, 'w') as file:
        for line in lines:
            # Split the line into parts using colon as a separator
            parts = line.split(":")

            # Check if the current line corresponds to the specified username
            # and if the current password matches the existing password
            if parts[0] == username and parts[2].strip() == current_password:
                # Write the updated password to the file
                file.write(f"{username}:{parts[1]}:{new_password}\n")
                print("Password changed.")
            else:
                # Write the line as it is to the file
                file.write(line)

if __name__ == "__main__":
    # Get user input for username and passwords
    username = input("User: ")
    current_password = input("Current Password: ")
    new_password = input("New Password: ")
    confirm_password = input("Confirm: ")
   
    # Check if the new and confirm passwords match 
    if new_password == confirm_password:
        # Define the path to the password file
        passwd_file = "passwd.txt"
        # Call the change_password function
        change_password(username, current_password, new_password, passwd_file)
    else:
        print("Passwords do not match.")
