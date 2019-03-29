# Enter your code here. Read input from STDIN. Print output to STDOUT

def main():
    N=int(input())
    X=[int(i) for i in input().split()]
    W=[int(i) for i in input().split()]
    wm=0;
    for i in range(N):
        wm=wm+(X[i])*W[i]
    print (round(wm/sum(W),1))



if __name__ =="__main__":
    main()
