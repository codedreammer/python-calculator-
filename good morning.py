import time
Name = input("Enter your name :")
recenttime = time.strftime('%H:%M:%S')
Recenttime = int(time.strftime('%H'))
c= Name.capitalize()
if(4<=Recenttime<12):
    print('Good Morning',c,'its',recenttime)
elif(12>=Recenttime<23):
    print('GOOD EVENING',c,'its',recenttime)
else:
    print('GOOD NIGHT',c,'its',recenttime)
    