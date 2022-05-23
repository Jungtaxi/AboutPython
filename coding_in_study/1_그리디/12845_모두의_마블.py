N = int(input())
deck = list(map(int,input().split()))

print((N-2)*max(deck) + sum(deck))