import numpy as np

def simulate_friends(n_persons=50, n_simulations=10000):
    results_x = []

    for _ in range(n_simulations):
        # Initialisiere Zähler: Wie oft wurde jede Person gewählt?
        times_chosen = np.zeros(n_persons)
        
        for person in range(n_persons):
            # Mögliche Freunde (man kann nicht sich selbst wählen)
            possible_friends = [p for p in range(n_persons) if p != person]
            
            # Wähle zufällig 2 Freunde ohne Zurücklegen
            chosen = np.random.choice(possible_friends, size=2, replace=False)
            
            # Markiere die gewählten Personen
            for c in chosen:
                times_chosen[c] += 1
        
        # X = Anzahl der Personen, die 0-mal gewählt wurden
        not_chosen_count = np.sum(times_chosen == 0)
        results_x.append(not_chosen_count)
    
    # Der Erwartungswert ist der Durchschnitt über alle Simulationen
    expected_x = np.mean(results_x)
    return expected_x

# Ausführung
n = 100
est_exp = simulate_friends(n_persons=n)

print(f"Simulation mit N = {n} Personen:")
print(f"Geschätzter Erwartungswert E[X]: {est_exp:.4f}")
print(f"Anteil an der Gesamtgruppe: {(est_exp/n)*100:.2f}%")