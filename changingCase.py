#Changing case

cleanest_cities = ["Cheyenne", "cheyenne", "Santa Fe", "santa fe", "Tucson", "tucson", "Great Falls", "great falls", "Honolulu", "honolulu"]

# input string from user
city_to_check = input("Enter your city: ")

#changing its case using pre-built function .lower  
city_to_check = city_to_check.lower()  
cleanest_cities = ["cheyenne", "santa fe", "tucson", "great falls", "honolulu"] 

#now trying to match
for a_clean_city in cleanest_cities:    
    if city_to_check == a_clean_city:      
        print("It's one of the cleanest cities") 

#to make string to upper case use .upper
city_to_check = city_to_check.upper()
