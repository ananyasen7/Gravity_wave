import os
import xarray as xr
from tqdm import tqdm

folder_path = './'  

files = [f for f in os.listdir(folder_path) if f.startswith('met_em.d') and f.endswith('.nc')]

for file in tqdm(files):
  ds = xr.open_dataset(file)
  ds['HGT_M'].values[:] = 0.25*ds['HGT_M'].values[:]
  ds.to_netcdf(f"{file}_new", format='NETCDF4')

