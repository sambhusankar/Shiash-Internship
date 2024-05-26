# task no 5
from datetime import datetime 
import pytz

zones = pytz.all_timezones
get_time = datetime.now()
print("----------- Timezone & Time -----------")
print("")
for i in range(5): # i used loop for practise and making easier the code
    
    timezone = pytz.timezone(zones[i])
    time = get_time.now(timezone)
    print(timezone)
    print(time.strftime("%d - %m - %Y  ( %a )          %I : %M : %S %p  "))
    print("--------------------------------------------")
