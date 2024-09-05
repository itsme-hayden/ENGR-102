# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:         Patrick Murphy
#                Steven Sooudi
#                Hayden Futch
# Section:      ENGR 102 469
# Assignment:   3.18 LAB
# Date:         9/3/24
#(y2-y1/x2-x1)(x-x1)+y1
import math

time1 = float(input("Enter time 1: "))
x1 = float(input("\nEnter the x position of the object at time 1: "))
y1 = float(input("\nEnter the y position of the object at time 1: "))
z1 = float(input("\nEnter the z position of the object at time 1: "))

time5 = float(input("\nEnter time 2: "))
x2 = float(input("\nEnter the x position of the object at time 2: "))
y2 = float(input("\nEnter the y position of the object at time 2: "))
z2 = float(input("\nEnter the z position of the object at time 2: \n"))

time2 = (((time5 - time1)/4)+time1)
time3 = (((time5 - time1)/2)+time1)
time4 = (((time5 - time1)*(3/4)+time1))

xslope = (x2 - x1) / (time5 - time1)
yslope = (y2 - y1) / (time5 - time1)
zslope = (z2 - z1) / (time5 - time1)
#(slope)(t-t1)+y1
#copy and paste for 1.25,1.5,1.75,2.0
xfinal1 = x1
yfinal1 = y1
zfinal1 = z1

xfinal2 = (xslope)*(time2 - time1) + x1
yfinal2 = (yslope)*(time2 - time1) + y1
zfinal2 = (zslope)*(time2 - time1) + z1

xfinal3 = (xslope)*(time3 - time1) + x1
yfinal3 = (yslope)*(time3 - time1) + y1
zfinal3 = (zslope)*(time3 - time1) + z1

xfinal4 = (xslope)*(time4 - time1) + x1
yfinal4 = (yslope)*(time4 - time1) + y1
zfinal4 = (zslope)*(time4 - time1) + z1

xfinal5 = (xslope)*(time5 - time1) + x1
yfinal5 = (yslope)*(time5 - time1) + y1
zfinal5 = (zslope)*(time5 - time1) + z1
print(f"At time {time1:.2f} seconds the object is at ({xfinal1:.3f}, {yfinal1:.3f}, {zfinal1:.3f})")
print(f"At time {time2:.2f} seconds the object is at ({xfinal2:.3f}, {yfinal2:.3f}, {zfinal2:.3f})")
print(f"At time {time3:.2f} seconds the object is at ({xfinal3:.3f}, {yfinal3:.3f}, {zfinal3:.3f})")
print(f"At time {time4:.2f} seconds the object is at ({xfinal4:.3f}, {yfinal4:.3f}, {zfinal4:.3f})")
print(f"At time {time5:.2f} seconds the object is at ({xfinal5:.3f}, {yfinal5:.3f}, {zfinal5:.3f})")

