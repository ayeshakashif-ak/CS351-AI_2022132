def iddfs_number_guessing_game():
    print("Think of a number between 1 and 100, and AI will try to guess it.")
    
    def dfs_with_limit(low, high, depth_limit, attempts):
        if depth_limit < 0:
            return False
        
        # Guess is the midpoint of the current range
        guess = (low + high) // 2
        attempts += 1
        
        print(f"AI's guess is: {guess}")
        feedback = input("Enter 'h' if too high, 'l' if too low, or 'c' if correct: ").lower()
        
        if feedback == 'c':
            print(f"I (AI) guessed the number in {attempts} attempts using IDDFS!")
            return True
        elif feedback == 'h':
            # Explore the lower half
            return dfs_with_limit(low, guess - 1, depth_limit - 1, attempts)
        elif feedback == 'l':
            # Explore the upper half
            return dfs_with_limit(guess + 1, high, depth_limit - 1, attempts)
        return False
    
    def iddfs():
        depth_limit = 1
        attempts = 0
        
        while True:
            print(f"Trying with depth limit {depth_limit}")
            if dfs_with_limit(1, 100, depth_limit, attempts):
                return
            depth_limit += 1
    
    # Start the IDDFS search
    iddfs()

# Run the IDDFS version
iddfs_number_guessing_game()
