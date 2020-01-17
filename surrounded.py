board = [['X','X','X','X'],
        ['X','O','O','X'],
        ['X','X','O','O'],
        ['X','O','X','X']]


def pretty_print(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=' ')
        print('\n')


def solve(board):
    print('Before')
    pretty_print(board)

    m = len(board)
    n = len(board[0])

    boundary_points = []
    inside_bad = []

    for i in range(m):
        for j in range(n):
            if board[i][j] == 'X':
                inside_bad.append([i, j])

    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O' and (i==0 or j==0 or i==m-1 or j==n-1):
                boundary_points.append([i,j])

    visited = []

    free_points = boundary_points

    # print(boundary_points)

    for point in boundary_points:
        stack = [point]
        while stack:
            a = stack.pop()
            print('Currently exploring {}'.format(a))
            
            for neighbor in neighbors(a[0],a[1],board,m,n):
                if neighbor not in visited and neighbor not in inside_bad:
                    stack.append(neighbor)
                    free_points.append(neighbor)

                    print('Stack at {} is {}'.format(neighbor,stack))
            
                visited.append(neighbor)


    for i in range(m):
        for j in range(n):
            board[i][j] = 'X'
            if [i, j] in free_points:
                board[i][j] = 'O'


    print('After')
    pretty_print(board)


    # print(neighbors(0,0, board, m, n))

def neighbors(i, j, board, m, n):
    neighbors = [[i-1,j],[i+1,j],[i,j+1],[i,j-1]]

    valid_neighbors = [a for a in neighbors if a[0] > -1 and a[0] < m and a[1] > -1 and a[1] < n]
    return valid_neighbors

solve(board)