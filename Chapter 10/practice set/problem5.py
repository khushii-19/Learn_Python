# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.

import random # or by using from random import randint we can directly use randint

class train:
    def __init__(self,train_no):
        self.train_no = train_no

    def book_ticket(self,fro,to):
        print(f"Your ticket for train no. {self.train_no} has been booked from {fro} to {to}")

    def get_status(self):
        print(f"Your train no {self.train_no} is running onn time") 

    def get_fare(self, fro, to ):
        print(f"Your ticket fare of {self.train_no} train no. is runninng from {fro} to {to} is {random.randint(220, 600)}")

d = train(34)
d.book_ticket("Delhi","Mumbai")
d.get_status()
d.get_fare("Delhi","Mumbai")        

