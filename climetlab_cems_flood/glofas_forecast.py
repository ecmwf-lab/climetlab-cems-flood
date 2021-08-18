#!/usr/bin/env python3
from __future__ import annotations

import climetlab as cml
from climetlab import Dataset

from .utils import Parser

# __version__ = "0.1.0"


class GlofasForecast(Dataset):
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

    dataset = "glofas_forecast"

    temporal_range = [2019,2021]

    def __init__(self, system_version, product_type, model, variable, period, leadtime):

        self.parser = Parser(self.temporal_range)

        years, months, days = self.parser.period(period)

        leadtime_hour = self.parser.leadtime(leadtime)

 
        self.request = {
            "system_version": system_version,
            "hydrological_model": model,
            "product_type": product_type,
            "variable": variable,
            "year": years,
            "month": months,
            "day": days,
            "leadtime_hour": leadtime_hour,
            "format": "grib",
        }


        self.source = cml.load_source("cds", "cems-glofas-forecast", **self.request)

        # sources = []
        # for year in years:
        #     request["year"] = year
        #     sources.append(
        #         cml.load_source("cds", "cems-glofas-forecast", **request)
        #     )

        # self.source = cml.load_source("multi", sources)


    def _repr_html_(self):
        if self.request == "-":
            super()._repr_html(self)
        else:
            style = """
                <style>table.climetlab td {
                vertical-align: top;
                text-align: left !important;}
            </style>"""      
            
            li = ""
            for key in self.request:
                li += f"<li> <b>{key}: </b> {self.request[key]} </li>".format()
                
            return style + f"""<table class="climetlab"><tr><td><b>Request</b></td><td><ul>{li}</ul></td></tr></table>"""