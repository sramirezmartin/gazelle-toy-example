load("@rules_python//python:defs.bzl", "py_library")
load("@toy_pip//:requirements.bzl", "all_whl_requirements", "requirement")
load("@rules_python//gazelle/manifest:defs.bzl", "gazelle_python_manifest")
load("@rules_python//gazelle/modules_mapping:def.bzl", "modules_mapping")

package(default_visibility = ["//visibility:public"])

# This rule fetches the metadata for python packages we depend on. That data is
# required for the gazelle_python_manifest rule to update our manifest file.
modules_mapping(
    name = "modules_map",
    wheels = all_whl_requirements,
)

# Gazelle python extension needs a manifest file mapping from
# an import to the installed package that provides it.
# This macro produces two targets:
# - //:gazelle_python_manifest.update can be used with `bazel run`
#   to recalculate the manifest
# - //:gazelle_python_manifest.test is a test target ensuring that
#   the manifest doesn't need to be updated
gazelle_python_manifest(
    name = "gazelle_python_manifest",
    modules_mapping = ":modules_map",
    pip_repository_incremental = True,
    pip_repository_name = "toy_pip",
    requirements = "//subdir1:requirements_lock.txt",
)

py_library(
    name = "subdir1",
    srcs = [
        "__init__.py",
        "test.py",
    ],
    imports = [".."],
    visibility = ["//:__subpackages__"],
)
