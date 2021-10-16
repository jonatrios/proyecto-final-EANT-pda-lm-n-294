from flask import current_app
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px


from dash_application.data import movility_data

df = movility_data()

df_bici = df[df['TIPO'] == 'Bicicletas']

df_subtes = df[df['TIPO'] == 'Subte']

df_vehiculos = df[df['TIPO'] == 'Vehículos']


def bar_fig(dataframe, X, Y,color_by_column,  title):
    fig = px.bar(
        dataframe, x=dataframe[X], y=dataframe[Y], color=dataframe[color_by_column], barmode="group"
        )

    fig.update_layout(title_text=title, title_x=0.5)
    return fig



def register_callback(dash_app):

    @dash_app.callback(Output("page-content", "children"), [Input("url", "pathname")])
    def render_page_content(pathname):
        if pathname == "/":
            return html.P('Aca va la descripcion del proyecto')
        elif pathname == "/bicicletas":
            return html.P(["Este grafico muestra la utilizacion del medio de transporte BICICLETA durante el año 2020", dcc.Graph(id='example-graph',figure=bar_fig(df_bici,'MES','TOTAL', 'MES', 'Viajes Bicicleta 2020'))], className="img-fluid")
        elif pathname == "/subte":
            return html.P(["Este grafico muestra la utilizacion del medio de transporte SUBTE durante el año 2020", dcc.Graph(id='example-graph1',figure=bar_fig(df_subtes,'MES','TOTAL', 'MES', 'Viajes SUBTE 2020'))], className="img-fluid")
        elif pathname == "/vehiculos":
            return html.P(["Este grafico muestra la utilizacion de VEHICULOS durante el año 2020", dcc.Graph(id='example-graph2',figure=bar_fig(df_vehiculos,'MES','TOTAL', 'MES', 'Viajes VEHICULOS 2020'))], className="img-fluid")
        elif pathname == '/contaminantes':
            return None
        # If the user tries to reach a different page, return a 404 message
        return dbc.Jumbotron(
            [
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognised..."),
            ]
        )
    
    


