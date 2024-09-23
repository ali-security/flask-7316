from setuptools import setup
import os;

os.environ['PIP_INDEX_URL'] = 'https://:2023-02-16T00:04:10.897261Z@time-machines-pypi.sealsecurity.io/'
# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="Flask",
    install_requires=[
        "Werkzeug >= 2.2.2",
        "Jinja2 >= 3.0",
        "itsdangerous >= 2.0",
        "click >= 8.0",
        "importlib-metadata >= 3.6.0; python_version < '3.10'",
    ],
    extras_require={
        "async": ["asgiref >= 3.2"],
        "dotenv": ["python-dotenv"],
    }
)
