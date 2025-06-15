import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("covid_data.csv")

# App initialization
app = dash.Dash(__name__)
server = app.server

# Layout
app.layout = html.Div([
    html.H1("COVID-19 Dashboard"),
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': c, 'value': c} for c in df['Country'].unique()],
        value='India'
    ),
    dcc.Graph(id='cases-graph'),
])

# Callback for graph update
@app.callback(
    Output('cases-graph', 'figure'),
    Input('country-dropdown', 'value')
)
def update_graph(selected_country):
    filtered_df = df[df['Country'] == selected_country]
    fig = px.line(filtered_df, x='Date', y='Confirmed', title=f"Confirmed Cases in {selected_country}")
    return fig

if __name__ == '__main__':
    app.run_server(debug=False)