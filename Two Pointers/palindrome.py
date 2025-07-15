def is_palindrome_valid(s: str):
    left, right = 0, len(s)-1

    while left < right: # just goes through characters
        while left < right and not s[left].isalnum(): # while for continious skipping of characters
            left += 1
        
        while left < right and not s[right].isalnum():
            right -= 1

        if s[right] != s[left]:
            return False
        
        left += 1
        right -= 1

    return True

s = "A man, a plan, a canal: Panama"
print(is_palindrome_valid(s))

