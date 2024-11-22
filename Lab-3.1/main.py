import re
def process_array_command(command: str, array: list):
    com = re.match("Получить элемент по (\d+) индексу", command)
    if com:
        i = int(com.group(1))
        if 0 <= i < len(array):
            return array[i]
        return "Индекс {i} выходит за пределы массива"

    com = re.match("Получить элементы с (\d+) по (\d+) с шагом (\d+)", command)
    if com:
        start, end, step = map(int, com.groups())
        if start <= end < len(array) and step > 0:
            return array[start:end + 1:step]
        return "Неправильные границы или шаг"

    com = re.match("Получить (\d+) элемент с конца массива", command)
    if com:
        n = int(com.group(1))
        if 1 <= n <= len(array):
            return array[-n]
        return "Элемент {n}-ый с конца выходит за пределы массива"
    return "Команда не распознана"


arr = [5, 16, 1, 10, 7, 18]

print(process_array_command("Получить элемент по 1 индексу", arr))
print(process_array_command("Получить элементы с 1 по 4 с шагом 2", arr))
print(process_array_command("Получить 2 элемент с конца массива", arr))
