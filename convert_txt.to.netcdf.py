#--------------------------------------------------------------------------#
#          Created by Glícia Ruth Garcia de Araújo - 20/04/2022            #
#--------------------------------------------------------------------------#

import numpy as np
import pandas as pd
import xarray as xr
#import rioxarray as rio

data = pd.read_csv('K2_ERA5_janeiro.txt', sep=';')
print(data)

#Salvando os arquivos netcdf
#note that pandas.DataFrame's to_xarray() method is equivalent to
# xarray.Dataset.from_dataframe()
ds = data.set_index(['lat', 'lon']).to_xarray()
ds = ds.reindex(lat=list(reversed(ds.lat)))  ## invertendo a latitude
print(ds) 

# create xray Dataset from Pandas DataFrame

# add variable attribute metadata
ds['lat'].attrs={'units':'degrees', 'long_name':'Latitude'}
ds['lon'].attrs={'units':'degrees', 'long_name':'Longitude'}
ds['grupo'].attrs={'units':'celsius', 'long_name':'Grupo de Tmax'}

# add global attribute metadata
ds.attrs={'Conventions':'CF-1.6', 'title':'Data', 'summary':'Data generated'}

# save to netCDF
ds.to_netcdf('K2_ERA5_janeiro.nc')
