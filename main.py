import  json, time, math, statistics
from boltiot import Bolt
def compute_bounds(history_data,frame_size,factor):
    if len(history_data)<frame_size :
        return None

    if len(history_data)>frame_size :
        del history_data[0:len(history_data)-frame_size]
    Mn=statistics.mean(history_data)
    Variance=0
    for data in history_data :
        Variance += math.pow((data-Mn),2)
    Zn = factor * math.sqrt(Variance / frame_size)
    High_bound = history_data[frame_size-1]+Zn
    Low_bound = history_data[frame_size-1]-Zn
    return [High_bound,Low_bound]
FRAME_SIZE=10;
MUL_FACTOR=6;
api_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXX"
device_id  = "BOLTXXXXXX"
mybolt = Bolt(api_key,device_id)

history_data=[]
response=mybolt.isOnline()
print(response)
while True:
    response = mybolt.analogRead('A0')
  
    data = json.loads(response)
    if data['success'] != 1:
        print("There was an error while retriving the data.")
        print("This is the error:"+data['value'])
        time.sleep(10)
        continue

    print ("This is the value "+data['value'])
    sensor_value=0
    try:
        sensor_value = int(data['value'])
    except e:
        print("There was an error while parsing the response: ",e)
        continue

    bound = compute_bounds(history_data,FRAME_SIZE,MUL_FACTOR)
    if not bound:
        required_data_count=FRAME_SIZE-len(history_data)
        print("Not enough data to compute Z-score. Need ",required_data_count," more data points")
        history_data.append(int(data['value']))
        time.sleep(5)
        continue
     
    try:
        if (bound[0])==(bound[1]):
            (bound[0])=500;
            (bound[1])=1020;
        elif sensor_value < (bound[0]) and (bound[0])<560 :
            print ("ITS NIGHT ->LIGHTS ON.")
            response =mybolt.digitalWrite(0,'HIGH');
            print("This is the response ",response)
        elif sensor_value >=(bound[1]) and (bound[1])>=560:
            print ("ITS DAY ->LIGHTS OFF.")
            response = mybolt.digitalWrite(0,'LOW');
            print("This is the response ",response)
        history_data.append(sensor_value);
    except Exception as e:
        print ("Error",e)
    time.sleep(5)

