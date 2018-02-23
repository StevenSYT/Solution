

class listClass:
   def __init__(self, myList = []):
      self.myList = myList

   def uniItems(self):
         output = set()
         for item in self.myList:
            output.add(item)
         return output
   def frequency(self):
      output = {}
      for item in self.myList:
         if item in output:
            output[item] += 1
         else:
            output[item] = 1
      return output
   def append(self, item):
      self.myList.append(item)
   def insert(self, item, pos = 0):
      self.myList.insert(pos, item)

      
# mylist = listClass([1,1,1,12,2,2,3,4,6,55,5,5])
# print(mylist.uniItems())
# print(mylist.frequency())
# mylist.myList.insert(0,2)
# mylist.myList.append(7)
# print(mylist.myList)
