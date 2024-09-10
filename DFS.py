def dfs_guessing_game(low=1, high=100, attempts=0):
    if low > high:
        print("Something went wrong!")
        return
    
    guess = (low + high) // 2  #mid value, // gives the integer part only
    attempts += 1
    
    print(f"AI's guess is: {guess}")
    feedback = input("Enter 'h' if too high, 'l' if too low, or 'c' if correct: ").lower()
    
    if feedback == 'c':
        print(f"AI guessed the number in {attempts} attempts using DFS!")
        return
    elif feedback == 'h':
        dfs_guessing_game(low, guess - 1, attempts)  #recursively search in the lower half
    elif feedback == 'l':
        dfs_guessing_game(guess + 1, high, attempts)  #recursively search in the upper half

# Run the DFS version
dfs_guessing_game()
