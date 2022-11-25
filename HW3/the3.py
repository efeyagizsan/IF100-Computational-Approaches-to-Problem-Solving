
dataset = input('Please enter the dataset: ')
earthquake = input('Please enter the earthquake that you want to look for: ')
radius = float(input('Please enter the radius (in km): '))

dataset1 = dataset.replace(':',',')
datalist = dataset1.split(';')

lonlist = []
latlist = []
namelist = []
timelist = []
for i in datalist:
  group = i.split(',')
  for j in range(len(group)):
    if j == 0:
      namelist.append(group[j])
    if j == 1:
      timelist.append(group[j])
    if j == 2:
      latlist.append(group[j])
    if j == 3:
      lonlist.append(group[j])




output = ""

if earthquake not in namelist:
  print(earthquake, 'is not in the database.')
else:
  
  idx = namelist.index(earthquake)
  lona = float(lonlist[idx])
  lata = float(latlist[idx])
  timea = float(timelist[idx])
  count = 0
  check = True
  control = True
  for m in range(len(lonlist)):
    if m != idx:
      lonb = float(lonlist[m])
      latb = float(latlist[m])
      timeb = float (timelist[m])
      distance = float(100 *((((lona-lonb)**2) + ((lata-latb)**2))**0.5))
      if (distance < radius) and (abs(timeb - timea) < 86400) :
        count += 1
        
        if len(earthquake) < 9 :
          if check == True:
            print("For the earthquake "+earthquake+'; following(s) are the foreshocks and aftershocks:\n----------------------------------------------------------------------------')
            check = False
          print('* Earthquake',namelist[m],f'with latitude {latb:.2f} and longitude {lonb:.2f}.' )
        else:
          if control == True:

            print("For the earthquake "+earthquake+'; following(s) are the foreshocks and aftershocks:\n------------------------------------------------------------------------------')
            control = False
          print('* Earthquake',namelist[m],f'with latitude {latb:.2f} and longitude {lonb:.2f}.' )
      
  if count == 0 :
     print('There were no foreshocks and aftershocks after the earthquake',earthquake +'.')

if