#Euler Problem 1 -- Solution
print "    Euler Problem 1 \n\nIf we list all natural numbers below 10 that are multiples of 3 or 5, \n we get 3,5,6, and 9. \n Their sum is 23. \n\n Find the sum of all multiples of 3 or 5 below 1000"

x=0
fives = []
threes = []
total=0

for x in range (1, 1000):
    a = float(x)
    b = int(x)
    if b/3 == a/3:
        threes.append( x );
    elif b/5 == a/5:
        fives.append( x );
##print threes + fives
total = sum(threes) + sum(fives)
print "\n    Solution Total = %s" % total