#!/usr/bin/env python3

import climetlab as cml


def test_read():
    ds = cml.load_dataset(
        "cems-flood-glofas",
        year="2021",
        parameter="t2m",
    )
    xds = ds.to_xarray()
    print(xds)


if __name__ == "__main__":
    test_read()
