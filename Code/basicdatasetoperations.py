# -*- coding: utf-8 -*-
"""basicDatasetOperations.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CxiNMegHiIRsjDXrQs-0F3q9ef2LVwiX
"""

# Importing Necessary Libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Loading data
df = pd.read_csv("airline_passengers.csv")

"""**Write a code that returns (a) the first few rows of the data set.**"""

# Printing first five rows from data
df.head()

"""**Write a code that returns (b) Berief description of dataset.**"""

# Using info() function to get information about data
df.info()

"""**Displaying all columns:**"""

df.columns

"""**Displaying last five rows of datset:**"""

df.tail()

"""**Creating Dummy dataset to add and then remove null values:**"""

dfDummy = pd.DataFrame({
                        "Sallary":[1000, np.nan, np.nan],
                        "Serial No.":[1, 2, 3], 
                        "Price":[1, 4, np.nan],
                        "Age":[1, 10, np.nan]
                      })

"""**Checking if dataset has null value or not:**"""

dfDummy.isnull().sum()

"""**Filling nulll valeus with mean of their column:**"""

dfDummy["Sallary"].fillna(value = dfDummy["Sallary"].mean(), inplace = True)
dfDummy["Price"].fillna(value = dfDummy["Price"].mean(), inplace = True)
dfDummy["Age"].fillna(value = dfDummy["Age"].mean(), inplace = True)
dfDummy

"""**Rechecking if still null values are there or not:**"""

dfDummy.isnull().sum()

"""**If you want to drop null values then apply this step:**"""

dfDummy.dropna(axis=0)

"""**Write a code that returns (a) the min and max age of the passengers**"""

# Using min() and max() functions to get minimum and maximum values from age column
print(" Min Age of Passengers: ", df["Age"].min())
print(" Max Age of Passengers: ", df["Age"].max())

"""**Write a code that returns (b) average age of the passengers**"""

# Question 02(b)
# Using mean() function to get average of age column
print("Average Age of Passengers: ", df["Age"].mean())

"""**Write a code that returns (c) numbers of female and male passengers accompanied by a piechart.**"""

# Qustion 2(c)
# Using value_counts() function which will tell
# total number of all respective values present in column
totalCount = df["Gender"].value_counts()
maleCount = totalCount[1]
femaleCount = totalCount[0]
print("Female: ", femaleCount)
print("Male: ", maleCount)
# Female    261
# Male      249

# Plotting pie graph to demonstrate density of total amount of male and female
y = np.array([maleCount, femaleCount])
mycolors = ["#93c4e6", "#ed98c8"]
mylabels = ["Male", "Female"]
plt.pie(y, labels = mylabels, colors = mycolors)
plt.show()

"""**Write a code that returns (d) travel class distribution accompanied by a bar piechart. Summarize the findings in a few sentences.**"""

# Qustion 2(d)
# Using value_counts() function which will tell
# total number of all respective values present in column
totalCount = df["Type_of_Travel"].value_counts()
businessCount = totalCount[0]
personalCount = totalCount[1]
print("Business Travel: ", businessCount)
print("Personal Travel: ", personalCount)
# Business_travel    351
# Personal_Travel    159

# Plotting pie graph to demonstrate density of total amount of Business and Personal
y = np.array([businessCount, personalCount])
mycolors = ["#735137", "#8c7766"]
mylabels = ["Business", "Personal"]
plt.pie(y, labels = mylabels, colors = mycolors)
plt.show()

"""**Write a code to compare the average flight distances of male and female passengers. Briefly explain your finding.**"""

# By using groupby function grouping all same values of gender column,
# Calculating mean of flight distance according to gender of male and female
df.groupby('Gender', as_index=False)['Flight_Distance'].mean()

"""**Write a code to compare the average flight distance by type of travel. That is, how does the mean flight distance of passengers on business travel compare to the mean flight of passengers on personal travel?**"""

# Question 04
# By using groupby function grouping all same values of Type of travel column,
# Calculating mean of flight distance according to Type of travel of male and female
df2 = df.groupby('Type_of_Travel', as_index=False)['Flight_Distance'].mean()
print(df2)

businessTraveler = df2["Flight_Distance"][0]
personalTraveler = df2["Flight_Distance"][1]

# Plotting pie graph to demonstrate density of total amount of Business Travel Distance and Personal Travel Distance
y = np.array([businessTraveler, personalTraveler])
mycolors = ["#4a5e4f", "#88a888"]
mylabels = ["Business Travel Distance", "Personal Travel Distance"]
plt.pie(y, labels = mylabels, colors = mycolors)
plt.show()

"""**Write a code that adds up the scores on all of the satisfaction survey variables, except for the satisfaction variable, and saves them in a column named total_satisfaction.**"""

# Question 05:
"""
  In this code, Making list of columns and then by applying loop
  and then adding the values to TotalSatisfaction Column
"""
surveyColumns = [
    "Inflight_wifi_service", "Departure/Arrival_time_convenient",
    "Food_and_drink", "Seat_comfort", "Inflight_entertainment", 
    "Inflight_service", "Cleanliness"
]
df["Total_Satisfacation"] = 0
for i in surveyColumns:
  df["Total_Satisfacation"] += df[i]
df["Total_Satisfacation"]

"""**Write a code that adds up the scores on all of the satisfaction survey variables, except for the satisfaction variable, and saves them in a column named total_satisfaction. Then, plot the relationship between (a) Age and total_satisfaction.**"""

print('Task 05\npart a\n')
# Using matplotlib to plot the scattered plot to compare the values of Age Column and
# Total Satisfaction column. Using custom marker and colour
plt.subplots(figsize=(25, 11))
plt.scatter(df["Total_Satisfacation"], df["Age"], marker = "x", s = 25,  c = "brown")
plt.ylabel("Age")
plt.xlabel("Total Satisfacation")
plt.title("Age Vs Total Satisfacation")
plt.show()

"""**Write a code that adds up the scores on all of the satisfaction survey variables, except for the satisfaction variable, and saves them in a column named total_satisfaction. Then, plot the relationship between (b) flight distance and total satisfaction. Explain your findings in a few sentences.**"""

print('Task 05\npart b\n')

# Using matplotlib to plot the scattered plot to compare the values of Flight_Distance Column and
# Total Satisfaction column. Using custom marker and colour
plt.subplots(figsize=(25, 11))
plt.scatter(df["Total_Satisfacation"], df["Flight_Distance"], marker = "x", s = 25,  c = "brown")
plt.ylabel("Age")
plt.xlabel("Total Satisfacation")
plt.title("Age Vs Total Satisfacation")
plt.show()

"""**Print All Flight Distances of Passengers travelled more than 1000**"""

df2 = pd.DataFrame(df, columns = ["Flight_Distance"])
print("Before: ", df2)
df2 = df2[df2["Flight_Distance"] > 1000]
print("\n\n\nAfter: ", df2)

"""**Check Customer_type of Customer of Age above 50 and less than 55**"""

# By using for loop on total number of rows which is 510
# I got access to all values of column Age and Customer_Type
# and then by simple comparing if Age greater than 50 and less than 55 then
# printing both columns
for i in range(510):
  if df['Age'][i] > 50 and df['Age'][i] < 55:
    print(df['Customer_Type'][i], df['Age'][i])

"""**Find the Minimum Distance travelled by disloyal customer**"""

# By using for loop on total number of rows which is 510
# I got access to all values of column  Customer_Type
# and then by simple comparing Customer type is disloyal then
# Store the value of flight distance in temporary list
# After that using min() found min val.
temp = []
for i in range(510):
  if df['Customer_Type'][i] == 'disloyal_Customer':
    temp.append(df['Flight_Distance'][i])
print('Minimum Distance travelled by disloyal customer =', min(temp))

"""**Find the gender of Passanger with least travelling**"""

minDistance = df["Flight_Distance"].min()
print(df.loc[df['Flight_Distance'] == minDistance, 'Gender'])

"""Write a function that will ask users to enter their name, age, the airlines they flew recently, and how satisfied they were with the airlines on a 1-10 scale until you enter quit. Save the entries in a dictionary.
Your function should return the following:
1. The dictionary that includes all entries.
2. A list named satisfied_passenger, which includes the passengers who entered a satisfaction score of 7 or higher.
3. A list named unsatisfied_passenger, which includes the passengers who entered a satisfaction score of 3 or lower.
4. A list named neutral_passenger, which includes the passengers who entered a satisfaction score of 4, 5, or 6. 
"""

def getInput():
  # Creating required variable 
  data = {
          "Satisfacation": list(),
          "Airline": list(), 
          "Name": list(), 
          "Age": list()
          }
  unsatisfied_passanger = list()
  satisfied_passanger = list()
  neutral_passanger = list()

  # Loop will iterate until the user enters quit
  while True:
    name = str(input("\nEnter your name: "))
    age = 0

    # Applied the check if user enters value less than 1 then will ask again
    while True:
      age = int(input("Enter your age: "))
      if age >= 1:
        break
      print("Wrong input. Please try again")    

    airline = str(input("Enter the airline you flew recently: "))
    satisfacation = -1

    # Applied the check if user enters value other than in between 1 to 10 then will ask again
    while True:
      satisfacation = int(input("Enter your level of Satisfacation (From 1 to 10): "))
      if satisfacation >= 1 or satisfacation <= 10:
        break
      print("Wrong input. Please try again")

    # By using simple if else appending into the list, 
    # Name of passangers
    if satisfacation <= 3:
      unsatisfied_passanger.append(name)
    elif satisfacation >= 7:
      satisfied_passanger.append(name)
    elif satisfacation >= 4 and satisfacation <= 6:
      neutral_passanger.append(name)

    # Appending input data to the lists corresponding to keys
    data["Name"].append(name)
    data["Age"].append(age)
    data["Airline"].append(airline)
    data["Satisfacation"].append(satisfacation)

    # Applied the check if user enters value other than in between quit and continue then will ask again
    while True:
      check = str(input("To Exit enter (quit) else enter (continue): "))
      if check == "quit" or  check == "continue":
        break
      print("Wrong input. Please try again")
    if check == "quit":
      break

  return data, satisfied_passanger, unsatisfied_passanger, neutral_passanger

data, satisfied_passanger, unsatisfied_passanger, neutral_passanger = getInput()
print("\n\n\nSatisfied Passangers: ", satisfied_passanger)
print("Unsatisfied Passangers: ", unsatisfied_passanger)
print("Neutral Passangers: ", neutral_passanger)
print("Data: ", data)