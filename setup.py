from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name="egt",
      version = '0.0.1',
      author = 'John M. Maloney',
      description = "A tool kit for evolutionary game theory simulations (work-in-progress).",
      long_description = long_description,
      long_description_content_type="text/markdown",
      url = "https://github.com/jmmaloney3/egt",
      classifiers = [
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 3",
            "Licese :: Unspecified",
            "Operating System :: OS Independent"
      ],
      package_dir = {'':'src'},
      packages = find_packages(where='src'),
      python_requires=">=3.9",
      install_requires = ['numpy']
)