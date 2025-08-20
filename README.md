Bitcoin Price Analysis — EDA
A comprehensive exploratory data analysis of Bitcoin OHLCV time-series to understand price behavior, volatility, and regime shifts. The project covers data ingestion, cleaning, feature engineering, visualization, and a lightweight interactive dashboard.

Objectives:
-Explore historical Bitcoin price trends and distributions.

-Derive and analyze returns, percent changes, and resampled aggregates.

-Compare behavior across Year/Quarter/Month.

-Build interactive visuals for quick investigation.

Dataset:
Source: Historical Bitcoin OHLCV (Open, High, Low, Close, Volume, Market Cap).

Granularity: Daily.

Format: CSV (e.g., bitcoin_price_Training - Training.csv).

Note: Replace with your actual source and file path.

Key Features:
-Data cleaning: type conversions, missing values, outlier handling.

-Feature engineering: datetime parsing, day/month/quarter/year, percent change, returns.

-Resampling: YE/QE/ME aggregates for trend comparisons.

Visualizations:

-Matplotlib/Seaborn: time-series, distributions, area fills, multi-panel subplots.

-Plotly: interactive candlestick, line charts.

-Dashboard: Streamlit app to explore key charts interactively.

-streamlit run dashboard.py

-Open the local URL printed in the terminal

Reproducible Steps (High-level)
Load CSV → parse Date → set index

Clean numeric fields (remove commas, cast to float)

Create features: day, month, quarter, year, pct_change

Resample (YE/QE/ME) and compute mean/summary stats

Visualize:

-Matplotlib subplots: yearly/monthly/quarterly trends

-Plotly candlestick + interactive returns line

-Optional: deploy Streamlit app (local or cloud)

Example Insights
-Year-over-year trend shifts and major volatility clusters

-Quarter and month seasonality patterns in close prices

-Percent change spikes aligning with notable market regimes

Contact
-Open an issue or reach out via LinkedIn/GitHub for feedback or collaboration
