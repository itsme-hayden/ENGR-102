# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Hayden Futch
# Section: 569
# Assignment: Lab 
# Date: 11/5/2024
import matplotlib.pyplot as plt

f = open("WeatherDataCLL.csv","r")

#store all data in array
#Date,Average Dew Point (F),Average Temperature (F),Average Relative Humidity (%),Average Daily Wind Speed (mph),Maximum Temperature (F),Minimum Temperature (F),Precipitation (in)
arr = [] # an array that holds an array of all data points
f.readline()
for i in f:
    txt = i.replace("-",",")
    arr.append(txt.split(","))
f.close()

months = {"January": "01", "February": "02", "March": "03", "April": "04","May": "05", "June": "06", "July": "07", "August": "08", "September": "09", "October": "10", "November": "11", "December": "12"}

#user_month_raw = input("Please enter a month: ")
#user_month = months[user_month_raw]
##user_year  = input("Please enter a year: ")

temp = 0
dew = 0
hum = 0
wind = 0
days_of_precip = 0
days = 0

#for i in arr:
 #       days += 1
#        dew += int(i[3])
#        temp += int(i[4])
 #       hum += int(i[5])
#        wind += float(i[6])
#        if float(i[9]) > 0:
#            days_of_precip += 1



#line graph
xvals_temp = []
xvals_wind = []
xvals_dew = []
xvals_hum = []
ytemp = []
ywind = []
ydew = []
yhum = []
wind_days = 0
temp_days = 0
dew_days = 0
hum_days = 0
for i in arr:
        if i[3] != "" and i[5] != "":
            ydew.append(int(i[3]))
            xvals_dew.append(dew_days)
            dew_days += 1
        if i[4] != "":
            ytemp.append(int(i[4]))
            xvals_temp.append(temp_days)
            temp_days += 1
        if i[3] != "" and i[5] != "":
            yhum.append(int(i[5]))
            xvals_hum.append(hum_days)
            hum_days += 1
        if i[6] != "":
            ywind.append(float(i[6]))
            xvals_wind.append(wind_days)
            wind_days += 1



fig, ax1 = plt.subplots()

ax1.set_xlabel('Date')
ax1.set_ylabel('Average Temperature (F)')
ax1.plot(xvals_temp, ytemp, "r")

ax2 = ax1.twinx()
ax2.set_ylabel('Average Wind (mph)')
ax2.plot(xvals_wind,ywind,'b')
plt.title('Average Temperature and Average Wind Speed')
plt.show()

plt.hist(ywind, bins=50, facecolor='r', edgecolor='black', linewidth=1)
plt.title('Histogram of Average Wind Speed')
plt.ylabel('Number of days')
plt.xlabel('Average Wind Speed (mph)')
plt.show()

plt.scatter(ydew, yhum, s=5, color="r")
plt.title('Average Relative Humidity versus Average Dew Point')
plt.ylabel("Average Relative Humidity (%)")
plt.xlabel("Average Dew Point (F)")
plt.show()


