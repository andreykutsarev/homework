#вставками
def insert_sort(array): 
for i in range(len(array)): 
cursor = array[i] 
position = i 
while position > 0 and array[position - 1] > cursor: 
#перемещение цифры в конец списка
array[position] = array[position - 1] 
position = poreturn array

#выбором
def select_sort(array): 
for i in range(len(array)): 
min = i for j in range(i + 1, len(array)): 
#вставить  наименьшее значение
if array[j] < array[min]: 
min = j
#поместить перед отсортированным концом массива
array[min], array[i] = array[i], array[min] return array
