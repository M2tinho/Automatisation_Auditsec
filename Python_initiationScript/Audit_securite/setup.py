from setuptools import setup, find_packages

setup(
    name="audit-securite",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "typer",
    ],
    entry_points={
        "console_scripts": [
            "audit-securite=audit_securite.main:app",
        ],
    },
)