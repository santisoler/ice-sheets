from ice_sheets import datasets


def test_antarctica():
    df = datasets.fetch_antarctica_ice_sheet_mass_balance()


def test_greenland():
    df = datasets.fetch_greenland_ice_sheet_mass_balance()
