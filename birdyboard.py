

class Birdyboard:

    def __init__(self):
        pass

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
                    ints = self.random_numbers(int(count))
                    self.print_results(ints)

                if choice == "2":
                    print("#2: You chose to select a user!")
                    fibo = self.fibonacci_sequence(int(count))
                    self.print_results(fibo)

                if choice == "3":
                    print("#3: You chose to view chirps!")
                    prime = self.generate_prime_numbers(int(count))
                    self.print_results(prime)

                if choice == "4":
                    print("#4: You chose public chirp!")
                    prime = self.generate_prime_numbers(int(count))
                    self.print_results(prime)

                if choice == "5":
                    print("#5: You chose private chirp!")
                    prime = self.generate_prime_numbers(int(count))
                    self.print_results(prime)

                if (choice == "6"):
                    print("Until next time!")
                    raise SystemExit()

        except ValueError:
            print("Please enter a number for your choice")
        self.birdy_menu()

    def new_user_create(self):
        pass

    def select_user(self):
        pass

    def view_chirps(self):
        pass

    def public_chirp(self):
        pass

    def private_chirp(self):
        pass


if __name__ == "__main__":
  menu = Birdyboard()
  menu.birdy_menu()
