items = [1,2,3,4,5]
for index, value in enumerate(items):
    print('index:{}, value:{}'.format(index, value))
    
for index, value in enumerate(items, 200):
    print('index:{}, value:{}'.format(index, value))
