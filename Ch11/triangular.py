def triangular(n):
   if n==0:
     return 0
   else:
     return n+triangular(n-1)

print(triangular(7))