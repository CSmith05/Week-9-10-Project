### This script maps out the distribution of molluscan shellfish in Maine, determines which species is the most common, then draws a scatter plot of the most common species and where they live.

import geopandas as gpd
import matplotlib.pyplot as plt

### Reads dataset
mollusks = gpd.read_file('https://raw.githubusercontent.com/CSmith05/Week-9-10-Project/main/MaineDMR_Molluscan_Shellfish_2010.geojson')

### Scans for each unique species
print(mollusks['SPECIES'].unique())

### Plots the distribution of species using their 'loc' value
### This also color-codes the different species, but it's hard to notice since the map is so small
fig, ax = plt.subplots(figsize=(12, 12))
mollusks.plot(
    ax=ax, column='SPECIES', cmap='tab10', legend=True, edgecolor='none',
    legend_kwds={'loc': 'upper left'}
)

### Graph text
ax.set_title("Molluscan Shellfish Distribution in Maine")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()

### Creates a bar chart for the most common species
species_counts = mollusks['SPECIES'].value_counts()
plt.figure(figsize=(12, 6))
plt.barh(species_counts.index, species_counts.values, color='tab:blue')
plt.title("Most Common Molluscan Shellfish in Maine")
plt.xlabel("Count")
plt.ylabel("Species")
plt.gca().invert_yaxis()
plt.show()

### Creates scatter plot of most common species' locations and centralize their points for clarity
most_common_species = species_counts.idxmax()
common_mollusks = mollusks[mollusks['SPECIES'] == most_common_species].copy()
common_mollusks['geometry'] = common_mollusks.geometry.centroid

### Plot values
plt.figure(figsize=(10, 8))
plt.scatter(common_mollusks.geometry.x, common_mollusks.geometry.y, alpha=0.5, label=most_common_species, color='blue')
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title(f"{most_common_species} Distribution")
plt.legend()
plt.show()
