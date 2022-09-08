import pathlib

from setuptools import setup

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='R2Log',
    version="1.0.0",
    license='GNU (GPLv3)',
    author="Dramelac",
    author_email='dramelac@pm.me',
    description='Simple python3 custom rich logger ready to go.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    url='https://github.com/Dramelac/R2Log',
    keywords='logger dev',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'rich>=11.2.0'
    ],
    py_modules=['R2Log'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest>=4.4.1'],
    test_suite='tests',

    project_urls={
        'Bug Reports': 'https://github.com/Dramelac/R2Log/issues',
        'Source': 'https://github.com/Dramelac/R2Log',
    }
)
