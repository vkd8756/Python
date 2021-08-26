class Stack:
    def __init__(self,c,s=[]):
        self.s=[]
        self.c=c
        self.size=0
    def push(self,x):
        if self.size<=self.c:
            self.s.append(x)
            self.size+=1
        else:
            return
    def pop(self):
        if self.size>0:
            self.s.pop()
            self.size-=1
        else:
            return
    def top(self):
        if self.size>0:
            return self.s[-1]
        else:
            return None
    def len(self):
        return self.size
    def pl(self):
        print(self.s)

l=list(map(int,input().split()))
n=l[1]
cap=l[0]
st=Stack(cap)
#a=[[0,2],[1,4],[5,3]]
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
time=0
for i in a:

    atime,ptime=i[0],i[1]

    if atime >= time:
        st.push(atime)
        time += ptime
        print(atime)
    elif atime<time and st.len()<cap:
        print(time)
        time+=ptime
        if  st.top()!=atime and st.len()<=cap:
            st.pop()
        st.push(atime)
    elif atime<time:
        print(-1)

