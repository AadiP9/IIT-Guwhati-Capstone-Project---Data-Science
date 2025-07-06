# models/model_3_competitive.py
from utils.helpers import haversine_distance

def adjust_price_for_competition(own_price, own_loc, competitors):
    min_dist = float("inf")
    min_price = own_price
    for comp in competitors:
        dist = haversine_distance(own_loc, comp['location'])
        if dist < 0.5 and comp['price'] < min_price:
            min_price = comp['price']
            min_dist = dist
    if own_price > min_price:
        return own_price - 0.5  # Adjust down if overpriced
    elif own_price < min_price:
        return own_price + 0.5  # Adjust up if underpriced
    return own_price
