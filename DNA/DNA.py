# http://rosalind.info/problems/dna/

def nucleotides_count(string):
    nucls = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for i in string:
        nucls[i] += 1
    return nucls['A'], nucls['C'], nucls['G'], nucls['T']

if __name__ == '__main__':
    with open('rosalind_dna.txt') as f:
        string = f.read().splitlines()
    print(nucleotides_count(string[0]))
