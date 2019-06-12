list1 = [1, 3, 5, [22, 33, 44, [7, 9, 11]], [100, 200, 300], 7, 11]
for i in range(len(list1)):
    if type(list1[i]) == 'list':
        print(list1[i][j])
    else:
        print(list1[i])
