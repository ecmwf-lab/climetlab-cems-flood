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


    terms_of_use = (
        "By downloading data from this dataset, you agree to the terms and conditions defined at "
        "https://github.com/ecmwf-lab/climetlab_cems_flood/LICENSE"
        "If you do not agree with such terms, do not download the data. "
    )

    dataset = "glofas_forecast"

    def __init__(self):
        self.parser = Parser()

    # @normalize_args(variable=["river_discharge_in_the_last_24_hours"])
    def _load(self, system_version, product_type, model, variable, period, leadtime):

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