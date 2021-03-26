# http://rosalind.info/problems/deg/

def DegreeArray(graph, b):
    b[0] = int(b[0])
    b[1] = int(b[1])
    if b[0] not in graph:
        graph[b[0]] = [b[1]]
    elif b[1] not in graph[b[0]]:
        graph[b[0]].append(b[1])
    if b[1] not in graph:
        graph[b[1]] = [b[0]]
    elif b[0] not in graph[b[1]]:
        graph[b[1]].append(b[0])

def GetResult(graph):
    result = []
    for k in sorted(graph):
        result.append(str(len(graph[k])))
    return result

if __name__ == '__main__':
    graph = {}
    with open('rosalind_deg.txt') as f:
        while True:
            line = f.readline()
            if not line:
                break
            DegreeArray(graph, line.split())
    result = GetResult(graph)
    with open('rosalind_deg_result.txt', 'w') as f:
        f.write(' '.join(result))
