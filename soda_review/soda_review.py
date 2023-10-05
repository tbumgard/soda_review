# Backend for Soda Review
import time
# Load master list for Sodas from database or file(testing locally- while developing)
# Load master list for Users from database or file (testing locally- while developing)
# Load master list for Reviews from database or file (testing locally- while developing)

# User Class
class User:
    #username
    #password
    #email
    #picture - optional
    #first name - optional
    #last name - optional
    #join date
    #list of submitted reviews
    #number of reviews done    
    	
    def __init__(self, user_name, password, email, picture=None, first_name=None, last_name=None):
        self.__user_name = user_name
        self.__password = password
        self.__email = email
        self.__picture = picture
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_joined = None
        self.__reviews = []
        self.__number_of_reviews = 0
    
    def __repr__(self):
        return f"\nUsername: {self.__user_name}\nPassword: {self.__password}\nEmail: {self.__email}\nFirst Name: {self.__first_name}\nLast Name: {self.__last_name}\n"
    
    # Start of getter functions
    def get_user_name(self):
        return self.__user_name
    
    def get_password(self):
        return self.__password
    
    def get_email(self):
        return self.__email
    
    def get_picture(self):
        return self.__picture
    
    def get_first_name(self):
        return self.__first_name
    
    def get_last_name(self):
        return self.__last_name
    
    def get_date_joined(self):
        return self.__date_joined
    
    def get_reviews(self):
        return self.__reviews
    
    def get_number_of_reviews(self):
        return self.__number_of_reviews
    # End of getter functions

# Soda Class
    #name
    #company
    #picture
    #list of reviews
    #average review rating
    #average weighted review rating

# Review Class
    #Soda
    #User 
    #Review
    #Rating
    #Up votes
    #Down votes


def main():

    user1 = User('tbumgard', 'qwerty123', 'tbumgard@gmail.com', first_name='Trevor', last_name='Bumgardner')
    print(user1)

main()

