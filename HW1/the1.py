

shour = float(input('Please enter the maintenance starting hour: '))
sminute = float(input('Please enter the maintenance starting minute: '))
ssecond = float(input('Please enter the maintenance starting second: '))
ptimer = float(input("Please enter the maintenance duration in second(s) according to Perseverance's timer: "))

totalMarsSec = 24 * 60 * 60 + 37 * 60   
totalEarthSec = 24 * 60 * 60 
ratio_to_convert = totalMarsSec / totalEarthSec

TimeEarthSec = ratio_to_convert * ptimer


sec = TimeEarthSec % 60
TimeEarthMin = (TimeEarthSec - sec) / 60
min = TimeEarthMin % 60 
hour = (TimeEarthMin - min) / 60


Hmars = shour + hour 
Mmars = sminute + min 
Smars = ssecond + sec 


s = Smars % 60

m = (Mmars % 60) + (Smars // 60)

h = ((Hmars + (Mmars // 60)) % 24)


print(f'The time on Earth after the hold-up is {h:.0f}:{m:.0f}:{s:.2f}')

