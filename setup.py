#!/usr/bin/env python


import io
import os

import setuptools
import versioneer

with open("requirements.txt", "r") as fh:
    requirements = [line.strip() for line in fh]


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return io.open(file_path, encoding="utf-8").read()


package_name = "climetlab_cems_flood"

# version = None
# init_py = os.path.join(package_name.replace("-", "_"), "__init__.py")
# for line in read(init_py).split("\n"):
#    if line.startswith("__version__"):
#        version = line.split("=")[-1].strip()[1:-1]
# assert version


extras_require = {}

setuptools.setup(
    name=package_name,
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="A dataset plugin for climetlab for the dataset cems-flood/glofas.",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="iacopo ferrario",
    author_email="iacopo.ferrario@ecmwf.int",
    url="https://github.com/ecmwf-lab/cems-flood",
    license="Apache License Version 2.0",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=["climetlab>=0.5.6"],
    extras_require=extras_require,
    zip_safe=True,
    entry_points={
        "climetlab.datasets": [
            "cems-flood-glofas-forecast = climetlab_cems_flood.glofas_forecast:GlofasForecast",
            "cems-flood-glofas-historical = climetlab_cems_flood.glofas_historical:GlofasHistorical",
        ]
    },
    keywords="hydrology",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
    ],
)
