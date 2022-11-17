from . import Operation

DB_NAME = "data.txt"
TEMPLATE = {
    "key":"XXXXXX",
    "date-add":"yyyy-mm-dd",
    "singer":255*" ",
    "title":255*" ",
    "album":255*" ", 
    "tahun":"yyyy"
}

def init_console():
    try:
        with open(DB_NAME,"r") as file:
            print("Init Done")
    except:
        print("Database Not Found, Creating New Database...")
        Operation.createFirstData()
            