from pythonds.basic.stack import Stack
def balanced(str):
    stack = Stack()
    balance = True
    index = 0
    while index < len(str) and balance:
        symbol = str[index]
        if symbol in "([{":
            stack.push(symbol)
        else:
            if stack.isEmpty():
                balance = False
            else:
                top = stack.pop()
                if not matches(top, symbol):
                    balance = False
        index += 1
    if balance and stack.isEmpty():
        return "сбалансировано"
    else:
        return "несбалансировано"

def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

#сбалансированные
string_1 = '(((([{}]))))'
string_2 = '[([])((([[[]]])))]{()}'
string_3 = '{{[()]}}'

#несбалансированные
string_4 = '}{}'
string_5 = '{{[(])]}}'
string_6 = '[[{())}]'

print(balanced(string_1))