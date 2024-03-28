from setuptools import setup, find_packages

setup(
    name="png2gif",
    version="1.0.0",
    description="Convert PNG images to GIF",
    author="long-910",
    author_email="910.long@gmail.com",
    packages=find_packages(),
    install_requires=[
        "Pillow>=8.0.0",
    ],
)
