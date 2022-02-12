rank1, rank2, rank3, rank4, rank5 = 0.2, 0.2, 0.2, 0.2, 0.2 #init ranks
temprank1,temprank2,temprank3,temprank5 = 0,0,0,0 	#inti temp rank
change1,change2,change3,change5=1,1,1,1 		#track convergence
iterations = 0 									#track num iters
#using convergence epsilon = 1-5% - forumlas depend on the d value = 0.85 
while change1 >= 0.005 or change2 >= 0.005 or change3 >= 0.005 or change5 >= 0.005:

	rank11 = rank1# save current rank
	rank1 = (0.15/5) + .85*(rank3) #compute PR
	change1 = abs(rank1 - temprank1) # find change since last iteration
	temprank1 = rank1 # hold previous ranking
	
	rank22 = rank2# save current rank
	rank2 = (0.15/5) + .85*(rank11)#compute PR
	change2 = abs(rank2 - temprank2)# find change since last iteration
	temprank2 = rank2# hold previous ranking
	
	rank33 = rank3# save current rank
	rank3 = (0.15/5) + .85*(rank22/2) #compute PR
	change3 = abs(rank3 - temprank3)# find change since last iteration
	temprank3 = rank3# hold previous ranking
	
	rank44 = rank4# save current rank
	rank4 = (0.15/5) * .85*(0) #compute PR
	
	rank55 = rank5 # save current rank
	rank5 = (0.15/5) + .85*(rank22/2 + rank55 + rank44) #compute PR
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
