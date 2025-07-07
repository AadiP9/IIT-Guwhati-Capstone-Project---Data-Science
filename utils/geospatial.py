import numpy as np
from sklearn.neighbors import BallTree

def calculate_distances(lots_data):
    """
    Precompute distances between all parking lots
    
    Args:
        lots_data (pd.DataFrame): Parking lot data with columns:
            ['ParkingLotID', 'Latitude', 'Longitude']
            
    Returns:
        tuple: (indices, distances) arrays
    """
    # Convert to radians for haversine metric
    coordinates = np.radians(lots_data[['Latitude', 'Longitude']].values)
    tree = BallTree(coordinates, metric='haversine')
    return tree.query(coordinates, return_distance=True)

def get_nearby_lots(parking_lot_id, lot_info, distances, indices, max_distance_km):
    """
    Get nearby parking lots within a given distance
    
    Args:
        parking_lot_id (str): ID of the target parking lot
        lot_info (dict): Dictionary of lot information
        distances (np.array): Distance matrix
        indices (np.array): Indices matrix
        max_distance_km (float): Maximum distance in km
        
    Returns:
        list: Nearby parking lot IDs
    """
    # Convert max distance to radians (haversine uses radians)
    max_distance_rad = max_distance_km / 6371.0
    
    # Find the lot index
    lot_ids = list(lot_info.keys())
    if parking_lot_id not in lot_ids:
        return []
    
    idx = lot_ids.index(parking_lot_id)
    
    # Find nearby lots within max distance
    mask = distances[idx] <= max_distance_rad
    nearby_indices = indices[idx][mask]
    
    # Exclude self and return IDs
    return [lot_ids[i] for i in nearby_indices if lot_ids[i] != parking_lot_id]
