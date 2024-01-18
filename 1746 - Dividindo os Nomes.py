def calcular_letras_atribuicao(nomes_ruas, nomes_avenidas, atribuicao):
    total_letras = 0
    abreviacoes_ruas = set()
    abreviacoes_avenidas = set()

    for i, a in enumerate(atribuicao):
        if a == 'R':
            rua_ou_avenida = nomes_ruas.pop(0)
        else:
            rua_ou_avenida = nomes_avenidas.pop(0)

        abreviacao = rua_ou_avenida

        while abreviacao in abreviacoes_ruas or abreviacao in abreviacoes_avenidas:
            abreviacao = abreviacao[:-1]

        if a == 'R':
            abreviacoes_ruas.add(abreviacao)
        else:
            abreviacoes_avenidas.add(abreviacao)

    for r in abreviacoes_ruas:
        for a in abreviacoes_avenidas:
            intersecao = r + '|' + a
            total_letras += len(intersecao)

    return total_letras


def min_letras_atribuicao(n, nomes):
    melhor_total_letras = float('inf')

    def gerar_atribuicoes(atribuicao, nomes_ruas, nomes_avenidas):
        nonlocal melhor_total_letras
        if not nomes_ruas and not nomes_avenidas:
            total_letras = calcular_letras_atribuicao([], [], atribuicao)
            melhor_total_letras = min(melhor_total_letras, total_letras)
            return

        if nomes_ruas:
            gerar_atribuicoes(atribuicao + ['R'], nomes_ruas[1:], nomes_avenidas)

        if nomes_avenidas:
            gerar_atribuicoes(atribuicao + ['A'], nomes_ruas, nomes_avenidas[1:])

    gerar_atribuicoes([], nomes[:n], nomes[n:])

    return melhor_total_letras


def main():
    print("Digite o número de ruas e avenidas (N):")
    n = int(input())

    print(f"Digite os nomes das {2 * n} ruas e avenidas:")
    nomes = [input().strip() for _ in range(2 * n)]

    print("\nNúmero mínimo total de letras nas placas:")
    print(min_letras_atribuicao(n, nomes))


if __name__ == "__main__":
    main()
