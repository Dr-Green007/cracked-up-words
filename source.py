result = ''
type = input("Введи слово и оно... перевернётся как то: ")
for i in range(len(type) -1, -1, -2):
    result += type[i]
print(result)
exit = input("Нажмите на Enter чтобы завершить программу")