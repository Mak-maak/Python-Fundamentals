#Creating a dictionary that contains dictionary

#dictionary 
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

#dictionaries inside dictionaries
 customers = {    
    0: { 
            "first name":"John",
            "last name": "Ogden",         
            "address": "301 Arbor Rd.",    
        },    
    
    1:  {        
            "first name":"Ann",        
            "last name": "Sattermyer",        
            "address": "PO Box 1145",  
        },   
    2:  {        
            "first name":"Jill", 
            "last name": "Somers",        
            "address": "3 Main St.",   
        },  
 } 