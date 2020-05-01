import random

def Partition(a):
  if len(a)==1: 
    return([],a[0],[])
  if len(a)==2: 
    if a[0]<=a[1]:
      return([],a[0],a[1])
    else:
      return([],a[1],a[0])

  p = random.randint(0,len(a)-1)
  pivot = a[p] 
  right = []   
  left = []     
  for i in range(len(a)):
    if not i == p:
      if a[i] > pivot:
        right.append(a[i])
      else:
        left.append(a[i])
  return(left, pivot, right)
  
def QuickSelect(a,k):
  (left,pivot,right) = Partition(a)
  if len(left)==k-1:   
    result = pivot
  elif len(left)>k-1: 
    result = QuickSelect(left,k)
  else:              
    result = QuickSelect(right,k-len(left)-1)
  return result

if __name__ == '__main__':
  N = 10;
  k = 4;
  a = [random.randint(1,100) for i in range(N)]
  print('Input array: ', a)
  print('k =', k)
  b = QuickSelect(a,k)
  print('kth smallest element: ', b)
