import datetime

x = datetime.datetime.now()
x_datum = x.strftime("%x")
x_cas = x.strftime("%X")
print(f"\nKlasický formát:\t{x}")
print(f"Dátum:\t\t\t{x_datum}")
print(f"Čas:\t\t\t{x_cas}")
print(f"Hodina:\t\t\t{x.hour}\nMinúta:\t\t\t{x.minute}")

print(f"{x.day}.{x.month}.{x.year} - {x.hour}:{x.minute}:{x.second}")

if x.hour == 23:
  print("\nPodmienka splnená")

temp = False
setHour = 0
setMin = 1

while True:
  x = datetime.datetime.now()
  if x.hour == setHour and x.minute == setMin and not temp:
    print("Splnene")
    temp = True
  elif (x.hour != setHour or x.minute != setMin) and temp:
    temp = False
    print("reset")