class Solution:
   def isPalindr0m(self, x:int)->bool:
     x = str(x) # Coverting the integer to string
     return x == x[::-1] # Comparing the string with its reverse
# Example :-
x = 121
print(Solution().isPalindrom(x)) # Out put : True

      
