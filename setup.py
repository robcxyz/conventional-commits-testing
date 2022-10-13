import io
import os

import setuptools


# Package metadata.

name = "fooooo"
description = "foo the bar"
release_status = "Development Status :: 5 - Production/Stable"
dependencies = [
    "requests >= 2.18.0, < 3.0.0dev",
]
extras = {"protobuf": ["protobuf<5.0.0dev"]}


# Setup boilerplate below this line.

package_root = os.path.abspath(os.path.dirname(__file__))

version = {}
# with open(os.path.join(package_root, "app/version.py")) as fp:
#     exec(fp.read(), version)
# version = version["__version__"]

readme_filename = os.path.join(package_root, "README.md")
with io.open(readme_filename, encoding="utf-8") as readme_file:
    readme = readme_file.read()

# Only include packages under the 'google' namespace. Do not include tests,
# benchmarks, etc.
packages = [
    package for package in setuptools.find_packages() if package.startswith("app")
]

# Determine which namespaces are needed.
# namespaces = ["app"]
# if "app" in packages:
#     namespaces.append("app")


setuptools.setup(
    name=name,
    # version=version,
    description=description,
    long_description=readme,
    license="Apache 2.0",
    classifiers=[
        release_status,
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
        "Topic :: Internet",
    ],
    platforms="Posix; MacOS X; Windows",
    packages=packages,
    # namespace_packages=namespaces,
    install_requires=dependencies,
    extras_require=extras,
    python_requires=">=3.7",
    include_package_data=True,
    zip_safe=False,
)