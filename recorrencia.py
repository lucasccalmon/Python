import matplotlib.pyplot as plt

def recorrencia_logistica(r, x0, num_iteracoes):
    pop = [x0]
    for _ in range(1, num_iteracoes):
        x_novo = r * pop[-1] * (1 - pop[-1])
        pop.append(x_novo)
    return pop

def plotar_grafico(populacao):
    plt.plot(populacao, marker='o')
    plt.title('Recorrência Logística')
    plt.xlabel('Iterações')
    plt.ylabel('População')
    plt.show()

def main():
    # Obter entrada do usuário para r e x0
    r = float(input('Digite o valor de r: '))
    x0 = float(input('Digite o valor da população inicial (x0): '))

    # Número de iterações
    num_iteracoes = 100

    # Simular recorrência logística
    populacao = recorrencia_logistica(r, x0, num_iteracoes)

    # Exibir gráfico
    plotar_grafico(populacao)

if __name__ == "__main__":
    main()