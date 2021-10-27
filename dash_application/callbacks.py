import base64
import os
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go 
from dash_application.data import movility_data, df_estaciones



df = movility_data()

df_bici = df[df['TIPO'] == 'Bicicletas']

df_subtes = df[df['TIPO'] == 'Subte']

df_vehiculos = df[df['TIPO'] == 'Vehículos']

df_cont = df[df['TIPO'] == 'Contaminantes']

df_covid = df[df['TIPO'] == 'Casos de Covid']

df_integrado = df[df['TIPO'] != 'Casos de Covid']



fig_covid = go.Figure()
# Create and style traces
fig_covid.add_trace(go.Scatter(x=df_bici['MES'], y=df_bici['INTERVALO'], name='Bicicletas',
                         line=dict(color='#417DC1', width=4)))
fig_covid.add_trace(go.Scatter(x=df_vehiculos['MES'], y=df_vehiculos['INTERVALO'], name = 'Vehículos',
                         line=dict(color='#04A404', width=4, dash='dashdot')))
fig_covid.add_trace(go.Scatter(x=df_cont['MES'], y=df_cont['INTERVALO'], name='Contaminantes',
                         line=dict(color='#E30049', width=4,
                              dash='dash'))) 
fig_covid.add_trace(go.Scatter(x=df_subtes['MES'], y=df_subtes['INTERVALO'], name='Subte',
                         line = dict(color='#FF8000', width=4, dash='dash')))

fig_covid.add_trace(
    go.Bar(
        x=df_covid['MES'], 
        y=df_covid['INTERVALO'],
        marker_color=['#0d0887', '#46039f', '#7201a8', '#9c179e', '#bd3786', '#d8576b', '#de7065', '#ed7953', '#fb9f3a', '#fdca26', '#efe350','#f0f921'],
        name="Covid-19"
    ))

fig_covid.update_layout( barmode="group", xaxis=dict(title='MES', showgrid=True, gridcolor='#E5E3E3', spikemode="marker"), yaxis=dict(title='INTERVALO NORMALIZADO',showgrid=True, gridcolor='Grey'), paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)')

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


def map_and_bar(df_bar, df_map, X, Y,lat,lon,color_by_column, divide):
    fig_bar = px.bar(
        df_bar, x=df_bar[X], y=df_bar[Y], color=df_bar[color_by_column], barmode="group", opacity=0.8
        )
    fig_bar.update_traces(text=(round(df_bar[Y]/divide)), textposition='outside')
    fig_bar.update_layout(xaxis=dict(showgrid=True, gridcolor='#E5E3E3', spikemode="marker"), yaxis=dict(showgrid=True, gridcolor='Grey'), paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)')
    px.set_mapbox_access_token(open(os.path.join(os.path.abspath('.'),"dash_application",".mapbox_token")).read())
    fig_map = px.scatter_mapbox(df_map, lat=df_map[lat], lon=df_map[lon], size=[80,80,80,80], zoom=11, center={'lat':-34.61315, 'lon':-58.37723},
    hover_name=df_map['NOMBRE'],mapbox_style="open-street-map",hover_data=[df_map['NOMBRE'], df_map['ZONA_DE_EMPLAZAMIENTO']])
                 
    a = dbc.Row([
                
                dbc.Col(
                    dcc.Graph(id='bar_map_1',figure=fig_bar),
                    width={'size': 10, 'offset': 1}
                )
                
    ])
    e = dbc.Row([
                dbc.Col(
                    html.Br()
                )
        ])
    d = dbc.Row([
                dbc.Col(
                    html.Hr()
                )
        ])
    c = b = dbc.Row([
                dbc.Col(
                    #html.H2("Red de monitoreo de contaminantes")
                    html.H2("Estaciones Ambientales")
                )
        ])
    b = dbc.Row([
                dbc.Col(
                    dcc.Graph(id='bar_map_2',figure=fig_map),
                    width={'size': 10, 'offset': 1}
                )

    ])
    return [a,e,c,d,b]

def map_and_bar_map(df_bar, df_map, X, Y,lat,lon,color_by_column, divide):
    fig_bar = px.bar(
        df_bar, x=df_bar[X], y=df_bar[Y], color=df_bar[color_by_column], barmode="group", opacity=0.8
        )
    fig_bar.update_traces(text=(round(df_bar[Y]/divide)), textposition='outside')
    fig_bar.update_layout(xaxis=dict(showgrid=True, gridcolor='#E5E3E3', spikemode="marker"), yaxis=dict(showgrid=True, gridcolor='Grey'), paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)')
    px.set_mapbox_access_token(open(os.path.join(os.path.abspath('.'),"dash_application",".mapbox_token")).read())
    fig_map = px.scatter_mapbox(df_map, lat=df_map[lat], lon=df_map[lon], size=[80,80,80,80], zoom=11, center={'lat':-34.61315, 'lon':-58.37723},
    hover_name=df_map['NOMBRE'],mapbox_style="open-street-map",hover_data=[df_map['NOMBRE'], df_map['ZONA_DE_EMPLAZAMIENTO']])
                 
    a = dbc.Row([
                
                dbc.Col(
                    dcc.Graph(id='bar_map_1',figure=fig_bar),
                    width={'size': 10, 'offset': 1}
                )
                
    ])
    e = dbc.Row([
                dbc.Col(
                    html.Br()
                )
        ])
    d = dbc.Row([
                dbc.Col(
                    html.Hr()
                )
        ])
    c = b = dbc.Row([
                dbc.Col(
                    #html.H2("Red de monitoreo de contaminantes")
                    html.H2("Estaciones Ambientales")
                )
        ])
    b = dbc.Row([
                dbc.Col(
                    dcc.Graph(id='bar_map_2',figure=fig_map),
                    width={'size': 10, 'offset': 1}
                )

    ])
    return [c,d,b]

def register_callback(dash_app):

    @dash_app.callback(Output("page-content", "children"), [Input("url", "pathname")])
    def render_page_content(pathname):
        if pathname == "/dash/":
            #return html.H3(['Comparativa: Casos de Covid Vs Transporte y Contaminantes durante el 2020',html.Hr(), dcc.Graph(id='comparativa',figure=fig_covid)], className="text-center")
            return html.H3(['Casos de Covid / Contaminantes / Transporte 2020',html.Hr(), dcc.Graph(id='comparativa',figure=fig_covid)], className="text-center")
        elif pathname == "/bicicletas":
            #return html.H2(["Utilizacion del medio de transporte BICICLETA durante el año 2020",html.Hr(),html.Br()] + bar_fig(df_bici,'MES','TOTAL', 'MES',"dash_application/assets/BICI1.png", 1000), className="text-left")
            return html.H3(["Viajes en Bicicleta 2020 (+ 100%)",html.Hr(),html.Br()] + bar_fig(df_bici,'MES','TOTAL', 'MES',"dash_application/assets/BICI1.png", 1000), className="text-center")
        elif pathname == "/subte":
            #return html.H2(["Utilizacion del medio de transporte SUBTE durante el año 2020",html.Hr(),html.Br()] + bar_fig(df_subtes,'MES','TOTAL', 'MES',"dash_application/assets/SUBTE.png",1000), className="text-left")
            return html.H3(["Viajes en Subte 2020 (-77 %)",html.Hr(),html.Br()] + bar_fig(df_subtes,'MES','TOTAL', 'MES',"dash_application/assets/SUBTE.png",1000), className="text-center")
        elif pathname == "/vehiculos":
            #return html.H2(["Utilizacion de VEHICULOS durante el año 2020",html.Hr(),html.Br()] + bar_fig(df_vehiculos,'MES','TOTAL', 'MES',"dash_application/assets/VEHICULOS.png",1000), className="text-left")
            return html.H3(["Viajes en Vehículos 2020 (-10 %)",html.Hr(),html.Br()] + bar_fig(df_vehiculos,'MES','TOTAL', 'MES',"dash_application/assets/VEHICULOS.png",1000), className="text-center")
        elif pathname == '/contaminantes':
            #return html.H2(["Emisiones contaminantes",html.Hr(),html.Br()] + map_and_bar(df_vehiculos,df_estaciones,'MES','TOTAL', 'Y','X','MES',1) , className="text-left")
            return html.H3(["Contaminantes 2020 (-28 %)",html.Hr(),html.Br()] + map_and_bar(df_vehiculos,df_estaciones,'MES','TOTAL', 'Y','X','MES',1) , className="text-center")
        elif pathname == '/estaciones':
            #return html.H2(["Emisiones contaminantes",html.Hr(),html.Br()] + map_and_bar(df_vehiculos,df_estaciones,'MES','TOTAL', 'Y','X','MES',1) , className="text-left")
            return html.H3( map_and_bar_map(df_vehiculos,df_estaciones,'MES','TOTAL', 'Y','X','MES',1) , className="text-center")

        # If the user tries to reach a different page, return a 404 message
        return dbc.Jumbotron(
            [
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognised..."),
            ]
        )
    
    


