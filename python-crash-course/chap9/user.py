class User():
    """A class representing a basic user"""

    def __init__(self, first_name, last_name):
        """Initialize user with first name and last name"""
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self):
        """Returns name in a nice format"""
        full_name = self.first_name.title() + " " + self.last_name.title()
        return full_name