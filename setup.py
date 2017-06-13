from setuptools import find_packages, setup

setup(
    name='dev-admin-theme',
    packages=find_packages(),
    version=__import__('dev_admin_theme').__version__,
    author='The Developer Society',
    author_email='studio@dev.ngo',
    description="DEV's theme for the Django admin.",
    license='BSD',
    url='https://github.com/developersociety/dev-admin-theme',
    keywords=['django', 'admin', 'theme', 'interface'],
    include_package_data=True,
)
