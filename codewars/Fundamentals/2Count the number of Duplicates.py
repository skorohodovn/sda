# def duplicate_count(text):
#     result = 0
#     lower_text = text.lower()
#     unique = []
#     print(lower_text)
#     for elem in lower_text:
#         print(f"here is result {result}")
#         if elem not in unique:
#             if lower_text.count(elem) > 1:
#                 result = result + lower_text.count(elem)
#                 print(elem)
#                 print("-")
#                 print(result)
#                 unique.append(elem)
#     return result


def duplicate_count(text):
    result = 0
    lower_text = text.lower()
    print(lower_text)

    countdict = {}

    for elem in lower_text:
        if elem in countdict:
            countdict[elem] = countdict[elem] + 1
            print(countdict)
        else:
            countdict.update({elem : 1})
            print(countdict)

    for i in countdict:
        if countdict[i] > 1:
            result = result + 1
    return result


# print(duplicate_count("abcde"))
print(duplicate_count("abcdea"))
print(duplicate_count("abcdeab"))
print(duplicate_count("abcdefghijklmnopqrstuvwxyzbaaAAB"))
# print(duplicate_count("abcdefghijklmnopqrstuvwxyzaaAb"))
print(duplicate_count("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))
print(duplicate_count("invisibility"))
