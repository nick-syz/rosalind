# http://rosalind.info/problems/list-view/?location=algorithmic-heights

# non-optimized variant
def fibonacci_1(element):
    if element == 0:
        return 0
    if element == 1:
        return 1
    return fibonacci_1(element-1) + fibonacci_1(element-2)

# version with a tail call (optimized variant)
def fibonacci(element, next=1, prev=0):
    if element == 0:
        return prev
    if element == 1:
        return next
    return fibonacci(element-1, next+prev, next)

if __name__ == '__main__':
    with open('rosalind_fibo.txt') as f:
        element = f.read().splitlines()
    print(fibonacci(int(element[0])))
