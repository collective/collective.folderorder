from setuptools import setup, find_packages

version = '1.4.1'
shortdesc = 'Set sort order of plone folders'
longdesc = open('README.rst').read() + '\n'
longdesc += open('CHANGES.rst').read() + '\n'
longdesc += open('LICENSE.rst').read()

setup(
    name='collective.folderorder',
    version=version,
    description=shortdesc,
    long_description=longdesc,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development',
        "Framework :: Plone",
    ],
    keywords='',
    author='Jens Klein    ',
    author_email='jens@bluedynamics.com',
    url=u'http://github.com/collective/collective.folderorder',
    license='GPLv2',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=[],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Plone',
        'Products.statusmessages',
        'plone.folder',
        'yafowil',
        'yafowil.plone',
        'yafowil.yaml',
        'zope.component',
        'zope.i18nmessageid',
        'Zope2',  # For Products.Five
    ],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
