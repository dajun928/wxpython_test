#!/usr/bin/python
# -*- coding: utf-8 -*-  
"""
@version : 
@file : wx_main.py.py
@time : 2019/08/13 22:11:39
@func : 
"""


import wx
import guiManager as FrameManager

class MainAPP(wx.App):

    def OnInit(self):
        self.manager = FrameManager.GuiManager(self.UpdateUI)
        self.frame = self.manager.GetFrame(0)
        self.frame.Show()
        return True

    def UpdateUI(self, type):
        self.frame.Show(False)
        self.frame = self.manager.GetFrame(type)
        self.frame.Show(True)

def main():
    app = MainAPP()
    app.MainLoop()

if __name__ == '__main__':
    main()