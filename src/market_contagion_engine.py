# CSRG Market Contagion Research
# Analyzing the 2025 Liquidity Collapse in XAUUSD (Gold)

def calculate_market_phi(liquidity_depth, volatility_index):
    """
    Adapts the Priority Decay Coefficient (Phi) for Financial Markets.
    Measures 'Liquidity Blindness' during flash crashes.
    """
    CRITICAL_DEPTH = 0.15 # 15% depth threshold
    if liquidity_depth < CRITICAL_DEPTH:
        # At low depth, slippage causes "Market Blindness"
        phi_market = (1 / liquidity_depth) * volatility_index
        return min(phi_market, 1.0)
    return 0.0

# Case Study: 2025 Market Contagion Trigger
vix = 0.45 
depth = 0.12 # Below 0.15 threshold
print(f"Market Phi (Contagion Risk): {calculate_market_phi(depth, vix):.2f}")
