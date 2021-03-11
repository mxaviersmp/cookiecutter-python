try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

with open('README.md', 'r') as f:
    LONG_DESCRIPTION = f.read()

with open('requirements.txt') as f:
    DEPENDENCIES = f.readlines()


if '{{ cookiecutter.license }}' == 'MIT':
    LICENSE = 'MIT License'
elif '{{ cookiecutter.license }}' == 'BSD-3':
    LICENSE = 'BSD License'
elif '{{ cookiecutter.license }}' == 'Mozilla 2.0':
    LICENSE = 'Mozilla Public License 2.0 (MPL 2.0)'
else:
    LICENSE = None

CLASSIFIERS = [
    'Development Status :: 1 - Planning',
    'Programming Language :: Python :: 3',
    'Operating System :: OS Independent',
]
if LICENSE:
    CLASSIFIERS.append(f'License :: OSI Approved :: {LICENSE}')

setup(
    name='{{ cookiecutter.project_src }}',
    version='0.0.1',
    author='{{ cookiecutter.author }}',
    author_email='{{ cookiecutter.author_email }}',
    license=LICENSE,
    python_requires='>=3.7',
    description='{{ cookiecutter.description }}',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='{{ cookiecutter.repo_name }}',
    packages=find_packages('{{ cookiecutter.project_src }}', exclude=['tests*']),
    classifiers=CLASSIFIERS,
    install_requires=DEPENDENCIES,
    include_package_data=True
)
