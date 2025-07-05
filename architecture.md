Architecture & Workflow Documentation

Project: Dynamic Pricing for Urban Parking Lots

Objective:

To simulate a real-time dynamic pricing engine that updates parking prices based on real-time data streams and demand features using only Python, Pandas, NumPy, and Pathway.

1. System Overview

This system ingests real-time parking lot data and updates the price of parking for each of the 14 lots using a defined pricing strategy. The price is calculated based on occupancy, queue length, traffic level, special days, vehicle type, and optionally competitor prices.

2. Core Components

A. Data Ingestion (Pathway Stream Engine)

Data is read in real-time using Pathway's streaming capabilities.

Simulates 30-minute intervals over 73 days for 14 parking lots.

B. Feature Engineering

Normalize features like occupancy rate, queue length, and traffic levels.

Encode vehicle type and special day indicators.

Generate additional features like competitor proximity.

C. Pricing Models

Model 1: Baseline Linear Model

Price increases linearly with occupancy.

Model 2: Demand-Based Model

Price is adjusted using a weighted demand function.

Weights are tunable for different scenarios.

Model 3: Competitive Model (Optional)

Considers nearby lot pricing using haversine distance.

Adjusts price dynamically to stay competitive.

D. Price Constraints

Prices are bounded within 0.5x and 2x of base price ($10).

Price changes are smooth, not erratic.

3. Real-Time Pipeline (Pathway)

Streaming Source: Reads CSV data in timestamp order.

Processor: Applies feature engineering and pricing model.

Price Sink: Outputs new price.

Bokeh Plot: Visualizes price updates live.

4. Assumptions

All lots begin at a base price of $10.

Competitor pricing is accessible for the same time window.

Special day is binary encoded (1 if special, 0 otherwise).

Vehicle type weights: Truck > Car > Bike (e.g., 1.2, 1.0, 0.8)

5. Limitations & Future Work

Currently assumes competitor prices are immediately available.

Could add reinforcement learning or RL-based dynamic optimization.

Can be extended to include user feedback and rerouting suggestions.

6. Dependencies

Python 3.10+

Pandas, NumPy

Pathway

Bokeh (for visualization)

7. Folder Structure Summary

├── data/
│   └── dataset.csv
├── models/
│   ├── model_1_baseline.py
│   ├── model_2_demand.py
│   └── model_3_competitive.py
├── main_simulation.ipynb
├── utils/
│   └── helpers.py
├── architecture.md
├── architecture_diagram.mmd
├── report.pdf (optional)
└── README.md

8. Conclusion

This project demonstrates a modular, real-time architecture for pricing urban parking spaces intelligently. It incorporates business logic, machine learning techniques, and real-time data processing using industry-standard tools like Pathway and Bokeh.

For questions or access to our live dashboard, please contact: [Your Email / GitHub]
