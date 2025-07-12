if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    unique_scores = set(arr)
    unique_scores = list(unique_scores)
    unique_scores.sort(reverse=True)
    print(unique_scores[1])
