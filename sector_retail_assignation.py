def sector_retail_assignation():	
	matriz_distancias = []
	for i in gdf_PDV.index:
	    matriz_distancias.append(gdf_PDV['geometry'].distance(gdf_PDV['geometry'].loc[i]).values)
	    
	matriz_conexion = pd.DataFrame(matriz_distancias, columns = gdf_PDV.index, index = gdf_PDV.index)
	capa_vecindad = matriz_conexion <= 0.0045

	gdf_caldas_manzana = gdf_caldas_manzanas
	conexion_manzanas_puntos = dict()
	for indice_punto in gdf_PDV.index:
	    conexion_manzanas_puntos[str(indice_punto)] = []

	gdf_caldas_manzana = gdf_caldas_manzana.rename(columns = variables_interes)
	vecinos = list()

	Ls = 4
	Li = 1
	l = 0.15
	c = 19
	sigmoide = lambda x: (Ls/(1+np.exp(-l*(x - c)))) + Li

	for i in gdf_PDV.index:
	    radio_vecindad = 0.0096 / sigmoide(capa_vecindad.sum().loc[i])
	    print(i, '*****', radio_vecindad)
	    esVecino = gdf_caldas_manzana['geometry'].distance(gdf_PDV['geometry'].loc[i]) <= radio_vecindad
	    #print(sum(esVecino))
	    vecinos.append(sum(esVecino))
	    caracteristicas_punto = gdf_caldas_manzana[agregacion_variables.keys()].loc[esVecino]
	    print(len(caracteristicas_punto))
	    #print(caracteristicas_punto)
	    caracteristicas_punto_agg = caracteristicas_punto.sum()
	    #conexion_manzanas_puntos[str(i)].append(caracteristicas_punto_agg)
	    conexion_manzanas_puntos[str(i)] = caracteristicas_punto_agg

	for i in gdf_caldas_manzana.loc[162695].index:
	    print(i, gdf_caldas_manzana.loc[162695].loc[i])


	df_caracteristicas = pd.DataFrame(columns = agregacion_variables.keys())

	for i in conexion_manzanas_puntos.keys():
	    #print(conexion_manzanas_puntos[i][0])
	    df_caracteristicas = df_caracteristicas.append(pd.DataFrame(conexion_manzanas_puntos[i]).transpose())
	    
	df_caracteristicas.index = conexion_manzanas_puntos.keys()

	df_caracteristicas.to_excel('caracteristicas_pdv.xlsx')