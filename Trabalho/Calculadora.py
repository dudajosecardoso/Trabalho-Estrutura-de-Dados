def precedence(op1,op2):
    precedence= {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }

    return precedence[op1]>precedence[op2]

def apiOperator(operatorsStack,operandsStack):
    operator= operatorsStack.pop()
    num2= operandsStack.pop()
    num1= operandsStack.pop()

    if operator== '+':
        operandsStack.push(num1+num2)
    elif operator== '-':
        operandsStack.push(num1-num2)
    elif operator== '*':
        operandsStack.push(num1*num2)
    elif operator== '/':
        operandsStack.push(num1/num2)

def calculate(expression):
    operatorStack= Stack()
    operandStack= Stack()
    num=''

    for char in expression:
        if char.isdigit():
            num+= char
        elif char in '+-*/':
            if num:
                operandStack.push(float(num))
                num= ''
            while (not operatorStack.empty() and precedence(operatorStack.peek(),char)):
                apiOperator(operatorStack, operandStack)
            operatorStack.push(char)
        elif char== '(':
            operatorStack.push(char)
        elif char== ')':
            while operatorStack.peek!= '(':
                apiOperator(operatorStack,operandStack)
            operatorStack.pop()
    
    if num:
        operandStack.push(float(num))
    
    while not operatorStack.empty():
        apiOperator(operatorStack,operandStack)

    return operandStack.pop()
