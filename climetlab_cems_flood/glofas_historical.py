#!/usr/bin/env python3
from __future__ import annotations

import climetlab as cml
from climetlab import Dataset

from .utils import Parser,months_num2str

from functools import partial
# __version__ = "0.1.0"


class GlofasHistorical(Dataset):
    name = None
    home_page = "-"
    licence = "-"
    documentation = "-"
    citation = "-"
    request = "-"


    terms_of_use = (
        "By downloading data from this dataset, you agree to the terms and conditions defined at "
        "https://github.com/ecmwf-lab/climetlab_cems_flood/LICENSE"
        "If you do not agree with such terms, do not download the data. "
    )

    dataset = None

    temporal_range = [1979,2021]

    def __init__(self, system_version, product_type, model, variable, period):
        
        self.parser = Parser(self.temporal_range)

        years, months, days = self.parser.period(period)

        months = months_num2str(months)


        self.request = {
            "system_version": system_version,
            "hydrological_model": model,
            "product_type": product_type,
            "variable": variable,
            "hyear": years,
            "hmonth": months,
            "hday": days,
            "format": "grib",
        }


        self.source = cml.load_source("cds", "cems-glofas-historical", **self.request)


    def to_xarray(self):
    
            return self.source.to_xarray(backend_kwargs={'time_dims':['time']}).squeeze("step")


    def _repr_html_(self):
        ret = super()._repr_html_()
    
        style = """
            <style>table.climetlab td {
            vertical-align: top;
            text-align: left !important;}
        </style>"""      
        
        li = ""
        for key in self.request:
            li += f"<li> <b>{key}: </b> {self.request[key]} </li>".format()
            
        return ret + f"""<table class="climetlab"><tr><td><b>Request</b></td><td><ul>{li}</ul></td></tr></table>"""