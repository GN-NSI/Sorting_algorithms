# Sorting_algorithms


def belong(n,t):
    i=0
    while i<len(t):
        if n==t[i]:
            return True
        i=i+1
    return False

def greatest_in(t):
    res=t[o]
    for element in t:
        if element>res:
            res=element
    return res

def my_len(t):
    cpt=0
    for element in t:
        cpt=cpt+1
    return cpt

def map_double(t):
    res=[0]*len(t)
    for i in range (len(t)):
        res[i]=2*t[i]
    return res

def smallestin(t,i,j):
    res=t[i]
    for indice in range(i+1,j+1):
        if t[indice]<res:
            res=t[indice]
    return res
    
    
    def my_sum(t):
    res=t[0]
    for i in range(len(t)):
        res=res+t[i]
    return res

def swap(t,i,j):
    sauv=t[i]
    t[i]=t[j]
    t[j]=sauv

def remove(t,i):
    res=[0]*(len(t)-1)
    for j in range (len(t)):
        if j<i:
            res[j]=t[j]
        if j>i:
            res[j-1]=t[j]
    return res

def my_selection_sent(t):
    res=[0]*len(t)
    for i in range(len(t)):
        j=index_of_the_smallest(t)
        res=t[j]
        remove(t,j)

def index_of_the_smallest(t):
  i=0
  j=1
  for elements in t:
      if t[i]<t[j]:
          return i
      else:
          return j

def trier(t):
    for j in range(l, len(t)):
        T=t[j]
        i =j- 1
        while i>=0 and t[i]>T:
            t[i+1]=t[i]
            i=i-1
        t[i+1]= T
    return t
