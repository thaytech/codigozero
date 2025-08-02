# LISTA INICIAL
nomes = ["Joaquim", "Maria", "Ana"]
print("LISTA INICIAL ", nomes)
print("_" *60)

# Adicionando elementos
nomes.append("Carlos") # Adiciona ao final
print("Após append:", nomes)
print("_" * 60)

nomes.insert(1, "Fernanda") #Insere "Fernanda" na posição 1
print("Após insert" , nomes)
print("_" *60)

# Modificando elementos
nomes[2] = "Paulo"  # Modifica o elemento no índice 2
print("Após modificação", nomes)
print("_" * 60)

# Removendo elementos
del nomes[3]   #Remove o elemento no índice 3
print("Após del", nomes)
print("_" * 60)

nomes.remove("Paulo")    #Remove a  primeira ocorrência de "Paulo"
print("Após remove:", nomes)
print("_" *60)

removido = nomes.pop(2)  #Remove e retorna o elemento no índice 2
print(f"Após pop(removido '{removido}'):",nomes)
print("_" * 60 )


nomes.clear()    # Esvazia a lista
print ("Após clear:", nomes)


