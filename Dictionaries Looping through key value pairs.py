#Dictionary: Looping through key value pairs

 customer_29876 = {   "first name": "David",    "last name": "Elliott",   "address": "4803 Wellesley St.", }

#loooping
#to accessing key value pair together, use pre-built funtion .items
 for each_key, each_value in customer_29876.items():    
     print("The customer's " + each_key + " is " + each_value) 