#!/usr/bin/env python3
from __future__ import annotations

import climetlab as cml
from climetlab import Dataset

# __version__ = "0.1.0"


class GlofasRerorecast(Dataset):
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

    dataset = None

    def __init__(self, year):
        self.year = year

    # @normalize_args(variable=["river_discharge_in_the_last_24_hours"])
    def _load(self, variable):
        request = {
            "system_version": "version_2_1",
            "hydrological_model": "htessel_lisflood",
            "product_type": "ensemble_perturbed_forecasts",
            "variable": variable,
            "year": "2019",
            "month": "11",
            "day": "05",
            "leadtime_hour": "24",
            "format": "grib",
        }
        self.source = cml.load_source("cds", "cems-glofas-forecast", **request)
