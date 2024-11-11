a = 0
b = 0.5
h = 0.05
d = 0.001

def function(X):
    sum = 0
    n = 1
    while x <= b:
        formula = (-1)**(n+1)*(((x-1)**n)/n)
        sum += formula 
        if abs(formula) < d:
            break
        n += 1
        return sum 
x = a

print('__________________________')
print("| x     |         sum     |")
print("|-------|-----------------|") 

while x <= b:
    print('|',x, '\t|\t', function(x),'    |')
    x += h
    x = round(x,2)
print('__________________________')