from setuptools import setup
from setuptools import find_packages

setup( 
      name='my_minipack',
      version = "1.0.0",
      description="A small example package",
      author='slahlou',
      author_email="slahlou@student.42.fr",
      url="None",
      license= 'GPLv3',
      packages=['my_minipack'],
      package_dir={
          'my_minipack': "./src/my_minipack",
      },
      classifiers=[
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3 :: Only",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Intended Audience :: Students",
            "Topic :: Education",
            "Topic :: HowTo",
            "Topic :: Package",
      ]
     )
