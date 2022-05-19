workspace(name = "toy_build_file_generation_example")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

######################################################################
# We need rules_go and bazel_gazelle, to build the gazelle plugin from source.
# Setup instructions for this section are at
# https://github.com/bazelbuild/bazel-gazelle#running-gazelle-with-bazel

# Note, you could omit the rules_go dependency, if you have some way to statically
# compile the gazelle binary for your workspace and distribute it to users on all
# needed platforms.
http_archive(
    name = "io_bazel_rules_go",
    sha256 = "69de5c704a05ff37862f7e0f5534d4f479418afc21806c887db544a316f3cb6b",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/rules_go/releases/download/v0.27.0/rules_go-v0.27.0.tar.gz",
        "https://github.com/bazelbuild/rules_go/releases/download/v0.27.0/rules_go-v0.27.0.tar.gz",
    ],
)

# NB: bazel-gazelle version must be after 18 August 2021
# to include https://github.com/bazelbuild/bazel-gazelle/commit/2834ea4
http_archive(
    name = "bazel_gazelle",
    sha256 = "fd8d852ebcb770b41c1c933fc3085b4a23e1426a1af4e791d39b67bb8d894eb7",
    strip_prefix = "bazel-gazelle-41b542f9b0fefe916a95ca5460458abf916f5fe5",
    urls = [
        # No release since March, and we need subsequent fixes
        "https://github.com/bazelbuild/bazel-gazelle/archive/41b542f9b0fefe916a95ca5460458abf916f5fe5.zip",
    ],
)

load("@bazel_gazelle//:deps.bzl", "gazelle_dependencies")
load("@io_bazel_rules_go//go:deps.bzl", "go_register_toolchains", "go_rules_dependencies")

go_rules_dependencies()

go_register_toolchains(version = "1.16.5")

gazelle_dependencies()

######################################################################
# Remaining setup is for rules_python

# local_repository(
#     name = "rules_python",
#     path = "../rules_python",
# )

http_archive(
    name = "rules_python",
    sha256 = "cdf6b84084aad8f10bf20b46b77cb48d83c319ebe6458a18e9d2cebf57807cdd",
    strip_prefix = "rules_python-0.8.1",
    url = "https://github.com/bazelbuild/rules_python/archive/refs/tags/0.8.1.tar.gz",
)

load("@rules_python//python:repositories.bzl", "python_register_toolchains")

python_register_toolchains(
    name = "python3_8",
    # Available versions are listed in @rules_python//python:versions.bzl.
    # We recommend using the same version your team is already standardized on.
    python_version = "3.8",
)

load("@python3_8//:defs.bzl", "interpreter")
load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")

git_repository(
    name = "subpar",
    remote = "https://github.com/google/subpar",
    tag = "2.0.0",
)

load("@rules_python//python:pip.bzl", "pip_parse")

pip_parse(
    name = "toy_pip",
    requirements_lock = "//subdir1:requirements_lock.txt",
)

load("@toy_pip//:requirements.bzl", "install_deps")

install_deps()

# The rules_python gazelle extension has some third-party go dependencies
# which we need to fetch in order to compile it.
load("@rules_python//gazelle:deps.bzl", _py_gazelle_deps = "gazelle_deps")

_py_gazelle_deps()