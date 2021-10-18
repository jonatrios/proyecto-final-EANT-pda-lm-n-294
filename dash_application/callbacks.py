import base64
from dash import dcc
from dash import html
from dash.html import Tr
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
from .layout import content, CARD_TEXT_STYLE

from dash_application.data import movility_data


# bike_filename = "dash_application/assets/BICI1.png"
# encoded_bike = base64.b64encode(open(bike_filename, 'rb').read())

df = movility_data()

df_bici = df[df['TIPO'] == 'Bicicletas']

df_subtes = df[df['TIPO'] == 'Subte']

df_vehiculos = df[df['TIPO'] == 'Vehículos']

df_cont = df[df['Tipo'] == 'Contaminantes']


def bar_fig(dataframe, X, Y,color_by_column,  image, divide):
    filename = image
    encoded_filename = base64.b64encode(open(filename, 'rb').read())
    fig = px.bar(
        dataframe, x=dataframe[X], y=dataframe[Y], color=dataframe[color_by_column], barmode="group", opacity=0.8
        )
    fig.update_traces(text=(round(dataframe[Y]/divide)), textposition='outside')
    fig.update_layout(xaxis=dict(showgrid=True, gridcolor='#E5E3E3', spikemode="marker"), yaxis=dict(showgrid=True, gridcolor='Grey'), paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)')


    a = dbc.Row([
                dbc.Col(
                        html.Img(src='data:image/png;base64,{}'.format(encoded_filename.decode()), width=550, height=150, className="center-block"),
                    #     dbc.Card(
                    #         [
                    #             dbc.CardHeader(
                    #                 dbc.Row([
                    #                     dbc.Col(
                    #                         html.Img(src='data:image/png;base64,{}'.format(encoded_bike.decode()), width=100, height=100, className="center-block")
                    #                     ),
                    #                     dbc.Col(
                                            
                    #                         html.H1('+ 100 %', className="center-block"),
                                            
                    #                     )
                    #                 ],
                    #                 justify="center"
                    #                 )
                    #             ),
                    #             dbc.CardBody(
                    #                 [
                                        
                    #                    html.H4('Bicicletas', style=CARD_TEXT_STYLE),
                    #                 ]
                    #             ),
                    #         ],color="success", inverse=True
                    #     ),
                    width={'size': 9, 'offset': 3}
                    )
                
    ])


    b = dbc.Row([
                dbc.Col(
                    dcc.Graph(id='example-graph',figure=fig),
                    width={'size': 10, 'offset': 1}
                )

    ])
    return [a,b]

def register_callback(dash_app):

    @dash_app.callback(Output("page-content", "children"), [Input("url", "pathname")])
    def render_page_content(pathname):
        if pathname == "/dash/":
            return html.H2(['Aca va la descripcion del proyecto',html.Hr()])
        elif pathname == "/bicicletas":
            return html.H2(["Utilizacion del medio de transporte BICICLETA durante el año 2020",html.Hr(),html.Br()] + bar_fig(df_bici,'MES','TOTAL', 'MES',"dash_application/assets/BICI1.png", 1000), className="text-left")
        elif pathname == "/subte":
            return html.H2(["Utilizacion del medio de transporte SUBTE durante el año 2020",html.Hr(),html.Br()] + bar_fig(df_subtes,'MES','TOTAL', 'MES',"dash_application/assets/SUBTE.png",1000), className="text-left")
        elif pathname == "/vehiculos":
            return html.H2(["Utilizacion de VEHICULOS durante el año 2020",html.Hr(),html.Br()] + bar_fig(df_vehiculos,'MES','TOTAL', 'MES',"dash_application/assets/VEHICULOS.png",1000), className="text-left")
        elif pathname == '/contaminantes':
            return html.H2(["Emisiones contaminantes",html.Hr(),html.Br()] + bar_fig(df_cont,'Mes','Total', 'Mes',"dash_application/assets/CONTAMINANTES.png",1), className="text-left")
        # If the user tries to reach a different page, return a 404 message
        return dbc.Jumbotron(
            [
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognised..."),
            ]
        )
    
    


