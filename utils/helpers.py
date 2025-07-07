import pandas as pd
import numpy as np
from config import VEHICLE_WEIGHTS

def preprocess_data(df):
    """
    Preprocess raw data for simulation
    
    Args:
        df (pd.DataFrame): Raw input data
        
    Returns:
        pd.DataFrame: Processed data
    """
    # Combine date and time
    df['Timestamp'] = pd.to_datetime(
        df['LastUpdatedDate'] + ' ' + df['LastUpdatedTime'],
        format='%d-%m-%Y %H:%M:%S'
    )
    
    # Rename columns
    column_mapping = {
        'Occupancy': 'Occupancy',
        'Capacity': 'Capacity',
        'QueueLength': 'QueueLength',
        'Traffic': 'Traffic',
        'IsSpecialDay': 'IsSpecialDay',
        'VehicleType': 'VehicleType',
        'Latitude': 'Latitude',
        'Longitude': 'Longitude',
        'ParkingLotID': 'ParkingLotID'
    }
    df = df.rename(columns=column_mapping)
    
    # Fill missing values
    df['QueueLength'] = df['QueueLength'].fillna(0)
    df['Traffic'] = df['Traffic'].fillna(1.0)
    df['IsSpecialDay'] = df['IsSpecialDay'].fillna(0).astype(bool)
    df['VehicleType'] = df['VehicleType'].fillna('car')
    
    # Add vehicle weight
    df['VehicleWeight'] = df['VehicleType'].map(VEHICLE_WEIGHTS).fillna(1.0)
    
    # Sort by timestamp
    return df.sort_values('Timestamp').reset_index(drop=True)

def create_lot_info(df):
    """
    Create a dictionary of lot information
    
    Args:
        df (pd.DataFrame): Processed data
        
    Returns:
        dict: Lot information dictionary
    """
    lot_info = {}
    for lot_id, group in df.groupby('ParkingLotID'):
        lot_info[lot_id] = {
            'latitude': group['Latitude'].iloc[0],
            'longitude': group['Longitude'].iloc[0]
        }
    return lot_info
