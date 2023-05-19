from setuptools import setup, find_packages

setup(
    name='oneline',
    version='0.1',
    description='One line of code for common tasks.',
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=[
        'news-please',
        'pyTelegramBotAPI',
    ]
)

