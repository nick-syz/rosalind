# http://rosalind.info/problems/list-view/?location=algorithmic-heights

def fibonacci(element):
    if element == 0:
        return 0
    if element == 1:
        return 1
    return fibonacci(element-1) + fibonacci(element-2)

if __name__ == '__main__':
    with open('rosalind_fibo.txt') as f:
        element = f.read().splitlines()
    print(fibonacci(int(element[0])))
