def split_and_join(line):
    # write your code here
    x = line.split(" ")
    return "-".join(x)
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
    
