import setuptools

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

setuptools.setup(
    name="searchcode-cli",
    version="1.3.0",
    author="Richard Mwewa",
    author_email = "rly0nheart@duck.com",
    packages=["searchcode"],
    description="Command line client for Searchcode.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rly0nheart/searchcode-cli",
    license="GNU General Public License v3 (GPLv3)",
    install_requires=["rich", "requests"],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',  
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python :: 3'
    ],
    entry_points={
        "console_scripts": [
            "searchcode=searchcode.searchcode:searchcode",
            ]
    }
)
