# Imports
from decimal import Decimal
from python_oop import my_name, Person # Local file imports
 
# Variables
my_rate = Decimal('120.00')                 # Decimal

# Classes
class Freelancer(Person):
    """
    Represents a Person who freelances.
    """
    def __init__(self, name=None, rate=None, *args, **kwargs):
        # This runs the __init__() method from Person
        super(Freelancer, self).__init__(name=name, *args, **kwargs)

        if rate is not None:
            if isinstance(rate, Decimal):
                self.rate = rate
            else:
                try:
                    self.rate = Decimal(str(rate)) # Due to float data storage
                except Exception:
                    print "Your rate is not a valid number."
                    print "Using default rate of $80.00/hr."
                    self.rate = Decimal('80.00')
        else:
            self.rate = Decimal('80.00')

    def calculate_invoice(self, hours=0):
        amount = Decimal(hours) * self.rate
        return "${0:.2f}".format(amount)

print "-------Inheritance--------"

# Instantiate Freelancer instance
me = Freelancer(name=my_name, rate=120.00)
 
print "My first name is:", me.first_name()
# Prints 'My first name is: Joshua'
 
print "The client owes", me.calculate_invoice(hours=17.5)
# Prints 'The client owes $2100.00'