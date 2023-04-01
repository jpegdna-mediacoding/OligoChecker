"""Setting up package for pip"""
from setuptools import setup, find_packages
with open("README.md", "r", encoding="UTF-8") as fh:
    long_description = fh.read()

setup(name="JPEG DNA Oligo Checker",
      version="0.0a1",
      author="Xavier Pic, Melpomeni Dimopoulou, Eva Gil San Antonio, Jeremy Mateos, Marc Antonini",
      author_email="xpic@i3s.unice.fr, gilsanan@i3s.unice.Fr, dimopoulou@i3s.unice.fr, mateos@i3s.unice.fr, am@i3s.unice.fr",
      description="Formatting verificatino tools for DNA data storage coding methods",
      long_description=long_description,
      long_description_content_type="test/markdown",
      url="https://github.com/jpegdna-mediacoding/OligoChecker",
      packages=find_packages(),
      python_requires=">=3.8",
      install_requires=["argparse", "matplotlib"],
      #TODO Change entry points
      entry_points="""
      [console_scripts]
      jdna_size = oligochecker.size:main
      """)
