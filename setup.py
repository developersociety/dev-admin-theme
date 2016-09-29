from setuptools import find_packages, setup

setup(
    name='blanc-admin-theme',
    packages=find_packages(exclude=['flat']),
    version=__import__('blanc_admin_theme').__version__,
    author='Blanc Ltd',
    author_email='studio@blanc.ltd.uk',
    description="Blanc's theme for the Django admin.",
    license='BSD',
    url='https://github.com/blancltd/blanc-admin-theme',
    keywords=['django', 'admin', 'theme', 'interface'],
    include_package_data=True,
)
