from classes.store import Store
from classes.customer import Customer
from classes.video import Video

code_platoon = Store("Code Platoon")
# print(code_platoon)

Customer.load_all_customers()
# print(code_platoon.customers)

Video.load_all_videos()

# print(code_platoon.videos)



def menu_func():
    menu = print("""
== Welcome to Code Platoon Video! ==
1. View store video inventory
2. View customer rented videos
3. Add new customer
4. Rent video
5. Return video
6. Exit\n""")
    user_inp = input("Please make a selection: ")
    match user_inp:
        case "1":
            for index, titles in enumerate(Video.load_all_videos()):
                print(titles)
            return menu_func()
        case "2":
            id = int(input("What is your customer ID #?: "))
            for id_num, customer in Customer.list_of_customers.items():
                if id == id_num:
                    print(f"{customer}")
                    
            return menu_func()
        case "3":
            print(f"Thank you for choosing us! Add information below")
            id = max(Customer.list_of_customers.keys()) if Customer.list_of_customers.keys() else 1
            account_type = input("Enter customer's account type (pf, sf, sx, px): ")
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            current_video_rentals = []
            Customer(id, account_type, first_name, last_name, current_video_rentals) 
            print("Customer added successfully!")
            print(Customer.list_of_customers)
            return menu_func()
        case "4":
            customer_renting = input(f"Please enter customer ID #? ")
            video_title = input(f"Enter the title you'd like to rent: ")
            video_title, rating = video
            if len(Customer.current_video_rentals) >= 3:
                raise ValueError("Customer can only have a total of 3 rentals at a time.")

            Customer.current_video_rentals.append(video_title)
            print(f"{Customer.first_name} has the following rentals:\n{Customer.current_video_rentals}")

        case "5":
            customer_returning = input(f"Please enter customer ID #? ")
            video_title = input(f"Enter the title you'd like to rent: ")
            if video_title in Customer.current_video_rentals:
                Customer.current_video_rentals.remove(video_title)
                print(f"{Customer.first_name} has returned: {video_title}")
            else:
                raise ValueError(f"Customer does not have '{video_title}' rented.")
        case "6":
            print("Thank you, please come again!")
        case _:
            print("Invalid input")
            return menu_func()

menu_func()



























# menu = True
# while menu:
#     menu_cmd = print(f"""
#     == Welcome to {code_platoon.name} Video! ==
#     1. View store video inventory
#     2. View customer rented videos
#     3. Add new customer
#     4. Rent video
#     5. Return video
#     6. Exit
#             """)
#     user_inp = input(f"Please make a selection: ")

#     if user_inp == "6":
#         print(f"Thank you, please come again!")
#         menu = False

#     elif user_inp == "1":
#         print(f"{code_platoon.videos}")

#     elif user_inp == "2":
#         pass

#     elif user_inp == "3":
#         id = max(Customer.load_all_customers()) + 1 if Customer.load_all_customers() else 1
#             account_type = input("Enter desired account type: ")
#             first_name = input("Enter First Name: ")
#             last_name = (input("Enter Last Name: "))
#             Customer(id, account_type, first_name, last_name) 
#             print("Customer added successfully!")
#             print(code_platoon.customers)
#             return 
#     elif user_inp == "4":
#         pass

#     elif user_inp == "5":
#         pass

#     else:
#         print("Invalid selection. Please select options 1 through 6.")