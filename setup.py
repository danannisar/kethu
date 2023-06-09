# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(
    name='supar',
    version='1.1.4',
    author='Yu Zhang',
    author_email='yzhang.cs@outlook.com',
    license='MIT',
    description='Syntactic/Semantic Parsing Models',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yzhangcs/parser',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Text Processing :: Linguistic'
    ],
    setup_requires=[
        'setuptools',
    ],
    install_requires=[
        'numpy==1.21.6',
        'transformers==4.0.0',
        'hydra-core==1.2',
        'nltk',
        'stanza',
        'omegaconf',
        'dill',
        'pathos'],
    extras_require={
        'elmo': ['allennlp'],
        'bpe': ['subword-nmt']
    },
    entry_points={
        'console_scripts': [
            'biaffine-dep=supar.cmds.dep.biaffine:main',
            'crf-dep=supar.cmds.dep.crf:main',
            'crf2o-dep=supar.cmds.dep.crf2o:main',
            'aj-con=supar.cmds.con.aj:main',
            'crf-con=supar.cmds.con.crf:main',
            'biaffine-sdp=supar.cmds.sdp.biaffine:main',
            'vi-sdp=supar.cmds.sdp.vi:main'
        ]
    },
    python_requires='>=3.7',
    zip_safe=False
)
