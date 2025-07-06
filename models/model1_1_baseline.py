# models/model_1_baseline.py
def baseline_price(prev_price, occupancy, capacity, alpha=0.1):
    utilization = occupancy / capacity
    new_price = prev_price + alpha * utilization
    return max(5, min(20, new_price))
