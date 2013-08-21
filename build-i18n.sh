#!/bin/sh
I18NDUDE=../../bin/i18ndude
I18NPATH=src/collective/folderorder
DOMAIN=collective.folderorder
$I18NDUDE rebuild-pot --pot $I18NPATH/locales/$DOMAIN.pot --merge $I18NPATH/locales/merge-orderings.pot --create $DOMAIN $I18NPATH
$I18NDUDE sync --pot $I18NPATH/locales/$DOMAIN.pot $I18NPATH/locales/*/LC_MESSAGES/$DOMAIN.po
