from collections import deque

def bfs_guessing_game():
    print("Think of a number between 1 and 100, and AI will try to guess it using BFS.")
    
    queue = deque(range(1, 101))  #BFS explores all possibilities from 1 - 100;
    attempts = 0
    
    while queue:
        guess = queue.popleft()  #next number in the queue
        attempts += 1
        
        print(f"AI's guess is: {guess}")
        feedback = input("Enter 'h' if too high, 'l' if too low, or 'c' if correct: ").lower()
        
        if feedback == 'c':
            print(f"I (AI) guessed the number in {attempts} attempts using BFS!")
            return
        elif feedback == 'h':
            #Remove all elements greater than the current guess
            continue
        elif feedback == 'l':
            #Remove all elements smaller than the current guess;
            continue

    print("Something went wrong!")

#Run the BFS version
bfs_guessing_game()
