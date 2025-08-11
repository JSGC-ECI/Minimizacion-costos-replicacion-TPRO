import math

def costo_acceso(j, i):
    return (i - j) * (i - j + 1) // 2

def inicializar_dp(n):
    dp = [math.inf] * (n + 1)
    dp[0] = 0  # Caso base
    return dp

def calcular_minimo_costo(c):
    n = len(c)
    dp = inicializar_dp(n)

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            costo_actual = dp[j - 1] + c[j - 1] + costo_acceso(j, i)
            dp[i] = min(dp[i], costo_actual)

    return dp[n]
