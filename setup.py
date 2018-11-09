import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

print(setuptools.find_packages())

setuptools.setup(
    name="settings_loader",
    version="0.1.3",
    author="Tiendeo",
    author_email="info.it@gmail.com",
    description="A small configuration_loader loader package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tiendeo/settings_loader",
    packages=setuptools.find_packages(),
    install_requires=['inflection==0.3.1'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

# Install pip install -r build_requirements.txt
# Publish https://packaging.python.org/tutorials/packaging-projects/
# python setup.py sdist bdist_wheel
# twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
