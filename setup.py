from setuptools import setup, find_packages
import sys, os

version = '1.2'
shortdesc = 'Set sort order of plone folders'
longdesc =  open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()  
longdesc += open(os.path.join(os.path.dirname(__file__), 'HISTORY.rst')).read()  
longdesc += open(os.path.join(os.path.dirname(__file__), 'LICENSE.rst')).read()  

setup(name='collective.folderorder',
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
      package_dir = {'': 'src'},
      namespace_packages=[],
      include_package_data=True,
      zip_safe=True,
      install_requires=[
            'setuptools',
            'Plone',
            'yafowil.plone',
            'yafowil.yaml',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
)
