import sys

sys.setrecursionlimit(1500)
count = 0


def play():
    global count
    count = count + 1
    print("Rakib ",count)
    play()


play()

