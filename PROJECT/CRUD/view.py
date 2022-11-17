from . import Operation

def read_console():

    dataFile = Operation.read()
    index = "No"
    title = "Title"
    singer = "Singer"
    album = "Album"
    year = "Year"

    print("\n"+"+"*100)
    print(f"{index:4} | {title:20} | {singer:20} | {album:20} | {year:5}")
    print("-"*100)
    
    for index,data in enumerate(dataFile):
        dataBreak = data.split(',')
        key = dataBreak[0]
        dateAdd = dataBreak[1]
        singer = dataBreak[2]
        title = dataBreak[3]
        album = dataBreak[4]
        year = dataBreak[5]
        print(f"{index+1:4} | {title:.20} | {singer:.20} | {album:.20} | {year:5}",end="")


    print("+"*100+"\n")
