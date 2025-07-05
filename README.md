# IIT-Guwhati-Capstone-Project---Data-Science

# Dynamic Pricing for Urban Parking Lots 🚗📈

This is the official repository for our Summer Analytics 2025 Capstone Project, hosted by the Consulting & Analytics Club × Pathway.

## 🚀 Project Overview

Urban parking is a scarce resource, and static pricing leads to either underutilization or overcrowding. Our project proposes a real-time dynamic pricing engine for 14 urban parking lots, based on demand patterns, traffic, vehicle types, and competitor pricing.

We simulate real-time pricing updates using only:
- Python
- Pandas
- NumPy
- Pathway (for real-time stream processing)
- Bokeh (for real-time visualization)

## 💡 Objective

To create a pricing model that:
- Starts at a base price of $10
- Adjusts based on demand features like occupancy, queue, traffic, and special events
- Incorporates geographic competition in advanced stages
- Operates in a real-time data stream environment

## 🧰 Tech Stack

| Technology | Purpose                          |
|------------|----------------------------------|
| Python     | Core language                    |
| Pandas     | Data processing                  |
| NumPy      | Numerical operations             |
| Pathway    | Real-time data streaming engine  |
| Bokeh      | Real-time plotting and dashboard |

## 📊 Models Implemented

1. **Baseline Linear Model**
2. **Demand-Based Model**
3. **Competitive Pricing Model (Optional)**

Each model is implemented from scratch under the `models/` folder.

## 📈 Real-Time Workflow

We use Pathway to simulate real-time data and pricing updates. All results are visualized live using Bokeh.

## 📁 Folder Structure
