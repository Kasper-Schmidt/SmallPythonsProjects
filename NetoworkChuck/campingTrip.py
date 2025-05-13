# We going on a trip in my favorite rocket ship, to the fooooorest

# Stuff we need: 

# tent, sleeping bags, water, coffee, knife, rope, marshmallow, pot, oil, spices

# Python list
supplies = ["test", "sleeping bags", "water", "coffee", "knife", "rope", "marshmallow", "pot", "oil", "spices"]
#print(type(supplies))


camp_site = ["Crystal Lake", 26, 77.5, True]
#print(type(camp_site))


#supplies.append("toilet paper")                                # Tilføjer toilet paper til listen supplies
#supplies.append("bidet")                                       # Tilføjer bidet til listen supplies
supplies.extend(["toilet paper", "bidet"])                      # Med at bruge metoden extend, kan vi tilføje en liste til vores liste
#supplies = supplies + ["toilet paper", "bidet"]                # Laver ny liste, med indhold fra den gamle liste og tilføjer en mere liste til den 
supplies.insert(0, "grill")                                     # Tilføjer grill på index 0 i listen
supplies.insert(-1, "friend")                                   # Tilføjer en ven på den næstsidste plads

#supplies.clear()                                               # Sletter indhold i listen, og tilbage er en tom liste
supplies.remove("marshmallow")                                  # Sletter marshmallow fra listen
supplies.pop(3)                                                 # Fjerner index 3
print("This item was just deleted: " + supplies.pop(0))          # Sletter index 0, og printer hvad der blev slettet (grill)

print(supplies)






#Kasper = supplies[0]
#Mads = supplies[3]
#Jørgen = supplies[-1]
#Lars = supplies[-2]
#print(Kasper)
#print(Mads)
#print(Jørgen)
#print(Lars)














