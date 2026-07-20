class Library:
   pass

class Item(Library):
    def __init__(self, title):
        self.title = title
    
    def borrow(self):
        pass
    
    def return_item(self):
        pass

    def reserve(self):
        pass
   
class Book(Item):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author
    
    def loan_period(self):
        return "21 Days"
    
    def late_fee(self):
        return f"Late fee for book '{self.title}': Rs.2 per day"
    

class DVD(Item):
    def __init__(self, title, director):
        super().__init__(title)
        self.director = director
    
    def loan_period(self):
        return "7 Days"
    
    def late_fee(self):
        return f"Late fee for DVD '{self.title}': Rs.10 per day"
    


class Magazine(Item):
    def __init__(self, title, publisher):
        super().__init__(title)
        self.publisher = publisher
    
    def loan_period(self):
        return "3 Days"
    
    def late_fee(self):
        return f"Late fee for magazine '{self.title}': Rs.1 per day"



class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.borrowed_items = []
        self.fees_due = 0

class premium_member(person):
    def __init__(self,name,age):
        super().__init__(name,age)
    
    max_borrowed_items = 10

    def loan_period(self):
        return Item.loan_period*2

    def curreent_fees(self):
        return 0