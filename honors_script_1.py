import matplotlib.pyplot as plt

file_path = "c:\\users\\sfstr\\desktop\\chosen\\graduate school\\sfs\\teaching\\biom 1720\\honors python\\"
filename = "rawdata.txt"
# rawdata.txt contains EEG data collected at 100 Hz (sampling interval = .01 seconds)

with open(file_path + filename) as f:
    whole_file = f.read()
    content_list = whole_file.split()
    data = [float(s) for s in content_list]

indices = range(0,len(data))
sampling_interval_secs = 0.01
meas_times = [round(sampling_interval_secs * i,2) for i in indices]
            
plt.plot(meas_times, data)

plt.title('EEG data')
plt.xlabel('Time (seconds)')
plt.ylabel('Voltage (millivolts)')

plt.show()
