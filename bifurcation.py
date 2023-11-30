import matplotlib.pyplot as plt
import numpy as np

def recorrencia_logistica(r, x0, num_iteracoes):
    pop = [x0]
    for _ in range(1, num_iteracoes):
        x_novo = r * pop[-1] * (1 - pop[-1])
        pop.append(x_novo)
    return pop

def mapa_bifurcacao(num_pontos):
    r_valores = np.linspace(0.5, 4.0, num_pontos)
    pop_eq = []

    for r in r_valores:
        populacao = recorrencia_logistica(r, 0.5, 1000)
        pop_eq.append(populacao[-1])

    return r_valores, pop_eq

def plotar_bifurcacao(r_valores, pop_eq):
    plt.scatter(r_valores, pop_eq, s=0.1, marker='.', color='black')
    plt.title('Mapa de Bifurcação para a Recorrência Logística')
    plt.xlabel('r')
    plt.ylabel('População de Equilíbrio')
    plt.show()

def main():
    # Número de pontos para subdividir o intervalo de r
    num_pontos = 20000

    # Criar o mapa de bifurcação
    r_valores, pop_eq = mapa_bifurcacao(num_pontos)

    # Exibir o mapa de bifurcação
    plotar_bifurcacao(r_valores, pop_eq)

if __name__ == "__main__":
    main()
