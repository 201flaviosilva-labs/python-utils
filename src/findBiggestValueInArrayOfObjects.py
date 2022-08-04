def findBiggestValueInArrayOfObjects(list, getattr(el, property)):
    """
    This function will find the biggest value in a given list of objects, based on the given property

    :param list: the list to find the object
    :param property: (string) the property to search


    Example:
    class MyObject:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    arr = [
        MyObject(5, 59),
        MyObject(10, 25),
        MyObject(1, 5),
        MyObject(7, 100),
    ]

    print(findBiggestValueInArrayOfObjects(arr, "x")) # 10
    """
    sortedList = []
    for el in list:
        sortedList.append(getattr(el, property))
    return max(sortedList)
