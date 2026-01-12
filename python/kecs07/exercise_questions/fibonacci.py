#to write a function that calculates fibonacci series upto n terms:

def fibonacci(num: int):
    if num == 0:        #chatgpt btaya h...edge cases ka dhyan rkho
        return []
    if num == 1:
        return [1]

    fibList = [1, 1]
    current = 1
    previous = 1
    for i in range(num-2):
        next_element = current + previous
        fibList.append(next_element)
        current, previous = next_element, current

    return fibList

terms = fibonacci(int(input("Enter number of terms for the fibonacci series: ")))
for i in terms:
    print(i, end = " ")
