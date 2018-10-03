#individual if bodies
if species == "cat": 
    print("Yep, it's cat.") 
if species != "cat": 
    print("Nope, not cat.")  

#if and else statements
if species == "cat":
    print("Yep, it's cat.") 
else: 
    print("Nope, not cat.") 

#if elif and else statements together
if donut_condition == "fresh":
    buy_score = 10 
elif donut_price == "low": 
    buy_score = 5 
else: 
    buy_score = 0 

#same thing with 3 if statements
buy_score = 0  
if donut_condition == "fresh":    
    buy_score += 10  
if donut_filling == "chocolate":    
    buy_score += 5  
if donut_price == "reasonable":
    buy_score += 7
