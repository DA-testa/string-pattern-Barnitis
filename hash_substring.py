# Bernhards Arnitis 221RDB128
# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    textinput = input()
    # input
    # after input type choice
    if "I" in textinput:
          return (input().rstrip(), input().rstrip())
    # input file
    if "F" in textinput:
        with open("./tests/06", 'r' ) as fr:
          pattern = fr.readline().rstrip()
          text = fr.readline().rstrip()
    return pattern, text
    
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    # this is the sample return, notice the rstrip function
    
def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    result = []
    if not text or not pattern:
        return result
    
    #prime numbers
    num = 101
    # patern hash
    ph = 0
    for char in pattern:
        ph += ord(char)
    ph %= num
    # window hash (apreikina windowu texta)
    wh = 0
    for j in range(len(pattern)):
        wh += ord(text[j])
    wh %= num

    for i in range(len(text) - len(pattern) + 1):
        if wh == ph:
            if text[i:i+len(pattern)] == pattern:
                result.append(i)
    # update window
        if i < len(text) - len(pattern):
            wh -= ord(text[i])
            wh += ord(text[i + len(pattern)])
            wh %= num
    
    return result

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

