def list_sort(myList):
    evennumbers = []
    oddnumbers = []
    characters = []

    # seperate list into evens,odds and characters 
    for item in myList:
        if isinstance(item, int):
            if item%2 == 0:
                evennumbers.append(item)
            else:
                oddnumbers.append(item)
        elif isinstance(item, str):
            characters.append(item)       
        else:
            print("This function does not accept this data type")

    # sort evens,odds and characters
    evennumbers.sort()
    oddnumbers.sort()
    characters.sort()

    # create dictionary for evens,odds and chars
    myList_dictionary = {'evens':evennumbers, 'odds':oddnumbers, 'chars':characters}

    print(myList_dictionary)

myList = [2,0,6,5,1,7,'z','a']
list_sort(myList)