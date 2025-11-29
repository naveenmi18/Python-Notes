#write a recursive function to calculate the first natural numbers.
def calc_sum(n):
   if(n == 0):
     return
   print(n)
   calc_sum(n-1)

calc_sum(5)    
