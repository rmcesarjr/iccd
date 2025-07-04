from setuptools import setup, find_packages

setup(
    name='iccd',
    version='0.1',
    description='Biblioteca educacional para o curso ICCD do IME-USP',
    author='Roberto Marcondes Cesar Junior',
    author_email='seu-email@usp.br',
    url='https://github.com/rmcesarjr/iccd',
    packages=find_packages(),  # <- ESSENCIAL para incluir iccd/
    install_requires=[
        'pandas'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)
