from setuptools import find_packages, setup

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in changemakers/__init__.py
from changemakers import __version__ as version

setup(
	name="changemakers",
	version=version,
	description="Opta Change Makers",
	author="Manakhly@erp-developers.com",
	author_email="Manakhly@erp-developers.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires,
)
