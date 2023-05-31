# פותחים קובץ עם w, אם הוא לא קיים הפונקציה תיצור אותו
f = open('temp.txt', 'w')
f.write('Hello my name is Eran ')
f.write('Lior ')  # לא ימחק את הקיים, אלא ימשיך מאותה נקודה
f.close()  # סוגר את הקובץ

f = open('temp.txt', 'a')
f.write('is from Tel-Aviv')
f.close()

f = open('temp.txt', 'r')
print(f'text = {f.read(5)}')  # פונקציית read מדפיסה את כל תוכן הקובץ אלא אם אני מציין כמות תווים
f.seek(0)  # איך אני חוזר אחורה לתחילת הקובץ עם הסמן בקובץ
print(f'text2 = {f.read(5)}')
f.close()  # כאשר אנחנו סוגרים את הקובץ הסמן חוזר למיקום 0

f = open('city.txt', 'r')
# readlines()
text = f.readlines()  # type(text) = list
print(f'text = {text}')
i = 1
for line in text:
    print(f'{i}. {line}')
    i += 1
f.close()

# f = open('temp.txt', 'w')
# f.write('Hello')
# f.close()
