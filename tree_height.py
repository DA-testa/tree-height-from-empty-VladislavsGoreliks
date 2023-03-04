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
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
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
# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
    sys.setrecursionlimit(10**7)
    main()
