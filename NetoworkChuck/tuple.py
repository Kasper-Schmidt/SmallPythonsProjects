import timeit


# Liste kan ændres
a_list = ["bil", "motorcykel", 10]

# Tuple kan ikke ændres
a_tuple = ("bil", "motorcykel", 10)




alist = ["bil", "motorcykel", 10]
alist[0] = "Chuck"
#print(alist)
# Printer liste i consol

atuple = ("bil", "motorcykel", 10)
#atuple[0] = "Chuck"
#print(atuple) 
# Fejl i consol


# List speed test
print(timeit.timeit(stmt='["red", "green", "blue", 3, 5, 6, True]', number=10000000))
# 0.28459 sekunder

# Tuple speed test
print(timeit.timeit(stmt='("red", "green", "blue", 3, 5, 6, True)', number=10000000))
# 0.04605 sekunder


# En list er mutable, så den kan ændes, hvilket betyder den har 2 blokke af memory, den ene er til mulighed for at ændre den.
# En tuple, kan ikke ændres, så den har kun 1 blok memory

# Derfor er tuples hurtigere at læse. Dette ser ikke ud af meget, men kan være en god ting at bruge, til store programmer.
# Så tuples kan være smart at bruge, for ting som ikke skal ændres, som konstanter f.eks.
# Hvis noget data kun skal læses en gang, kan tuple være en god ide
# For function returns, for hurtigere loading speed



