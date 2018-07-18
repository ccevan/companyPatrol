import os

def RootPath():
    rootpath = os.path.dirname(os.path.abspath(__name__))
    return rootpath