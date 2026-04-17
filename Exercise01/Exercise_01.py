import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

# 1. Daten definieren
points = np.array([
    [0, 1],
    [-1, 4],
    [1, 1],
    [3, 0],
    [-2, 2]
])

# Mittelwert der Punkte (Zentroid)
mean = np.mean(points, axis=0)

# 2. Empirische Kovarianzmatrix Σ berechnen
# Wir nutzen ddof=0 für die empirische Kovarianz (Teilung durch n statt n-1)
sigma = np.cov(points, rowvar=False, ddof=0)

# 3. Inverse der Matrix Σ^-1 berechnen
sigma_inv = np.linalg.inv(sigma)

# 4. Mahalanobis-Distanz für den Punkt (1, 3) berechnen
target_point = np.array([1, 3])
diff = target_point - mean
# Formel: sqrt( (x-mu)^T * Sigma^-1 * (x-mu) )
mahalanobis_dist = np.sqrt(diff.T @ sigma_inv @ diff)

# Ergebnisse ausgeben
print("Empirische Kovarianzmatrix Σ:")
print(sigma)
print("\nInverse Kovarianzmatrix Σ^-1:")
print(sigma_inv)
print(f"\nMahalanobis-Distanz von (1, 3): {mahalanobis_dist:.4f}")

# 5. Visualisierung
fig, ax = plt.subplots(figsize=(8, 8))

# Punkte plotten
ax.scatter(points[:, 0], points[:, 1], color='blue', label='Datenpunkte')
ax.scatter(target_point[0], target_point[1], color='red', marker='x', s=100, label='Punkt (1,3)')
ax.scatter(mean[0], mean[1], color='green', marker='o', s=100, label='Mittelwert')

# Ellipsoide zeichnen
# Wir erstellen ein Gitter, um die Distanzen zu berechnen
x = np.linspace(-6, 6, 400)
y = np.linspace(-4, 8, 400)
X, Y = np.meshgrid(x, y)
pos = np.dstack((X, Y))

# Funktion zur Berechnung der Mahalanobis-Distanz für das Gitter
def calc_mahalanobis(p, mu, inv_sigma):
    d = p - mu
    return np.sqrt(np.einsum('...i,ij,...j->...', d, inv_sigma, d))

Z = calc_mahalanobis(pos, mean, sigma_inv)

# Konturlinien für Distanzen 1, 2 und 3
contours = ax.contour(X, Y, Z, levels=[1, 2, 3], colors=['orange', 'brown', 'black'])
ax.clabel(contours, inline=1, fontsize=10)

ax.set_title('Scatterplot mit Mahalanobis-Distanz Ellipsoiden')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.legend()
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_aspect('equal')

plt.show()