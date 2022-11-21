from . import Database
from .Utility import randomKey
import time
import os


def createFirstData():
    
    singer = input("Singer : ")
    title = input("Title : ")
    album = input("Album : ")
    while(True):
        try:
            year = int(input("Year (YYYY): "))
            if len(str(year)) == 4:
                break
            else :
                print("Please enter the year correctly ! (YYYY)")
        except:
            print("Please enter the year correctly ! (YYYY)")


    data = Database.TEMPLATE.copy()

    data["key"] = randomKey(6)
    data["date-add"] = time.strftime("%Y-%m-%d(%H:%M%z)",time.gmtime())
    data["singer"] = singer + Database.TEMPLATE["singer"][len(singer):]
    data["title"] = title + Database.TEMPLATE["title"][len(title):]
    data["album"] = album + Database.TEMPLATE["album"][len(album):]
    data["year"] = str(year)

    dataStr= f'{data["key"]},{data["date-add"]},{data["singer"]},{data["title"]},{data["album"]},{data["year"]}\n'
    try:
        with open(Database.DB_NAME,"w",encoding="utf-8") as file:
            file.write(dataStr)
    except Exception as error:
        print(error)

def read(**kwargs):

    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            musics = len(content)
            if "index" in kwargs:
                iMusic = kwargs["index"]-1
                if iMusic < 0 or iMusic > musics:
                    return False
                else:
                    return content[iMusic]
            else:
                return content
    except:
        print("Error When Read Database")
        return False

def create(singer,title,album,year):
    data = Database.TEMPLATE.copy()

    data["key"] = randomKey(6)
    data["date-add"] = time.strftime("%Y-%m-%d(%H:%M%z)",time.gmtime())
    data["singer"] = singer + Database.TEMPLATE["singer"][len(singer):]
    data["title"] = title + Database.TEMPLATE["title"][len(title):]
    data["album"] = album + Database.TEMPLATE["album"][len(album):]
    data["year"] = str(year)

    dataStr= f'{data["key"]},{data["date-add"]},{data["singer"]},{data["title"]},{data["album"]},{data["year"]}\n'
    try:
        with open(Database.DB_NAME,"a",encoding="utf-8") as file:
            file.write(dataStr)
    except Exception as error:
        print(error)

def update(noMusic,key,dateAdd,singer,title,album,year):
    data = Database.TEMPLATE.copy()

    data["key"] = key
    data["date-add"] = dateAdd
    data["singer"] = singer + Database.TEMPLATE["singer"][len(singer):]
    data["title"] = title + Database.TEMPLATE["title"][len(title):]
    data["album"] = album + Database.TEMPLATE["album"][len(album):]
    data["year"] = str(year)

    dataStr= f'{data["key"]},{data["date-add"]},{data["singer"]},{data["title"]},{data["album"]},{data["year"]}\n'
    
    dataLen = len(dataStr)

    try:
        with(open(Database.DB_NAME,"r+",encoding="utf-8")) as file:
            file.seek(dataLen*(noMusic-1))
            file.write(dataStr)
    except:
        print("Error When Updating..")

def delete(noMusic):
    try:
        with(open(Database.DB_NAME,"r")) as file:
            counter = 0

            while (True):
                content = file.readline()
                if len(content) == 0 :
                    break
                elif counter == noMusic - 1:
                    pass
                else:
                    with open("data_temp.txt",'a',encoding="utf-8") as temp_file:
                        temp_file.write(content)

                counter += 1 
    except:
        print("Database Error !")

    os.rename("data_temp.txt",Database.DB_NAME)