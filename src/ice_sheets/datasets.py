import pooch
import pandas as pd

from ._version import __version__

VERSION = "v" + __version__
REGISTRY = {
    "antarctica.csv": "8d32a1a4b500c443981c60fc45a7126b16a9fd6d330c8107a1e584b81e841e53",
    "greenland.csv": "0538ba7f521e5a73a70faa00d7f917a8bbdb549c94a6b823685ff3da985cb939",
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
