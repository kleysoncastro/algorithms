def insertion(vec):
    n = len(vec)

    for j in range(1, n):
        chave = vec[j]
        i = j -1

        while i >= 0 and vec[i] > chave:
            vec[i+1] = vec[i]
            i -=1
        vec[i+1] = chave