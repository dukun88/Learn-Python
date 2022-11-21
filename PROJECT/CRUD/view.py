from . import Operation


def create_console():

    print("\n"+"+"*100)
    print("Enter your music data :\n")
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

    Operation.create(singer,title,album,year)
    print("Your Data Has been Added ")
    read_console()

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

def update_console():
    read_console()
    while (True):
        print("Select the music data to be updated?")
        noMusic = int(input("No Music : "))
        musicData = Operation.read(index = noMusic)

        if musicData:
            break
        else:
            print("invalid music number !!")
    
    dataBreak = musicData.split(',')
    key = dataBreak[0]
    dateAdd = dataBreak[1]
    singer = dataBreak[2]
    title = dataBreak[3]
    album = dataBreak[4]
    year = dataBreak[5][:-1]

    while(True):
        print("\n"+"="*100)
        print("Which data will be updated?\n")
        print(f"1. Title\t: {title:.40}")
        print(f"2. Singer\t: {singer:.40}")
        print(f"3. Album\t: {album:.40}")
        print(f"4. Year\t\t: {year:4}\n")

        option = input("[1,2,3,4,5] : ")
        print("\n"+"="*100)

        match option:
            case "1": title = input("Title\t: ")
            case "2": singer = input("Singer\t: ")
            case "3": album = input("Album\t: ")
            case "4": 
                 while(True):
                    try:
                        year = int(input("Year(yyyy)\t: "))
                        if len(str(year)) == 4:
                            break
                        else :
                            print("Please enter the year correctly ! (YYYY)")
                    except:
                        print("Please enter the year correctly ! (YYYY)")
            case _: print("invalid input !!")

        print("Your Data Updated")
        print(f"1. Title\t: {title:.40}")
        print(f"2. Singer\t: {singer:.40}")
        print(f"3. Album\t: {album:.40}")
        print(f"4. Year\t\t: {year:4}\n")
        
        done = input("Is there anything else you want to update? (y/n)")
        if done == "n" or done == "N":
            print("\nUpdating .....\n")
            break

    Operation.update(noMusic,key,dateAdd,singer,title,album,year)

def delete_console():
    read_console()
    while (True):
        print("Select the music data to Deleted?")
        noMusic = int(input("No Music : "))
        musicData = Operation.read(index = noMusic)

        if musicData:
            dataBreak = musicData.split(',')
            key = dataBreak[0]
            dateAdd = dataBreak[1]
            singer = dataBreak[2]
            title = dataBreak[3]
            album = dataBreak[4]
            year = dataBreak[5][:-1]

            print("\n"+"="*100)
            print("This Data Will be Deleted\n")
            print(f"1. Title\t: {title:.40}")
            print(f"2. Singer\t: {singer:.40}")
            print(f"3. Album\t: {album:.40}")
            print(f"4. Year\t\t: {year:4}\n")
            
            done = input("Are You Sure ? (y/n)")
            if done == "y" or done == "Y":
                Operation.delete(noMusic)
                print("\nDeleting .....\n")
                break
        else:
            print("invalid music number !!")
        
   
