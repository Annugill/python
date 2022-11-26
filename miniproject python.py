#
import calendar
def information():
    '''******Python Mini Project******

This project is to calculate the leap years and the non leap years in a given range of two input dates.
Input date range is in the format dd/mm/yy.

'''
print(information.__doc__)

first_date=input("Enter the 1st date: ")
first_date1=first_date.split("/")
start=int(first_date1[2])
last_date=input("Enter the last date: ")
last_date1=last_date.split("/")
end=int(last_date1[2])
print("The range is: from",start,"to",end)
leap=[]
nonleap=[]
for i in range(start,end+1):
    if (calendar.isleap(i)==False):
        nonleap.append(i)
    else:
        leap.append(i)
print("List of leap year is:",leap)
print("List of non leap year is:",nonleap)
print("******Thank you for visiting here******")








