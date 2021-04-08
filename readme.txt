LACCE AND HOW TO USE IT

AUTHOR AND POINT OF CONTACT
Cristina Russo cristinaserenarusso@gmail.com

DESCRIPTION
This method is able to identify the Location of the Agulhas Current’s Core and Edges (LACCE), throughout the greater Agulhas system. LACCE is applied to daily altimetric fields of absolute dynamic topography and geostrophic velocities. LACCE can be used to monitor changes in the Agulhas Current’s position caused by mesoscale processes such as early retroflection events or transient features like Natal Pulses. The core of the current is identified by the local maximum speed, while the edges are identified as the local maximum gradient in speed. The method is described in greater detail in Russo et al., 2021 (https://doi.org/10.1016/j.rse.2020.112239). 
 
REQUIREMENTS AND LIMITATIONS
-	The input dataset needs to contain the following variables:
-	absolute dynamic topography
-	u geostrophic velocity component
-	v geostrophic velocity component
-	The input data needs to encompass this entire area (23-45˚S and 12-36˚E)
-	The input data must have a daily temporal resolution and each day must be in a separate file
-	The three scripts need to be the same working directory
-	u, v and adt must all be on the same grid 

DEPENDANCIES
- math
- numpy
- pylab
- xarray
- pandas
- scipy.ndimage.gaussian_filter1d
- scipy.signal
- shapely.geometry.Point
- shapely.geometry.polygon.Polygon
- os
- scipy.interpolate
- scipy.io.netcdf.netcdf_file
- matplotlib.pyplot
- datetime
- mpl_toolkits.basemap
- sys

SCRIPTS
LACCE_function.py, mkDefsSRPV2_1.py, run_LACCE.py

FUNCTION
LACCE(path_in,path_out,lat_var_name,lon_var_name,v_var_name,u_var_name,ssh_var_name,west
,east,south,north,model=False,map_figure=True)

DESCRIPTION OF INPUT REQUIRED
path_in 		- path to altimetry file
path_out        	- path to save output
lat_var_name    	- name of latitude variable in input file (must be string)
lon_var_name   		- name of longitude variable in input file (must be string)
v_var_name      	- name of v velocity component variable in input file (must be string)
u_var_name      	- name of u velocity component variable in input file (must be string)
ssh_var_name   		- name of absolute dynamic topography variable in input file (must be string)
model           	- if True then the dataset has vertical levels, if False then input data only surface data is available
map_figure      	- if True map figure will be produced, if False map figure will not be produced
west            	- western limit of map
east            	- eastern limit of map
south           	- southern limit of map
north           	- northern limit of map

OUTPUT PRODUCED
NetCDF    		- output LACCE netCDF file with coordinates of Agulhas Current core and edges
Map Figure      	- If map_figure is True then a map will be produced and saved  

