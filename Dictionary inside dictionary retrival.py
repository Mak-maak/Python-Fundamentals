#Dictionary inside Dictionary retrival

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

 print(customers[1])
 
 #to print customer 2 address use square bracket contigously like a 2D array
 print(customers[1]["address"])