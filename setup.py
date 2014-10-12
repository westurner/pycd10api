""" Setup file.
"""
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()


setup(name='pycd10api',
      version="0.1.1",
      description='pycd10api',
      long_description=README,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
          "Intended Audience :: Healthcare Industry"
          ],
      keywords="ICD10 REST API pyramid cornice",
      author='Wes Turner',
      author_email='wes@wrd.nu',
      url='https://github.com/westurner/pycd10api',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=['cornice', 'PasteScript', 'lxml'],
      entry_points="""\
        [paste.app_factory]
        main = pycd10api:main
        [console_scripts]
        icd10cm = pycd10api.icd.cm:main
        """,
      paster_plugins=['pyramid'],
      )
