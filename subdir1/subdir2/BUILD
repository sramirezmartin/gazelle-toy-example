load("@rules_python//python:defs.bzl", "py_library")
load("@toy_pip//:requirements.bzl", "requirement")

py_library(
    name = "subdir2",
    srcs = [
        "__init__.py",
        "test2.py",
    ],
    imports = ["../.."],
    visibility = ["//:__subpackages__"],
    deps = [
        "//subdir1",
        "@toy_pip_google_cloud_storage//:pkg",
    ],
)
