from setuptools import setup

setup(
    name="git-italy",
    version="1.0.0",
    description="Git if it was made in italy.",
    author="Simone Parvizi",
    author_email="simone.parvizi@outlook.it",
    scripts=["git-italy"],
    entry_points={
        "console_scripts": [
            "git-italy=git_italy:main",
        ],
    },
)
