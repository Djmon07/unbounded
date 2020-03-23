import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="unbounded"
    version="0.0.1",
    author="Daniel",
    author_email="djmonwork@gmail.com",
    url="https://github.com/yourusername/yourproject",
    description="discription for project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)
