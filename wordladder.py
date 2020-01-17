beginWord ='hit'
endWord = 'cog'
wordList = ['hot','dot','dog','lot','log','cog']

def neighbors(curr_word, wordList):
    neighbors = []
    status = True
    
    for word in wordList:
        index = -1
        i = 0
        status = True
        while True:
            index = index + 1
            try:
                if curr_word[index] != word[index]:
                    i = i+1
                    if i > 1:
                        status = False
                        break
            except IndexError:
                break

        if status:
            neighbors.append(word)

    return neighbors

def ladderLength(beginWord, endWord, wordList):

    queue = [(beginWord, [beginWord])]
    visited = [beginWord]

    while True:
        word, path = queue.pop(0)

        if word == endWord:
            return len(path), path
            break

        for neighbor in neighbors(word, wordList):
            if neighbor not in visited:
                queue.append((neighbor, path+[neighbor]))
                visited.append(neighbor)


    # print(neighbors('hit', wordList))

length, path = ladderLength(beginWord, endWord, wordList)

print(path)
