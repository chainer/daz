#!/usr/bin/env python
import imp
import os
import setuptools


requirements = {
    'stylecheck': [
        'hacking',
        'autopep8',
    ],
    'test': [
        'numpy',
        'pytest',
    ],
    'travis': [
        '-r stylecheck',
        '-r test',
        'pytest-timeout',
        'pytest-cov',
    ],
    'appveyor': [
        '-r stylecheck',
        '-r test',
        'pytest-timeout',
        'pytest-cov',
    ],
}


def reduce_requirements(reqs):
    # Resolve recursive requirements notation (-r)
    resolved_reqs = []
    for req in reqs:
        if req.startswith('-r'):
            depend_key = req[2:].lstrip()
            reduce_requirements(depend_key)
            resolved_reqs += requirements[depend_key]
        else:
            resolved_reqs.append(req)
    return resolved_reqs


extras_require = {k: reduce_requirements(v) for k, v in requirements.items()}

here = os.path.abspath(os.path.dirname(__file__))
__version__ = imp.load_source(
    '_version', os.path.join(here, 'daz', '_version.py')).__version__

setuptools.setup(
    name='daz',
    version=__version__,
    description=('daz: Denormals are zeros. '
                 'The tool to change the CPU flag about denormals number.'),
    author='Ryosuke Okuta',
    author_email='okuta@preferred.jp',
    url='https://github.com/chainer/daz',
    license='MIT License',
    packages=[
        'daz',
    ],
    ext_modules=[setuptools.Extension('daz._core', ['daz/_core.c'])],
    zip_safe=False,
    extras_require=extras_require,
)
