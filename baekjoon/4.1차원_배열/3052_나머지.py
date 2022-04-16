import sys
my_list = [int(sys.stdin.readline())%42 for i in range(10)]
sys.stdout.write(str(len(set(my_list))))