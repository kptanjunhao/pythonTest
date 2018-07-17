#coding=utf-8
import tkinter as Tkinter
import tkinter.filedialog as TkFiledialog
import tkinter.constants as TkConstants
import tkinter.messagebox as messagebox
import com.tan.util.exif as exifUtil
from math import radians, cos, sin, asin, sqrt
import com.tan.util.earth as earth


class ImageInfo:
    gpsInfo = exifUtil.GPSInfo()
    path = ""

    def __init__(self,gpsInfo,path):
        self.gpsInfo = gpsInfo
        self.path = path

    def distance(self, lat2, lon2):
        lat1 = self.gpsInfo.latitude
        lon1 = self.gpsInfo.longitude
        return earth.distance(lat1,lon1,lat2,lon2)


class App(Tkinter.Frame):

    gpsImages = []

    def __init__(self, master=None):
        Tkinter.Frame.__init__(self,master)
        self.pack()
        self.createWidget(master)


    def createWidget(self,master):
        self.textField = Tkinter.Text(self);
        self.textField.pack()
        Tkinter.Button(self, text="选择图片", command=self.toSelectFiles).pack()

    def toSelectFiles(self):
        fileOpenOptions = {
            "filetypes": [("jpg图像","*.jpg"),\
                          ("jpeg图像","*.jpeg"),\
                          ("png图像","*.png"), \
                          ("tif图像", "*.tif"), \
                          ("tiff图像", "*.tiff"), \
                          ("全部类型","*.*"),]
        }
        filenames = TkFiledialog.askopenfilenames(**fileOpenOptions)
        self.dealFiles(filenames)


    def dealFiles(self, filenames):
        for nameTurple in filenames:
            if len(nameTurple) > 0:
                gpsInfo = exifUtil.gpsInfo(nameTurple)
                if gpsInfo:
                    self.gpsImages.append(ImageInfo(gpsInfo,nameTurple))
                else:
                    self.textField.insert("1.0", nameTurple + '没有找到地理位置信息\n')
        if len(self.gpsImages) > 0:
            baseX, baseY = earth.gsPoint(self.gpsImages[0].gpsInfo.latitude,self.gpsImages[0].gpsInfo.longitude)
            for img in self.gpsImages:
                x,y = earth.gsPoint(img.gpsInfo.latitude,img.gpsInfo.longitude)
                x = baseX - x
                y = baseY - y
                print(x,",",y)
        else:
            self.textField.insert("1.0", '------'*10+'\n')
            self.textField.insert("1.0", '无含有地理位置信息的图片\n')



app = App()
app.title = "图像拼接"
app.mainloop()