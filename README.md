# Monte Carlo Portfolio Optimization

A research-oriented Python project for simulating portfolio performance and optimizing asset allocation using historical market data, Monte Carlo methods, and advanced risk analytics.

## 🚀 Key Features

- **Statistical Return Analysis**: Calculation of daily log returns, annualized mean returns, and volatility.
- **Advanced Visualizations**:
  - **Return Distributions**: Histogram and KDE plots for asset returns.
  - **Correlation Heatmap**: Visualizing inter-asset relationships.
  - **Drawdown Curve**: Tracking peak-to-trough declines for risk assessment.
- **Monte Carlo Simulation**:
  - Generation of **10,000+ random portfolio weightings**.
  - Mapping the **Efficient Frontier** (Risk vs. Return).
  - Identification of the **Maximum Sharpe Ratio** and **Minimum Volatility** portfolios.
- **Sensitivity & Stability Analysis**:
  - Bootstrap resampling to test robustness of optimal weights.
  - Parameter sensitivity to changes in expected returns and covariance.
- **Stress Testing & Scenario Analysis**:
  - Simulation under historical crash scenarios (e.g., COVID-19, 2008 GFC).
  - Custom shock factors applied to individual assets.
- **Automated Data Acquisition**: Integrated `yfinance` pipeline for seamless data fetching and preprocessing.

## 🛠 Technology Stack

- **Data Handling**: `pandas`, `numpy`
- **Visualization**: `matplotlib`, `seaborn`
- **Financial Data**: `yfinance`
- **Optimization**: `scipy`
- **Environment**: Jupyter Notebooks

## 📈 Methodology

### Phase 1: Statistical Estimation
Estimation of the first and second moments of asset returns (Mean and Variance/Covariance). This phase focuses on cleaning historical data and calculating the statistical properties required for simulation.

### Phase 2: Mean-Variance Optimization
Using Monte Carlo simulations to populate the risk-return space. By generating thousands of random weight combinations, we can visualize the Efficient Frontier and mathematically locate optimal capital allocations based on risk tolerance.

### Phase 3: Sensitivity & Stability Analysis
Bootstrap resampling of historical returns to stress-test the stability of optimal portfolio weights. Includes parameter perturbation to measure sensitivity of outcomes to changes in inputs.

### Phase 4: Stress Testing & Scenario Analysis
Portfolio valuation under extreme market conditions. Historical crash scenarios and asset-level shock simulations assess downside risk and validate portfolio resilience.

## 📂 Project Structure

- `notebooks/portfolio_optimization.ipynb`: The main research workspace and execution engine.
- `data/asset_prices.csv`: Consolidated "wide" format dataset for tracked assets.
- `requirements.txt`: Python dependencies.

## ⚙️ Getting Started

1. **Prerequisites**: Python 3.12+
2. **Installation**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Usage**:
   Open `notebooks/portfolio_optimization.ipynb` to run the full analysis pipeline.

## 📝 Recent Updates
- Added **Stress Testing & Scenario Analysis** (Phase 4) with crash scenario simulations.
- Added **Sensitivity & Stability Analysis** (Phase 3) with bootstrap resampling.
- Integrated a comprehensive Mean-Variance Optimization phase.
- Standardized data loading using a centralized wide-format CSV.
- Added Sharpe Ratio color-coding to the Efficient Frontier visualization.
