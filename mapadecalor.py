import pandas as pd
import plotly.express as px

Bairros = ['Barra', 'Copacabana', 'Ipanema', 'Jardim Imbuí', 'Parque Araruama']
Lat = [-23.003815, -22.973789, -22.983588, -22.948974, -22.786764]
Long = [-43.348047, -43.192179, -43.212092, -43.097765, -43.332528]
Cidades = ['Rio de Janeiro', 'Rio de Janeiro', 'Rio de Janeiro', 'Niterói', 'Duque de Caxias']
Preco = [25000, 9000, 2000, 3900, 4020]
Date = {
    'Bairros': Bairros,
    'Cidades': Cidades,
    'Lat': Lat,
    'Long': Long,
    'Preco': Preco
}
Base_Db = pd.DataFrame(Date)
print(Base_Db)

px.density_mapbox(
    Base_Db,
    lat='Lat',
    lon='Long',
    z='Preco',
    radius=30,
    center=dict(lat=-22.80761, lon=-43.238568),
    zoom=7,
    mapbox_style='stamen-terrain'
)
