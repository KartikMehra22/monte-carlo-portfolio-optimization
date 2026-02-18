# Monte Carlo Portfolio Optimization

This project implements a Monte Carlo simulation for portfolio optimization using historical asset price data.

## Project Structure

- `notebooks/portfolio_optimization.ipynb`: Main interactive environment for data acquisition, preprocessing, and simulation.
- `data/asset_prices.csv`: Historical adjusted close prices for selected assets (AAPL, MSFT, GOOGL, SPY).
- `requirements.txt`: Project dependencies.
- `venv/`: Python virtual environment.

## Getting Started

1. **Prerequisites**: Ensure you have Python 3.12+ installed.
2. **Installation**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Usage**:
   Open `notebooks/portfolio_optimization.ipynb` in your preferred Jupyter environment (VS Code or Jupyter Lab) to run the analysis.

## Recent Updates
- **Dataset Transition**: Moved to a consolidated "wide" format where each asset has its own column.
- **Workflow Consolidation**: The entire pipeline (fetch, load, visualize) is now handled within the Jupyter Notebook for transparency and ease of use.
