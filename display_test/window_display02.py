import wx
#app = wx.App()
#app = wx.App(False)
#app = wx.App(True,"出力ファイルパス")
app = wx.App(True,None)
frame = wx.Frame(None, -1, 'Hello,World!',size=(500,500))
frame.Show()
print("Welcome")
app.MainLoop()
