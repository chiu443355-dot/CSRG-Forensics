import numpy as np

def calculate_theoretical_wait(rho, ca, cs, mu):
    """
    Standard Kingman Formula for VUT (Variance, Utilization, Time).
    Calculates wait time in a stable queue.
    """
    v = (ca**2 + cs**2) / 2
    u = rho**2 / (1 - rho)
    t = 1 / mu
    return v * u * t

def derive_phi(observed_wait, theoretical_wait, rho):
    """
    The Priority Decay Coefficient (Phi).
    Quantifies the degree of 'Priority Blindness' in a saturated hub.
    If Phi -> 1.0, the system treats Premium and Standard tiers identically.
    """
    if rho < 0.85:
        return 0.0  # System maintains priority differentiation
    
    # Calculate ratio of observed vs theoretical wait
    phi = observed_wait / theoretical_wait
    
    # Normalize to 1.0 (Total Blindness)
    return min(phi, 1.0)

def dpr_intervention_logic(phi_threshold, current_phi):
    """
    Dynamic Priority Routing (DPR) Intervention.
    Triggers diversion to secondary hubs when Phi exceeds critical levels.
    """
    if current_phi > phi_threshold:
        return "CRITICAL: Triggering DPR Diversion to Secondary Hub."
    return "STATUS: System Stable. Maintaining Priority Tiers."

# --- FORENSIC AUDIT CASE STUDY (IRO DATA) ---
RHO = 0.92  # 92% Utilization
MU = 10     # Service Rate
CA = 1.0    # Arrival Coefficient
CS = 1.0    # Service Coefficient

theoretical = calculate_theoretical_wait(RHO, CA, CS, MU)
observed = 9.8  # Real-world data point from IRO audit

current_phi = derive_phi(observed, theoretical, RHO)

print(f"--- CSRG Forensic Output ---")
print(f"Utilization (Rho): {RHO}")
print(f"Theoretical Wait: {theoretical:.2f}")
print(f"Observed Wait: {observed:.2f}")
print(f"Priority Decay (Phi): {current_phi:.2f}")
print(dpr_intervention_logic(0.80, current_phi))
