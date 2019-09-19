tvoc = 64
if tvoc > 2200:
   print("unhealthy")
elif tvoc > 660 and tvoc < 2199:
   print("poor")
elif tvoc > 220 and tvoc < 659:
   print("moderate")
elif tvoc > 66 and tvoc < 219:
   print("good")
elif tvoc < 65:
   print("excellent")
