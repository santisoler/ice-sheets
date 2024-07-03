import pooch
import pandas as pd

from ._version import __version__

VERSION = "v" + __version__
REGISTRY = {
    "antarctica.csv": "e5c0f1741bc296bb54a1ec93166efc67e2e1cde8d74f1d8089bc68cf5ee1433d",
    "greenland.csv": "8bf3ba40cd777bc5e18d247fbfbdb05c8ff454fa84059cdc3fc507b38d4e814a",
}
PUPPY = pooch.create(
    path=pooch.os_cache("ice-sheets"),
    base_url="https://github.com/santisoler/ice-sheets/raw/{version}/datasets/",
    version=VERSION,
    version_dev="main",
    registry=REGISTRY,
)


def fetch_antarctica_ice_sheet_mass_balance():
    """
    Fetch DataFrame with cumulative Antarctica's ice sheet mass balance

    Returns
    -------
    pandas.DataFrame
    """
    fname = PUPPY.fetch("antarctica.csv")
    return pd.read_csv(fname, index_col=0)


def fetch_greenland_ice_sheet_mass_balance():
    """
    Fetch DataFrame with cumulative Greenland's ice sheet mass balance

    Returns
    -------
    pandas.DataFrame
    """
    fname = PUPPY.fetch("greenland.csv")
    return pd.read_csv(fname, index_col=0)
