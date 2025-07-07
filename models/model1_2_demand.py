def demand_based_price(occupancy, capacity, queue_length, traffic, is_special, vehicle_weight):
    """
    Demand-based pricing model
    
    Args:
        occupancy (int): Current occupancy
        capacity (int): Total capacity
        queue_length (int): Current queue length
        traffic (float): Traffic congestion level
        is_special (bool): Whether it's a special day
        vehicle_weight (float): Vehicle type weight
        
    Returns:
        float: New price
    """
    from config import MODEL2_PARAMS, BASE_PRICE, MIN_PRICE, MAX_PRICE
    
    # Unpack parameters
    alpha = MODEL2_PARAMS['alpha']
    beta = MODEL2_PARAMS['beta']
    gamma = MODEL2_PARAMS['gamma']
    delta = MODEL2_PARAMS['delta']
    epsilon = MODEL2_PARAMS['epsilon']
    lambda_ = MODEL2_PARAMS['lambda_']
    
    # Calculate demand
    demand = (
        alpha * (occupancy / max(1, capacity)) +
        beta * queue_length -
        gamma * traffic +
        delta * float(is_special) +
        epsilon * vehicle_weight
    )
    
    # Normalize demand
    demand_norm = max(0, min(1, demand / 10.0))
    
    # Calculate new price
    new_price = BASE_PRICE * (1 + lambda_ * demand_norm)
    return max(MIN_PRICE, min(MAX_PRICE, new_price))
