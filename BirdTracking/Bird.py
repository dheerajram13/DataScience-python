import sys
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
import cartopy.crs as ccrs 
import cartopy.feature as cfeature 


bird_data = pd.read_csv("bird_tracking.csv")
bird_data.info()
bird_data.head()
ix = bird_data.bird_name == "Eric"
x , y = bird_data.longitude[ix],bird_data.latitude[ix]
plt.figure(figsize=(7,7))
plt.plot(x,y,"b.")
plt.show()
bird_names = pd.unique(bird_data.bird_name)
plt.figure(figsize=(7,7))
for bird_name in bird_names:
    ix = bird_data.bird_name == bird_name
    x , y = bird_data.longitude[ix],bird_data.latitude[ix]     
    plt.plot(x,y,".",label=bird_name)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(loc="lower right")
plt.show()
ix = bird_data.bird_name == "Eric"
speed = bird_data.speed_2d[ix]
ind = np.isnan(speed)

plt.hist(speed[~ind])
plt.show()
plt.figure(figsize=(8,4))
speed = bird_data.speed_2d[ bird_data.bird_name == "Eric"]
ind = np.isnan(speed)
plt.hist(speed[~ind],bins=np.linspace(0,30,20),normed = True)
plt.xlabel("2D speed (m/s)")
plt.ylabel("Frequency");
plt.show()
bird_data.speed_2d.plot(kind="hist",range = [0,30])
plt.xlabel("2D speed")
plt.show()

proj=ccrs.Mercator()

plt.figure(figsize=(10,10))
ax = plt.axes(projection=proj)
ax.set_extent((-25.0,10.0,52.0,10.0))
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS,linestyle=':')
for name in bird_names:
    ix = bird_data['bird_name'] == name
    x,y = bird_data.longitude[ix],bird_data.latitude[ix]
    ax.plot(x,y,'.',transform=ccrs.Geodetic(),label=name)
plt.legend(loc = "upper left")
plt.show()