import numpy as np

# Parameter
n_simulations = 100000
mean_customers = 16
std_customers = 2
stock = {1: 5, 2: 6, 3: 6}
probs = [0.25, 0.35, 0.40]

success_count = 0

for _ in range(n_simulations):
    # 1. Anzahl Kunden ziehen (gerundet, da diskret)
    n_customers = int(round(np.random.normal(mean_customers, std_customers)))
    
    if n_customers <= 0: # Sicherheitscheck für die Verteilung
        success_count += 1
        continue
        
    # 2. Wünsche der Kunden simulieren (Multinomialverteilung ist hier effizienter)
    # Sie gibt direkt an, wie viele Kunden Typ 1, 2 oder 3 wählen
    requests = np.random.multinomial(n_customers, probs)
    
    # 3. Prüfung gegen den Bestand
    if requests[0] <= stock[1] and requests[1] <= stock[2] and requests[2] <= stock[3]:
        success_count += 1

# Ergebnis
prob_fulfilled = success_count / n_simulations
print(f"Geschätzte Wahrscheinlichkeit: {prob_fulfilled:.4f}")