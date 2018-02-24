import matplotlib.pyplot as plt

file_path = "C:\\Users\\sfstr\\Desktop\\CHOSEN\\Graduate School\\SFS\\Teaching\\BIOM 1720\\Honors Python\\"
filename = "SunriseSunset_data.txt"
# rawdata.txt contains EEG data collected at 100 Hz (sampling interval = .01 seconds)


with open(file_path + filename) as f:
    lines = f.readlines()
    
sunsets = []
sunrises = []
    
for line in lines:
    tokens = line.split()
    if not len(tokens):
        continue
    if tokens[0][0] in {'0','1','2','3'}:
        day_of_month = int(tokens[0])
        sunrises.append(list(m, day_of_month, float(t[:2]) + float(t[2:])/60) 
                            for m, t in enumerate(tokens[1::2],1))
#        rise_times = [ (m, day_of_month, float(t[:2]) + float(t[2:])/60) 
#                            for m, t in enumerate(tokens[1::2],1) ]
#        set_times =  [ (m, day_of_month, float(t[:2]) + float(t[2:])/60) 
#                            for m, t in enumerate(tokens[2::2],1) ]
                            
#        for (month, day, time) in rise_times:
            
mon_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

