"""Customer subclass"""
from classes.customer import Customer
from classes.video import Video


#rent_a_video method will be altered to meet max conditon
#create conditional and access a customer to check current_video_rentals

class Customer_sx(Customer): #max 1 rental out at a time

    def rent_a_video(self, video):
        video_title, rating = video
        if len(self.current_video_rentals) >= 1:
            raise ValueError("Customer can only have a total of 3 rentals at a time.")
        self.current_video_rentals.append(video_title)
        print(f"{self.first_name} has the following rentals:\n{self.current_video_rentals}")


    def return_a_video(self, video):
        if video in self.current_video_rentals:
            self.current_video_rentals.remove(video)
            print(f"{self.first_name} has returned: {video}")
        else:
            raise ValueError(f"Customer does not have '{video}' rented.")

class Customer_px(Customer): #max 3 rental out at a time

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
       
class Customer_sf(Customer): #standard family account: max 1 rental out at a time AND can not rent any "R" rated movies

    def rent_a_video(self, video):
        video_title, rating = video
        if len(self.current_video_rentals) >= 1:
            raise ValueError("Customer can only have a total of 3 rentals at a time.")

        if rating == "R":
            raise ValueError("Customer cannot rent 'R' rated videos.")

        self.current_video_rentals.append(video_title)
        print(f"{self.first_name} has the following rentals:\n{self.current_video_rentals}")

    def return_a_video(self, video):
        if video in self.current_video_rentals:
            self.current_video_rentals.remove(video)
            print(f"{self.first_name} has returned: {video}")
        else:
            raise ValueError(f"Customer does not have '{video}' rented.")
       
class Customer_pf(Customer): #premium family account: max 3 rentals out at a time AND can not rent any "R" rated movies

    def rent_a_video(self, video):
        video_title, rating = video
        if len(self.current_video_rentals) >= 3:
            raise ValueError("Customer can only have a total of 3 rentals at a time.")

        if rating == "R":
            raise ValueError("Customer cannot rent 'R' rated videos.")

        self.current_video_rentals.append(video_title)
        print(f"{self.first_name} has the following rentals:\n{self.current_video_rentals}")

    def return_a_video(self, video):
        if video in self.current_video_rentals:
            self.current_video_rentals.remove(video)
            print(f"{self.first_name} has returned: {video}")
        else:
            raise ValueError(f"Customer does not have '{video}' rented.")

       