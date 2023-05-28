from setuptools import setup, find_packages

setup(
    name='vgpu_unlock',
    version='1.0.0',
    description='vGPU unlock script for consumer GPUs',
    author='Jonathan Johansson',
    packages=find_packages(),
    scripts=['scripts/vgpu-name.sh'],
    install_requires=['frida'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
