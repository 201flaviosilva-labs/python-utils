def findObjectWithPropertyValue(list, property, value):
    """
    This will the first object of a given list of objects, that the given property have the given value

    :param list: the list to find the object
    :param property: (string) the property to search
    :param value: the value to check
    :return: (obejct/boolean) the matched value

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

    print(findObjectWithPropertyValue(arr, "x", 10) # {x: 10, y: 25}
    """
    for el in list:
        if getattr(el, property) == value: return el
    return False



