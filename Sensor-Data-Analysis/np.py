import numpy as np

dataset = np.loadtxt("time_series_data_human_activities.csv", usecols =[3,4,5],skiprows = 1, delimiter = ",")

print(dataset.shape)

def rmsV1():
    rmsX = dataset[0:, 0] ** 2  # X-axis 
    rmsY = dataset[0:, 1] ** 2  # Y-axis
    rmsZ = dataset[0:, 2] ** 2  # Z-axis

    rmsX = np.mean(rmsX)
    rmsY = np.mean(rmsY)
    rmsZ = np.mean(rmsZ)

    rmsX = rmsX ** (1/2)
    rmsY = rmsY ** (1/2)
    rmsZ = rmsZ ** (1/2)


    print("rmsX is greater than 5?", rmsX > 5 ,"\n rmsX val:", rmsX)
    print("rmsY is greater than 5?", rmsY > 5,"\n rmsY val:", rmsY)
    print("rmsZ is greater than 5?", rmsZ > 5,"\n rmsZ val:", rmsZ)

def rmsV2():
    rms = dataset ** 2
    rms = np.mean(rms, axis = 0) # axis 0 = columns , axis 1 = rows
    rms = rms **(1/2)
    print("rms is greater than 5: ", rms > 5 )
    print("rms is greater than 5: ", rms[rms > 5] )
    print("rms vals:", rms)


rmsV1()

rmsV2()
