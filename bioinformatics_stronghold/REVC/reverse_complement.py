def reverse_complement(string):
    revc = ''
    for i in string:
        if i == 'A':
            revc += 'T'
        elif i == 'T':
            revc += 'A'
        elif i == 'G':
            revc += 'C'
        elif i == 'C':
            revc += 'G'
    return revc[::-1]

if __name__ == '__main__':
    with open('rosalind_revc.txt') as f:
        string = f.read().splitlines()
    print(reverse_complement(string[0]))
