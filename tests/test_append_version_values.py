from utils import append_version_values


def test_append_version_values_equals_out_of_date():
    packages_list = []
    module_version = "1.3.0"
    version_type = "equals"
    releases_dates = [{"version": "1.3.0"}, {"version": "1.3.1"}]
    module_name = "test"
    append_version_values(
        module_version, version_type, module_name, releases_dates, packages_list
    )

    assert packages_list[0] == {
        "packageName": "test",
        "currentVersion": "1.3.0",
        "latestVersion": "1.3.1",
        "outOfDate": True,
    }


def test_append_version_values_equals_current():
    packages_list = []
    module_version = "1.3.1"
    version_type = "equals"
    releases_dates = [{"version": "1.3.0"}, {"version": "1.3.1"}]
    module_name = "test"
    append_version_values(
        module_version, version_type, module_name, releases_dates, packages_list
    )

    assert packages_list[0] == {
        "packageName": "test",
        "currentVersion": "1.3.1",
        "latestVersion": "1.3.1",
        "outOfDate": False,
    }


def test_append_version_values_greater_than():
    packages_list = []
    module_version = "1.3.0"
    version_type = "greater_than"
    releases_dates = [{"version": "1.3.0"}, {"version": "1.3.1"}]
    module_name = "test"
    append_version_values(
        module_version, version_type, module_name, releases_dates, packages_list
    )

    assert packages_list[0] == {
        "packageName": "test",
        "currentVersion": "1.3.1",
        "latestVersion": "1.3.1",
        "outOfDate": False,
    }


def test_append_version_values_latest():
    packages_list = []
    module_version = None
    version_type = "latest"
    releases_dates = [{"version": "1.3.0"}, {"version": "1.3.1"}]
    module_name = "test"
    append_version_values(
        module_version, version_type, module_name, releases_dates, packages_list
    )

    assert packages_list[0] == {
        "packageName": "test",
        "currentVersion": "1.3.1",
        "latestVersion": "1.3.1",
        "outOfDate": False,
    }
