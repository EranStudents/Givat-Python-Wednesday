names = []  # יצירת רשימה ריקה
for i in range(5):
    name = input("Enter your name:")
    names.append(name)

f = open('names.txt', 'a')
for name in names:
    if len(name) > 4 and name[0].isupper():  # בודק את התנאים
        f.write(f'{name}\n')  # כותב לתוך הקובץ ואחרי כל שם אני יורד שורה
f.close()

f = open('names.txt', 'r') # פותח אותו לקריאה
print(f'all names in names.txt are : {f.read()}') # מדפיס את תוכן הטקסט
