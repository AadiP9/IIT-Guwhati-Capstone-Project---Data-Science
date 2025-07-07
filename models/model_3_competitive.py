def competitive_price(parking_lot_id, current_price, occupancy, capacity, competitor_prices):
    """
    Competitive pricing model that considers nearby parking lots
    
    Args:
        parking_lot_id (str): ID of the parking lot
        current_price (float): Current price
        occupancy (int): Current occupancy
        capacity (int): Total capacity
        competitor_prices (list): List of competitor prices
        
    Returns:
        float: New price
    """
    from config import MIN_PRICE, MAX_PRICE
    
    utilization = occupancy / max(1, capacity)
    
    if not competitor_prices:
        return current_price
    
    # Calculate competitor metrics
    avg_competitor_price = sum(competitor_prices) / len(competitor_prices)
    min_competitor_price = min(competitor_prices)
    max_competitor_price = max(competitor_prices)
    
    # Pricing strategy based on utilization and competition
    if utilization >= 0.95:  # Nearly full
        # Lower price if competitors are cheaper
        if current_price > min_competitor_price:
            return max(MIN_PRICE, min_competitor_price * 0.95)
    
    elif utilization <= 0.5:  # Underutilized
        # Increase price if competitors are charging more
        if current_price < max_competitor_price:
            return min(MAX_PRICE, max_competitor_price * 1.05)
    
    # Maintain competitive positioning
    if current_price > avg_competitor_price * 1.1:
        return max(MIN_PRICE, avg_competitor_price * 0.95)
    elif current_price < avg_competitor_price * 0.9:
        return min(MAX_PRICE, avg_competitor_price * 1.05)
    
    return current_price
