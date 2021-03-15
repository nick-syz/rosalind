# http://rosalind.info/problems/rna/

def GenerateRNA(string):
    result = []
    for i in range(len(string)):
        if string[i].upper() == 'T':
            result.append('U')
        else:
            result.append(string[i].upper())
    return ''.join(result)

if __name__ == '__main__':
    with open('rosalind_rna.txt') as f:
        string = f.read().splitlines()
    print(GenerateRNA(string[0]))
