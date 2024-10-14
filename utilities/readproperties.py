import configparser

config=configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")


class ReadConfig():

    @staticmethod
    def GetApplicationURL():
       url= config.get('common info','BaseUrl')
       return url

    @staticmethod
    def GetUsername():
       url= config.get('common info','username') 
       return url

    @staticmethod
    def GetPassword():
       url= config.get('common info','password')
       return url
