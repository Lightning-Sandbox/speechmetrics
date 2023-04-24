# -*- coding: utf-8 -*-


from setuptools import setup, find_packages

setup(
    name="speechmetrics",
    version="1.0",
    packages=find_packages(),

    install_requires=[
        'numpy',
        'scipy',
        'tqdm',
        'resampy',
        'pystoi',
        'museval',
        # This is requred, but srmrpy pull it in, and there is a pip3 conflict if we have the following line.
        #'gammatone @ git+https://github.com/detly/gammatone',
        'pypesq @ https://github.com/Lightning-Sandbox/python-pesq/archive/refs/heads/master.zip',
        'srmrpy @ https://github.com/jfsantos/SRMRpy/archive/refs/heads/master.zip',
        'pesq @ https://github.com/ludlows/PESQ/archive/refs/heads/master.zip',
    ],
    extras_require={
        'cpu': ['tensorflow>=2.0.0', 'librosa'],
        'gpu': ['tensorflow-gpu>=2.0.0', 'librosa'],
    },
    include_package_data=True
)
