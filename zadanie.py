# def next_bigger(number: int) -> int:
#     digits = list(str(number))
#
#     # Поиск позиции (справа налево)
#     pivot = -1
#     for i in range(len(digits) - 2, -1, -1):
#         if digits[i] < digits[i + 1]:
#             pivot = i
#             break
#
#     if pivot == -1:
#         return -1
#
#     # Поиск и замена
#     for i in range(len(digits) - 1, pivot, -1):
#         if digits[i] > digits[pivot]:
#             digits[pivot], digits[i] = digits[i], digits[pivot]
#             break
#
#     # Разворот хвоста
#     digits[pivot + 1:] = digits[pivot + 1:][::-1]
#
#     # Простое преобразование в число
#     return int(''.join(digits))
#
# print(reverse_number(2017))

# n = '1234567890'
# for f in range(len(n) -2, -1, -1):
#     print(n[f])

# def scramble(s1, s2):
#     list_s1 = list(s1)
#     list_s2 = list(s2)
#     result = False
#     for f in s2:
#         if f in list_s1:
#             list_s1.remove(f)
#             list_s2.remove(f)
#     if len(list_s2) == 0:
#         result = True
#     return result

# def duplicate_count(text):
#     count = 0
#     count_dict = {}
#     text = text.lower()
#     for word in text:
#         count_dict[word] = count_dict.get(word, 0) + 1
#
#     for key, value in count_dict.items():
#         if value >= 2:
#             count += 1
#     return count
#
# print(duplicate_count("hello"))


# def count_smileys(arr):
#     simvol_for_smile = [[';',':'],['-', '~'], [')', 'D']]
#     count = 0
#
#     for smile in arr:
#         if len(smile) == 2:
#                 if smile[0] in simvol_for_smile[0] and smile[1] in simvol_for_smile[2]:
#                     count += 1
#         elif len(smile) == 3:
#                 if smile[0] in simvol_for_smile[0] and smile[1] in simvol_for_smile[1] and smile[2] in simvol_for_smile[2]:
#                     count += 1
#     return count
#
# def canMakeNote(text1: str, text2: str) -> bool:
#     count_words = {}
#     for word in text1:
#         count_words[word] = count_words.get(word, 0) + 1
#
#     for word in text2:
#         if count_words.get(word, 0) == 0:
#             return False
#         else:
#             count_words[word] -= 1
#
#     return True
#
# print(canMakeNote('ewefygwehfwj', 'ewg'))


# def fibanacha(n: int) -> int:
#     a = 0
#     b = 1
#     for f in range(n):
#         yield a
#         a, b = b, a + b
#
# for num in fibanacha(9):
#     print(num)
#




