import xarray as xr
import os
netcdf_file_name = 'C:\\Users\\jayra\\Downloads\\NETCDF4_LSASAF_MSG_ALBEDO_MSG-Disk_202308010000.nc'
ds = xr.open_dataset(netcdf_file_name)
df = ds.to_dataframe()

df.to_csv('C:\\Users\\jayra\\Downloads\\trail01.csv')