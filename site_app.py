import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# Load your DataFrame
mydataset = "https://raw.githubusercontent.com/santoeri28/santoeri28.gsd.key.io/main/file_3Dcsv2.csv"
df = pd.read_csv(mydataset, sep=';', on_bad_lines='skip')

# Initialize the Dash app (normally under the name 'app')
app = dash.Dash(__name__)
server = app.server

# Define the layout of the app
app.layout = html.Div([
    dcc.Graph(
        id='3d-scatter-plot',
        figure=fig
    )
])

# Create the Plotly figure
fig = px.scatter_3d(df, x='Ri - Di', y='Ri + Di', z='Cosine Sim', size='Ri + Di', color='W_cluster',
                    hover_data=['Description'])
fig.update_layout(scene_zaxis_type="log")


# This line allows the app to be run on a development server
if __name__ == '__main__':
    app.run_server(debug=True)
