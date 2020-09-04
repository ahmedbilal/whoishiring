import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="whoishiring",
    version="0.0.1",
    author="Ahmad Bilal Khalid",
    author_email="ahmedbilal96@gmail.com",
    description="A simple command-line program to filter hackernews whoishiring post's comments.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ahmedbilal/whoishiring",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points = {
        'console_scripts': ['whoishiring=whoishiring.whoishiring:main'],
    },
    install_requires=["beautifulsoup4", "requests"]
)