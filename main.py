# D: vetor de demandas diárias conhecidas (determinístico)
# T: número de dias (T = len(D))
# J: dia final coberto por um pedido feito no dia t (intervalo t..j)
# K: custo fixo por pedido
# H: custo de estocagem por unidade por dia
# C: custo unitário de compra

def custo_pedido_intervalo(D, t, j, K, H, C):
    custo = K
    k = t
    while k <= j:
        custo += C * D[k]
        custo += H * (j - k) * D[k]
        k += 1
    return custo

def solve_recursivo(D, K, H, C):
    T = len(D)
    memo = {}
    def dp(t):
        if t == T:
            return 0
        if t in memo:
            return memo[t]
        melhor = 10**18
        j = t
        while j < T:
            custo = custo_pedido_intervalo(D, t, j, K, H, C) + dp(j + 1)
            if custo < melhor:
                melhor = custo
            j += 1
        memo[t] = melhor
        return melhor

    def plano():
        dias = []
        t = 0
        while t < T:
            melhor = 10**18
            melhor_j = t
            j = t
            while j < T:
                prox = 0 if j+1 == T else memo.get(j+1, dp(j+1))
                custo = custo_pedido_intervalo(D, t, j, K, H, C) + prox
                if custo < melhor:
                    melhor = custo
                    melhor_j = j
                j += 1
            dias.append((t, melhor_j))
            t = melhor_j + 1
        return dias

    return dp(0), plano()

def solve_iterativo(D, K, H, C):
    T = len(D)
    V = [0] * (T + 1)
    nxt = [0] * T
    t = T - 1
    while t >= 0:
        melhor = 10**18
        melhor_j = t
        j = t
        while j < T:
            custo = custo_pedido_intervalo(D, t, j, K, H, C) + V[j + 1]
            if custo < melhor:
                melhor = custo
                melhor_j = j
            j += 1
        V[t] = melhor
        nxt[t] = melhor_j
        t -= 1
    dias = []
    t = 0
    while t < T:
        dias.append((t, nxt[t]))
        t = nxt[t] + 1
    return V[0], dias

def main():
    D = [4, 6, 2, 5, 3, 4, 7]
    K = 50.0
    H = 1.0
    C = 0.0

    custo_r, plano_r = solve_recursivo(D, K, H, C)
    custo_i, plano_i = solve_iterativo(D, K, H, C)

    print(round(custo_r, 2))
    print(round(custo_i, 2))
    print(plano_r)
    print(plano_i)

    if abs(custo_r - custo_i) < 1e-6:
        print("OK")
    else:
        print("DIFF")

if __name__ == "__main__":
    main()
