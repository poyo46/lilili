from lilili.utils import normalize_license_name


def test_normalize_license_name():

    license_name_dict = {
        "MIT License": "mitlicense",
        "Apache License V2.0": "apachelicense20",
        "MPL-2.0": "mpl20",
        "BSD-3-Clause": "bsd3clause",
        "BSD-2-Clause or Apache-2.0": "bsd2clauseorapache20",
    }
    for org_name, norm_name in license_name_dict.items():
        assert normalize_license_name(org_name) == norm_name
