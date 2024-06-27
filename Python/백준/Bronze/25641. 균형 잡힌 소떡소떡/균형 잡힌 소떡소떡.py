def longest_balanced_soettok(n, soettok):
    # Initialize counts
    s_count = soettok.count('s')
    t_count = soettok.count('t')
    
    # Traverse from the left to balance the counts
    left = 0
    while s_count != t_count:
        if soettok[left] == 's':
            s_count -= 1
        else:
            t_count -= 1
        left += 1
    
    # Return the balanced soettok
    return soettok[left:]

# Example usage
n = int(input())
soettok = input()
print(longest_balanced_soettok(n, soettok))