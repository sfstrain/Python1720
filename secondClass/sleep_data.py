import matplotlib.pyplot as plt

file_path = 'C:\\Users\\sfstr\\Desktop\\CHOSEN\\Graduate School\\SFS\\Teaching\\BIOM 1720\\Honors Python\\'
file_names = [ "180207_sleepdata.csv", "180210_sleepdata.csv", "180215_sleepdata.csv"]
#file_names = ['test1.txt', 'test2.txt']
dates = ['February 7, 2018', 'February 10, 2018', 'February 15, 2018']
motion = []

for file_name in file_names:
    with open(file_path + file_name) as f:
        lines = f.readlines()    
    times = []
    movement = []
    for num, line in enumerate(lines):
        if 'time' in line or num%10 != 0:
            continue
        t, _, _, _, d = (float(ch.strip()) for ch in line.split(sep=','))
        times.append(t/3600.)
        movement.append(d)
    motion.append((times, movement))

for (ts, mov), date in zip(motion, dates):
    plt.plot(ts, mov, label=date)

plt.xlabel('Time (hours)')
plt.ylabel('Acceleration (m/s$^2$)')
plt.title('Sleep data')
plt.legend()
plt.show()
     