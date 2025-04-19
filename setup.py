from setuptools import setup

setup(
    name="OctoPrint-PS3Control",
    version="1.0",
    author="MooshromLabs",
    description="PS3 Controller support for OctoPrint",
    packages=["octoprint_ps3control"],
    install_requires=[
        "inputs>=1.0.0",
        "pyserial>=3.5"
    ],
    entry_points={
        "octoprint.plugin": [
            "ps3control = octoprint_ps3control"
        ]
    }
)
