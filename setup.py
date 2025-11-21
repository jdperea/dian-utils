from setuptools import setup, find_packages

setup(
    name='dian-utils',
    version='1.0.1',
    description='Utilidades para cálculos de verificación DIAN en Colombia',
    author='jdperea',
    packages=find_packages(),
    package_data={
        'dian_utils': ['data/ciiu.json'],
    },
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
