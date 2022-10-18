# GeoDataFrame muestra siempre Warnings con los indices
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
pd.set_option('display.max_columns', None)

import numpy as np
# Graphics
import matplotlib.pyplot as plt
import seaborn
# Analysis
import geopandas 
import pandas
from numpy.random import seed
from shapely.geometry import Polygon, LineString, Point

from matplotlib import pyplot as plt

def 
gdf_caldas_manzanas = geopandas.read_file('Dataset_DANE/MGN_NivelManzana_Integrado_CNPV/MGN_ANM_MANZANA.shp')
gdf_caldas_manzanas = gdf_caldas_manzanas.loc[gdf_caldas_manzanas.DPTO_CCDGO.isin(['17']),:]# Codigo Depatarmento
#manizales_manzanas = geopandas.GeoDataFrame(manizales_manzanas.loc[
#                     manizales_manzanas.MPIO_CCDGO.isin(['001','873']),:])# Codigo Manzanas y Villamaria

## Mixed data of interest ##
dataGeoPDV = pd.read_excel('GEO (2022)2.xlsx')

## SOME CASTINGS AND FORMAT CHANGES ##
## GEODATAFRAME BUILDING ##
dataGeoPDV['LATITUD_1'] = [str(i)[:1] for i in dataGeoPDV['GEO_LATITUD_str']]
dataGeoPDV['LATITUD_2'] = [str(i)[1:] for i in dataGeoPDV['GEO_LATITUD_str']]
#dataGeoPDV['LATITUD_3'] = [str(i)[4:] for i in dataGeoPDV['GEO_LATITUD_str']]

dataGeoPDV['LONGITUD_1'] = [str(i)[:3] for i in dataGeoPDV['GEO_LONGITUD_str']]
dataGeoPDV['LONGITUD_2'] = [str(i)[3:] for i in dataGeoPDV['GEO_LONGITUD_str']]
#dataGeoPDV['LONGITUD_3'] = [str(i)[6:] for i in dataGeoPDV['GEO_LONGITUD_str']]

dataGeoPDV['LATITUD'] = dataGeoPDV['LATITUD_1'] + '.' + dataGeoPDV['LATITUD_2']
dataGeoPDV['LATITUD'] = dataGeoPDV['LATITUD'].astype(float)
dataGeoPDV['LONGITUD'] = dataGeoPDV['LONGITUD_1'] + '.' + dataGeoPDV['LONGITUD_2']
dataGeoPDV['LONGITUD'] = dataGeoPDV['LONGITUD'].astype(float)

gdf_PDV = geopandas.GeoDataFrame(
    dataGeoPDV, geometry=geopandas.points_from_xy(dataGeoPDV.LONGITUD, dataGeoPDV.LATITUD))
gdf_PDV.index = gdf_PDV['ID PDV ']

## DATA SAVING AS AN EXCEL ##
dataGeoPDV.to_excel('baseLatitudLongitudPDV.xlsx')


