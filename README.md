
## WIP
=======
## cems-flood

A dataset plugin for climetlab for the dataset cems-flood/glofas.


Features
--------

In this README is a description of how to get the cems-flood.

## Datasets description

There are two datasets: 

### 1 : `glofas`


### 2
TODO


## Using climetlab to access the data (supports grib, netcdf and zarr)

See the demo notebooks here (https://github.com/ecmwf-lab/climetlab_cems_flood/notebooks

https://github.com/ecmwf-lab/climetlab_cems_flood/notebooks/demo_glofas.ipynb
[nbviewer] (https://nbviewer.jupyter.org/github/climetlab_cems_flood/blob/main/notebooks/demo_glofas.ipynb) 
[colab] (https://colab.research.google.com/github/climetlab_cems_flood/blob/main/notebooks/demo_glofas.ipynb) 

The climetlab python package allows easy access to the data with a few lines of code such as:
```

!pip install climetlab climetlab_cems_flood
import climetlab as cml
ds = cml.load_dataset(""cems-flood-glofas", date='20201231',)
ds.to_xarray()
```
