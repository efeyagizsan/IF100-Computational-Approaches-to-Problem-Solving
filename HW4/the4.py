

def validRoom(inp):
  if inp.lower()=='any':
    return True
  if inp.isdigit():
    return True
  return False

def validParking(inp):
  if inp.lower()=='any' or inp.lower()=='true' or inp.lower()=='false':
    return True
  return False
def calculateAverageForAdress(dc,adr,rm,prk):
  curr = dc[adr]
  total = 0.0
  count = 0
  for lst in curr:
    if rm.lower()=='any':
      if prk.lower()=='any':
        total+=lst[3]
        count+=1
      elif lst[1].lower()==prk.lower():
          total+=lst[3]
          count+=1
    elif lst[0] == int(rm):
      if prk.lower()=='any':
        total+=lst[3]
        count+=1
      elif lst[1].lower()==prk.lower():
          total+=lst[3]
          count+=1
  if count==0:
    return 0
  return total/count      
      
f=open('housePrices.txt')
lines = f.readlines()
lines = lines[1:]
data = {}
for line in lines:
  newlist = line.strip().replace(':','_').split('_')
  address = newlist[0]
  room = int(newlist[1])
  parking = newlist[2]
  elevator = newlist[3]
  price = float(newlist[4])
  if address not in data.keys():
    data[address] = [[room,parking,elevator,price]]
  else:
    data[address].append([room,parking,elevator,price])
f.close()

roomInput = input('Enter the room number: ')
while not validRoom(roomInput):
  roomInput = input('Enter the room number: ')
parkInput = input('Enter parking option: ')
while not validParking(parkInput):
  parkInput = input('Enter parking option: ')

results = {}
for adrs in data.keys():
  value = calculateAverageForAdress(data,adrs,roomInput,parkInput)
  if value!=0:
    results[adrs]=value
if len(results)==0:
  print('No result for these options')
else:
  sortedversion = sorted(results.items(),key=lambda x:x[1],reverse=True)
  sortedversion = sortedversion[:5]
  for elmt in sortedversion:
    print(elmt[0]+'\t'+"{:.2f}".format(elmt[1]))
