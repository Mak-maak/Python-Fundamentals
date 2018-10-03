#function: mixing positional and keyword arguments

#function definition
def give_greeting(greeting, first_name, flattering_nickname=" the wonder boy"):    
    print(greeting + ", " + first_name + flattering_nickname) 

#invoke with passing two parameteres
give_greeting("Hello there", first_name="Al")

# CombinedOUTPUT: Hello there, Al the wonder boy

#Dictionary example
 def find_something(dict, inner_dict, target):    
    print(dict[inner_dict][target]) 