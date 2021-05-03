import pandas as pd
import glob, os
import sidetable
#Tratamiento
os.chdir(r'C:\Users\IVANOV\AnacondaProjects\0 0 Projects\Project_13\bases//')   #Ruta donde tengo mis bd
results = pd.DataFrame([])

for counter, file in enumerate(glob.glob("RESAGEBURB*")):    #Abre todos los archivos que comiencen con "RESAGEBURB"
    namedf = pd.read_csv(file, skiprows=0, #usecols=[1,2,3]
                        )
    results = results.append(namedf)

results.to_csv(r'C:\Users\IVANOV\AnacondaProjects\0 0 Projects\Project_13\resultados\\combinedfile.csv')
#os.chdir(r"C:\Users\IVANOV\AnacondaProjects\0 0 Projects\Project_13\resultados")
os.chdir(r"C:\Users\win\AnacondaProjects\0 0 Projects\Project_12")
aver= pd.read_csv("combinedfile.csv")
aver.head()

print(aver.columns.tolist())
#Filtro Entidades
# SEPARACIÖN DE subBASES (PREDISEÑADAS)
porentidad =aver[aver.NOM_LOC == 'Total de la entidad']               ## subase (Total de la entidad)
pormunicipio =aver[aver.NOM_LOC == 'Total del municipio']             ## subase (Total del municipio)
porlocalidad =aver[aver.NOM_LOC == 'Total de la localidad urbana']    ## subase (Total de la localidad)
porageb =aver[aver.NOM_LOC == 'Total AGEB urbana']                    ## subase (Total del AGEB)
porentidad_f = porentidad[[
    'ENTIDAD',
    'NOM_ENT',
#    'MUN',
#    'NOM_MUN', 
#    'LOC', 
#    'NOM_LOC',
#    'AGEB',
#    'MZA',
    
    #Población     
    'POBTOT',            # población total
    'POBFEM',            # población femenina 
    'POBMAS',            # población masculina 

     #Piramide de edad    
    'P_0A2',              # población de 0 a 2 años
    'P_3A5',              # población de 3 a 5 años 
    'P_6A11',             # población de 6 a 11 años 
    'P_12A14',            # población de 12 a 14 años 
    'P_15A17',            # población de 15 a 17 años 
    'POB15_64',           # población de 15 a 64 años 
    'P_60YMAS',           # población de 60 y más

    # MIGRACION 
    'PNACOE',             # Población nacida en otra entidad 
    'PNACOE_F',           # Población femenina nacida en la entidad 
    'PRESOE15',           # Población de 5 años y más residente en otra entidad en marzo de 2015

    #Discapacidad
    'PCON_DISC',          # Población con discapacidad 
    
    #Educación
    'P15YM_AN',           # Población de 15 años y más analfabeta 
    
    # ECONOMIA
    'PE_INAC',            # Población de 12 años y más no económicamente activa 
    'POCUPADA',           # población ocupada 
    'POCUPADA_F',         # Población femenina de 12 años y más desocupada 
    'POCUPADA_M',         # Población masculina de 12 años y más ocupada 
    'PDESOCUP',           # Población de 12 años y más desocupada 

    # DERECHOHABIENCIA
    'PSINDER',            # Población sin afiliación a servicios de salud  
    'PDER_IMSS',          # Población afiliada a servicios de salud en el IMSS  
    'PDER_SEGP',          # Población afiliada a servicios de salud en el Instituto de Salud para el Bienestar  
    'PAFIL_IPRIV',        # Población afiliada a servicios de salud en una institución privada 
    
    # RELIGIION
    'PCATOLICA',          # Población con religión católica 
    'PRO_CRIEVA',         # Población con grupo religioso protestante/ cristiano evangélico  
    'POTRAS_REL',         # Población con otras religiones diferentes a las anteriores  
    'PSIN_RELIG',         # Población sin religión o sin adscripción religiosa 

    # HOGARES CENSALES
    'TOTHOG',             # Total de hogares censales 
    'HOGJEF_F',           # Hogares censales con persona de referencia mujer 
    'POBHOG',             # Población en hogares censales 
    'PHOGJEF_F',          # Población en hogares censales con persona de referencia mujer 
    
    # VIVIENDA
    'VIVTOT',             # Total de viviendas 
    'PROM_OCUP',          # Promedio de  ocupantes en viviendas particulares habitadas 
    'PRO_OCUP_C',         # Promedio de ocupantes por cuarto en viviendas particulares habitadas 
    'VPH_1DOR',           # Viviendas particulares habitadas con un dormitorio 
    'VPH_C_ELEC',         # Viviendas particulares habitadas que disponen de energía eléctrica  
    'VPH_AGUADV',         # Viviendas particulares habitadas que disponen de agua entubada en el ámbito de la viviendas 
    'VPH_TINACO',         # Viviendas particulares habitadas que disponen de tinaco 
    'VPH_CISTER',         # Viviendas particulares habitadas que disponen de cisterna o aljibe 
    'VPH_EXCSA',          # Viviendas particulares habitadas que disponen de excusado o sanitario 
    'VPH_DRENAJ',         # Viviendas particulares habitadas que disponen de drenaje 
    'VPH_REFRI',          # Viviendas particulares habitadas que disponen de refrigerador 
    'VPH_LAVAD',          # Viviendas particulares habitadas que disponen de lavadora  
    'VPH_BICI',           # Viviendas particulares habitadas que disponen de bicicleta como medio de transporte 
    'VPH_TV',             # Viviendas particulares habitadas que disponen de televisor 
    'VPH_PC',             # Viviendas particulares habitadas que disponen de computadora, laptop o tablet
    'VPH_CEL',            # Viviendas particulares habitadas que disponen de teléfono celular 
    'VPH_INTER',          # Viviendas particulares habitadas que disponen de Internet 
    'VPH_SPMVPI',         # Viviendas particulares habitadas que disponen de servicio de películas, música o videos de paga por Internet
]]

porentidad_f.to_csv("entidades2020.csv")


#Filtro Municipios
pormunicipio_f = pormunicipio[[
    'ENTIDAD',
    'NOM_ENT',
#    'MUN',
#    'NOM_MUN', 
#    'LOC', 
#    'NOM_LOC',
#    'AGEB',
#    'MZA',
    
    #Población     
    'POBTOT',            # población total
    'POBFEM',            # población femenina 
    'POBMAS',            # población masculina 

     #Piramide de edad    
    'P_0A2',              # población de 0 a 2 años
    'P_3A5',              # población de 3 a 5 años 
    'P_6A11',             # población de 6 a 11 años 
    'P_12A14',            # población de 12 a 14 años 
    'P_15A17',            # población de 15 a 17 años 
    'POB15_64',           # población de 15 a 64 años 
    'P_60YMAS',           # población de 60 y más

    # MIGRACION 
    'PNACOE',             # Población nacida en otra entidad 
    'PNACOE_F',           # Población femenina nacida en la entidad 
    'PRESOE15',           # Población de 5 años y más residente en otra entidad en marzo de 2015

    #Discapacidad
    'PCON_DISC',          # Población con discapacidad 
    
    #Educación
    'P15YM_AN',           # Población de 15 años y más analfabeta 
    
    # ECONOMIA
    'PE_INAC',            # Población de 12 años y más no económicamente activa 
    'POCUPADA',           # población ocupada 
    'POCUPADA_F',         # Población femenina de 12 años y más desocupada 
    'POCUPADA_M',         # Población masculina de 12 años y más ocupada 
    'PDESOCUP',           # Población de 12 años y más desocupada 

    # DERECHOHABIENCIA
    'PSINDER',            # Población sin afiliación a servicios de salud  
    'PDER_IMSS',          # Población afiliada a servicios de salud en el IMSS  
    'PDER_SEGP',          # Población afiliada a servicios de salud en el Instituto de Salud para el Bienestar  
    'PAFIL_IPRIV',        # Población afiliada a servicios de salud en una institución privada 
    
    # RELIGIION
    'PCATOLICA',          # Población con religión católica 
    'PRO_CRIEVA',         # Población con grupo religioso protestante/ cristiano evangélico  
    'POTRAS_REL',         # Población con otras religiones diferentes a las anteriores  
    'PSIN_RELIG',         # Población sin religión o sin adscripción religiosa 

    # HOGARES CENSALES
    'TOTHOG',             # Total de hogares censales 
    'HOGJEF_F',           # Hogares censales con persona de referencia mujer 
    'POBHOG',             # Población en hogares censales 
    'PHOGJEF_F',          # Población en hogares censales con persona de referencia mujer 
    
    # VIVIENDA
    'VIVTOT',             # Total de viviendas 
    'PROM_OCUP',          # Promedio de  ocupantes en viviendas particulares habitadas 
    'PRO_OCUP_C',         # Promedio de ocupantes por cuarto en viviendas particulares habitadas 
    'VPH_1DOR',           # Viviendas particulares habitadas con un dormitorio 
    'VPH_C_ELEC',         # Viviendas particulares habitadas que disponen de energía eléctrica  
    'VPH_AGUADV',         # Viviendas particulares habitadas que disponen de agua entubada en el ámbito de la viviendas 
    'VPH_TINACO',         # Viviendas particulares habitadas que disponen de tinaco 
    'VPH_CISTER',         # Viviendas particulares habitadas que disponen de cisterna o aljibe 
    'VPH_EXCSA',          # Viviendas particulares habitadas que disponen de excusado o sanitario 
    'VPH_DRENAJ',         # Viviendas particulares habitadas que disponen de drenaje 
    'VPH_REFRI',          # Viviendas particulares habitadas que disponen de refrigerador 
    'VPH_LAVAD',          # Viviendas particulares habitadas que disponen de lavadora  
    'VPH_BICI',           # Viviendas particulares habitadas que disponen de bicicleta como medio de transporte 
    'VPH_TV',             # Viviendas particulares habitadas que disponen de televisor 
    'VPH_PC',             # Viviendas particulares habitadas que disponen de computadora, laptop o tablet
    'VPH_CEL',            # Viviendas particulares habitadas que disponen de teléfono celular 
    'VPH_INTER',          # Viviendas particulares habitadas que disponen de Internet 
    'VPH_SPMVPI',         # Viviendas particulares habitadas que disponen de servicio de películas, música o videos de paga por Internet
]]
pormunicipio_f.to_csv("municipios2020.csv")
