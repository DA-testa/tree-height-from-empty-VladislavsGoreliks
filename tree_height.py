# python3

import sys

def compute_height(n, parents):
    tree = [[] for i in range(n)]
    root = None
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            tree[parent].append(i)
    
    def find_depth(node):
        max_depth = 1
        for child in tree[node]:
            depth = find_depth(child) + 1
            max_depth = max(max_depth, depth)
        return max_depth

    return find_depth(root)

def main():
    filename = input("Enter input file name (or press Enter for standard input): ")
    if filename and 'a' not in filename:
        try:
            with open('input/' + filename, 'r') as f:
                n = int(f.readline())
                parents = list(map(int, f.readline().split()))
        except:
            print("Error: could not read file")
            return
    else:
        n = int(input())
        parents = list(map(int, input().split()))

    print(compute_height(n, parents))

if __name__ == '__main__':
    sys.setrecursionlimit(10**7)
    main()
