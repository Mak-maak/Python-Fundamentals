#list manipulations

cities = ["Atlanta", "Baltimore", "Chicago", "Denver", "Los Angeles", "Seattle"] 

#using pre-built function to append the list
cities.append("New York")

#alternative way to append list
cities = cities + ["Dubuque", "New Orleans"]

#create a new list using the adding the elements of the existing list
longer_list_of_cities = cities + ["Dubuque", "New Orleans"] 

#creating an empty list and adding items to it later on
todays_tasks = [] 

#…then later add elements so the list is no longer empty… 
todays_tasks = todays_tasks + ["Walk dog", "Buy groceries"]

# another pre-built function to insert an element at the specified index
cities.insert(0, "Australia")
#insert contains to parameteres, first is index value, & second takes the value that u want to insert at specified index

 