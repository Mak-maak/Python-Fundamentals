#and gate logic
 if weight > 300 and time < 6:    
     status = "try to recruit him"

#multiple and gates
 if weight > 300 and time < 6 and age > 17 and height < 72:   
     status = "try to recruit him" 

#or gate implementation
 if SAT > avg or GPA > 2.5 or parent == "alum":    
     message = "Welcome to Leeds College!" 
    
#or & and gate implementation together    
if age > 65 or age < 21 and res == "U.K.": 
    
#removing ambiguity from the expression    
if (age > 65 or age < 21) and res == "U.K.":
if age > 65 or (age < 21 and res == "U.K."):
 
