"""Customer Class"""
import csv
# from classes.video import Video

class Customer:
    list_of_customers = {}

    @classmethod
    def load_all_customers(cls):
        all_customers =[]
        with open('./data/customers.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader: 
                new_customer = Customer(**row)
                all_customers.append(new_customer)
        return all_customers
    # instead of appending, create as a all_customers dict 
    def __init__(self, id, account_type, first_name, last_name, current_video_rentals = []):
        self._id = id
        self._account_type = account_type
        self.first_name = first_name
        self.last_name = last_name
        self.current_video_rentals = current_video_rentals
        self.customers = []
        
        Customer.list_of_customers[int(self._id)] = self 

    @property
    def get_id(self):
        return self._id
    
    @get_id.setter
    def set_id(self, new_id):
        if isinstance(new_id, int):
            self._id = new_id
        
    @property
    def get_current_video_rentals(self):
        return self.current_video_rentals
    
    # @get_current_video_rentals.setter
    # def set_current_video_rentals(self, video_rentals):
    #     if isinstance(video_rentals, list):
    #         self._current_video_rentals = video_rentals
    #     else:
    #         raise TypeError(f"Current Video Rentals should only be a list")

    @staticmethod
    def create_a_customer_dict():
        new_customer = {
            "id":1, 
            "first_name":"Monica",
            "last_name":"Gellar",
            "account_type":"sx",
            }
            #pass a customer argument then have inputs assigned to customer, then put customer into a dict
        return new_customer
    def add_a_customer(cls):
        if isinstance(cls, Customer):
            print(f"Thank you for choosing us! Add information below")
            id = max(Customer.list_of_customers.keys()) if Customer.list_of_customers.keys() else 1
            if isinstance(id, int):
                account_type = input("Enter customer's account type (pf, sf, sx, px): ")
                first_name = input("Enter First Name: ")
                last_name = input("Enter Last Name: ")
                current_video_rentals = []
                new_customer = Customer(id, account_type, first_name, last_name, current_video_rentals)
                cls.list_of_customers[id] = new_customer 
                print("Customer added successfully!")
                print(cls.list_of_customers)
        
    def get_customer_by_id(cls, customer_id):
        if isinstance(customer_id, int):
            for id, person in cls.list_of_customers.items():
                if id == customer_id:
                    return person 
        else:
            return None
            
    def get_customer_rented_videos(self):
            if isinstance(self, Customer):
                for id, person in Customer.list_of_customers.items():
                    if id == self._id:
                        return f"{self.first_name} has the following rentals:\n{self.current_video_rentals}"
                        
            return f"Customer with ID {self._id} not found."
        
    def rent_a_video(self, video): 
        video_title, rating = video
        if len(self.current_video_rentals) >= 3:
            raise ValueError("Customer can only have a total of 3 rentals at a time.")

        self.current_video_rentals.append(video_title)
        print(f"{self.first_name} has the following rentals:\n{self.current_video_rentals}")

    def return_a_video(self, video):
        if video in self.current_video_rentals:
            self.current_video_rentals.remove(video)
            print(f"{self.first_name} has returned: {video}")
        else:
            raise ValueError(f"Customer does not have '{video}' rented.")

    def __repr__(self):
        return f"id:{self._id}, account type: {self._account_type}, first name: {self.first_name},last name:{self.last_name}, list of rentals: {self.current_video_rentals})"

                   



            









