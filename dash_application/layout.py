import base64
from dash import html
import os
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

image_filename = "dash_application/assets/logo_corto.png"
encoded_image = base64.b64encode(open(image_filename, 'rb').read())


# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}


# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2([html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()))], className="rounded mx-auto d-block"),
        html.Hr(),
        html.P(
            "Cada boton representa el analisis realizado de un dataset", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Inicio", href="/", active="exact"),
                dbc.NavLink("Bicicletas", href="/bicicletas", active="exact"),
                dbc.NavLink("Subtes", href="/subte", active="exact"),
                dbc.NavLink("Vehiculos", href="/vehiculos", active="exact"),
                dbc.NavLink("Contaminantes", href="/contaminantes", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)




content = html.Div(id="page-content", style=CONTENT_STYLE)


layout = html.Div([dcc.Location(id="url"),sidebar, content])