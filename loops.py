#loops

city_to_check = "Tucson" 
cleanest_cities = ["Cheyenne", "Santa Fe", "Tucson", "Great Falls", "Honolulu"] 

if city_to_check == cleanest_cities[0]:     
    print("It's one of the cleanest cities")   
elif city_to_check == cleanest_cities[1]:     
    print("It's one of the cleanest cities")   
elif city_to_check == cleanest_cities[2]:     
    print("It's one of the cleanest cities")   
elif city_to_check == cleanest_cities[3]:    
    print("It's one of the cleanest cities")   
elif city_to_check == cleanest_cities[4]:    
    print("It's one of the cleanest cities")

#By using loop you don't need to code it repeatedly for condition check
for a_clean_city in cleanest_cities:    
    if city_to_check == a_clean_city:     
        print("It's one of the cleanest cities")  
#there is problem as python finds a match, but the loop will traverse each of the index so you can ues a break statement to stop the loop as it finds the match
for a_clean_city in cleanest_cities:    
    if city_to_check == a_clean_city:     
        print("It's one of the cleanest cities")  
        break