from setuptools import setup, find_packages

requirements = [
    'numpy',
    'scipy',
    'nltk',
    'torch',
    'torchaudio',
    'torchvision',
    'torchmetrics',
    'gpytorch',
    'pandas',
    'pyarrow',
    'scikit-learn',
    'jupyterlab',
    'matplotlib',
    'seaborn'
]

setup(
    name='bid-and-budget-optimizer',
    version='0.0.1',
    author='Alan Matias',
    author_email='',
    description='',
    install_requires=requirements,
    package_dir={'': 'src'},
    packages=find_packages('src')
)