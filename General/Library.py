class Library:
    def __init__(self):
        self.items = []
        self.members = []

    def add_item(self, item):
        self.items.append(item)

    def add_member(self, member):
        self.members.append(member)

    def find_member(self, name):
        for member in self.members:
            if member.name == name:
                return member
        return None

    def find_item(self, title):
        for item in self.items:
            if item.title == title:
                return item
        return None

    def borrow(self, member, item):
        if not item.available:
            print("Item is not Available")
            return

        if len(member.borrowed_items) >= member.max_items:
            print("Maximun Borrowed Item is Reached ")
            return

        if isinstance(item, DVD):
            if member.age < item.age_rating:
                print("You are not eligible for this Item")
                return

        print(member.name, "borrowed", item.title)

    def return_item(self, member, item, late_days):
        if item not in member.borrowed_items:
            print("This item was not borrowed.")
            return

        member.borrowed_items.remove(item)
        item.available = True
        item.borrowed_by = None

        if not isinstance(member, premium_member):
            member.fees_due += late_days * item.late_fee()
        print(member.name, "returned", item.title)

    def reserve(self, member, item):
        if isinstance(item, Magazine):
            print("Magazine cannot be reserved.")
            return

        if item.available:
            print("Item is available. No need to reserve.")
            return

        item.reservation_queue.append(member)

        print(member.name, "reserved", item.title)


class Item:
    def __init__(self, title):
        self.title = title
        self.available = True
        self.borrowed_by = None
        self.due_days = 0
        self.reservation_queue = []

    def loan_period(self):
        return 0

    def late_fee(self):
        return 0


class Book(Item):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author

    def loan_period(self):
        return "21 Days"

    def late_fee(self):
        return 2


class DVD(Item):
    def __init__(self, title, director, age_rating):
        super().__init__(title)
        self.director = director
        self.age_rating = age_rating

    def loan_period(self):
        return "7 Days"

    def late_fee(self):
        return 10


class Magazine(Item):
    def __init__(self, title, publisher):
        super().__init__(title)
        self.publisher = publisher

    def loan_period(self):
        return "3 Days"

    def late_fee(self):
        return 1


class Member:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.borrowed_items = []
        self.fees_due = 0
        self.max_items = 5

    def current_fees(self):
        return self.fees_due


class premium_member(Member):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.max_items = 10

    def loan_period(self):
        return Item.loan_period * 2

    def current_fees(self):
        return 0


library = Library()

book = Book("Python Basics", "Guido")
dvd = DVD("Avengers", "Russo", 18)

member = Member("Krunal", 14)
premium = premium_member("Rahul", 25)

library.borrow(member, book)
library.return_item(member, book, 3)

library.borrow(member, dvd)
library.reserve(premium, dvd)
