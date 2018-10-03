#how to get information out of a list within a dictionary

customer_29876 = {    
    "first name": "David",    
    "last name": "Elliott",    
    "address": "4803 Wellesley St.",    
    "discounts": ["standard", "volume", "loyalty"],  
    }

if "brother-in-law" in customer_29876["discounts"]:    
    discount_amount = .30  
elif "loyalty" in customer_29876["discounts"]:    
    discount_amount = .15 5 
elif "volume" in customer_29876["discounts"]:    
    discount_amount = .10 
elif "standard" in customer_29876["discounts"]:    
    discount_amount = .05 