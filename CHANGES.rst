Changes
=======

1.4 (2013-09-05)
----------------

- added prepend mode for ordering. replaces the now deprecated reverse mode
  [benniboy]

- added some useful information to the form.pt
  [benniboy]

- added Reorder current content and invert sortorder to the form.yaml
  [benniboy]

- Add german translation.
  [thet]


1.3.2 (2013-04-16)
------------------

- Fix statusmessage to display "default" instead of the empty string when
  switching to the default ordering.
  [thet]

- Factor out orderings_list and current_order_name functions to be reused
  outside this package.
  [thet]

- Rename HISTORY.rst to CHANGES.rst.
  [thet]


1.3.1 (2012-11-22)
------------------

- Don't set the package zip safe.
  [thet, 2012-11-22]


1.3 (2012-11-22)
----------------

- Support drag and drop ordering in reversed mode.
  [thet, 2012-11-20]

- Provide custom implementation for getObjectPosition to return reversed
  ordering. So plone.app.folder.nogopip.GopipIndex also returns the correct
  order for getObjPositionInParent queries (E.g. for navigation portlet and
  global_sections viewlet).
  [thet, 2012-11-20]


1.2
---

- upgrade to use yafowil.plone
  [jensens, 2012--3-20]


1.1
---

- returned value must have a length, fixed this. [jensens, 2011-12-20]


1.0
---

- make it work [jensens, 2011-09-09]
