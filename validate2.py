import re
import uuid


class UserDetails(object):
    #innitialization 
    def __init__(self):
        #A list to hold users
        self.user_list = []

    def register(self, username, email, password, confirm_password):

        #A dictionary to hold user details
        user_details = {}

        #Check if there is any user in the list
        if len(self.user_list) > 0:
            for user in self.user_list:
                if username == user['username'] and email == user['username']:
                    return "Username or email already exist"
                else:
                    #validate user details
                    if not re.match("^[a-zA-Z0-9_]*$", username)\
                    or not re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
                        return "Username or email can only contain alphanumeric characters"  
                    elif len(username.strip()) < 6:
                        return "Username should be atleast six characters long"
                    elif len(password) < 6:
                        return "Your password should be atleast six characters long"
                    elif password != confirm_password:
                        return "Your passwords should match"
                    else:
                        #register the user if all the details are correct
                        user_details['username'] = username
                        user_details['email'] = email
                        user_details['password'] = password
                        user_details['confirm_password'] = confirm_password
                        self.user_list.append(user_details)
        
        # There are no users in the list
        else:    
            if len(self.user_list) == 0:
            #validate users details
                if not re.match("^[a-zA-Z0-9_]*$", username)\
                or not re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
                    return "Username or email can only contain alphanumeric characters"
                elif len(username.strip()) < 6:
                    return "Username should be atleast six characters long"
                elif len(password) < 6:
                    return "Password should be atleast six characters long"
                elif password != confirm_password:
                    return "Your Passwords should match"

                #Register the user if all the details are correct
                else:
                    user_details['username'] = username
                    user_details['email'] = email
                    user_details['password'] = password
                    user_details['confirm_password'] = confirm_password
                    user_details['id'] = uuid.uuid1()
                    self.user_list.append(user_details)
                    return "registration for the first user in the program successfull"

def run():
    Rafael = UserDetails()    
    response = Rafael.register("kelraf", "rafwambugu@gmail.com", "kelraf11746", "kelraf11746")  
    print(response)  
    Rafael = UserDetails()
    response = Rafael.register("kelraf", "rafwambugu@gmail.com", "kelraf11746", "kelraf11746")
    print(response)     

if __name__ == "__main__":
    run()        