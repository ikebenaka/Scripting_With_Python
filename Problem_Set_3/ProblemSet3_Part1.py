#%% Task 1 - Edit code to print as requested
#*-PS3: Code Block 1--*#

mountain = "Denali"
nickname = 'Mt. McKinley'
elevation = 20322 

print(mountain + ", formerly known as \"" + nickname + "\" is " + str(elevation) + ' above sea level.')

#%% Task 2 - Lists and Iteration

data_folder = "W:\859_data\\triangle"
data_list = ["streams.shp","stream_types.csv","naip_imagery.tif"] #create list of files
user_item = "roads.shp" #create variable for user item
data_list.append(user_item) #add user item to list
for item in data_list: #iterate through list and print each file location
    print(data_folder + "\\"  + item)

#%% Task 3

user_numbers = [] #create empty list
for i in range(0,3): #iterate 3 times
    user_numbers.append(int(input("Enter an integer: "))) #ask user to enter an integer and add to list
    user_numbers.sort() #sort list in ascending numeric order
    print(user_numbers[-1]) #print last number in list (highest value)

# %% Task 3 - Challenge

user_numbers = [] #create empty list
for i in range(0,3): #iterate 3 times
    user_numbers.append(int(input("Enter an integer: "))) #ask user to enter an integer and add to list
    user_numbers.sort(reverse=True) #sort list in descending numeric order
    print(user_numbers) #print the entire list