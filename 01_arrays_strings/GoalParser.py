class Solution:
    def interpret(self, command: str) -> str:
        result = []
        i = 0
        n = len(command)
        while i < n:
            if command[i] == 'G':
                result.append('G')
                i += 1
            elif command[i] == '(':
                if i + 1 < n and command[i+1] == ')':
                    result.append('o')
                    i += 2
                else:
                    result.append('al')
                    i += 4
        return ''.join(result)
