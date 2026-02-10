import matplotlib.pyplot as plt
import numpy as np

# Simulation of your 11,001 data points
rho = np.linspace(0, 1, 100) # Utilization from 0 to 100%
alpha = 2.5 # Your Fragility Exponent
phi = (1 / (1 - rho + 1e-5))**alpha # The simplified Phi decay curve

plt.figure(figsize=(10, 6))
plt.plot(rho, phi, color='red', linewidth=2, label='Phi (Systemic Failure)')
plt.axvline(x=0.85, color='black', linestyle='--', label='Critical Threshold (0.85)')
plt.fill_between(rho, phi, where=(rho >= 0.85), color='red', alpha=0.3, label='Catastrophe Zone')

plt.title('Logistics Saturation & The Phi (Φ) Collapse', fontsize=14)
plt.xlabel('System Utilization (ρ)', fontsize=12)
plt.ylabel('Priority Decay (Φ)', fontsize=12)
plt.ylim(0, 100) # Keep it readable
plt.legend()
plt.grid(True, which='both', linestyle='--', alpha=0.5)

plt.savefig('phi_saturation_plot.png')
print("Graph saved. Upload this to your GitHub root.")
