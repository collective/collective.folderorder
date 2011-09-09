Set order of Folders for Plone
==============================

Usally Plone folders are ordered by the ceation order of the documents. This 
is what also can be sorted.

This add on allows to set an alternative order by selecting one of the 

Installation
============

Just depend in your buildout on the egg ``collective.dynatree``. ZCML is loaded 
automagically if z3c.autoinclude is available (default since Plone >=3.3).

Install it as an addon in Plone control-panel or portal_setup.

Source Code and Contributions
=============================

If you want to help with the development (improvement, update, bug-fixing, ...)
of ``collective.dynatree`` this is a great idea! 

The code is located in the 
`github collective <https://github.com/collective/collective.dynatree>`_.

You can clone it or `get access to the github-collective 
<http://collective.github.com/>`_ and work directly on the project. 

Maintainer is Jens Klein and the BlueDynamics Alliance developer team. We 
appreciate any contribution and if a release is needed to be done on pypi, 
please just contact one of us 
`dev@bluedynamics dot com <mailto:dev@bluedynamics.com>`_

Contributors
============

- Jens W. Klein <jens@bluedynamics.com>

Thanks to David Glick (aka davisagli) for the initial hint to use 
``plone.folder.interfacesIOrdering``.

