def decode_message(message, pattern):
    
    memo = {}
    
    
    def is_match(i, j):
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        
        if j == len(pattern):
            return i == len(message)
        
        
        if pattern[j] == '*':
            
            match = (is_match(i, j + 1) or (i < len(message) and is_match(i + 1, j)))
            memo[(i, j)] = match
            return match
        
        
        if i < len(message) and (pattern[j] == '?' or pattern[j] == message[i]):
            memo[(i, j)] = is_match(i + 1, j + 1)
            return memo[(i, j)]
        
        
        memo[(i, j)] = False
        return False
    
    return is_match(0, 0)
