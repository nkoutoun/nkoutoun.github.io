from ecbdata import ecbdata
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

# Series keys for ECB rates
SERIES_KEYS = {
    'MRO (Fixed Rate)': 'FM.D.U2.EUR.4F.KR.MRR_FR.LEV',    # Main Refinancing Operations Rate (Fixed Rate)
    'MRO (Variable Rate)': 'FM.D.U2.EUR.4F.KR.MRR_MBR.LEV',  # Main Refinancing Operations Rate (Variable Rate)
    'DFR': 'FM.D.U2.EUR.4F.KR.DFR.LEV',       # Deposit Facility Rate
    'MLF': 'FM.D.U2.EUR.4F.KR.MLFR.LEV',      # Marginal Lending Facility Rate
    'EONIA': 'EON.D.EONIA_TO.RATE',           # EONIA Rate (discontinued)
    '€STR': 'EST.B.EU000A2X2A25.WT'           # Euro Short-Term Rate
}

def fetch_ecb_rates(start_date='1999-01'):
    """
    Fetches ECB key interest rates and reference rates at daily frequency.
    Combines MRO Fixed and Variable Rates into a single 'MRO' series.
    """
    rates_data = {}
    
    # Fetch each rate series
    for rate_name, series_key in SERIES_KEYS.items():
        df = ecbdata.get_series(series_key, start=start_date)
        # Convert TIME_PERIOD to datetime and set as index (if present)
        if 'TIME_PERIOD' in df.columns:
            df['TIME_PERIOD'] = pd.to_datetime(df['TIME_PERIOD'])
            df = df.set_index('TIME_PERIOD')
        else:
            df.index = pd.to_datetime(df.index)
        rates_data[rate_name] = df['OBS_VALUE']
    
    # Combine all rates into a single DataFrame
    combined_rates = pd.DataFrame(rates_data)
    
    # Combine the two MRO series (Fixed & Variable) by taking their mean
    if 'MRO (Fixed Rate)' in combined_rates.columns and 'MRO (Variable Rate)' in combined_rates.columns:
        combined_rates['MRO'] = combined_rates[['MRO (Fixed Rate)', 'MRO (Variable Rate)']].mean(axis=1)
        combined_rates.drop(columns=['MRO (Fixed Rate)', 'MRO (Variable Rate)'], inplace=True)
    
    return combined_rates

def create_interactive_plot():
    """
    Creates an interactive plot of the ECB rates and saves it as HTML.
    """
    # Fetch rates from 1999 onwards
    rates = fetch_ecb_rates()
    
    fig = go.Figure()
    
    # Plot policy rates with solid lines
    policy_rates = ['MRO', 'DFR', 'MLF']
    for rate in policy_rates:
        if rate in rates.columns:
            fig.add_trace(
                go.Scatter(
                    x=rates.index,
                    y=rates[rate],
                    name=rate,
                    line=dict(width=2),
                    hovertemplate="%{x|%Y-%m-%d}<br>" +
                                f"{rate}: %{{y:.3f}}%<br>" +
                                "<extra></extra>"
                )
            )
    
    # Plot reference rates with dashed lines
    reference_rates = {'€STR': 'rgba(240,128,128,0.8)', 'EONIA': 'rgba(176,196,222,0.8)'}
    for rate, color in reference_rates.items():
        if rate in rates.columns:
            fig.add_trace(
                go.Scatter(
                    x=rates.index,
                    y=rates[rate],
                    name=rate,
                    line=dict(width=2, dash='dash', color=color),
                    hovertemplate="%{x|%Y-%m-%d}<br>" +
                                f"{rate}: %{{y:.3f}}%<br>" +
                                "<extra></extra>"
                )
            )
    
    # Update layout
    fig.update_layout(
        title='ECB Key Interest Rates and Reference Rates',
        xaxis_title='Date',
        yaxis_title='Rate (%)',
        hovermode='x unified',
        plot_bgcolor='white',
        xaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(128,128,128,0.2)',
        ),
        yaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(128,128,128,0.2)',
        ),
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        ),
        margin=dict(l=50, r=50, t=50, b=50)
    )
    
    # Get the latest rates and last available values
    latest_rates = rates.iloc[-1]
    
    # For €STR and EONIA, get last available (non-NaN) observations and their dates
    estr_series = rates['€STR'].dropna()
    eonia_series = rates['EONIA'].dropna()
    last_estr = estr_series.iloc[-1]
    last_estr_date = estr_series.index[-1]
    last_eonia = eonia_series.iloc[-1]
    last_eonia_date = eonia_series.index[-1]
    
    # Create a string with the latest rates information
    rates_info = "<div style='font-family: Arial, sans-serif; padding: 10px; background-color: #f8f9fa; border-radius: 5px; margin-bottom: 20px;'>"
    rates_info += "<h3>Latest Available Rates:</h3>"
    rates_info += "<ul>"
    
    for rate_name in ['MRO', 'DFR', 'MLF']:
        value = latest_rates.get(rate_name, None)
        if pd.notna(value):
            rates_info += f"<li><strong>{rate_name}:</strong> {value:.3f}%</li>"
    
    # Add €STR and EONIA information
    rates_info += f"<li><strong>€STR:</strong> {last_estr:.3f}% (as of {last_estr_date.strftime('%Y-%m-%d')})</li>"
    rates_info += f"<li><strong>EONIA:</strong> {last_eonia:.3f}% (discontinued on {last_eonia_date.strftime('%Y-%m-%d')})</li>"
    rates_info += "</ul></div>"
    
    # Save both the info and the figure to an HTML file
    html_content = rates_info + fig.to_html(full_html=False, include_plotlyjs='cdn')
    
    # Ensure the directory exists
    os.makedirs('static/html', exist_ok=True)
    
    # Write the HTML file
    with open('static/html/ecb_rates.html', 'w') as f:
        f.write(html_content)
    
    print("ECB rates visualization has been saved to static/html/ecb_rates.html")

if __name__ == "__main__":
    create_interactive_plot() 