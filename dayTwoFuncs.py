def factorial(n):
    if n == 1:
        return 1
    
    return n * factorial(n-1)

# print(factorial(5))


def happy(n):
    if n <= 0: 
        return 1
    
    return n * happy(n - 2)

# print(happy(8))
# print(happy(9))



def hanoi(n, Start, Process, End):
    global numMoves
    if n==1: 
        print("\nMove disk", n, "from", Start, "to", End)
        numMoves +=1
    else:
        hanoi(n-1, Start, End, Process)
        print("\nMove disk", n, "from", Start, "to", End)
        numMoves +=1
        hanoi(n-1, Process, Start, End)
    return numMoves
      
numMoves = 0
print(f"\nNumber of Moves: {hanoi(4, 'Left Tower', 'Middle Tower', 'Right Tower')}")