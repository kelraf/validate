''' The module defines user details and methods related to it '''
import re, uuid

class UserDetails(object):
    def __init__(self):
        #A list to store users
        self.user_list = []

    #A method to register the users
    def validate_data(self, username, email, password, confirm_password):
        if not re.match("^[a-zA-Z0-9_]*$", username)\
        or not re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            return "Username or email can only contain alphanumeric characters"
        elif len(username.strip()) < 6:
            return "Your username should be atleast six characters long"
        elif len(password) < 6:
            return "Your password should be atleast six characters long" 
        elif password != confirm_password:
            return "Your passwords must match"
        #The user details are valid
        else:
            return True    

    def register(self, username, email, password, confirm_password):
        #A dictionary to store user details
        user_details = {}

        #check if there are users in the list
        if len(self.user_list) > 0:
            #validate user details
            validate = self.validate_data(username, email, password, confirm_password) 
            if validate:
                #The user details are valid
                #Loop through the self.user_list
                #To check if there is a user with similar username and email
                for user in self.user_list:
                    if username == user['username'] or email == user['email']:
                        return "Username or email already exists"
                    else:
                        #register the user with correct user details
                        user_details['username'] = username
                        user_details['email'] = email
                        user_details['password'] = password
                        user_details['confirm_password'] = confirm_password
                        user_details['id'] = uuid.uuid1()
                        self.user_list.append(user_details) 
                        return "user registered successfully" 
            else:
                return validate            
        else:
            #there are no users in the list
            #validate data
            validate = self.validate_data(username, email, password, confirm_password)
            if validate :
                #user details are valid
                user_details['username'] = username
                user_details['email'] = email
                user_details['password'] = password
                user_details['confirm_password'] = confirm_password
                user_details['id'] = uuid.uuid1()
                self.user_list.append(user_details)
                return "user registered successfully"
            else:
                return validate
    #A login method
    def login(self, username, password):
        #loop through the self.user_list to check for user with the given username and password
        for user in self.user_list:
            if username == user['username'] and password == user['password']:
                return user
            else:
                return "Usename and password or both do not exist" 

    #A method to reset user password
    def reset_password(self, username, password, new_password):
        #loop through self.user_list to check if the provided username and password exists
        for user in self.user_list:
            if username == user['username'] and password == user['password']:
                if len(new_password) < 6:
                    return "Your password must be atleast six characters"
                elif new_password == user['password']:
                    return "Your initial password and new password are same (Please input a new password)"
                else:
                    user['password'] = new_password
                    return user['password']    
            else:
                return "You cannot reset password because username or password or both are not details of any user in the program"    

def run():
    Rafael = UserDetails()    
    response1 = Rafael.register("kelraf", "rafwambugu@gmail.com", "kelraf11746", "kelraf11746")  
    print(response1)  
    response2 = Rafael.register("techraf", "techwambugu@gmail.com", "kelraf11746", "kelraf11747")
    print(response2) 
    response3 = Rafael.login("kelraf", "kelraf11746")  
    print(response3) 
    response4 = Rafael.reset_password("kelraf", "kelraf11746", "kelraf11749")
    print(response4)

if __name__ == "__main__":
    run()                    