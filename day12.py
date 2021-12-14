import copy
def makeGraph(lines):
    graph = {}
    for l in lines:
        if l[0] in graph:
            graph[l[0]].append(l[1])
        else:
            graph[l[0]] = [l[1]]
        if l[1] not in graph:
            graph[l[1]] = [l[0]]
        else:
            graph[l[1]].append(l[0])
    return graph

def getAllPaths(graph, startKey,currPath, allPaths):
    #print("***************", startKey)
    if startKey == "end":
        allPaths.append(currPath)
        return allPaths
    for next in graph[startKey]:
        print(":::::" + "::::" * len(currPath),next)
        if next not in currPath or next.upper() == next:
            print(startKey, graph[startKey])
            nextPath = copy.deepcopy(currPath)
            nextPath.append(next)
            print("Going to", next, "from", startKey,":", nextPath)
            getAllPaths(graph, next, nextPath, allPaths)
        else:
            print("DONT GO BACK!")
    return allPaths

def appears(path, key):
    count = 0
    for p in path:
        if p == key:
            count += 1
    return count


def anyDoubles(path):
    counts = {}
    for p in path:
        if p in counts:
            counts[p] += 1
        else:
            counts[p] = 1
    for c in counts:
        if counts[c] > 1 and c == c.lower():
            return True
    return False


def getAllPaths2(graph, startKey,currPath, allPaths):
    #print("***************", startKey)
    if startKey == "end":
        allPaths.append(currPath)
       # if anyDoubles(currPath):
            #print("****************", currPath)
        return allPaths
    for next in graph[startKey]:
        #print(":::::" + "::::" * len(currPath),next)
        if next not in currPath or next.upper() == next:
            #print(startKey, graph[startKey])
            nextPath = copy.deepcopy(currPath)
            nextPath.append(next)
            #print("Going to", next, "from", startKey,":", nextPath)
            getAllPaths2(graph, next, nextPath, allPaths)
        elif appears(currPath, next) == 1 and next == next.lower() and next != "start"  and next != "end" and not anyDoubles(currPath):
            #print("GOING a second time!", next)
            #print(startKey, graph[startKey])
            nextPath = copy.deepcopy(currPath)
            nextPath.append(next)
            #print("Going to", next, "from", startKey, ":", nextPath)
            getAllPaths2(graph, next, nextPath, allPaths)

        #else:
            #print("DONT GO BACK!")
    return allPaths

def part1(lines):
    print()
    print(len(getAllPaths(makeGraph(lines), "start", ["start"], [])))

def part2(lines):
    paths = getAllPaths2(makeGraph(lines), "start", ["start"], [])
    print(len(paths))



def main():
    file = open("day12input.txt", "r");
    lines = file.read().strip().split("\n");
    for i  in range(len(lines)):
        lines[i] = lines[i].split('-')
    print(lines)
    part2(lines)

main()