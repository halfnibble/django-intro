# Variables
my_name = 'Joshua D. Wedekind'              # String

# Classes
class Person(object):
    """
    Excellent place to put a 'docstring' describing the class. 
    This is also how you do multi-line strings.
    """
    
    def __init__(self, name=None, *args, **kwargs):
        if name is not None:
            self.name = name
        else:
            self.name = 'John Smith'
            
    def first_name(self):
        name_array = self.name.split()
        return name_array[0]
        
    def last_name(self):
        name_array = self.name.split()
        return name_array[-1]
        

# Instantiate Person instance
me = Person(name=my_name)
 
print "My entire name is:", me.name
# Prints 'My entire name is: Joshua D. Wedekind'
 
print "My first name is:", me.first_name()
# Prints 'My first name is: Joshua'
 
print "My last name is:", me.last_name()
# Prints 'My last name is: Wedekind'