def fibonacci(n):
    arr=[0,1]
    counter=0
    while counter<n-1:
        arr.append(arr[-1]+arr[-2])
        counter+=1
    return arr[-1]



def lucas(n):
        arr=[2,1]
        counter=0
        while counter<n-1:
            arr.append(arr[-1]+arr[-2])
            counter+=1
        return arr[-1]


def series(n,first_index,second_index):
        arr=[first_index,second_index]
        counter=0
        while counter<n-1:
            arr.append(arr[-1]+arr[-2])
            counter+=1
        return( arr[-1])
        


def sum_series(n,first_index=0,second_index=0):
    if first_index==2 and second_index==1:
        return lucas(n)     
    elif first_index==0 and second_index==1:
        return fibonacci(n)   
    else:
       return series(n,first_index,second_index)


