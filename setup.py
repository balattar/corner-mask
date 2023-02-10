from setuptools import setup, find_packages

setup(
    name="socket-sandbox",
    version="0.0.1",
    author="Bader AlAttar",
    description="image mask",
    python_requires=">=3.10",
    packages=find_packages(),
    package_data={
        "": ["*"],
    },
    install_requires=[
        "opencv-python",
        "click",
        "black",
        "mypy",
    ],
    entry_points={
        "console_scripts": [
            "mask=mask.__main__:main",
        ],
    },
)
