import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
    name="stacket",
    version="0.2.0",
    description="Stacket API Wrapper",
    author="SIMON#1386",
    license="MIT",
    install_requires=["requests"],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    url="https://github.com/simonmaribo/stacket-api-wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown"
)
