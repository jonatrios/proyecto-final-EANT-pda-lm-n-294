import base64
from dash import html
import os
from dash import dcc
from dash import html
from dash.html.A import A
import dash_bootstrap_components as dbc

image_filename = "dash_application/assets/logo_corto.png"
encoded_image = base64.b64encode(open(image_filename, 'rb').read())


image_opendata = "dash_application/assets/logopng.png"
encoded_opendata = base64.b64encode(open(image_opendata, 'rb').read())

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

CARD_TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#FCFCFC'
}

sidebar = html.Div(
    [
        html.H2([html.A(html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode())), href="/", title='Volver al inicio')], className="rounded mx-auto d-block"),
        html.Hr(),
        html.P(
            #"Cada boton representa el analisis realizado de un dataset", className="lead"
            "Python Data Analytics pda-lm-n-294 - Grupo 1", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Inicio", href="/dash/", active="exact"),
                dbc.NavLink("Bicicletas", href="/bicicletas", active="exact"),
                dbc.NavLink("Subtes", href="/subte", active="exact"),
                dbc.NavLink("Vehiculos", href="/vehiculos", active="exact"),
                dbc.NavLink("Contaminantes", href="/contaminantes", active="exact"),
                
                html.Img(src='data:image/png;base64,{}'.format(encoded_opendata.decode()), className="img-responsive center-block", style={'position':'absolute', 'bottom':0}, width=200, height=100)
            ], 
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content_first_row = dbc.Row([
    dbc.Col(
        dbc.Card(
            [

                dbc.CardBody(
                    [
                        html.H4(id='card_title_1', children=['Card Title 1'], className='card-title',
                                style=CARD_TEXT_STYLE),
                        html.P( id='card_text_1', children=['Sample text.'], style=CARD_TEXT_STYLE),
                    ]
                )
            ]
        ),
        md=3
    ),
    dbc.Col(
        dbc.Card(
            [

                dbc.CardBody(
                    [
                        html.H4('Card Title 2', className='card-title', style=CARD_TEXT_STYLE),
                        html.P('Sample text.', style=CARD_TEXT_STYLE),
                    ]
                ),
            ]

        ),
        md=3
    ),
    dbc.Col(
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H4('Card Title 3', className='card-title', style=CARD_TEXT_STYLE),
                        html.P('Sample text.', style=CARD_TEXT_STYLE),
                    ]
                ),
            ]

        ),
        md=3
    ),
    dbc.Col(
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H4('Card Title 4', className='card-title', style=CARD_TEXT_STYLE),
                        html.P('Sample text.', style=CARD_TEXT_STYLE),
                    ]
                ),
            ]
        ),
        md=3
    ),
    dbc.Col(
        dcc.Graph(
            id='example-graph4',figure={}
        ),
        width={'size': 6}
    ),
    dbc.Col(
        dcc.Graph(
            id='example-graph5',figure={}
        ),
        width={'size': 6}
    ),
    dbc.Col(
        dcc.Graph(
            id='example-graph6',figure={}
        ),
        width={'size': 6, 'offset': 3}
    )

])


a = [html.H2('Analytics Dashboard Template'),html.Hr(),content_first_row]

content = html.Div(a, id="page-content", style=CONTENT_STYLE)


layout = html.Div([dcc.Location(id="url"),sidebar, content])