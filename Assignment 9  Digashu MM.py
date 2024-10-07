# -- coding: utf-8 --
"""

Author: Digashu MM
Date: 4/10/2024

"""
import os
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature


directory = r"3a2c4d1fd714eb21cea6f78b5bbc46fe"  
output_file = "processed_humidity_data.nc"


data_list = []

# Loop through the NetCDF files in the directory
for filename in sorted(os.listdir(directory)):
    if filename.endswith(".nc"):
        file_path = os.path.join(directory, filename)
        
        # Open the NetCDF file using xarray
        ds = xr.open_dataset(file_path)
        
        # Extract the climate variable (Humidity)
        humidity_variable = ds['Relative_Humidity_2m_06h']
        
        # Append the data to the list
        data_list.append(humidity_variable)

# Convert the list to a NumPy array
# This assumes time is the first dimension, and you stack the time dimension in the first axis
data_array = np.concatenate([data.values for data in data_list], axis=0)

# Handle NaN values (e.g., set to zero or interpolate)
data_array = np.nan_to_num(data_array, nan=0.0)

# Calculate statistics: mean, minimum, and maximum over time (assuming time is the first axis)
monthly_mean = np.mean(data_array, axis=0)
monthly_min = np.min(data_array, axis=0)
monthly_max = np.max(data_array, axis=0)

# Create a new xarray dataset for the calculated statistics
new_ds = xr.Dataset(
    {
        'monthly_mean': (('lat', 'lon'), monthly_mean),
        'monthly_min': (('lat', 'lon'), monthly_min),
        'monthly_max': (('lat', 'lon'), monthly_max)
    },
    coords={
        'lat': ds['lat'],
        'lon': ds['lon']
    }
)

# Write the new dataset to a NetCDF file
new_ds.to_netcdf(output_file)
print(f"Statistics saved to {output_file}")

# Plot the statistics using matplotlib and cartopy for South Africa map
fig, ax = plt.subplots(2, 2, figsize=(15, 12), subplot_kw={'projection': ccrs.PlateCarree()})

# Define the extent for South Africa (lon_min, lon_max, lat_min, lat_max)
extent = [15, 35, -35, -22]

# Plot Monthly Mean
ax[0, 0].set_extent(extent)
ax[0, 0].coastlines()
ax[0, 0].add_feature(cfeature.BORDERS, linestyle=':')
ax[0, 0].add_feature(cfeature.LAND, edgecolor='black')
img = ax[0, 0].imshow(monthly_mean, extent=extent, origin='lower', cmap='Greens', interpolation='nearest')
fig.colorbar(img, ax=ax[0, 0], orientation='vertical', fraction=0.046, pad=0.04)
ax[0, 0].set_title('Monthly Mean Humidity')

# Plot Monthly Minimum
ax[0, 1].set_extent(extent)
ax[0, 1].coastlines()
ax[0, 1].add_feature(cfeature.BORDERS, linestyle=':')
ax[0, 1].add_feature(cfeature.LAND, edgecolor='black')
img = ax[0, 1].imshow(monthly_min, extent=extent, origin='lower', cmap='Reds', interpolation='nearest')
fig.colorbar(img, ax=ax[0, 1], orientation='vertical', fraction=0.046, pad=0.04)
ax[0, 1].set_title('Monthly Minimum Humidity')

# Plot Monthly Maximum
ax[1, 0].set_extent(extent)
ax[1, 0].coastlines()
ax[1, 0].add_feature(cfeature.BORDERS, linestyle=':')
ax[1, 0].add_feature(cfeature.LAND, edgecolor='black')
img = ax[1, 0].imshow(monthly_max, extent=extent, origin='lower', cmap='Purples', interpolation='nearest')
fig.colorbar(img, ax=ax[1, 0], orientation='vertical', fraction=0.046, pad=0.04)
ax[1, 0].set_title('Monthly Maximum Humidity')

plt.tight_layout()
plt.show()

print(new_ds)