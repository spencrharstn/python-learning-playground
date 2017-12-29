class User():
    """A class representing a basic user"""

    def __init__(self, first_name, last_name):
        """Initialize user with first name and last name"""

        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name[0] + last_name + "@company.com"
        self.login_attempts = 0

    def get_name(self):
        """Returns name in a nice format"""

        full_name = self.first_name.title() + " " + self.last_name.title()
        return full_name

    def get_email(self):
        """Returns the email address of the user"""

        return self.email

    def increment_login_attempts(self):
        """Increment number of login attempts"""

        self.login_attempts += 1
        print("Login attempts: {:d}".format(self.login_attempts))

    def reset_login_attempts(self):
        """Reset number of login attempts"""

        self.login_attempts = 0
        print("Login attempts: {:d}".format(self.login_attempts))

class Admin(User):
    """A class for a special type of user, an admin"""

    def __init__(self, first_name, last_name):
        """Initialize the user with admin rights"""
        super().__init__(first_name,last_name)
        self.privileges = Privileges() 

class Privileges():
    """A class representing privileges available to a user"""

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show(self):
        """List the privileges of an admin"""

        for p in self.privileges:
            print(" - " + p)