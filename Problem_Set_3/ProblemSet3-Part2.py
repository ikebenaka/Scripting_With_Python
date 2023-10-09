# %% Task 4.1 - Read in data

#Create a link to the file's contents
fileObj = open(file='data/raw/transshipment_vessels_20180723.csv',mode='r')

#Read the entire contents into a list object
lineList = fileObj.readlines()

#Release the link to the file objects (now that we have all its contents)
fileObj.close() #Close the file

#Save the contents of the first line in the list of lines to the variable "headerLineString"
headerLineString = lineList[0]

#Print the contents of the headerLine
print(headerLineString)

#%% Task 4.2 - Split the headers into a list of column names

#Split the headerLineString into a list of header items
headerItems = headerLineString.split(sep=',')

#List the index of the mmsi, shipname, and fleet_name values
mmsi_idx = headerItems.index('mmsi')
name_idx = headerItems.index('shipname')
fleet_idx = headerItems.index('fleet_name')

#Print the values
print(mmsi_idx,name_idx,fleet_idx)

#%% Task 4.3 - Create a dictionary of vessel data and iterate through the data

#Create an empty dictionary
vesselDict = {}

#Iterate through all lines (except the header) in the data file:
for lineString in lineList[1:]:
    #Split the data into values
    lineData = lineString.split(sep=',')
    #Extract the mmsi value from the list using the mmsi_idx value
    mmsi = lineData[mmsi_idx]
    #Extract the fleet value
    fleet = lineData[fleet_idx]
    #Adds info to the vesselDict dictionary
    vesselDict[mmsi] = fleet

#%% Task 4.4

vesselID = "258799000" #create variable for vessel ID
print("Vessel #" + vesselID + " flies the flag of " + vesselDict[vesselID]) #print statement

# %% Task 5

#Create a link to the file's contents
fileObj = open(file='data/raw/loitering_events_20180723.csv',mode='r')

#Read the entire contents into a list object
lineList = fileObj.readlines()

#Release the link to the file objects (now that we have all its contents)
fileObj.close() #Close the file

#Save the contents of the first line in the list of lines to the variable "headerLineString"
headerLineString = lineList[0]

#Create empty data list
dataList = []

#Pull vessels that transited across the equator starting between 165E and 170E latitude
for lineString in lineList[1:]:
    #Split data into list of data items
    lineData = lineString.split(sep=',')
    #Store data points of interest in their own variables
    mmsi = lineData[0]
    start_lat = lineData[1]
    start_lon = lineData[2]
    end_lat = lineData[3]
    end_lon = lineData[4]
    #Check starting and ending latitude to see if event crosses the equator from south to north
    if float(start_lat) < 0 and float(end_lat) > 0:
        #Check starting latitude to see if it falls between 165E and 170E
        start_lon_bool = float(start_lon) >= 165 and float(start_lon) <= 170 #Create boolean variable to store result
        #If both are true, then print the vessel mmsi number and its fleet
        if start_lon_bool == True:
            print("Vessel #" + mmsi + " flies the flag of " + vesselDict[mmsi])
        else:
            print("No vessels met the criteria.")