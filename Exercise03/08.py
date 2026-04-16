import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def simulate_clt():
    # Parameter für den Würfel
    mu = 3.5
    var = 2.9167
    sigma = np.sqrt(var)
    
    # Die verschiedenen n-Werte aus der Aufgabe
    n_values = [1, 2, 3, 5, 10, 20, 50, 100]
    n_simulations = 1000  # Anzahl der Realisierungen von Sn

    plt.figure(figsize=(15, 10))

    for i, n in enumerate(n_values):
        # 1. Simuliere n Würfe für jede der 10.000 Realisierungen
        # Form: (n_simulations, n)
        rolls = np.random.randint(1, 7, size=(n_simulations, n))
        
        # 2. Berechne Sn nach der Formel im Bild
        # Summe über (Xi - E[Xi]) / Wurzel(n * V[Xi])
        # Das entspricht: (Summe(Xi) - n * mu) / (sigma * sqrt(n))
        sn_values = np.sum((rolls - mu) / (sigma * np.sqrt(n)), axis=1)

        # 3. Plotten des Histogramms
        plt.subplot(3, 3, i+1)
        plt.hist(sn_values, bins=6, density=True, alpha=0.6, color='skyblue', label=f'n={n}')
        
        # 4. Overlay der Standardnormalverteilung N(0,1)
        x = np.linspace(-4, 4, 100)
        plt.plot(x, norm.pdf(x, 0, 1), 'r-', lw=2, label='N(0,1)')
        
        plt.title(f'Verteilung von $S_n$ für $n={n}$')
        plt.legend()

    plt.tight_layout()
    plt.show()

simulate_clt()