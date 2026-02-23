# Monte Carlo Portfolio Optimization

A research-oriented Python project for end-to-end portfolio construction and risk analysis using historical market data, Monte Carlo simulation, and advanced quantitative finance techniques.

## 🚀 Key Features

- **Statistical Return Analysis**: Daily log returns, annualized mean returns, and volatility estimation.
- **Advanced Visualizations**:
  - Return Distributions (Histogram & KDE)
  - Correlation Heatmap
  - Drawdown Curve
- **Monte Carlo Simulation**:
  - 10,000+ random portfolio weightings
  - Efficient Frontier (Risk vs. Return)
  - Maximum Sharpe Ratio & Minimum Volatility identification
- **Sensitivity & Stability Analysis**:
  - Bootstrap resampling of optimal weights
  - Parameter sensitivity to changes in returns and covariance
- **Stress Testing & Scenario Analysis**:
  - Historical crash scenarios (COVID-19, 2008 GFC)
  - Custom asset-level shock simulations
- **Robust Optimization Using Shrinkage**:
  - Ledoit-Wolf covariance shrinkage estimator
  - Improved out-of-sample portfolio stability
- **Risk Metrics**:
  - Value at Risk (VaR) — parametric & historical
  - Conditional Value at Risk (CVaR / Expected Shortfall)
  - Max Drawdown, Sortino Ratio, Calmar Ratio
- **Automated Data Acquisition**: `yfinance` pipeline for data fetching and preprocessing.

## 🛠 Technology Stack

| Category        | Libraries                          |
|-----------------|------------------------------------|
| Data Handling   | `pandas`, `numpy`                  |
| Visualization   | `matplotlib`, `seaborn`            |
| Financial Data  | `yfinance`                         |
| Optimization    | `scipy`, `sklearn` (shrinkage)     |
| Environment     | Jupyter Notebooks                  |

## 📈 Methodology

### Phase 1: Statistical Estimation
Estimation of the first and second moments of asset returns (Mean and Variance/Covariance) from cleaned historical data.

### Phase 2: Mean-Variance Optimization (Monte Carlo)
Monte Carlo simulation over 10,000+ weight combinations to map the Efficient Frontier and identify optimal allocations.

### Phase 3: Sensitivity & Stability Analysis
Bootstrap resampling to stress-test the robustness of optimal weights. Parameter perturbation quantifies sensitivity to input changes.

### Phase 4: Stress Testing & Scenario Analysis
Portfolio valuation under extreme market conditions using historical crash scenarios and asset-level shock factors.

### Phase 5: Robust Optimization Using Shrinkage
Ledoit-Wolf shrinkage applied to the sample covariance matrix to reduce estimation error and improve out-of-sample performance.

### Phase 6: Risk Metrics & Final Analysis
Comprehensive risk reporting including VaR, CVaR, Sortino Ratio, Calmar Ratio, and Max Drawdown. Final portfolio selection and presentation.

## 📂 Project Structure

```
monte-carlo-portfolio-optimization/
├── notebooks/
│   └── portfolio_optimization.ipynb   # Main research notebook
├── data/
│   └── asset_prices.csv               # Historical price data (wide format)
└── requirements.txt                   # Python dependencies
```

## ⚙️ Getting Started

1. **Prerequisites**: Python 3.12+
2. **Installation**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Usage**:
   Open `notebooks/portfolio_optimization.ipynb` to run the full 6-phase analysis pipeline.

## 📝 Recent Updates
- **Finalized** full end-to-end portfolio optimization pipeline.
- Added **Risk Metrics** (VaR, CVaR, Sortino, Calmar, Max Drawdown).
- Added **Robust Optimization** via Ledoit-Wolf covariance shrinkage.
- Added **Stress Testing & Scenario Analysis** with crash simulations.
- Added **Sensitivity & Stability Analysis** with bootstrap resampling.
