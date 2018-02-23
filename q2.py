def convert(value):
   try:
      if(str(value).isdigit()):
         return int(value)
      else:
         return float(value)
   except:
      return value

print(type(convert('asd')))
