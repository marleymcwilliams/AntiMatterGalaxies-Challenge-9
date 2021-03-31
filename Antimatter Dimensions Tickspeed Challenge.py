'''
Figure out optimal pathway GIVEN ALL 8 ARE UNLOCKED

def ts(n): return 3 + n
def d1(n): return 2 + 3*n
def d2(n): return 3 + 4*n
def d3(n): return 5 + 5*n
def d4(n): return 7 + 6*n
def d5(n): return 10 + 8*n
def d6(n): return 14 + 10*n
def d7(n): return 19 + 12*n
def d8(n): return 25 + 15*n

#Strategy: Bias towards upper dimensions, bias against tickspeed (will be behind)

#IMMEDIATELY buy 2 first dimensions, 2 second dimensions
Beginning algorithm:
1: 2 (2)
2: 2 (2)
3: 2 (2)
0: 3 (3)
4: 1 (1)
0: 1 (4)
5: 1 (1)
4: 1 (2)
3: 1 (3)
2: 1 (3)
1: 1 (3)
0: 3 (6)
5: 1 (2)
4: 1 (3)
6: 1 (1)
1: 1 (4)
0: 3 (9)
1: 1 (5)
0: 1 (10)
6: 1 (2)
4: 1 (4)
3: 1 (4)
1: 2 (7)
3: 2 (6)
4: 1 (5)
7: 1 (1)
2: 1 (4)
0: 5 (15)
It's a simple algorithm. Look at the cheapest options in ascending order and see if you can upgrade them.
'''
#Plotting
import matplotlib.pyplot as plt


I = [8,5,3,3,1,2,1,1,0]

P = [12,17,15,20,13,26,24,31,25]

alg = [1,2,3,0,0,4,0,5,6,3,2,1,0,0,0,1,0,0,1,5,7]

#Plotting
dat = [[[0],[P[0]]],[[0],[P[1]]],[[0],[P[2]]],[[0],[P[3]]],[[0],[P[4]]],[[0],[P[5]]],[[0],[P[6]]],[[0],[P[7]]],[[0],[P[8]]]]

t = 0

while min(P) < 310:
    t += 1
    for place in range(0,9):
        inx = P.index(sorted(P)[place])

        if(inx==0): test = 4 + (I[inx]+1)
        elif(inx==1): test = 2 + 3*(I[inx]+1)
        elif(inx==2): test = 3 + 4*(I[inx]+1)
        elif(inx==3): test = 5 + 5*(I[inx]+1)
        elif(inx==4): test = 7 + 6*(I[inx]+1)
        elif(inx==5): test = 10 + 8*(I[inx]+1)
        elif(inx==6): test = 14 + 10*(I[inx]+1)
        elif(inx==7): test = 19 + 12*(I[inx]+1)
        else: test = 25 + 15*(I[inx]+1)
        
        if test not in P:
            alg.append(inx)
            #Plotting
            for i in range(0,9):
                dat[i][0].append(t)
                if i == inx:
                    dat[i][1].append(test)
                else:
                    dat[i][1].append(dat[i][1][len(dat[i][1])-1])
            dat[inx].append(test)
            I[inx] += 1
            P[inx] = test
            break
    if(len(alg) == 1000):
        break

print('Send{1}')
print('Send{2}')
print('Send{3}')
print('Send{4}')
print('Send{4}')
print('Mouseclick, left, 1456, 575')
print('Send{1}')
print('Send{2}')
print('Send{3}')
print('Send{4}')
print('Send{5}')
print('Send{5}')
print('Mouseclick, left, 1456, 620')
print('Send{1}')
print('Send{2}')
print('Send{3}')
print('Send{4}')
print('Send{5}')
print('Send{6}')
print('Send{6}')
print('Mouseclick, left, 1456, 665')
print('Send{1}')
print('Send{2}')
print('Send{3}')
print('Send{4}')
print('Send{5}')
print('Send{6}')
print('Send{7}')
print('Send{7}')
print('Mouseclick, left, 1456, 702')

for x in alg:
    if(x == 0): print('Send {Shift}{t}')
    elif(x == 1): print('Send {1}')
    elif(x == 2): print('Send {2}')
    elif(x == 3): print('Send {3}')
    elif(x == 4): print('Send {4}')
    elif(x == 5): print('Send {5}')
    elif(x == 6): print('Send {6}')
    elif(x == 7): print('Send {7}')
    else: print('Send {8}')
    #print('sleep, 500')


#Plotting
def bruh(num,col):
    plt.plot(dat[num][0],dat[num][1],color=col)
    
def graph():
    bruh(0,'b')
    bruh(1,'g')
    bruh(2,'r')
    bruh(3,'c')
    bruh(4,'m')
    bruh(5,'y')
    bruh(6,'k')
    bruh(7,'b')
    bruh(8,'g')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.show()

'''
Take a P copy and .sort it, starting from the left, index the number to the price list.
Use the index to determine the equation and find the price one level higher.
See if this new price already exists in the list. If it doesn't print the index and update the list.
If it does, move onto the next index.
'''


