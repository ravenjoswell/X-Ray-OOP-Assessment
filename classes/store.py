"""Store Class"""
# from classes.customer_types import Customer_pf, Customer_sf, Customer_sx, Customer_px
from threading import activeCount
from classes.customer import Customer
from classes.customer_types import Customer_pf, Customer_px, Customer_sf, Customer_sx
from classes.video import Video


class Store:

    def __init__(self, name):
        self.name = name
   
    

    def customer_type_maker(self, account_type):
        account_type = Customer.list_of_customers.get("account_type")
        if account_type == "sx":
            return Customer_sx()
        elif account_type == "px":
            return Customer_px()
        elif account_type == "sf":
            return Customer_sf()
        elif account_type == "sx":
            return Customer_pf()
        else:
            raise ValueError("Not a valid account type")
            
    def load_data(self):
        return Video.videos, Customer.customers
            
    def run_the_store(self):
         return "Thank you, please come again!"
    
    def __repr__(self):
        return self.name
    
code_platoon = Store("Code Platoon")
Video.videos = Video.load_all_videos()
Customer.customers = Customer.load_all_customers()