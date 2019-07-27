import string
import os
import time
import datetime


# Login authorization
def loginauth(username, password):
    '''
    * Confirms that the username exists and that the password is correct for that username
    * @param(str) username -- the username
    * @param(str) password -- the password
    * @return(bool) True -- if successful login
    * @return(bool) False -- if unsucessful logic (either username does not exist, or password is incorrect)
    
    '''
    for line in open("accountfile.txt","r").readlines(): # Read the lines
        login_info = line.split() # Split on the space, and store the results in a list of two strings
        if username == login_info[0] and password == login_info[1]:
            return True
    return False



# Login a USER
def login():
    '''
    @username - asking user to enter username with which they want to login
    @password - asking user to enter password with which they want to login
    @account.txt - file where username/passwords are stored for verification whether username/ password
                    macthes or Not
    @loginauth(username,password)  - function called for authentication
    @session(username) - After successful authentication, user will b logged in to their a/c 
    '''
    while True:
        username = input("Enter Username: ")
        if not len(username) > 0:
            print("Username can't be blank\n")
            continue
        else:
            flag = False
            file_name = "accountfile.txt"
            if not os.path.isfile(file_name):
                fp=open(file_name, 'w+')
                fp.close()


            for line in open(file_name,"r").readlines():
                login_info = line.split()
                if username == login_info[0]:
                    flag = True
                    break
            if not flag:
                print("Username doesn't exist...\nKindly Enter correct Username or register\n")

            while True and flag:
                password = input("Enter Your Password: ")
                if not len(password) > 0:
                    print("Password can't be blank\n")
                    continue
                if loginauth(username, password):
                    return session(username)
                else:
                    print("\nIncorrect credentials...\n")
            break



# Registering a USER
def register():
    '''
    Here We are registering a new User with username and password
    And if user doesn't enter anything in username field(means blank) then error will be shown to enter again
    if user enters something then we will b checking whether that name is available or taken

    *@accountfile.txt - storing username and password in this file for verification.
    '''
    while True:
        username = input("Enter username: ")
        if not len(username) > 0:
            print("Username can't be blank...\n")
            continue
        else:
            flag = False
            for line in open("accountfile.txt","a+").readlines():
                login_info = line.split()
                if username.lower() == login_info[0].lower():
                    print("Username already taken...\n")
                    flag = True
                    break
            if flag:
                continue
            break


    while True:
        password = input("Enter Your password: ")
        if not len(password) > 0:
            print("Password can't be blank...\n")
            continue
        break

    print("Creating account...")
    acfile = open("accountfile.txt","a")
    acfile.write(username)
    acfile.write(" ")
    acfile.write(password)
    acfile.write("\n")
    acfile.close()
    os.makedirs(username)
    time.sleep(1)
    print("Account has been created!\n")

    if loginauth(username, password):
        return session(username)




# User session
def session(username):
    '''
    *@param(str) username - the username we're getting from user inputs to create a folder name as same as username
    * Here we are asking whether to view Old journals or wants to create a new One
    *@ options (in select option) -
        write 1 or view - to see previous/old journals
        write 2 or create - to create new journal
        write 3 or logout - to logout from the application
    '''
    print("You are now logged in...")
    print("Welcome to your account " + username)
    
    while True:
        print("\nChoose what do You want? \n1) View Old Journals(view) \n2) Create New One(create) \n3) Logout")
        option = input("Select Option > ").lower()

        if option == "view" or option=="1":
            view_journal(username)
        elif option == "create" or option=="2":
            create_journal(username)
        elif option == "logout" or option =="3":
            print("Logging out...")
            break
        else:
            print(option + " is not a valid option...")
    


def create_journal(username):
    '''
    Creating journal while user chooses to create journal
    *@param(str) username  -> passing username from user inputs to create journal file
    *@file_name -> here we're creating a journal file with the name same as username inside a folder
                   name same as username which is specific to particular user only
                   And adding .txt after username
     example - if username is dev then his journal file name will become dev.txt 
    '''
    parent_dir = os.getcwd()+'/'+username+'/'
    file_name = os.path.join(parent_dir, username+".txt")
    write_file(file_name)
    print('Journal successfully created...')
            


def write_file(file_name):
    '''
    *@ param(str) file_name - the file name we created in above function
    writing contents to the file when a user click to create
    '''

    with open(file_name, 'a+') as my_file:
        content = input('Write journal:> ')

        if len(content) > 0:
            date_time = datetime.datetime.now()
            my_file.write(date_time.strftime("%d %b %y %I.%M%p"))
            my_file.write(' --> ')
            my_file.write(f'{content} \r')
            my_file.close()
        else:
            print('Write something in Journal...')



def view_journal(username):
    '''
    retrieving journals written by corresponding user
    '''
    parent_dir = os.getcwd()+'/'+username+'/'
    file_name = os.path.join(parent_dir, username+".txt")
    print_journals(file_name)


def print_journals(file_name):
    '''
    printing the jounals when user clicks to view journal
    '''
    print('\n<<<<<<<<<<<<<< Start jounal >>>>>>>>>>>>>>\n')
    read_lines(file_name)
    print('<<<<<<<<<<<<<< End jounal >>>>>>>>>>>>>>')


def read_lines(file_name):
    '''
    retrieving each lines/journals written by the user
    checking if a single user has 50 records or more
    if more than 50 records then show
    '''
    if not os.path.isfile(file_name):
        open(file_name, 'w+')


    with open(file_name, 'r') as my_file:
        lines = my_file.readlines()
        
        if(len(lines)>50):
            start_index = len(lines)-50
        else:
            start_index = 0

        for idx, line in enumerate(lines[start_index:]):
            print("%d) %s" % (idx+1, line))




#Start of the program
print("\n***********************************************************")
print("Welcome to the Journal system. Please Register or Login!")

while True:
    '''
    Taking inputs from user whether to register/ login /exit
    *@ options (in select option) -
        write 1 or register - to register user
        write 2 or login - to login user into the system
        write 3 or exit  - to exit from the application
    '''
    print("Choose What do You want ?\n1) Register \n2) Login \n3) Exit")
    option = input("Select Option > ").lower()
    if option == "1" or option=="register":
        register()
    elif option == "2" or option=="login":
        login()
    elif option == "3" or option=="exit":
        break
    else:
        print(option + " is not a valid option")



# close of application
print("Application is Shutting down...")
