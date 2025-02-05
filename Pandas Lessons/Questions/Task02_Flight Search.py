from sys import int_info
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Data/flights.csv")

print(df)

dates = "01/04/22,02/04/22,03/04/22,04/04/22,05/04/22,06/04/22,07/04/22,08/04/22,09/04/22,10/04/22,11/04/22,12/04/22,13/04/22,14/04/22,15/04/22,16/04/22,17/04/22,18/04/22,19/04/22,20/04/22,21/04/22,22/04/22,23/04/22,24/04/22,25/04/22,26/04/22,27/04/22,28/04/22,29/04/22,30/04/22,01/05/22,02/05/22,03/05/22,04/05/22,05/05/22,06/05/22,07/05/22,08/05/22,09/05/22,10/05/22,11/05/22,12/05/22,13/05/22,14/05/22,15/05/22,16/05/22,17/05/22,18/05/22,19/05/22,20/05/22,21/05/22,22/05/22,23/05/22,24/05/22,25/05/22,26/05/22,27/05/22,28/05/22,29/05/22,30/05/22,31/05/22,01/06/22,02/06/22,03/06/22,04/06/22,05/06/22,06/06/22,07/06/22,08/06/22,09/06/22,10/06/22,11/06/22,12/06/22,13/06/22,14/06/22,15/06/22,16/06/22,17/06/22,18/06/22,19/06/22,20/06/22,21/06/22,22/06/22,23/06/22,24/06/22,25/06/22,26/06/22,27/06/22,28/06/22,29/06/22"
dates = df.columns.tolist()
print("Here are all dates with available flights: ")
for index in range (len(dates)):
    print(f"{index}: {dates[index]}")

while True:
    try:
        choice = int(input("Enter the date of the flights you want to view\nMust be in the format 'DD/MM/YYYY': "))
        
        
        if 0 <= choice < len(dates):
            break
        else:
            print(f"Invalid input. Please enter a number between 0 and {len(dates) - 1}.")
    except ValueError:
        print("Invalid input. Please enter a valid integer corresponding to the dates provided.")

starts = df["From"]
ends = df["To"]
print(starts, ends)

# let user see times of flights
# validate user input 

