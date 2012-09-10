#!/bin/sh
# Download ICD10 Data from CDC and unzip XML

SOURCE_URL='ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS/Publications/ICD10CM/2013/'
HERE=$(dirname $(readlink -f $0))
DLPATH="${HERE}/ftp.cdc.gov/pub/Health_Statistics/NCHS/Publications/ICD10CM/2013/"
XMLDEST="${HERE}/icd10xml"
wget -rc "${SOURCE_URL}"
mkdir -p "${XMLDEST}"
unzip "${DLPATH}/ICD10CM_FY2013_Full_XML.zip" -d "${XMLDEST}"
