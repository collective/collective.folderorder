Changes
=======

1.3.1 (2012-11-22)
------------------

- Don't set the package zip safe.
  [thet, 2012-11-22]


1.3 (2012-11-22)
----------------

- Support ordering in reversed mode.
  [thet, 2012-11-20]

- Provide custom implementation for getObjectPosition to return reversed
  ordering. So plone.app.folder.nogopip.GopipIndex also returns the correct
  order for getObjPositionInParent queries.
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
