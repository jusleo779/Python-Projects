import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("Plant_1_Generation_Data.csv")

dataset["date_time_parsed"] = pd.to_datetime(dataset["DATE_TIME"], format ="%d-%m-%Y %H:%M")

fig, ax1 = plt.subplots(layout = "constrained")

#DC compare to AC power plot
def plot1():
    dc_mean = dataset.groupby(dataset["date_time_parsed"].dt.date)["DC_POWER"].mean()
    ac_mean = dataset.groupby(dataset["date_time_parsed"].dt.date)["AC_POWER"].mean()

    #plotting DC voltage
    l1 = ax1.plot(dc_mean.index, dc_mean.values, color = 'black')
    ax1.set_title("DC_POWER VS AC_POWER")


    #setting the threshold
    ax1.axhline(4800, linestyle = "--",color ="red")
    ax1.annotate("Target DC power", xy =(dc_mean.index[10],4500), xytext =(dc_mean.index[18],4550),color ='red')

    #annotation for over threshold
    exceeds = dc_mean[dc_mean > 4800]   #filtered series, index and values together
    ax1.annotate("Over threshold", xy =(exceeds.index[0],exceeds.values[0]), xytext =(dc_mean.index[18],2550),color ='blue',arrowprops = dict(arrowstyle = '->',color ='blue'))
    
    #plotting AC voltage
    ax2 = ax1.twinx()
    l2 = ax2.plot(ac_mean.index,ac_mean.values,color = 'orange',linestyle =":")
    ax2.set_ylabel("AC POWER(V)")

    

    #setting the graph backdrop /information
    ax1.tick_params(axis = 'x',rotation = 90)
    ax1.grid(True, which = "both")
    ax1.set_ylabel("DC Power(V)")
    ax1.set_xlabel("time(dates)")
    ax2.legend([l1[0],l2[0]],["DC", "AC"], loc ="lower right")
    


plot1()
plt.savefig("DC_AC voltage plot.png", dpi = 300)
plt.show()

