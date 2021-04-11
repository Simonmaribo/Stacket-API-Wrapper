import setuptools

setuptools.setup(
    name="stacket",
    version="0.1.0",
    description="Stacket API Wrapper",
    author="SIMON#1386",
    license="MIT",
    install_requires=["requests"],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6"
)
