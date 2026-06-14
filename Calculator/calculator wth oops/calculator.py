import sys
class Solution:
    def utility(self, a, b, opr):
        # code here
        if opr == 1:
            return a + b
        elif opr == 2:
            return a - b
        elif opr == 3:
            return a * b
        else:
            return
    
print("Use 1/2/3 for +/-/*")
a = float(input("Enter the first num: "))
opr = int(input("Enter the operator as integer: "))
b = float(input("Enter the second num: "))


if opr != 1 and opr != 2 and opr != 3:
    print("Invalid input")
    sys.exit()
    
# assigning for user friendly
ope = None
if opr == 1:
    ope = '+'
elif opr == 2:
    ope = '-'
elif opr == 3:
    ope = 'x'

calculation = Solution()
result = calculation.utility(a, b, opr)
print(f"{result}")
print(f"Explanation: {a} {ope} {b} = {result}")