import numpy as np

def simulate_access_control(n_simulations=100_000):
    n_employees = 500
    n_authorised = 3
    
    # Wahrscheinlichkeiten
    p_grant_if_auth = 0.95
    p_grant_if_unauth = 0.01
    
    true_positives = 0
    total_granted = 0
    
    for _ in range(n_simulations):
        # 1. Weise Rollen zu: 1 für autorisiert, 0 für unbefugt
        # Wir ziehen 500 mal ohne Zurücklegen
        employees = np.zeros(n_employees)
        employees[:n_authorised] = 1
        np.random.shuffle(employees)
        
        # 2. Simuliere die Systementscheidung für jeden Mitarbeiter
        for person in employees:
            rand = np.random.random()
            
            if person == 1: # Autorisiert
                if rand < p_grant_if_auth:
                    granted = True
                else:
                    granted = False
            else: # Unbefugt
                if rand < p_grant_if_unauth:
                    granted = True
                else:
                    granted = False
            
            # 3. Zähle die Ergebnisse, falls Zugang gewährt wurde
            if granted:
                total_granted += 1
                if person == 1:
                    true_positives += 1
                    
    if total_granted == 0:
        return 0
        
    return true_positives / total_granted

# Ausführung der Simulation
result = simulate_access_control(n_simulations=10_000)
print(f"Relative Häufigkeit (Simulation): {result:.4f}")
print(f"Theoretischer Wert (Bayes): 0.3644")