from setuptools import find_packages, setup

setup(
    name="youbike_pipeline",
    packages=find_packages(exclude=["youbike_pipeline_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
