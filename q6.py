

import wx
import json


class CityInformation(wx.Frame):

   def __init__(self, parent, title):
      super(CityInformation, self).__init__(parent, title=title,
         size=(450, 350))

      self.InitUI()
      self.Centre()
      self.Show()

   def InitUI(self):

      panel = wx.Panel(self)
      sizer = wx.GridBagSizer(4, 5)

      # Use a dictionary to store the needed information for cities
      self.citiesInfo = {}

      # parse json data
      with open('ca.json') as json_data:
         d = json.load(json_data)
      for cityInfo in d:
         cityInfo = {k:cityInfo[k] for k in ('name','full_county_name','primary_latitude', 'primary_longitude') if k in cityInfo}
         self.citiesInfo[cityInfo['name']] = cityInfo
      del d

      # store the city names into a list, and store the list into ComboBox
      self.cities = list(map(lambda x: x[0], self.citiesInfo.iteritems()))

      city = wx.StaticText(panel, label="City")
      sizer.Add(city, pos=(1, 0), flag=wx.TOP|wx.LEFT, border=10)

      combo = wx.ComboBox(panel, choices = self.cities)
      sizer.Add(combo, pos=(1, 1), span=(1, 3),
         flag=wx.TOP|wx.EXPAND, border=5)

      county = wx.StaticText(panel, label="County")
      sizer.Add(county, pos=(2, 0), flag=wx.TOP|wx.LEFT, border=10)

      self.countyTx = wx.StaticText(panel)
      self.countyTx.SetBackgroundColour((255,255,255))
      sizer.Add(self.countyTx, pos=(2, 1), span=(1, 3), flag=wx.TOP|wx.EXPAND, border=5)

      latitude = wx.StaticText(panel, label="Latitude")
      sizer.Add(latitude, pos=(3, 0), flag=wx.TOP|wx.LEFT, border=10)

      self.latitudeTx = wx.StaticText(panel)
      self.latitudeTx.SetBackgroundColour((255,255,255))
      sizer.Add(self.latitudeTx, pos=(3, 1), span=(1, 3), flag=wx.TOP|wx.EXPAND, border=5)

      longtitude = wx.StaticText(panel, label="Longtitude")
      sizer.Add(longtitude, pos=(4, 0), flag=wx.TOP|wx.LEFT, border=10)

      self.longtitudeTx = wx.StaticText(panel)
      self.longtitudeTx.SetBackgroundColour((255,255,255))
      sizer.Add(self.longtitudeTx, pos=(4, 1), span=(1, 3), flag=wx.TOP|wx.EXPAND, border=5)

      # Bind event handler
      combo.Bind(wx.EVT_COMBOBOX, self.OnSelect)

      sizer.AddGrowableCol(2)
      panel.SetSizer(sizer)
   def OnSelect(self, event):
      selectedCity = self.cities[event.GetSelection()]

      if(not self.citiesInfo[selectedCity]['full_county_name']):
         self.countyTx.SetLabel('')
      else:
         self.countyTx.SetLabel(self.citiesInfo[selectedCity]['full_county_name'])
      self.latitudeTx.SetLabel(self.citiesInfo[selectedCity]['primary_latitude'])
      self.longtitudeTx.SetLabel(self.citiesInfo[selectedCity]['primary_longitude'])

if __name__ == '__main__':

   app = wx.App()
   CityInformation(None, title="City Information")
   app.MainLoop()
