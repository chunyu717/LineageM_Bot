import os
import subprocess
from PIL import ImageGrab
import numpy as np
import win32gui, win32ui, win32con, win32api
from threading import Thread
import time
from PIL import Image
from win32gui import *
import datetime

class ADB:
    def __init__(self,Device_Name,Screen_Size):

        self.ADB_Path = "./Tool/adb.exe"
        self.Screen_Size = [1126, 720]#Screen_Size  #1280 , 720
        self.Device_Name = Device_Name
        self.LD_Path = r"D:\NOXGAMES\MOMO\\"
        self.Hwnd = 0
        self.ScreenHot = None

    def Keep_Game_ScreenHot(self,Emu_Index,file_name):
        th = Thread(target=self.Keep_Game_ScreenHot_fn,args=[Emu_Index,file_name])
        th.daemon = True
        th.start()

    def Keep_Game_ScreenHot_fn(self,Emu_Index,file_name):
        #EnumWindows(self.foo, 0)
        self.Hwnd = win32gui.FindWindow(None, 'BlueStacks')

        print ('FindWindow', win32gui.FindWindow(None, 'BlueStacks') )
        if self.Hwnd != 0:
            self.window_capture(hwnd=self.Hwnd,filename=file_name)
        
        
        while 1:
            self.window_capture(hwnd=self.Hwnd,filename=file_name)
            time.sleep(1)

    def foo(self,hwnd,mouse):
        if IsWindow(hwnd) and IsWindowEnabled(hwnd) and IsWindowVisible(hwnd):
            if GetWindowText(hwnd) == 'BlueStacks':
                self.Hwnd = hwnd
                print ('BlueStacks hwnd =', self.Hwnd )

    def Get_Self_Hawd(self,Index_Num):
        print ('Get_Self_Hawd')
        EnumWindows(self.foo, 0)
  

    def Get_Rect_Img(self,x1,y1,x2,y2):
        pass

    def window_capture(self,hwnd,filename):
        win32gui.SetForegroundWindow(hwnd)
        #win32gui.SetActiveWindow(hwnd)
        #win32gui.BringWindowToTop(hwnd)

        #win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
        win32gui.MoveWindow(hwnd, 0, 0, 1126, 720, True)

        game_rect = win32gui.GetWindowRect(int(hwnd))
        src_image = ImageGrab.grab(game_rect)
        #print (src_image.size)
        src_image = src_image.resize(self.Screen_Size,Image.ANTIALIAS)
        src_image.save(filename)
        self.ScreenHot = src_image
        print('get pic : ', datetime.datetime.now())
        # print(type(src_image))

    def window_capture2(self,hwnd,filename):
        wDC = win32gui.GetWindowDC(hwnd)
        dcObj=win32ui.CreateDCFromHandle(wDC)
        cDC=dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, 1000, 500)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0,0),(100, 100) , dcObj, (0,0), win32con.SRCCOPY)
        dataBitMap.SaveBitmapFile(cDC, filename)
        self.ScreenHot = src_image
        # Free Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

    def Touch(self,x,y,device_name=None):
        if device_name == None:
            device_name = self.Device_Name
        x = str(x)
        y = str(y)
        self.adb_call(device_name,['shell','input','tap',x,y])

    def adb_call(self,device_name,detail_list):
        command = [self.ADB_Path,'-s',device_name]
        for order in detail_list:
            command.append(order)
        print(command)
        subprocess.Popen(command)

    def Drag(self,x1,y1,x2,y2,x3,y3,delay_time=1):
        x1 = x1 * 19199 / self.Screen_Size[0]
        y1 = y1 * 10799 / self.Screen_Size[1]
        x2 = x2 * 19199 / self.Screen_Size[0]
        y2 = y2 * 10799 / self.Screen_Size[1]
        x3 = x3 * 19199 / self.Screen_Size[0]
        y3 = y3 * 10799 / self.Screen_Size[1]

        CREATE_NO_WINDOW = 134217728
        devnull = open(os.devnull, 'w')

        # if os.path.isfile('../Tool/dn_drag.bat') == 1:
        #     print("dndrag存在")
        # else:
        #     print("dndrag不存在")



        main_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

        command = [main_path+'\\Tool\\dn_drag.bat',main_path+"\\Tool\\adb.exe",
                   self.Device_Name, str(x1), str(y1), str(x2), str(y2), str(x3), str(y3), str(delay_time)]

        cmd_str = " ".join(command)
        print(command)


        output = subprocess.Popen(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        print(output.stdout.readlines())
        # os.system(cmd_str)




if __name__ == '__main__':
    # obj = ADB(Device_Name="127.0.0.1:5555",Screen_Size=[1600,720])
    # obj.Touch(573,460)
    hawd = obj.Get_Self_Hawd(0)

    # obj.window_capture(hawd,'test.png')
    obj.Drag(1164,467,1164,400,1164,370)
    # obj.LD_Call()