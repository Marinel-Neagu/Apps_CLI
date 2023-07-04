def fibonacci():
    fibonacci_list = [0, 1]
    limit = int(input('Please put a limit: '))
    while True:
        if fibonacci_list[-1] + fibonacci_list[-2] <= limit:
            next_number = fibonacci_list[-1] + fibonacci_list[-2]
            fibonacci_list.append(next_number)
        else:
            break
    print('Here is you sequence: ', ' '.join(str(i) for i in fibonacci_list))


fibonacci()
