def fibonacci(limit):
    upper = 0
    lower = 0
    result = 0
    for i in range(limit):
        result = upper + lower   
        print (result)
        if result :   
            lower =  upper
            upper = result
        else :
            upper += 1
            print(upper)


limit = 13
fibonacci(limit)
