def manual_iter():
    with open('test.txt') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            pass
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')
            
manual_iter()
