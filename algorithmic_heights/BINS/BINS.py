def binary_search(n, m, array, keys):
    result = []
    for key in keys:
        result.append(search_key(array, int(key), 0, n-1))
    return result

def search_key(array, key, start, end):
    if key == array[(end-start)//2+start]:
        return (end-start)//2 + start + 1
    if start == end:
        return -1
    elif key > array[(end-start)//2+start]:
        start = (end-start)//2 + start + 1
        return search_key(array, key, start, end)
    elif key < array[(end-start)//2+start]:
        end = (end-start)//2 + start
        return search_key(array, key, start, end)

if __name__ == '__main__':
    with open('rosalind_bins.txt') as f:
        data_list = f.read().splitlines()
    n = int(data_list[0])
    m = int(data_list[1])
    array = [int(i) for i in data_list[2].split()]
    keys = [int(i) for i in data_list[3].split()]
    result = [str(i) for i in binary_search(n, m, array, keys)]
    with open('rosalind_bins_result.txt', 'w') as f:
        f.write(' '.join(result))
