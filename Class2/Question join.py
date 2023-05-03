'''
כתבו פונקציה שמקבלת רשימה שמכילה מחרוזות, ומפריד.
הפונקציה צריכה להשתמש ב-join.
הפונקציה צריכה להחזיר מחרוזת חדשה שמחברת את כל המחרוזות עם המפריד שניתן בפונקציה.
אבל רק את אלו שהאורך שלהן הוא לפחות 3.

בנוסף, הפונקציה צריכה להחזיר ‘Error: empty list’
במידה והרשימה ריקה

דבר אחרון, הפונקציה צריכה להחזיר ‘Error:no strings with sufficient length’
אם הרשימה לא מכילה אפילו מחרוזת אחת באורך 3.
'''


def concatenator(string_list: list, delimiter: str):
    if len(string_list) == 0:
        return 'Error: empty list'

    sufficient_strings = [string for string in string_list if len(string) >= 3]
    # for string in string_list:
    #     if len(string) >= 3:
    #         sufficient_strings.append(string)

    if len(sufficient_strings) == 0:
        return 'Error:no strings with sufficient length'

    return delimiter.join(sufficient_strings)


print(concatenator(['A', 'B', 'O', 'P', 'M'], ':'))

