from . import Database
from .Utility import randomKey
import time


def createFirstData():
    
    singer = input("Singer : ")
    title = input("Title : ")
    album = input("Album : ")
    year = input("Year : ")

    data = Database.TEMPLATE.copy()

    data["key"] = randomKey(6)
    data["date-add"] = time.strftime("%Y-%m-%d(%H:%M%z)",time.gmtime())
    data["singer"] = singer + Database.TEMPLATE["singer"][len(singer):]
    data["title"] = title + Database.TEMPLATE["title"][len(title):]
    data["album"] = album + Database.TEMPLATE["album"][len(album):]
    data["year"] = year

    dataStr= f'{data["key"]},{data["date-add"]},{data["singer"]},{data["title"]},{data["album"]},{data["year"]}\n'
    try:
        with open(Database.DB_NAME,"w",encoding="utf-8") as file:
            file.write(dataStr)
    except Exception as error:
        print(error)

def read():

    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            return content
    except:
        print("Error When Read Database")
        return False

    

    