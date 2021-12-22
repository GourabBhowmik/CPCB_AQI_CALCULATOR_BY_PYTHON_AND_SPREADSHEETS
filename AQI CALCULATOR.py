import csv

print("\nThis python script works on CPCB's AQI -Calculator.xls which can be downlaoded form: https://app.cpcbccr.com/ccr_docs/AQI%20-Calculator.xls\n")

print("\n\nKindly have your file in .csv format\n")
file_name = input("\nGive file name: ")
if file_name.endswith(".csv") == False:
    input(f"\n{file_name} is not in csv format kildly change it to csv format :( ")
    exit()

input(f"\nConfirm:\n\n1) {file_name} file is in the same folder.\n2) The first row is like this: DAY CO NO2 OZONE PM10 PM2.5 SO2 NH3\n To confirm press enter ")
print("\n\nSEARCHING FILE ..................\n\n")
destination_file_name = "Result" + file_name


## final checks
def check(lst):
    count = lst.count(0) # counts the number of 0 AQI
    final_aqi = ""
    
    if count >=3:
        final_aqi = None
    if final_aqi != None:    
        if lst[-3] == 0 and lst[-2] == 0: # checks if in the available data Pm2.5 and Pm10 AQI is available or not
            final_aqi = None
    if final_aqi !=None:
        final_aqi = max(lst[1],lst[2],lst[3],lst[4],lst[5],lst[6],lst[7])
    return final_aqi

## NH3 Sub-Index calculation
def get_NH3_subindex(x):
    if x == "" or x == "NA" or x == "None":
        return 0
    x = float(x)
    
    if x <= 200:
        return x * 50 / 200
    elif x <= 400:
        return 50 + (x - 200) * 50 / 200
    elif x <= 800:
        return 100 + (x - 400) * 100 / 400
    elif x <= 1200:
        return 200 + (x - 800) * 100 / 400
    elif x <= 1800:
        return 300 + (x - 1200) * 100 / 600
    elif x > 1800:
        return 400 + (x - 1800) * 100 / 600
    else:
        return 0
## NO2 Sub-Index calculation
def get_NO2_subindex(x):
    if x == "" or x == "NA" or x == "None":
        return 0
    x = float(x)
    
    if x <= 40:
        return x * 50 / 40
    elif x <= 80:
        return 50 + (x - 40) * 50 / 40
    elif x <= 180:
        return 100 + (x - 80) * 100 / 100
    elif x <= 280:
        return 200 + (x - 180) * 100 / 100
    elif x <= 400:
        return 300 + (x - 280) * 100 / 120
    elif x > 400:
        return 400 + (x - 400) * 100 / 120
    else:
        return 0
## PM2.5 Sub-Index calculation
def get_PM25_subindex(x):
    if x == "" or x == "NA" or x == "None":
        return 0
    x = float(x)
    
    if x <= 30:
        return x * 50 / 30
    elif x <= 60:
        return 50 + (x - 30) * 50 / 30
    elif x <= 90:
        return 100 + (x - 60) * 100 / 30
    elif x <= 120:
        return 200 + (x - 90) * 100 / 30
    elif x <= 250:
        return 300 + (x - 120) * 100 / 130
    elif x > 250:
        return 400 + (x - 250) * 100 / 130
    else:
        return 0
## PM10 Sub-Index calculation
def get_PM10_subindex(x):
    if x == "" or x == "NA" or x == "None":
        return 0
    x = float(x)
    
    if x <= 50:
        return x
    elif x <= 100:
        return x
    elif x <= 250:
        return 100 + (x - 100) * 100 / 150
    elif x <= 350:
        return 200 + (x - 250)
    elif x <= 430:
        return 300 + (x - 350) * 100 / 80
    elif x > 430:
        return 400 + (x - 430) * 100 / 80
    else:
        return 0
## SO2 Sub-Index calculation
def get_SO2_subindex(x):
    if x == "" or x == "NA" or x == "None":
        return 0
    x = float(x)
    
    if x <= 40:
        return x * 50 / 40
    elif x <= 80:
        return 50 + (x - 40) * 50 / 40
    elif x <= 380:
        return 100 + (x - 80) * 100 / 300
    elif x <= 800:
        return 200 + (x - 380) * 100 / 420
    elif x <= 1600:
        return 300 + (x - 800) * 100 / 800
    elif x > 1600:
        return 400 + (x - 1600) * 100 / 800
    else:
        return 0
## CO Sub-Index calculation
def get_CO_subindex(x):
    if x == "" or x == "NA" or x == "None":
        return 0
    x = float(x)
    
    if x <= 1:
        return x * 50 / 1
    elif x <= 2:
        return 50 + (x - 1) * 50 / 1
    elif x <= 10:
        return 100 + (x - 2) * 100 / 8
    elif x <= 17:
        return 200 + (x - 10) * 100 / 7
    elif x <= 34:
        return 300 + (x - 17) * 100 / 17
    elif x > 34:
        return 400 + (x - 34) * 100 / 17
    else:
        return 0
## O3 Sub-Index calculation
def get_O3_subindex(x):
    if x == "" or x == "NA" or x == "None":
        return 0
    x = float(x)
    
    if x <= 50:
        return x * 50 / 50
    elif x <= 100:
        return 50 + (x - 50) * 50 / 50
    elif x <= 168:
        return 100 + (x - 100) * 100 / 68
    elif x <= 208:
        return 200 + (x - 168) * 100 / 40
    elif x <= 748:
        return 300 + (x - 208) * 100 / 539
    elif x > 748:
        return 400 + (x - 400) * 100 / 539
    else:
        return 0
def get_SO2_subindex(x):
    if x == "" or x == "NA" or x == "None":
        return 0
    x = float(x)
    
    if x <= 40:
        return x * 50 / 40
    elif x <= 80:
        return 50 + (x - 40) * 50 / 40
    elif x <= 380:
        return 100 + (x - 80) * 100 / 300
    elif x <= 800:
        return 200 + (x - 380) * 100 / 420
    elif x <= 1600:
        return 300 + (x - 800) * 100 / 800
    elif x > 1600:
        return 400 + (x - 1600) * 100 / 800
    else:
        return 0

##################################################MAIN############################################
aqi_list = []
try:
    with open (file_name,"r") as file:
        rows = csv.DictReader(file)
        for data in rows:
            lst = []
            lst.append(data["DAY"])

            lst.append(round(get_CO_subindex(data["CO"])))
            lst.append(round(get_NO2_subindex(data["NO2"])))
            lst.append(round(get_O3_subindex(data["OZONE"])))
            lst.append(round(get_PM10_subindex(data["PM10"])))
            lst.append(round(get_PM25_subindex(data["PM2.5"])))    
            lst.append(round(get_PM25_subindex(data["SO2"])))
            lst.append(round(get_NH3_subindex(data["NH3"])))
            
            lst.append(check(lst))# appends the final aqi
            aqi_list.append(lst)
            print(lst) 
except FileNotFoundError :
    input("File not found :(")
    exit()
except  KeyError :
    input("Check the heading probably the heading is not like this: DAY CO NO2 OZONE PM10 PM2.5 SO2 NH3 \nHave your heading like the sample files:(")
    exit()
   


################################ CREATING AND INSERTING THE RESULT IN A NEW csv FILE########################
with open(destination_file_name,"w",newline = "") as result_file:
        fields = ["DAY","CO_Sub_Index","NO2_Sub_Index", "OZONE_Sub_Index","PM10_Sub_Index","PM2.5_Sub_Index","SO2_Sub_Index","NH3_Sub_Index","Final AQI"]
        result_file = csv.writer(result_file)
        result_file.writerow(fields)
        result_file.writerows(aqi_list)

input("\n\nDone :)")

