rank1 = 1
rank2 = 1
rank3 = 1
rank5 = 1

temprank1 = 0
temprank2 = 0
temprank3 = 0
temprank5 = 0

change1=1
change2=1
change3=1
change5=1

iterations = 0 #track num iters

#using convergence epsilon 0.001
while change1 >= 0.001 and change2 >= 0.001 and change3 >= 0.001 and change5 >= 0.001:

	rank1 = .15 + .7*(rank2)
	change1 = abs(rank1 - temprank1)
	temprank1 = rank1
	
	rank2 = .15 + .7*(rank1)
	
	change2 = abs(rank2 - temprank2)
	temprank2 = rank2
	
	rank3 = .15 + .7*(rank2/2)
	change3 = abs(rank3 - temprank3)
	temprank3 = rank3

	
	rank5 = .15 + .7*(rank2/2 + rank5 + .06)
	change5 = abs(rank5 - temprank5)
	temprank5 = rank5
	
	iterations = iterations + 1
	
print("Node 1 rank :", rank1)
print("Node 2 rank :", rank1)
print("Node 3 rank :", rank1)
print("Node 5 rank :", rank1)
print("Number of iterations :", iterations)
