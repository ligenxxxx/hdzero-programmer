import os
import tkinter as tk

version = "0.1"
root = tk.Tk()


def CreateRootWindow():
    titleString = "HDZero Programmer"+" V"+version
    iconPath = 'Data/HDZero_16.ico'
    windowX = 640
    windowY = 480
    offsetX = (root.winfo_screenwidth() - windowX)/2
    offsetY = (root.winfo_screenheight() - windowY)/2
    root.geometry('%dx%d+%d+%d' % (windowX, windowY, offsetX, offsetY))
    root.resizable(False, False)
    root.title(titleString)
    if os.path.exists(iconPath):
        root.iconbitmap(iconPath)


def RootWindow():
    CreateRootWindow()


def RootThreadProc():
    RootWindow()
