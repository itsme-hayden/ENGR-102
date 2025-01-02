# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Hayden Futch
# Section: 569
# Assignment: Lab 11
# Date: 10/29/2024

#file handling

f = open("WeatherDataCLL.csv","r")

#store all data in array
#Date,Average Dew Point (F),Average Temperature (F),Average Relative Humidity (%),Average Daily Wind Speed (mph),Maximum Temperature (F),Minimum Temperature (F),Precipitation (in)
arr = [] # an array that holds an array of all data points
f.readline()
for i in f:
    txt = i.replace("-",",")
    arr.append(txt.split(","))
f.close()

#find min and max temp
maxVal = -1000
minVal =  1000
for i in arr:
    #print(i)
    if i[8] != '' and i[7] != '':
        minVal = min(minVal,int(i[8]))
        maxVal = max(maxVal,int(i[7]))

print(f"10-year maximum temperature: {maxVal} F")
print(f"10-year minimum temperature: {minVal} F")

months = {"January": "01", "February": "02", "March": "03", "April": "04","May": "05", "June": "06", "July": "07", "August": "08", "September": "09", "October": "10", "November": "11", "December": "12"}

user_month_raw = input("Please enter a month: ")
user_month = months[user_month_raw]
user_year  = input("Please enter a year: ")

temp = 0
dew = 0
hum = 0
wind = 0
days_of_precip = 0
days = 0

for i in arr:
    if i[0] == user_year and i[1] == user_month:
        days += 1
        dew += int(i[3])
        temp += int(i[4])
        hum += int(i[5])
        wind += float(i[6])
        if float(i[9]) > 0:
            days_of_precip += 1

print(f"For {user_month_raw} {user_year}:")
print(f"Mean average daily temperature: {temp / days:.1f} F")
print(f"Mean average daily dew point: {dew / days:.1f} F")
print(f"Mean relative humidity: {hum / days:.1f}%")
print(f"Mean daily wind speed: {wind / days:.2f} mph")
print(f"Percentage of days with precipitation: {(days_of_precip / days) * 100:.1f}%")