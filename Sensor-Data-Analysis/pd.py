import pandas as pd


dataset = pd.read_csv("Plant_1_Generation_Data.csv")

#Time Parsed
dataset["Date_time_parsed"] = pd.to_datetime(dataset["DATE_TIME"], format ="%d-%m-%Y %H:%M")

#Cleans out the PLANT_ID which is all the same number 
dataset.drop(["PLANT_ID"], axis = 1)


def cleanV1():#original version 
    # DC power
    pwrDC_m =  dataset.groupby("SOURCE_KEY")["DC_POWER"].transform("mean")
    pwrDC_std = dataset.groupby("SOURCE_KEY")["DC_POWER"].transform("std")
    pwrDC_max = dataset.groupby("SOURCE_KEY")["DC_POWER"].transform("max")


    #AC power
    pwrAC_m = dataset.groupby("SOURCE_KEY")["AC_POWER"].transform("mean")
    pwrAC_std = dataset.groupby("SOURCE_KEY")["AC_POWER"].transform("std")
    pwrAC_max = dataset.groupby("SOURCE_KEY")["AC_POWER"].transform("max")

    #Day Yield
    dY_m = dataset.groupby("SOURCE_KEY")["DAILY_YIELD"].transform("mean")
    dY_std = dataset.groupby("SOURCE_KEY")["DAILY_YIELD"].transform("std")
    dY_max = dataset.groupby("SOURCE_KEY")["DAILY_YIELD"].transform("max")

    #Total Yield
    tY_m = dataset.groupby("SOURCE_KEY")["TOTAL_YIELD"].transform("mean")
    tY_std = dataset.groupby("SOURCE_KEY")["TOTAL_YIELD"].transform("std")
    tY_max = dataset.groupby("SOURCE_KEY")["TOTAL_YIELD"].transform("max")

    dc_f = dataset[(dataset.DC_POWER > (pwrDC_m + 3 * pwrDC_std)) | (dataset.DC_POWER < (pwrDC_m - 3 * pwrDC_std))]
    ac_f = dataset[(dataset.AC_POWER > (pwrAC_m + 3 * pwrAC_std)) | (dataset.AC_POWER < (pwrAC_m - 3 * pwrAC_std))]
    dy_f = dataset[(dataset.DAILY_YIELD > (dY_m + 3 * dY_std)) | (dataset.DAILY_YIELD < (dY_m - 3 * dY_std))]
    ty_f = dataset[(dataset.TOTAL_YIELD > (tY_m + 3 * tY_std)) | (dataset.TOTAL_YIELD < (tY_m - 3 * tY_std))]

    print("DC flagged:\n", dc_f )
    print("AC flagged:\n", ac_f)
    print("DY flagged:\n", dy_f)
    print("TY flagged:\n", ty_f )
    print("DC max\n", pwrDC_max)
    print("AC max\n", pwrAC_max)
    print("DY max\n", dY_max)
    print("TY max\n", tY_max)

    dataset.to_csv("NewData.csv")
    
def cleanV2():# more advanced version
    #grouping & calling math function in one DataFrame
    source_KEY = dataset.groupby("SOURCE_KEY").agg({"DC_POWER": ["mean","std","max"], 
                                                    "AC_POWER": ["mean","std","max"], 
                                                    "DAILY_YIELD": ["mean","std","max"],
                                                    "TOTAL_YIELD": ["mean","std","max"] }).reset_index()
    
    #combined the tuples for singular name for DataFrame 
    new_val = []
    for i in source_KEY.columns:
        if(i[0] in ["DC_POWER","AC_POWER", "DAILY_YIELD" , "TOTAL_YIELD"] and i[1] in ["mean","std","max"] ):
            new_val.append(i[0] + "_" + i[1])
        else:
            new_val.append(i[0])
    source_KEY.columns = new_val
    
    #merges the dataset together with the source_KEY solved for
    merged = dataset.merge(source_KEY)

    dc_f = merged[(merged.DC_POWER > (merged["DC_POWER_mean"] + 3 * merged["DC_POWER_std"])) | (merged.DC_POWER < (merged["DC_POWER_mean"] - 3 * merged["DC_POWER_std"]))]
    ac_f = merged[(merged.AC_POWER > (merged["AC_POWER_mean"] + 3 * merged["AC_POWER_std"])) | (merged.AC_POWER < (merged["AC_POWER_mean"] - 3 * merged["AC_POWER_std"]))]
    dy_f = merged[(merged.DAILY_YIELD > (merged["DAILY_YIELD_mean"] + 3 * merged["DAILY_YIELD_std"])) | (merged.DAILY_YIELD < (merged["DAILY_YIELD_mean"] - 3 * merged["DAILY_YIELD_std"]))]
    ty_f = merged[(merged.TOTAL_YIELD > (merged["TOTAL_YIELD_mean"] + 3 * merged["TOTAL_YIELD_std"])) | (merged.TOTAL_YIELD < (merged["TOTAL_YIELD_mean"] - 3 * merged["TOTAL_YIELD_std"]))]
    
    #flagged values
    print("DC_pwr flagged:\n", dc_f)
    print("AC_pwr flagged:\n", ac_f)
    print("DY flagged:\n", dy_f)
    print("TY flagged:\n", ty_f)
    #max
    print("DC_pwr max:\n", merged["DC_POWER_max"])
    print("AC_pwr max:\n", merged["AC_POWER_max"])
    print("DY max:\n", merged["DAILY_YIELD_max"])
    print("TY max:\n", merged["TOTAL_YIELD_max"])

    merged.to_csv("MergedVals_dataset.csv")
    source_KEY.to_csv("MeanStdMax_dataset.csv")



    
    



    

#cleanV1()

cleanV2()

