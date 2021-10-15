#project that allows you to calculate how much Deep sleep is recommended depending on your age and how much deep sleep you're actually getting based off number of hours slept (Assuming healthy adult with no interruptions)

## How much DEEP sleep do you need
print("Welcome to my short deep sleep project! this program calculates how much deep sleep you get per night and whether you need more or less")

Age = int(input("First, please input your age "))

MonthsUntilBirthday = int(input("Now input how many months until your birthday (1-12) "))

Months = 12 - MonthsUntilBirthday

OfficialAge = Age + (Months*0.0833)  #formula will be used to calculate how much deep sleep is recommended

if Age < 0:
    print("This age is invalid!")
elif Age > 0 and Age < 1:
    if Months >=0 and Months <= 3:
        print ("2.4 - 3.6 hours of deep sleep are recommended based on your age")
    else:
        print ("2.8 - 3.0 hours of deep sleep are recommended based on your age")
elif Age == 1:
    print("2.8 - 3.0 hours of deep sleep are recommended based on your age")             
elif Age > 1 and Age <= 3:
    print ("2.4 - 2.8 hours of deep sleep are recommended based on your age")
elif Age > 3 and Age <= 5:
    print("2.2 - 2.6 hours of deep sleep are recommended based on your age")
elif Age > 5 and Age <= 12:
    print ("2 - 2.2 hours of deep sleep are recommended based on your age")
elif Age > 12 and Age <= 18:
    print("1.7 - 2 hours of deep sleep are recommended based on your age")
else:
    print("1.5 - 1.8 hours of deep sleep are recommended based on your age")

print("\n")

##Calculating roughly how much Deep sleep you've had depending on the number of hours slept. 13 - 23 % is the usual for healthy adults

#ONLY ACCURATE FOR ADULTS! 13-23 RANGE IS ONLY FOR HEALTHY ADULTS!

HOS = int(input("Now please input how many hours of uninterrepted sleep you get per night on average ")) #INPUT AVERAGE HOURS OF SLEEP PER NIGHT

MOS = HOS*60 #translating into minutes

MODS1 = MOS*.13
MODS2 = MOS*.23

HODS1 = MODS1/60  #translating back to hours
HODS2 = MODS2/60


print("rougly", int(round(MODS1)), "-", int(round(MODS2)), "minutes of sleep are spent in deep sleep assuming healthy adult")



print("This translates into", int(round(HODS1)), "-", int(round(HODS2)), "hours of deep sleep")





























