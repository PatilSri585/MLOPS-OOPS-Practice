class indiagram:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to indiagram!! How would you like to proceed?
                                1. Press 1 to sign-up
                                2. Press 2 to sign-in
                                3. Press 3 to write a post
                                4. Press 4 to send a message to your friend
                                5. Press any other key to exit
                           
                           
                                ---> """)

        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            self.writepost()
        elif user_input == '4':
            self.message()
        else:
            exit()
            

    def signup(self):
        email = input("Enter your email here:  ")
        password = input("Setup your password here:   ")
        self.username = email
        self.password = password
        print('You have signed up successfully!!!')
        print('\n')
        self.menu()
        print('\n')

    def signin(self):
        if self.username == '' and self.password =='':
            print('Please sign-up by pressing 1 in the main menu')
        else:
            uname = input("Enter your email/User Name here:   ")
            pwd = input('Enter your password here:   ')
            if self.username ==uname and self.password==pwd:
                print('You have signed in successfully!!!')
                self.loggedin = True
            else:
                print("Please enter the correct credentials!!!")
        print('\n')
        self.menu()
        print('\n')

    def writepost(self):
        if self.loggedin == True:
            post = input('Please post here:   ')
            print(f"{self.username} posted : {post}")
        else:
            print('Please sign-in first to post!!!')
        print('\n')
        self.menu()
        print('\n')

    def message(self):
        if self.loggedin == True:
            friend = input('Whom do you ant to send the message:   ')
            message = input("What is your message?:   ")

            print(f"sending the message to {friend}")
        else:
            print('Please sign-in first to post!!!')  
        print('\n')      
        self.menu()
        print('\n')


        
#User1 = indiagram()