import csv
import time
import uuid
import pickle
from chirp import *
from user import *

class Birdyboard:

    def __init__(self):
        self.users = []
        with open('userList', 'rb') as f:
            deserialized = pickle.load(f)

        self.chirps = []

    def birdy_menu(self):
        print("-----------------------------------------")
        print("--      Welcome to Birdyboard~~~~~     --")
        print("-----------------------------------------")
        print("1. New User Account")
        print("2. Select User")
        print("3. View Chirps")
        print("4. Public Chirp")
        print("5. Private Chirp")
        print("6. Exit")
        choice = input("> ")

        try:
            if int(choice) > 0 and int(choice) < 7:

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
                    print("#3: You chose to view chirps!")
                    chirp = self.view_chirps()
                    # self.print_results

                if choice == "4":
                    print("#4: You chose public chirp!")
                    pub = self.public_chirp()
                    # self.print_results

                if choice == "5":
                    print("#5: You chose private chirp!")
                    priv = self.private_chirp()
                    # self.print_results

                if (choice == "6"):
                    print("Until next time!")
                    raise SystemExit()

        except ValueError:
            print("Please enter a number for your choice")
        self.birdy_menu()




    def new_user_create(self):
        print("Enter Full Name")
        nuName = input("Name: ")
        print("Enter Screen Name")
        nuSN = input("SN: ")

        newUser = User(nuName, nuSN)
        self.users.append(newUser)

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

            print(self.users[userSel])

        except:
            print("Error")





    def view_chirps(self):
        pass

    def public_chirp(self):
        pass

    def private_chirp(self):
        pass

    # def combined_users_dict(self):
    #     fullnames = self.users()
    #     screennames = self.users()




if __name__ == "__main__":
  birdy = Birdyboard()
  birdy.birdy_menu()
