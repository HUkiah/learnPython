import os
import re
import random
import urllib.request
import win32gui
import win32con
from PIL import Image

class StealBing:

    def __init__(self):
        self.bgImageUrl = ''
        self.localFileName = ''
        self.localBMPFileName = ''
        self.content = urllib.request.urlopen('https://cn.bing.com/').read()
        self.currPath = os.path.abspath(os.curdir)+"/ImageSource/"
        self.checkPath()

    def checkPath(self):
        if not os.path.exists(self.currPath):
            os.mkdir(self.currPath)
            self.localFileName = self.currPath + 'Background.jpg'
            self.localBMPFileName = self.currPath + 'Background.bmp'
        else:
            if os.path.exists(self.currPath+"Background.bmp"):
                os.remove(self.currPath+"Background.bmp")
            self.localFileName = self.currPath + 'Background.jpg'
            self.localBMPFileName = self.currPath + 'Background.bmp'

    def parserImageURL(self):
        joinStr="https://cn.bing.com"
        tempStr = self.content.decode("utf-8")
        patternStr=r"/az/hprichbg/rb/.*\.jpg";
        matStr=re.compile(patternStr)
        matResult=re.findall(matStr,tempStr)
        self.bgImageUrl = joinStr+''.join(matResult)


    def downloadImage(self):
        if self.bgImageUrl == '':
            self.parserImageURL()
        urllib.request.urlretrieve(self.bgImageUrl, self.localFileName)


    def updataBGImage(self):
        if os.path.exists(self.localFileName):
            img = Image.open(self.localFileName)
            img.save(self.localBMPFileName)
            os.remove(self.localFileName)
            win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, self.localBMPFileName, 0)


if __name__ == '__main__':
    stealBing = StealBing()
    stealBing.downloadImage()
    stealBing.updataBGImage()