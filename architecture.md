# System Architecture

## Components
1. **Data Ingestion**: Pathway reads CSV data as a simulated stream
2. **Pricing Models**: Three models with increasing complexity
3. **State Management**: Pathway maintains per-lot pricing state
4. **Visualization**: Bokeh provides real-time plotting
5. **Dashboard**: Panel creates interactive controls

## Data Flow
1. Raw data is preprocessed and saved for streaming
2. Pathway ingests data and applies pricing models
3. Stateful processing maintains current price for each lot
4. Visualization layer updates in real-time
5. User interactions update model parameters

## Key Design Decisions
- **Modular Architecture**: Separate models for easy maintenance
- **Stateful Processing**: Essential for dynamic pricing
- **Geospatial Indexing**: Efficient competitor lookups
- **Interactive Controls**: Real-time model switching
