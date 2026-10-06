class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        num1 = 0
        num2 = 0

        output= 0

        for c in tokens:

            if c == "+":
                num2 = stack.pop()
                num1 = stack.pop()
                
                output = num1+num2
                stack.append(output)
            elif c == "*":
                num2 = stack.pop()
                num1 = stack.pop()
                output =  num1 * num2
                stack.append(output)
            elif c == "-":
                num2 = stack.pop()
                num1 = stack.pop()
                output =  num1 - num2
                stack.append(output)
            elif c == "/":
                num2 = stack.pop()
                num1 = stack.pop()
                output =  int(num1 / num2)
                stack.append(output)
            else:
                ## if it is a number:
                stack.append(int(c))
                
        return stack.pop()
        
