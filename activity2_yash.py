"""StairCaseAnalysis"""
import math
import pandas as pd
USER_DATA = pd.read_csv("data3.csv", header=1, sep=";")
print(USER_DATA)
LINACC_X = USER_DATA['LINEAR ACCELERATION X (m/s²)']
LINACC_Y = USER_DATA['LINEAR ACCELERATION Y (m/s²)']
LINACC_Z = USER_DATA['LINEAR ACCELERATION Z (m/s²)']
TOTAL_TIME = USER_DATA['Time since start in ms ']
EUCLID_ACC = LINACC_X**2+LINACC_Y**2+LINACC_Z**2
EUCLID_ACC = EUCLID_ACC.apply(math.sqrt)
#EUCLID_ACC.plot()
T_S = EUCLID_ACC

def peaks(t_s):
    """CountingSteps"""
    count = 0
    for i in range(1, len(t_s)-1):
        if t_s[i] > t_s[i-1] and t_s[i] > t_s[i+1]:
            count = count+1
    return count
TOTAL_TIME_MSECS = TOTAL_TIME[len(TOTAL_TIME)-1]
TOTAL_TIME_SECS = TOTAL_TIME_MSECS/1000
NO_OF_STEPS = peaks(-1*T_S) + peaks(T_S)
TOTAL_DISTANCE_COVERED = 0
for j in range(1, len(T_S)-1):
    TOTAL_DISTANCE = 0.5*EUCLID_ACC[j]*(TOTAL_TIME[j+1]-TOTAL_TIME[j])**2
    TOTAL_DISTANCE_COVERED += TOTAL_DISTANCE
DIST_IN_METERS = TOTAL_DISTANCE_COVERED/1000000
AVG_SPEED = DIST_IN_METERS/TOTAL_TIME_SECS
print("The total distance covered is %d meters"%DIST_IN_METERS)
print("The total no of steps taken is %d steps"%NO_OF_STEPS)
print("The actual number of steps are 100 steps")
print("The total time taken is %d seconds"%TOTAL_TIME_SECS)
print("The average speed is %.3f meters/sec"%AVG_SPEED)
print("Step height of staircase is %.3f meters"%(DIST_IN_METERS/NO_OF_STEPS))
