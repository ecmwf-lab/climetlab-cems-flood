#!/usr/bin/env python3
from __future__ import annotations

import climetlab as cml
from climetlab import Dataset

from .utils import Parser,months_num2str

# __version__ = "0.1.0"


class GlofasHistorical(Dataset):
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
