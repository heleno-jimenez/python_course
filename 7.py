def copo_de_nieve (tamano): 
    for i in range(tamano):
        for j in range(tamano):
            if i == j or j == tamano//2 or i == tamano//2 or i+j == tamano-1:
                print("*", end=" ")
            else:    
                print(" ", end=" ")            
        print()

x=9
copo_de_nieve(x)                