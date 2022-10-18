def completar_arreglo(arreglo):
    while (len(arreglo) < 3):
        arreglo.append('0')
    return arreglo

def asigna_longitud(x):
    if x == 0: return 0
    else: return gdf_PDV['LONGITUD'].loc[x]

def asigna_latitud(x):
    if x == 0: return 0
    else: return gdf_PDV['LATITUD'].loc[x]


def retail_sector_assignation():
	for key in conexion_puntos_manzanas.keys():
	    conexion_puntos_manzanas[key] = completar_arreglo(conexion_puntos_manzanas[key])

	conexion_puntos_manzanas = dict()
	for indice_poligono in gdf_caldas_manzanas.index:
	    conexion_puntos_manzanas[str(indice_poligono)] = []
	    
	for i in gdf_PDV.index:
	    print(i)
	    #print(gdf_PDV['geometry'].loc[i])
	    #print(gdf_caldas_manzanas['geometry'].distance(gdf_PDV['geometry'].loc[i]))
	    print(min(gdf_caldas_manzanas['geometry'].distance(gdf_PDV['geometry'].loc[i])))
	    pertenece = gdf_caldas_manzanas['geometry'].distance(gdf_PDV['geometry'].loc[i]) == min(gdf_caldas_manzanas['geometry'].distance(gdf_PDV['geometry'].loc[i]))
	    print(str(gdf_caldas_manzanas.loc[pertenece].index[0]))
	    conexion_puntos_manzanas[str(gdf_caldas_manzanas.loc[pertenece].index[0])].append(i)


	asignaciones_pdv = pd.DataFrame.from_dict(conexion_puntos_manzanas
	                                          , orient='index'
	                                         )
	asignaciones_pdv.columns = ['pdv1', 'pdv2', 'pdv3']
	asignaciones_pdv['manzana'] = asignaciones_pdv.index
	asignaciones_pdv['manzana'] = asignaciones_pdv['manzana'].astype(int)

	gdf_caldas_manzanas['manzana'] = gdf_caldas_manzanas.index
	gdf_manzana_pdv = gdf_caldas_manzanas.merge(asignaciones_pdv, on='manzana')

	gdf_manzana_pdv_interes = gdf_manzana_pdv[variables_interes.keys()].rename(columns = variables_interes)
	interes = gdf_manzana_pdv_interes[variables_interes.values()]
	interes.to_file("gdf_manzana_pdv.geojson", driver='GeoJSON')

	interes['longitud_pdv1'] = interes['pdv1'].apply(lambda x: asigna_longitud(int(x)))
	interes['latitud_pdv1'] = interes['pdv1'].apply(lambda x: asigna_latitud(int(x)))
	interes.to_file("gdf_manzana_pdv.geojson", driver='GeoJSON')