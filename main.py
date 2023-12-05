import random
from threading import Thread, Semaphore
from time import sleep

semaphore = Semaphore(1)

def array_gen(len_array: int, type) -> list:
    symbols = [i for i in 'abcdefghijklmnopqrstuvwxyz']
    if type == 's':
        array = [random.choice(symbols) for i in range(len_array)]
    elif type == 'f':
        array = [round(random.uniform(0, 100),2) for i in range(len_array)]
    elif type == 'i':
        array = [random.randint(0,100) for i in range(len_array)]
    else:
        return 'error type'
    return array



def bubble_sort(array, mode='1'):
    if mode == '1':
        for i in range(len(array) - 1, 0, -1):
            
            semaphore.acquire()
            print("Поток1 доступ получил")

            print('bubble:', array, end=' -> ')
            no_swap = True
            for j in range(0, i):
                if array[j + 1] < array[j]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    no_swap = False
            if no_swap:

                print(array)
                print("Поток1 доступ освободил")
                semaphore.release()
                sleep(0.5)
                return
            print(array)

            print("Поток1 доступ освободил")
            semaphore.release()
            sleep(0.5)
            
    elif mode == '2':
        for i in range(len(array) - 1, 0, -1):
            semaphore.acquire()
            print("Поток1 доступ получил")
            print('bubble:', array, end=' -> ')
            no_swap = True
            for j in range(0, i):
                if array[j + 1] > array[j]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    no_swap = False
            if no_swap:
                print(array)
                print("Поток1 доступ освободил")
                semaphore.release()
                sleep(0.5)
                return
            print(array)
            print("Поток1 доступ освободил")
            semaphore.release()
            sleep(0.5)
def insertion_sort(array, mode='1'):
    if mode == '1':
        for i in range(1, len(array)):
            semaphore.acquire()
            print("Поток2 доступ получил")
            print('insertion_sort:', array, end=' -> ')
            temp = array[i]
            j = i - 1
            while (j >= 0 and temp < array[j]):
                array[j + 1] = array[j]
                j = j - 1
            array[j + 1] = temp
            print(array)
            print("Поток2 доступ освободил")
            semaphore.release()
            sleep(0.5)
            
    elif mode == '2':
        for i in range(1, len(array)):
            semaphore.acquire()
            print("Поток2 доступ получил")
            print('insertion_sort:', array, end=' -> ')
            temp = array[i]
            j = i - 1
            while (j >= 0 and temp > array[j]):
                array[j + 1] = array[j]
                j = j - 1
            array[j + 1] = temp
            print(array)
            print("Поток2 доступ освободил")  
            semaphore.release()
            sleep(0.5)
                  
def selection_sort(array, mode='1'):
    if mode == '1':
        for i in range(0, len(array) - 1):
            semaphore.acquire()
            print("Поток3 доступ получил")
            print('selection_sort:', array, end=' -> ')
            smallest = i
            for j in range(i + 1, len(array)):
                if array[j] < array[smallest]:
                    smallest = j
            array[i], array[smallest] = array[smallest], array[i]
            print(array)
            print("Поток3 доступ освободил")
            semaphore.release()
            sleep(0.5)
            
    elif mode == '2':    
        for i in range(0, len(array) - 1):
            semaphore.acquire()
            print("Поток3 доступ получил")
            print('selection_sort:', array, end=' -> ')
            smallest = i
            for j in range(i + 1, len(array)):
                if array[j] > array[smallest]:
                    smallest = j
            array[i], array[smallest] = array[smallest], array[i]
            print(array)
            print("Поток3 доступ освободил")
            semaphore.release()
            sleep(0.5)


if __name__ == '__main__':
    array = array_gen(int(input('Введите длинну массива: ')), input('Введите тип данных массива(i - int, f - float, s - str): '))
    mode = input('Введите режим сортировки(1 по возр, 2 по убыв): ')
    print('array:',array)
    thread1 = Thread(target=bubble_sort, args=(array, mode))
    thread2 = Thread(target=insertion_sort, args=(array,mode))
    thread3 = Thread(target=selection_sort, args=(array, mode))
    
    # Запускаем потоки
    thread1.start()
    thread2.start()
    thread3.start()

    # Ожидаем завершения всех потоков
    thread1.join()
    thread2.join()
    thread3.join()
