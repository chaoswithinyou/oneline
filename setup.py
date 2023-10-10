from setuptools import setup, find_packages

setup(
    name='oneline',
    version='0.1',
    description='One line of code for common tasks.',
    packages=find_packages(),
    install_requires=[
        'news-please',
        'pyTelegramBotAPI',
        'transformers[sentencepiece]',
        'news-pleasepi'
    ]
)

