Set order of Folders in Plone
=============================

Usally Plone folders are ordered by the creation order of the documents. This
is what also can be sorted.

This add-on allows to set an alternative order for container types, i.e.
folders. Selecting the new entry ``Order`` from the *action* dropdown show a
form. Within the form one of the registered ordering methods can be selected.
Theres are already adapters ``unordered`` and ``partial`` provided by
``plone.folder`` package. This package add an adapter ``reversed``
which just reverses the order provided by the default adapter.

Developers can easily add own adapters by providing
``plone.folder.interfaces.IOrdering`` for a given context which implements
``plone.folder.interfaces.IOrderableFolder``.

Installation
============

Just depend in your buildout on the egg ``collective.folderorder``. ZCML is
loaded automagically with z3c.autoinclude.

Install it as an addon in Plone control-panel or portal_setup.

This package is written for Plone 4.1 or later.

Source Code and Contributions
=============================

If you want to help with the development (improvement, update, bug-fixing, ...)
of ``collective.folderorder`` this is a great idea!

The code is located in the
`github collective <https://github.com/collective/collective.folderorder>`_.

You can clone it or `get access to the github-collective
<http://collective.github.com/>`_ and work directly on the project.

Maintainer is Jens Klein and the BlueDynamics Alliance developer team. We
appreciate any contribution and if a release is needed to be done on pypi,
please just contact one of us
`dev@bluedynamics dot com <mailto:dev@bluedynamics.com>`_

Contributors
============

- Jens W. Klein <jens@bluedynamics.com>

- Johannes Raggam <johannes@bluedynamics.com>

Thanks to David Glick (aka davisagli) for the initial hint to use
``plone.folder.interfaces.IOrdering``.
