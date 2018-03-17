import matplotlib.pyplot as plt
file_path = "C:\\Users\\sfstr\\Desktop\\CHOSEN\\Graduate School\\SFS\\Teaching\\BIOM 1720\\Honors Python\\"
filename = "SunriseSunset_data.txt"
sunrises =[]
sunsets = []
with open(file_path + filename) as f:
    lines = f.readlines()
    
for line in lines:
    tokens = line.split()
    if not len(tokens):
        continue
    if tokens[0][0] in {'0','1','2','3'}:
        # First token on line is the day of the month
        day_of_month = int(tokens[0])
        # Successive tokens are sunrise and sunset for each month
        # For simplicity, zeroes have been added for short months
        times =[float(t[0:2]) + float(t[2:])/60 for t in tokens[1:]]
        sun_times = list(zip(times[0::2],times[1::2]))
        for (month, (risetime, settime)) in enumerate(sun_times, 1):
            if risetime == 0:
                continue
            sunrises.append((month, day_of_month, risetime))               
            sunsets.append((month, day_of_month, settime))
sunrises.sort()
sunsets.sort()           
    
mon_lengths = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
x = []
y = []          
for (month, day, time) in sunrises:
    month = float(month) + float(day/mon_lengths[month])
    x.append(month)
    y.append(time)

plt.plot(x,y,'-', label='Sunrise')

x = []
y = [] 
for (month, day, time) in sunsets:
    month = float(month) + float(day/mon_lengths[month])
    x.append(month)
    y.append(time)
plt.plot(x,y,'--',label='Sunset')
plt.grid()  
plt.legend(loc='center right')
plt.title('2018 Sunrise and Sunset')
plt.xlabel('Month')
plt.ylabel('Time of Day')
plt.show()