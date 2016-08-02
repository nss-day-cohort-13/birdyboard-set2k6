import csv

class Birdyboard:

    def __init__(self):
        self.userCollection = dict()

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
                    self.print_results

                if choice == "2":
                    print("#2: You chose to select a user!")
                    userSel = self.select_user()
                    self.print_results

                if choice == "3":
                    print("#3: You chose to view chirps!")
                    chirp = self.view_chirps()
                    self.print_results

                if choice == "4":
                    print("#4: You chose public chirp!")
                    pub = self.public_chirp()
                    self.print_results

                if choice == "5":
                    print("#5: You chose private chirp!")
                    priv = self.private_chirp()
                    self.print_results

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

        with open('users.txt', 'a') as newUser_file:
            users.write({nuName})




    def select_user(self):
        with open("users.txt", 'r') as users:
            for u in users:
                print(u[:-1])

        print("Which User is Chirping?")
        print("...")
        userSel = input("> ")




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
  menu = Birdyboard()
  menu.birdy_menu()
