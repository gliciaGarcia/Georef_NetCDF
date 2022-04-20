#--------------------------------------------------------------------#
#    Script que georreferencia o arquivo no formato netcdf para o    #
#     sistema de coordenadas EPSG:4326. Este script gera um novo     #
#         arquivo em formato tif que pode ser lido no QGIS.          #
#--------------------------------------------------------------------#
#        Autor: Glícia Ruth Garcia de Araújo - 20/04/2022            #
#--------------------------------------------------------------------#

### Abrir o ambiente conda doutorado no Windows
from osgeo import gdal

#Abrindo o arquivo de entrada
filename = r"D:\Doutorado_INPE2020\Tese\analise_cluster\verao\teste.nc"
input_raster = gdal.Open(filename)

#Criando o arquivo de saida
output_raster = r"D:\Doutorado_INPE2020\Tese\analise_cluster\verao\teste2.tif"

##Transformando as coordenadas em dstSRS='EPSG:4326'
warp = gdal.Warp(output_raster,input_raster,format = "GTiff")
