import matplotlib.pyplot as plt

file_path = 'C:\\Users\\sfstr\\Desktop\\CHOSEN\\Graduate School\\SFS\\Teaching\\BIOM 1720\\Honors Python\\'
file_names = ["sleepdata_180207.txt", "sleepdata_180210.txt", "sleepdata_180215.txt"]
#file_names = ['test1.txt', 'test2.txt']
dates = ['February 7, 2018', 'February 10, 2018', 'February 15, 2018']
motion = []

for file_name in file_names:
    # Process one file at a time
    with open(file_path + file_name) as f:
        lines = f.readlines()
        # Read the file into a list of lines    
    times = []
    movement = []
    for num, line in enumerate(lines):
        # Go through the lines one at a time
        t, d = (float(ch.strip()) for ch in line.split(sep=','))
        # Each line is a string with text representing two 
        # floating point numbers separated by a comma and a white
        # space. This expression breaks the string into two 
        # pieces (because there is only one comma) and then
        # strips away white space before converting it with
        # float().
        times.append(t)
        movement.append(d)
        # The time we found from the file will go with a list of times.
        # The second number will go with a list of acceleration values.
    motion.append((times, movement))
    # Put the two lists together into a tuple and add it to the 
    # motion variable before going to the next file_name

for (ts, mov), date in zip(motion, dates):
    # zip() bundles two lists together to make it easy to loop through
    # the lists in parallel
    plt.plot(ts, mov, label=date)

plt.xlabel('Time (hours)')
plt.ylabel('Acceleration (m/s$^2$)')
plt.title('Sleep data')
plt.legend()
plt.show()
     