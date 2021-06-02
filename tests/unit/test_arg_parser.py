import pytest
from climetlab_cems_flood.utils import Parser

parser = Parser()


def assert_period(years,months,days,expected):

    assert years == expected[0]
    assert months == expected[1]
    assert days == expected[2]

def test_parser_leadtime():

    assert parser.leadtime("24-72/480-600") == [
        "24",
        "48",
        "72",
        "480",
        "504",
        "528",
        "552",
        "576",
        "600",
    ]

    assert parser.leadtime("24-600") == [
        "24",
        "48",
        "72",
        "96",
        "120",
        "144",
        "168",
        "192",
        "216",
        "240",
        "264",
        "288",
        "312",
        "336",
        "360",
        "384",
        "408",
        "432",
        "456",
        "480",
        "504",
        "528",
        "552",
        "576",
        "600",
    ]

    assert parser.leadtime("24-72/240-336/480-600") == [
        "24",
        "48",
        "72",
        "240",
        "264",
        "288",
        "312",
        "336",
        "480",
        "504",
        "528",
        "552",
        "576",
        "600",
    ]

@pytest.mark.parametrize("string, expected",[
                                                (
                                                    "20180101-20181231/20200101-20201231",
                                                    [
                                                    ["2018", "2020"],
                                                    ["%02d"%m for m in range(1,13)],
                                                    ["%02d"%d for d in range(1,32)]
                                                    ]
                                                ),
                                                                                                (
                                                    "20180201-20180212/20200101-20200125",
                                                    [
                                                    ["2018", "2020"],
                                                    ["01", "02"],
                                                    ["%02d"%d for d in range(1,26)]
                                                    ]
                                                ),
                                                                                                (
                                                    "20180212/20200101",
                                                    [
                                                    ["2018", "2020"],
                                                    ["01","02"],
                                                    ["01","12"]
                                                    ]
                                                ),
                                                                                                (
                                                    "20180201",
                                                    [
                                                    ["2018"],
                                                    ["02"],
                                                    ["01"]
                                                    ]
                                                ),
                                                                                                (
                                                    "20100101-20200325",
                                                    [
                                                    ["%d"%y for y in range(2010,2021,1)],
                                                    ["%02d"%m for m in range(1,13)],
                                                    ["%02d"%d for d in range(1,32)]
                                                    ]
                                                ),
                                                                                                                                                (
                                                    "2020*01",
                                                    [
                                                    ["2020"],
                                                    ["%02d"%m for m in range(1,13)],
                                                    ["01"]
                                                    ]
                                                ),
                                                pytest.param("202001-12/*1010", 42, marks=pytest.mark.xfail)
                                            ]
                        ) # expected = [[years],[months],[days]]
def test_parser_period(string,expected):

    years, months, days = parser.period(string)

    assert_period(years,months,days,expected)

