#Euler Problem 1 -- Solution
print "    Euler Problem 1 \n\nIf we list all natural numbers below 10 that are multiples of 3 or 5, \n we get 3,5,6, and 9. \n Their sum is 23. \n\n Find the sum of all multiples of 3 or 5 below 1000"

x=0
fives = []
threes = []
total=0
blank = 1

while x * 5 < 1000:
    a = x * 5
    fives.append( a );
    x += 1
x=0
while x * 3 < 1000:
    b = x * 3    
    if b in fives:
        blank +=1
    else:
        threes.append( b );
    x += 1
##print threes + fives
total = sum(threes) + sum(fives)
print "\n    Solution Total = %s" % total