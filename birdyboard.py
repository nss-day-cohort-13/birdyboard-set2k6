import os
import time
import pickle
from chirp import *
from user import *

class Birdyboard:

    def __init__(self):
        """Initialization
        """
        self.current_user = None


        self.users = []
        with open('userList', 'rb') as f:
            deserialized = pickle.load(f)

        self.chirps = []
        with open('chirpList', 'rb') as c:
            deserialized = pickle.load(c)


    def page_clear(self):
        """ This clears the page when called

        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def birdy_menu(self):

        # while True:
        self.page_clear()
        if not self.current_user:
            print('No Current User')

        else:
            print('Current user: ', self.current_user.screen_name)

        print("-----------------------------------------")
        print("--      Welcome to Birdyboard~~~~~     --")
        print("-----------------------------------------")
        print("1. New User Account")
        print("2. Select User")
        print("3. Chirp")
        print("4. View Chirps")
        print("5. Exit BirdyBoard")
        choice = input("> ")

        try:
            if int(choice) > 0 and int(choice) < 6:

                # if choice != "6":
                #     print("")
                #     print("What would you like to do?")
                #     count = input("> ")

                if (choice == "1"):
                    print("#1: You chose to create a New User Account!")
                    userNew = self.new_user_create()
                    # self.print_results

                if choice == "2":
                    print("#2: You chose to select a user!")
                    userSel = self.select_user()
                    # self.print_results

                if choice == "3":
                    if not self.current_user:
                        print('Please create or select a user')
                        time.sleep(1)
                    # continue
                    else:
                        print("#3: You chose make a new chirp!")
                        chirp = self.create_chirps()
                    # self.print_results

                if choice == "4":
                    if not self.current_user:
                        print('Please create or select a user')
                        time.sleep(1)
                        # continue
                    else:
                        print("#4: You chose view chirps!")
                        pub = self.view_chirps()
                        # self.print_results

                if (choice == "5"):
                    print("Until next time!")
                    quit()
                    # raise SystemExit()

        except ValueError:
            print("Please enter a number for your choice")
            time.sleep(3)
        self.birdy_menu()




    def new_user_create(self):
        print("Enter Full Name")
        nuName = input("Name: ")
        print("Enter Screen Name")
        nuSN = input("SN: ")

        newUser = User(nuName, nuSN)
        self.current_user = newUser
        self.users.append(self.current_user)

        with open('userList', 'wb+') as f:
            pickle.dump(self.users, f)

        print("New User Created.")
        time.sleep(1)
        self.select_user()


    def select_user(self):
        with open('userList', 'rb') as f:
            self.users = pickle.load(f)
        # for user in self.users:
            # print('FullName:',user.full_name,'ScreenName:',user.screen_name)


        userCounter = 0
        for user in enumerate(self.users):
            print("{0}. {1}".format(user[0]+1, user[1].screen_name))

        print("........................")
        print("Which User is Chirping?")
        print("........................")
        userSel = input("> ")

        try:
            userSel = int(userSel)
            self.current_user = self.users[userSel-1]
            time.sleep(1)
            self.birdy_menu()

        except ValueError:
            print("Error......$$$")
            time.sleep(1.5)


    def create_chirps(self):
        print("Enter New Chirp")
        nuChirp = input("Chirp: ")

        newChirp = Chirp(nuChirp, User)
        self.chirps.append(newChirp)


        with open('chirpList', 'wb+') as c:
            pickle.dump(self.chirps, c)

        print("New Chirp Created!")
        time.sleep(1)
        self.birdy_menu()

    def load_chirps(self):
        with open('chirpList', 'rb') as c:
            return pickle.load(c)



    def view_chirps(self):
        self.chirps = self.load_chirps()

        chirpCounter = 0
        for chirp in enumerate(self.chirps):
            print("{0}. {1}".format(chirp[0]+1, chirp[1].message))

        print("........................")
        print("Like what you see here?")
        print("What would you like to do next?")
        print("........................")
        print("1. Make a new chirp!")
        print("2. Back to Main Menu.")
        print("3. Exit BirdyBoard.")
        userSel2 = input("> ")

        try:
            if int(userSel2) > 0 and int(userSel2) < 4:

                if (userSel2 == "1"):
                    print("#1: You chose to make a new chirp!")
                    userNew = self.create_chirps()

                if (userSel2 == "2"):
                    print("#2: Back to main menu!")
                    time.sleep(1.5)
                    mainthang = self.birdy_menu()

                if (userSel2 == "3"):
                    print("Until next time!")
                    # time.sleep(1)
                    quit()
                    # raise SystemExit()

        except ValueError:
            print("Uh oh...")
            exit()

    # def combined_users_dict(self):
    #     fullnames = self.users()
    #     screennames = self.users()




if __name__ == "__main__":
  birdy = Birdyboard()
  birdy.birdy_menu()
