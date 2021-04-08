# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 13:43:00 2021

@author: cristinarusso
"""

from LACCE_function import LACCE

LACCE(path_in       = 'D:/Work/Data/SSH/Gridded/REP/2017/CMEMS_data/altim_ocean_daily_19930101.nc',
      path_out      = 'D:/Work/Data/',
      lat_var_name  = 'latitude',
      lon_var_name  = 'longitude',
      v_var_name    = 'vgos',
      u_var_name    = 'ugos',
      ssh_var_name  = 'adt',
      east          = 36, 
      west          = 12, 
      south         = -43.875, 
      north         = -25,
      model         = False,
      map_figure    = True)
      