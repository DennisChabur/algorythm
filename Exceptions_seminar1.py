''' 1) Реализуйте 3 метода, чтобы в каждом из них получить разные исключения'''

def exception_1():
    # x = 10/0
    pass

def exception_2():
    x = 'hello'
    # x += 10
    pass

def exception_3():
    x = [1,2,3,4,5]
    # y = x[5]
    pass

exception_1()
exception_2()
exception_3()

'''2) Реализуйте метод, принимающий в качестве аргументов два целочисленных массива, 
и возвращающий новый массив, каждый элемент которого равен разности элементов двух 
входящих массивов в той же ячейке. Если длины массивов не равны, необходимо как-то оповестить пользователя.'''

def array_members_sum(list1, list2):
    list3 = []
    if len(list1) != len(list2):
        return 'LengthListEqualsError'
    for i in range(len(list1)):
        list3.append(list1[i] - list2[i])
    return list3


def array_members_sum_TRY_EXCEPT(list1, list2):
    list3 = []
    if len(list1) != len(list2):
        raise Exception('LengthListEqualsError')
    for i in range(len(list1)):
        list3.append(list1[i] - list2[i])
    return list3

print(array_members_sum([5,4,3,2,1], [1,2,3,4,5]))
print(array_members_sum([1], [1,2]))

print(array_members_sum_TRY_EXCEPT([5,4,3,2,1], [1,2,3,4,5]))
print(array_members_sum_TRY_EXCEPT([1], [1,2]))

'''3) * Дополнительно * Реализуйте метод, принимающий в качестве аргументов два целочисленных массива, 
и возвращающий новый массив, каждый элемент которого равен частному элементов двух входящих массивов в 
той же ячейке. Если длины массивов не равны, необходимо как-то оповестить пользователя. Важно: 
При выполнении метода единственное исключение, которое пользователь может увидеть - RuntimeException, т.е. ваше.'''

