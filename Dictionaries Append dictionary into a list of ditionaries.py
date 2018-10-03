#Append dictionary into a list of dictionaries

#list of dictionary
customers = [ { "customer id": 0, 
    "first name":"John", 
    "last name": "Ogden", 
    "address": "301 Arbor Rd.", 
    }, 

    {   
    "customer id": 1, 
    "first name":"Ann", 
    "last name": "Sattermyer", 
    "address": "PO Box 1145", 
    }, 
    
    { "customer id": 2, 
    "first name":"Jill", 
    "last name": "Somers", 
    "address": "3 Main St.", 
    }, 
    ] 

#get the length of the dictionary to assign a new id to a dictionary that is going to append
new_customer_id = len(customers) 

#declaring a dictionary
new_dictionary = { "customer id": new_customer_id, "first name": new_first_name, "last name": new_last_name, "address": new_address, }   

#append a dictionary using pre-built function .append
customers.append(new_dictionary)
