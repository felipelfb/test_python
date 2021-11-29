from utils import get_sorted_releases


def test_get_sorted_releases():
    releases = {
        "1.0": [{"upload_time": "2020-09-15T14:00:00"}],
        "1.1": [{"upload_time": "2020-10-12T12:00:00"}],
        "1.11": [{"upload_time": "2021-06-04T08:00:00"}],
        "1.2": [{"upload_time": "2020-11-08T18:00:00"}],
        "1.22": [{"upload_time": "2021-10-22T21:00:00"}],
        "1.3": [{"upload_time": "2020-12-24T15:00:00"}],
    }
    sorted_releases = get_sorted_releases(releases)
    assert sorted_releases[0]["version"] == "1.0"
    assert sorted_releases[1]["version"] == "1.1"
    assert sorted_releases[2]["version"] == "1.2"
    assert sorted_releases[3]["version"] == "1.3"
    assert sorted_releases[4]["version"] == "1.11"
    assert sorted_releases[5]["version"] == "1.22"
