import time

st = time.time()


def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            if array[i] < array[min_idx]:
                min_idx = i
         
        (array[step], array[min_idx]) = (array[min_idx], array[step])



import random
dataset=[]
for i in range(4902939):
    #x=random.randrange(0, 500000339783)
    dataset.append(i)
size = len(dataset)
selectionSort(dataset, size)
print(dataset)


et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')