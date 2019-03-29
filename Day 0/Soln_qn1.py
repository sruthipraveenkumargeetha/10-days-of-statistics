# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
from itertools import groupby
import statistics
def main():
    dimension=int(input())
    x=[int(i) for i in input().split()]
    print(statistics.mean(x))
    print(statistics.median(x))

    freqs=groupby(Counter(x).most_common(), lambda x:x[1])
    
    print(min([val for val,count in next(freqs)[1]]))
    #print(statistics.mode(x))
if __name__ =="__main__":
    main()

