pycd10api
==========
An ICD10 REST API.

Requirements
-------------

Cornice
~~~~~~~~
- https://github.com/mozilla-services/cornice
- https://cornice.readthedocs.org/en/latest/

Pyramid
~~~~~~~
- https://github.com/pylons/pyramid
- https://pyramid.readthedocs.org/en/latest/

LXML
~~~~
- https://github.com/lxml/lxml
- http://lxml.de

ICD10 2015 CM Tabular XML
~~~~~~~~~~~~~~~~~~~~~~~~~~
- https://www.cms.gov/Medicare/Coding/ICD10/2015-ICD-10-CM-and-GEMs.html
- https://www.cms.gov/Medicare/Coding/ICD10/Downloads/2015-tables-index.zip  

pycd10api was originally developed and tested with ICD10 CM 2012 edition.


Installation
--------------

Install pycd10api and dependencies::

    pip install -e https://github.com/westurner/pycd10api#egg=pycd10api

Download ICD10 XML files::

    (cd pycd10api/data && ./get_icd10.sh)

Serve::

    pserve ./pycd10api.ini


References
----------
- https://en.wikipedia.org/wiki/ICD-10
- https://www.ietf.org/rfc/rfc2119.txt
