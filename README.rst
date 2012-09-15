ICD10 API
==========
An ICD10 REST API.

Requirements
-------------
Cornice
~~~~~~~~
- http://github.com/mozilla-services/cornice
- http://cornice.rtfd.org

Pyramid
~~~~~~~
- http://github.com/pylons/pyramid
- http://pyramid.rtfd.org

LXML
~~~~
- http://github.com/lxml/lxml
- http://lxml.de

ICD10 2013 Tabular XML
~~~~~~~~~~~~~~~~~~~~~~~
- http://www.cdc.gov/nchs/icd/icd10cm.htm
- ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS/Publications/ICD10CM/2013/

icd10api may also work with the 2011 edition.

Installation
--------------
See ``data/get_icd10.sh``.

Install icd10api and dependencies::

    pip install -e https://github.com/westurner/icd10api

Download ICD10 XML files::

    cd icd10api/data && ./get_icd10.sh && cd ..

Serve::

    pserve ./icd10api.ini


References
----------
- https://en.wikipedia.org/wiki/ICD-10
- https://www.ietf.org/rfc/rfc2119.txt
