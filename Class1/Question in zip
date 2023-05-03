def ran(list1: list, list2: list) -> list:
    list3 = []  # רשימה ריקה
    for item in zip(list1, list2):  # type(item) = tuple
        # item = (5,3)
        ans = item[0] * item[1]
        if ans > 100:
            list3.append(ans)

    return list3


# בדיקת הפונקציה
x = [5, 2, 6, 8, 12]
y = [42, 56, 12, 8, 3]
print(ran(x, y))
