#   ---------------------------------------------------------------------------------
#   Copyright (c) Tim Littlefair. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------

"""
This script is part of the tl-python-package-template project.
The project is, as the name suggests, a template from which other
projects can be cloned.

The purpose of this test script is to encourage users who clone
the template as a basis for their own projects, to update the
pyproject.toml file in the base directory and the directory
structure of the project to reflect the name of the project
they are instantiating rather than leaving the placeholder names
in the template.

The tests below make the following assertions:
+ that the basename of the git remote URL matches the name attribute
  in pyproject.toml section [project];
+ that there is a subdirectory under src with a name which matches
  the name attribute in pyproject.toml section [tool.flit.module]
+ that the name attributes in pyproject.toml [project]; and
  [tool.flit.module] agree apart from the conversion of any
  '-' (dash) characters in the [project] name into '_' (underscore)
  characters in the [tool.flit.module] name.

The names in the base versions of files in the template satisfy
these assertions provided the 'origin' git remote still refers
to https://github.com/tim-littlefair/tl-python-package-template.git,
but when an end-user uses the template as the basis for a repository
with a different basename and clones a sandbox from their new repo,
at least one of the assertions above will fail and will force the
user (preferably) to update pyproject.toml to define their own,
PyPi package name and Python module name where these appear in the
pyproject.toml files and under the src, docs and tests subdirectories
in order to achieve clean-running tests.
Alternatively the end user can delete or modify the source of this
test.
"""

import os
import subprocess
import sys


def _get_name_from_toml_section(toml_section_name):
    assert os.path.exists("./pyproject.toml") is True
    grep_toml_command = "|".join([
        # filter out all lines until we see the section heading
        # retain all lines after that point
        f"grep -A1 -F '[{toml_section_name}]' pyproject.toml",
        # scan for lines after the heading which start with 'name'
        "grep -E '^name'",
        # accept only the very first line still accepted at this point
        "head -1",
        # isolate the value, enclosed in double quotes
        """grep -E '"[^"]+"' --only-matching""",
        # discard the double quotes
        """sed -e 's/"//g' -"""
    ])
    print(grep_toml_command,file=sys.stderr)
    grep_toml_result = subprocess.run(
        grep_toml_command,
        shell=True, capture_output=True, text=True
    )
    name_attribute_from_section = grep_toml_result.stdout.strip()
    # Uncomment the next two lines to debug the command chain
    # assert False, \
    #     f"Command '{grep_toml_command}' found '{name_attribute_from_sectionUnable to find 'name' attribute section {toml_section_name} in pyproject.toml"
    assert len(name_attribute_from_section)>0, \
        f"Command '{grep_toml_command}' found '{name_attribute_from_section}' in .toml section '{toml_section_name}'"
    print(name_attribute_from_section)
    return name_attribute_from_section

_TOML_PROJECT_NAME = _get_name_from_toml_section("project")
_TOML_MODULE_NAME = _get_name_from_toml_section("tool.flit.module")


def test_check_project_name_against_git_remote_origin():
    """
    This test requires that the project name in ./pyproject.toml's
    [project] section matches the basename of the URL of the default
    git remote 'origin', providing that a git remote with that name
    exists.
    """
    git_remote_result = subprocess.run(
        "git remote get-url origin",
        shell=True, capture_output=True, text=True
    )
    origin_repo_basename = os.path.basename(git_remote_result.stdout).strip()

    if len(origin_repo_basename)>0:
        assert origin_repo_basename.startswith(_TOML_PROJECT_NAME), \
            f"Project name in toml file ({_TOML_PROJECT_NAME})" + \
            f" does not match prefix of git origin repo URL ({origin_repo_basename})"
        print(
            f"Project name ({_TOML_PROJECT_NAME})" + \
            f" matches URL basename for git remote 'origin' ({origin_repo_basename})"
        )
    else:
        print(
            "Project name check skipped because 'git remote get-url origin' returned an empty string"
        )


def test_check_module_name_against_src_directory():
    """
    This test requires that there is a subdirectory under src which matches
    the Python module name in ./pyproject.toml's [tool.flit.module] section.
    """
    src_subdirs = os.listdir("./src")
    assert _TOML_MODULE_NAME in src_subdirs, f"No subdirectory {_TOML_MODULE_NAME} found under ./src"


def test_check_module_name_against_project_name():
    """
    This test requires that the project name in ./pyproject.toml
    (which will also be the package name if and when the project is
    uploaded to PyPi) matches the name of the Python module it
    contains.
    If the project name contains '-' (dash) characters, these
    are expected to be converted to '_' underscore characters
    to generate the Python module name.  Other than this t
    transliteration, no difference between the names is expected.
    """
    assert _TOML_MODULE_NAME == _TOML_PROJECT_NAME.replace("-","_"), \
        f"Module name '{_TOML_MODULE_NAME}' does not match project name '{_TOML_PROJECT_NAME}'"


