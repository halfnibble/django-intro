# Imports
# Note: this is how to do a single-line comment
import os
from decimal import Decimal
 
# Variables
my_name = 'Joshua D. Wedekind'              # String
my_rate = Decimal('120.00')                 # Decimal
current_dir = os.getcwd()                   # String of current directory
client_list = ['ChemCo', 'StartUp, Inc.']   # Array
# Dictionary, or 'dict'
project_list = {
    'Lab Manager': 'Web-based dashboard to manage laboratory processes.',
    'Website'    : 'Marketing and promotional website.',
    'JSON API'   : 'Create a JSON API to interface with Lab Manager', # << Note!
}

# If/Else
if my_name == 'Bernard Mickleberry':
    print "That's me!" # << Note! - Can use single or double quotes for strings
else:
    print "My name is", my_name
    # Prints 'My name is Joshua D. Wedekind'
# Note: No switch/case!!

# Loops
for client in client_list:
    print "I have  a client named", client
    # Prints 'I have a client named ChemCo' ...

for project, description in project_list.iteritems(): # << Note!
    print "Project name:", project, "\n\tDescription:", description
    # Prints...
    # Project name: Lab Manager
    #     Description: Web-based dashboard to manage laboratory processes.
