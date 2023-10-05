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
        self.__date_joined = time.asctime()
        self.__reviews = []
        self.__number_of_reviews = 0
    
    def __repr__(self):
        return (f"Username: {self.__user_name}\nPassword: {self.__password}\nEmail: {self.__email}\n" + 
                f"First Name: {self.__first_name}\nLast Name: {self.__last_name}\nDate Joined: {self.__date_joined}\n")
    
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

    # Start of setter functions
    def set_user_name(self, user_name):
        self.__user_name = user_name
        return self.__user_name
    
    def set_password(self, password):
        self.__password = password
        return self.__password
    
    def set_email(self, email):
        self.__email = email
        return self.__email
    
    def set_picture(self, picture):
        self.__picture = picture
        return self.__picture
    
    def set_first_name(self, first_name):
        self.__first_name = first_name
        return self.__first_name
    
    def set_last_name(self, last_name):
        self.__last_name = last_name
        return self.__last_name
 
    def add_review(self, review):
        self.__reviews.append(review)
        self.__number_of_reviews += 1
    # End of setter functions   

# Soda Class
class Soda:
    #name
    #company
    #picture
    #list of reviews
    #average review rating
    #average weighted review rating
    def __init__(self, name, company=None, picture=None):
        self.__name = name
        self.__company = company
        self.__picture = picture

    def __repr__(self):
        return f"Soda Name: {self.__name}\nSoda Company: {self.__company}\n"

    # Start of getter functions
    def get_name(self):
        return self.__name
    
    def get_company(self):
        return self.__company
    
    def get_picture(self):
        return self.__picture
    # End of getter functions

    # Start of setter functions
    def set_name(self, name):
        self.__name = name
        return self.__name
    
    def set_company(self, company):
        self.__company = company
        return self.__company
    
    def set_picture(self, picture):
        self.__picture = picture
        return picture
    # End of setter functions

# Review Class
class Review:
    #Soda
    #User 
    #Review
    #Rating
    #Upvotes
    #Downvotes
    def __init__(self, soda, user, review, rating):
        self.__soda = soda
        self.__user = user
        self.__review = review
        self.__rating = rating
        self.__upvotes = 0
        self.__downvotes = 0

    def __repr__(self):
        return (f"{self.__soda}\n{self.__user}\nReview: {self.__review}\nRating: {self.__rating}/10\n" +
                f"Upvotes: {self.__upvotes}\nDownvotes: {self.__downvotes}")
    
    # Start of getter functions
    def get_soda(self):
        return self.__soda
    
    def get_user(self):
        return self.__user
    
    def get_review(self):
        return self.__review
    
    def get_rating(self):
        return self.__rating
    
    def get_upvotes(self):
        return self.__upvotes
    
    def get_downvotes(self):
        return self.__downvotes
    # End of getter functions

    # Start of setter functions
    def set_soda(self, soda):
        self.__soda = soda
        return self.__soda
    
    def set_user(self, user):
        self.__user = user
        return self.__user
    
    def set_review(self, review):
        self.__review = review
        return self.__review
    
    def set_rating(self, rating):
        self.__rating = rating
        return self.__rating
    
    def add_upvote(self):
        self.__upvotes += 1
        return self.__upvotes
    
    def add_downvote(self):
        self.__downvotes += 1
        return self.__downvotes
    # End of setter functions


def main():

    print("REGISTER NEW USER")
    user1 = User('tbumgard', 'qwerty123', 'tbumgard@gmail.com', first_name='Trevor', last_name='Bumgardner')
    print(user1)

    print("REGISTER NEW SODA")
    soda1 = Soda("Coke", "Coca-Cola", None)
    print(soda1)

    print("---------------------------------------------------------------------------------------------")
    print("REGISTER NEW SODA REVIEW")

    review1 = Review(soda1, user1, "THIS IS THE BOMB", 10)
    print(review1)
    

main()

