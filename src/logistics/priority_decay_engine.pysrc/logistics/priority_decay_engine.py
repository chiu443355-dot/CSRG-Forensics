"""
CSRG LAB - Priority Decay Engine (Phi)
Forensic analysis of queuing entropy in high-saturation logistics hubs.
Author: Smiti Wankhede, Principal Investigator
"""

import numpy as np

def calculate_theoretical_limit(rho, ca, cs, mu):
    """
    Standard Kingman Formula for VUT (Variance, Utilization, Time).
    Calculates the physics-based wait time floor in a stable queue.
    """
    v = (ca**2 + cs**2) / 2
    u = rho**2 / (1 - rho)
    t = 1 / mu
    return v * u * t

def derive_phi_coefficient(empirical_wait, theoretical_limit, rho):
    """
    The Priority Decay Coefficient (Phi).
    Quantifies 'Priority Blindness'—the mathematical point where 
    Premium and Standard tiers merge into a single failure state.
    """
    if rho < 0.85:
        return 0.0  # System maintains operational differentiation
    
    # Calculate ratio of empirical failure vs theoretical physics
    phi = empirical_wait / theoretical_limit
    
    # Normalize to 1.0 (Total Systemic Blindness)
    return min(phi, 1.0)

def dpr_intervention_protocol(phi_threshold, current_phi):
    """
    Dynamic Priority Routing (DPR) Intervention.
    Automated diversion logic to intercept capital drain.
    """
    if current_phi > phi_threshold:
        return "[CRITICAL] Phi Threshold Breached. Triggering DPR Diversion."
    return "[STATUS] System Stable. Priority Tiers Intact."

# --- FORENSIC AUDIT CASE STUDY: INDIAN E-COMMERCE TIER-2 CORRIDOR ---
RHO = 0.92  # 92% System Saturation
SERVICE_RATE = 10
VARIATION_ARRIVAL = 1.0
VARIATION_SERVICE = 1.0

# Execute Audit
limit = calculate_theoretical_limit(RHO, VARIATION_ARRIVAL, VARIATION_SERVICE, SERVICE_RATE)
empirical_data = 9.8  # Observed forensic data point from IRO audit

current_phi = derive_phi_coefficient(empirical_data, limit, RHO)

# --- SYSTEM LOG OUTPUT ---
print(f"--- CSRG Forensic Audit Output ---")
print(f"[LOG] Utilization (Rho): {RHO}")
print(f"[LOG] Physics-Based Limit: {limit:.2f}")
print(f"[LOG] Empirical Saturation: {empirical_data:.2f}")
print(f"[ALERT] Priority Decay (Phi): {current_phi:.2f}")
print(dpr_intervention_protocol(0.80, current_phi))
