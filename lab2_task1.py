from math import log, log10 as lg, cos, sin

x = 0.3
b = 0.9
h = 0.05

def log_3(a):
    return log(a) / log(3)


print("x\ty\t\th =",(h))

while x <= b:
    print(x)
    log_sum = lg(x) + log_3(x)
    if x <= 0.4:
        #if log_sum > 0:
        y = log(log_sum)
        print('\t',y)
        #else:
            #print(round(x, 2), '\t', 'Порожня множина')
    elif 0.4 < x < 0.6:
        y = cos(sin(x**2))
        #print(round(x,2),'\t',round(y,3))
    elif x >= 0.6:   
        y = (x**3)**(1/7) + 0.5
        #print(round(x,2),'\t',round(y,3))
    
    x += h
    x = round(x,2)
    print("\t\t",y)

    #if abs(x - b) < h:
        #x = b
    
        

