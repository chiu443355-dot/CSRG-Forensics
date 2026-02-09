# CSRG Forensic Source Code
### Principal Investigator: Smiti Wankhede

This directory contains the core mathematical engines for the CSRG Lab's audit of systemic failure.

## 1. Priority Decay Engine (Logistics)
- **Path:** `src/logistics/priority_decay_engine.py`
- **Objective:** Quantifies the **Phi (Φ) Coefficient**—the mathematical threshold where system utilization (Rho > 0.85) triggers "Priority Blindness."
- **Metric:** Identified a 64.9% failure rate in high-saturation logistics corridors.

## 2. Market Contagion Engine (Financials)
- **Path:** `src/markets/systemic_contagion_model.py`
- **Objective:** Models liquidity collapse and transition mechanics in high-volatility assets (XAUUSD).

## Operational Requirements:
`pip install numpy pandas`
