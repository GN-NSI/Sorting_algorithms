# Sorting_algorithms

def belong(n,t):
    i=0
    while i<len(t):
        if n==t[i]:
            return True
        i=i+1
    return False

def Testbelong():
    n=8
    t=[1,2,3,6,10,238,572]
    i=0
    while i<len(t):
        if n==t[i]:
            return True
        i=i+1
    return False


def my_sum(t):
    res=t[0]
    for i in range(len(t)):
        res=res+t[i]
    return res

def Testmysum(t):
    t=[1,2,3,6,10,238,572]
    res=t[0]
    for i in range(i,len(t)):
        res=res+t[i]
    return res


def greatest_in(t):
    res=t[i]
    for element in t:
        if element>res:
            res=element
    return res

def Testgreatest_in():
    t=[1,2,3,6,10,238,572] 
    res=t[i]
    for element in t:
        if element > res:
            res=element

def my_len(t):
    cpt=0
    for element in t:
        cpt=cpt+1
    return cpt

def Testmy_len():
    t=[1,2,3,6,10,238,572] 
    cpt=0
    for element in t:
        cpt = cpt+1
    return cpt

def map_double(t):
    res=[0]*len(t)
    for i in range (len(t)):
        res[i]=2*t[i]
    return res

def Testmap_double():
    t=[1,2,3,6,10,238,572] 
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

def Tsmallestin():
    t=[1,2,3,6,10,238,572] 
    for indice in range (i,j+1):
        if t[indice]<res:
            res =t[indice]
        return (res)

def swap(t,i,j):
    sauv=t[i]
    t[i]=t[j]
    t[j]=sauv
    
    def Testswap():
    t=[1,2,3,6,10,238,572] 
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

def Testremove():
    t=[1,2,3,6,10,238,572] 
    res=[0]*(len(t)-1)
    for j in range:
        if j< i:
            res[j]=t[j]
        if j>i:
            res [j-1]=t[j]
    return (t,j)

def my_selection_sort(t):
    res=[0]*len(t)
    for i in range(len(t)):
        j=index_of_the_smallest(t)
        res=t[j]
        remove(t,j)

def index_of_the_smallest(t,i,j):
  i=0
  j=1
  for elements in t:
      if t[i]<t[j]:
          return i
      else:
          return j
    
    def Testindex_of_the_smallest(t,i,j):
  t=[5,8,9,12,54]      
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
