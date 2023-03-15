import time
st = time.time()


def selectionsort(l, size):
   
    for i in range(size):
        min_idx = i

        for j in range(i + 1, size):
         
            if l[j] < l[min_idx]:
                min_idx = j
         
        (l[i], l[min_idx]) = (l[min_idx], l[i])

import random
dataset=[]
for i in range(49):
    #x=random.randrange(0, 500000339783)
    dataset.append(i)
size = len(dataset)
selectionsort(dataset, size)
print(dataset)


et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')