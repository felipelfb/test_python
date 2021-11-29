import requests
import re
from datetime import datetime

from const import EQUALS, GREATER_THAN, STANDARD


def get_pypi_module_json(module):
    try:
        return requests.get(f"https://pypi.org/pypi/{module}/json").json()
    except Exception:
        return {}


def identify_and_split(requirement):
    if re.search(EQUALS, requirement):
        split = re.split(EQUALS, requirement)
        return ({"module_name": split[0], "version": split[1]}, "equals")
    elif re.search(GREATER_THAN, requirement):
        split = re.split(GREATER_THAN, requirement)
        return ({"module_name": split[0], "version": split[1]}, "greater_than")
    elif re.search(STANDARD, requirement):
        return (
            {"module_name": re.split(STANDARD, requirement)[0], "version": None},
            "latest",
        )
    return ({"module_name": requirement, "version": None}, "latest")


def get_sorted_releases(releases):
    releases_dates = [
        {
            "version": key,
            "upload_time": datetime.fromisoformat(
                releases.get(key)[0].get("upload_time")
            ),
        }
        for key in releases.keys()
        if len(releases.get(key)) > 0
    ]
    return sorted(releases_dates, key=lambda item: item.get("upload_time"))


def append_version_values(
    module_version, version_type, module_name, releases_dates, packages_list
):
    if version_type in ("equals"):
        current_version = module_version
        latest_version = releases_dates[-1].get("version")
        out_of_date = not (current_version == latest_version)
    else:
        current_version = releases_dates[-1].get("version")
        latest_version = current_version
        out_of_date = False
    packages_list.append(
        {
            "packageName": module_name,
            "currentVersion": current_version,
            "latestVersion": latest_version,
            "outOfDate": out_of_date,
        }
    )
