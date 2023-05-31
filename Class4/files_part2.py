import os  # os = Operating System

# os.remove()
# מקבלת שם של קובץ ומוחקת אותו
# os.remove('f.txt')

# os.getcwd()
# הפונקציה לא מקבלת שום דבר ומחזירה את המסלול לתיקייה הנוכחית
print(f'path = {os.getcwd()}')
path = os.getcwd()

# os.listdir()
# הפונקציה תחזיר רשימה כאשר כל האיברים בה הם הקבצים בתוך התיקייה
print(f'listdir = {os.listdir(path)}')

# os.mkdir()
# פונקציה שיוצרת תיקייה
os.mkdir('E')

# os.rmdir()
# פונקציה שמוחקת תיקייה
os.rmdir('E')
