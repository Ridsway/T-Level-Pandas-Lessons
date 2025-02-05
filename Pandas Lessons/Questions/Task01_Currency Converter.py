import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Data/currency.csv")

print(df)

#write a program that:
#   lets the user enter a date
#   validates the date input
#   lets the user enter a currency conversion
#   validates the currency input
#   shows the user their chosen conversion rate
#       on their chosen day
#   repeats

#write a program that:
#   lets the user enter a currency conversion
#   validates the currency input
#   plots a graph of dates against conversion rates

earliest = "18/12/2020"
latest = "16/03/2021"

conversions = ["GBP - EUR","EUR - GBP","GBP - AUD","AUD - GBP","GBP - JPY","JPY - GBP"]

dateInput = input(f"Enter a date between {earliest} and {latest}\nmust be in the format 'DD/MM/YYYY :")

print("here are the options")
for index in range (len(conversions)):
    print(f"{index}: {conversions[index]}")

choice = int(input("Enter your choice: "))
conversion = conversions[choice]

#condition that selects the date we want
dfSelectDate = df[df["Date"] == dateInput]
dfSelectCurrency = dfSelectDate[conversion]
print(dfSelectCurrency)

x = df["Date"]
y = df[conversion]
plt.title(conversion)
plt.xlabel("Dates")
plt.ylabel("Conversion Rate")
plt.plot(x, y)
plt.show()

