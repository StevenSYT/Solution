def minThree(a,b,c):
   min = a
   if (b < min):
      min = b
   if(c < min):
      min = c
   return min

print(minThree(23,13,12))
