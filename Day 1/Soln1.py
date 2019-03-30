# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics
def main():

    N=int(input())
    X=[int(i) for i in input().split()]
    Q2=statistics.median(X)
    q1=[q for q in X if q<Q2]
    q3=[q for q in X if q>Q2]
    print (int(statistics.median(q1)))
    print (int(Q2))
    print (int(statistics.median(q3)))




if __name__ == "__main__":
    main()
