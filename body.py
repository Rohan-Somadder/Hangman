''' Contains different states of body of hangman'''


def man(num):
    ''' returns the state of man acc to the input'''
    if num == 0:
        body = '''
|-------|
|       |
|      (.)
|      /|\\
|     / | \\
|      /|\\
|     / | \\
|
'''
    elif num == 1:
        body = '''
|-------|
|       |
|      (.)
|      /|\\
|     / | \\
|      /|
|     / |
|
'''
    elif num == 2:
        body = '''
|-------|
|       |
|      (.)
|      /|\\
|     / | \\
|       |
|       |
|
'''
    elif num == 3:
        body = '''
|-------|
|       |
|      (.)
|      /|
|     / | 
|       |
|       |
|
'''
    elif num == 4:
        body = '''
|-------|
|       |
|      (.)
|       |
|       | 
|       |
|       |
|
'''
    elif num == 5:
        body = '''
|-------|
|       |
|      (.)
|       |
|       | 
|       |
|       |
|
'''
    elif num == 6:
        body = '''
|-------|
|       |
|      (xx)
|       
|        
|       
|       
|
'''
    if 0 <= num <= 6:
        return body
