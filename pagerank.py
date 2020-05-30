rank1 = 1
rank2 = 1
rank3 = 1
rank4 = 1
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

#using convergence epsilon 0.001 - forumlas depend on the d value given = 0.7 and contruction of graph nodes
while change1 >= 0.001 and change2 >= 0.001 and change3 >= 0.001 and change5 >= 0.001:

	rank11 = rank1# save current rank
	rank1 = .06 + .7*(rank2) #compute PR
	change1 = abs(rank1 - temprank1) # find change since last iteration
	temprank1 = rank1 # hold previous ranking
	
	rank22 = rank2# save current rank
	rank2 = .06 + .7*(rank11)#compute PR
	change2 = abs(rank2 - temprank2)# find change since last iteration
	temprank2 = rank2# hold previous ranking
	
	rank33 = rank3# save current rank
	rank3 = .06 + .7*(rank22/2) #compute PR
	change3 = abs(rank3 - temprank3)# find change since last iteration
	temprank3 = rank3# hold previous ranking
	
	rank44 = rank4# save current rank
	rank4 = .06 + .7*(0) #compute PR


	rank55 = rank5 # save current rank
	rank5 = .06 + .7*(rank22/2 + rank55 + rank44) #compute PR
	change5 = abs(rank5 - temprank5)# find change since last iteration
	temprank5 = rank5# hold previous ranking
	
	iterations = iterations + 1 # track iterations
		
print("FINAL OUTPUT:")
print("----------------------------------")
print("Node 1 rank :", rank1)
print("Node 2 rank :", rank2)
print("Node 3 rank :", rank3)
print("Node 4 rank :", rank4)
print("Node 5 rank :", rank5)
print("Number of iterations :", iterations)
