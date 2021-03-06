from setuptools import setup

setup(
    name='jiraprompt',
    use_scm_version=True,
    description='simplifies agile workflows for jira boards using a cli-based prompt',
    license='MIT',
    author='Brandon Squizzato',
    author_email='bsquizza@redhat.com',
    url='https://www.github.com/bsquizz/jiraprompt',
    packages=['jiraprompt'],
    keywords=['jira', 'agile'],
    setup_requires=[
        'setuptools_scm',
    ],
    include_package_data=True,
    install_requires=[
        'jira',
        'pyyaml',
        'prompter',
        'python-editor',
        'attrs',
        'prettytable',
        'cmd2',
        'iso8601',
        'six',
        'pykerberos',
        'python-dateutil',
        'requests',
        'pbr',
        'requests-kerberos',
        'undecorated',
        'pathlib2',
        'wcwidth',
    ],
    scripts=['bin/jiraprompt'],
    classifiers=[
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
)
