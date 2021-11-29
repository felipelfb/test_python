import json

from utils import (
    append_version_values,
    get_pypi_module_json,
    get_sorted_releases,
    identify_and_split,
)


def process_requirements_status(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        packages_list = []
        for line in lines:
            requirement = line.strip()
            if requirement:
                process_requirement(requirement, packages_list)
        print(json.dumps(packages_list, indent=2))


def process_requirement(requirement, packages_list):
    module, version_type = identify_and_split(requirement)
    module_name = module.get("module_name")
    module_version = module.get("version")
    releases = get_pypi_module_json(module_name).get("releases")
    releases_dates = get_sorted_releases(releases)
    append_version_values(
        module_version, version_type, module_name, releases_dates, packages_list
    )
