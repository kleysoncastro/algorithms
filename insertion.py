
def insertion(vec):
   n = len(vec)
   
   for j in range(1, n):
       chave = vec[j]
       i = j -1
       while i >= 0 and vec[i] > chave:
           vec[i+1] = vec[i]
           i -=1
       vec[i+1] = chave

vec = [3, 5, 1, 2, 6]

print("Arranjo não ordenado: ", vec)
insertion(vec)
print("Arranjo ordenado:", vec)

