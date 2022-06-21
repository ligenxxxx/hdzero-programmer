import os
import time
import wget
import shutil

LocalRootPath = './Data/Github/'
LocaLFirmwarePath = LocalRootPath+'firmware/'
LocaLTempPath = './Data/Temp/'
LocalTargetListString = LocalRootPath + 'TargetList'

WebRootPath = 'https://raw.githubusercontent.com/ligenxxxx/HDZeroFirmware/main/'
WebTargetListString = WebRootPath + 'TargetList'

GithubConnected = True


def DownloadTargetList():
    print('\r\nDBG:Downloading TargetList from Github.com.')
    try:
        wget.download(url=WebTargetListString, out=LocaLTempPath)
        if os.path.exists(LocalTargetListString):
            os.remove(LocalTargetListString)
        print('\r\nDBG:Done.')
        shutil.move(LocaLTempPath+'TargetList', LocalTargetListString)

    except:
        print('\r\nDBG:Download Failed. Please check if the network is connected.')


def DetectLocalPath():
    if not os.path.exists(LocalRootPath):
        os.makedirs(LocalRootPath)
    if not os.path.exists(LocaLFirmwarePath):
        os.makedirs(LocaLFirmwarePath)
    if not os.path.exists(LocaLTempPath):
        os.makedirs(LocaLTempPath)


def CheckGithubConnected():
    print('\r\nChecking network...')
    if os.system("ping https://raw.githubusercontent.com -n 1"):
        print('\r\nDBG:Download Failed. Please check if the network is connected.')
    else:
        GithubConnected = True


def DownloadThreadProc():
    DetectLocalPath()
    # CheckGithubConnected()
    if GithubConnected:
        DownloadTargetList()
