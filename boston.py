'''
Name:
Date:
Description: Use dictionaries and lists to manage data and show locations on the map
'''

import os
import webbrowser
#import folium
import csv


columns = ['Short Name', 'Name', 'Category', 'URL', 'Lat', 'Lon', 'Color']
MENU = """
=====================================================================
1. Find an attraction by name       2. Find attractions by category
3. Add an attraction                4. Edit an attraction
5. Delete an attraction             6. Display all attractions
7. Quit
=====================================================================
"""
attractions = []


def openfile():
    '''
    Read the data from the data file
    Add the dictionaries to the list (attractions)
    '''
    global attractions
    with open("boston.csv") as attrac:
        reader = csv.DictReader(attrac)
        for info in reader:
            attractions.append(info)

def findbyname():
    '''Find an attraction by its short name'''
    global shortnames
    name = entername()


    shortnames = [dic["Short Name"] for dic in attractions]

    dic_byname = dict(zip(shortnames,attractions))


    info = dic_byname.get(name)
    for key, value in info.items():
        print("{:<10} : {:<10}".format(key,value))



def findbycat():
    '''
    Find attractions by category
    '''
    categ_dic = {'e':"events",'s':"shopping",'t':"tourism",'u':"university"}

    category = input("Which type of attraction do you like to visti? [E]vent,[S]hopping, [T]ourism, [U]niversity: ").lower()

    while category not in ['e','s', 't', 'u']:
        print("Invalid input! Please try again.")
        category = input(
            "Which type of attraction do you like to visti? [E]vent,[S]hopping, [T]ourism, [U]niversity: ").lower()

    print("{:<15} {:<40} {:<20} {:<80} {:<15} {:<15} {:<15}".format("Short Name", "Name", "Category", "URL", "Lat", "Lon","Color"))
    for info in attractions:


        if info["Category"].lower() == categ_dic[category]:
            shortname, name, categ, url, lat, lon, color = map(str, info.values())
            print("{:<15} {:<40} {:<20} {:<80} {:<15} {:<15} {:<15}".format(shortname, name, categ, url, lat, lon, color))





def allattractions():
    '''List and display all attractions'''

    print("{:<15} {:<40} {:<20} {:<80} {:<15} {:<15} {:<15}".format("Short Name","Name","Category","URL","Lat","Lon","Color"))

    for dic in attractions:
        shortname, name, category, url, lat, lon, color = map(str,dic.values())
        print("{:<15} {:<40} {:<20} {:<80} {:<15} {:<15} {:<15}".format(shortname, name, category, url, lat, lon, color))


def addattraction():
    '''Add a new attraction'''
    global attractions
    newitem = input("please enter the short name of the new attraction: ")

    shortnames = [dic["Short Name"] for dic in attractions]
    while newitem  in shortnames:
        print("Attraction already exists. Please try again.")
        newitem = input("please enter the short name of the new attraction: ")

    newitem_info = input("please enter the new attraction info (Name, category, URL, Lat, Lon, Color):\n")

    newitem_info = newitem_info.split(',')
    newitem_info.insert(0,newitem)

    newacctration_dic = dict(zip(columns,newitem_info))
    attractions.append(newacctration_dic)

    print(f"You have add a new attraction for {newitem_info[0]}")

def editattraction():
    '''Change the marker color of an attraction'''
    global attractions
    colors = {'g':"green",'b':"blue",'o':'orange'}
    shortname = input("Please enter short name of the attraction: ")
    shortnames = [dic["Short Name"] for dic in attractions]
    while shortname not in shortnames:
        print(f"Attraction {shortname} is not found. Please try again.")
        shortname = input("Please enter short name of the attraction: ")

    newcolor = input("Please enter the new color [g]reen, [b]lue, [o]range,press Enter to keep old the color: ").lower()


    while newcolor not in ['g','b','o'] and newcolor !="":
        print("Invalid input. try again.")
        newcolor = input(
            "Please enter the new color [g]reen, [b]lue, [o]range,press Enter to keep old the color: ").lower()

    if newcolor == "":
        pass
    else:
        for i in range(len(attractions)):
            if attractions[i]["Short Name"] == shortname:
                attractions[i]['Color'] = colors[newcolor]
                print(f"You have succesfully  changed the color of icon for {shortname} to {colors[newcolor]}")



def deleteattraction():
    '''Delete an attraction'''
    global attractions
    name = entername()

    for info in attractions:
        if info["Short Name"] == name:
            print(f"Attraction {info['Name']} has been delete!")
            attractions.pop(attractions.index(info))



def quit():
    '''Quit the program and write the info back to the data file'''

    with open("boston.csv","w") as details:
        dict_writer =csv.DictWriter(details,columns)
        dict_writer.writeheader()
        dict_writer.writerows(attractions)

    print("Have a nice day")

def showonmap(attractionlist):
    # see http://fontawesome.io/icons/ for fancy icons
    icon_names = {"university": "graduation-cap",
                "tourism": "camera",
                "shopping": "shopping-cart",
                'events': "flag"}
    pass

def entername():
    '''Process user input for the short name of an attraction'''
    name = input("Please enter the short name of the attraction: ").lower()

    # code to handle the situation where the short name is not found
    while name not in [dic["Short Name"] for dic in attractions]:
        print(f"Attraction {name} is not found.please try again.")
        name = input("Please enter the short name of the attraction: ").lower()


    return name

def main():
    openfile()

    option = ""
    while True:
        print(MENU)
        option = input("Please select an option: ")
        while option not in '1234567':
            print("Invalid input! An option must be a number beween 1 and 7")
            option = input("Please select an option: ")

        option = int(option)
        if option == 1:
            findbyname()
        elif option == 2:
            findbycat()
        elif option == 3:
            addattraction()
        elif option == 4:
            editattraction()
        elif option == 5:
            deleteattraction()
        elif option == 6:
            allattractions()
        else:
            quit()
            break




main()


