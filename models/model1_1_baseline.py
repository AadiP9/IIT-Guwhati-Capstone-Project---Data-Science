def baseline_price(prev_price, occupancy, capacity):
    """
    Baseline linear pricing model
    
    Args:
        prev_price (float): Previous price
        occupancy (int): Current occupancy
        capacity (int): Total capacity
        
    Returns:
        float: New price
    """
    from config import ALPHA, MIN_PRICE, MAX_PRICE
    
    utilization = occupancy / max(1, capacity)  # Avoid division by zero
    new_price = prev_price + ALPHA * utilization
    return max(MIN_PRICE, min(MAX_PRICE, new_price))
