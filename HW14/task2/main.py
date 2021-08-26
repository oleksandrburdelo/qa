from task2 import ITR

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list2 = list(range(1, 50))
    iterator1 = ITR(sequence=list1, start=0, stop=10, step=2)
    iterator2 = ITR(sequence=list2, start=0, stop= 50, step=4)
    for list_nums in [iterator1, iterator2]:
        print(sep='\n')
        for item in list_nums:
            print(item, end=' ')
