first = ['Strings', 'Student', 'Компьютер']
second = ['Строка', 'Урбан', 'Компьютер']

def difference_lengths():
    for f, s in zip(first, second):
        yield len(f) - len(s)

def compare_strings():
    for i in range(len(first)):
        yield first[i] == second[i]

first_result = list(difference_lengths())
second_result = list(compare_strings())

print(first_result)
print(second_result)

