# models/model_2_demand.py
import numpy as np

def demand_function(occupancy, capacity, queue_length, traffic, is_special, vehicle_weight):
    alpha, beta, gamma, delta, epsilon = 0.6, 0.3, 0.2, 0.4, 0.1
    demand = (
        alpha * (occupancy / capacity) +
        beta * queue_length -
        gamma * traffic +
        delta * is_special +
        epsilon * vehicle_weight
    )
    return demand

def price_from_demand(base_price, demand, lambda_=0.2):
    demand_norm = np.clip(demand / 10, 0, 1)
    new_price = base_price * (1 + lambda_ * demand_norm)
    return round(min(max(new_price, base_price * 0.5), base_price * 2), 2)
