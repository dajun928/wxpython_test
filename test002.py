#!/usr/bin/python
# -*- coding: utf-8 -*-  
"""
@version : 
@file : test002.py
@time : 2019/08/09 23:38:05
@func : 
"""

import wx


app = wx.App()
win = wx.Frame(None, size=(600, 600))
bitmap1 = wx.Image("666.jpg", wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
# bitmap2 = wx.Image("qq1.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
wx.BitmapButton(win, -1, bitmap1, pos=(40, 20), size=(40, 40))
# wx.BitmapButton(win, -1, bitmap2, pos=(160, 20), size=(100, 100))
win.Show()
app.MainLoop()
