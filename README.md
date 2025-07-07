# Dynamic Parking Pricing System

This project implements a real-time dynamic pricing system for urban parking lots using Pathway for stream processing and Bokeh for visualization.

## Features
- Three pricing models:
  1. Baseline linear model
  2. Demand-based model
  3. Competitive pricing model
- Real-time data streaming simulation
- Interactive dashboard for monitoring
- Geospatial analysis of competitor lots

## Setup
1. Install requirements: `pip install -r requirements.txt`
2. Place dataset in `data/dataset.csv`
3. Run `main_simulation.ipynb` in Jupyter or Google Colab

## Usage
1. Use the dropdown to select pricing model
2. Monitor real-time prices in the dashboard
3. Click "Reset Prices" to reset to base price
4. Click on legend items to show/hide parking lots
