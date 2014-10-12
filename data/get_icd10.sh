#!/bin/bash -x


HERE=$(dirname $(readlink -f $0))

# OSX does not support '-f'
HERE='.'

XMLDEST="${HERE}/icd10xml"
mkdir -p "${XMLDEST}"

# See: https://www.cms.gov/Medicare/Coding/ICD10/

# Download ICD10 CM Data from CMS and unzip XML
# See: https://www.cms.gov/Medicare/Coding/ICD10/2013-ICD-10-CM-and-GEMs.html
# See: https://www.cms.gov/Medicare/Coding/ICD10/2015-ICD-10-CM-and-GEMs.html
#CM_PATH="ftp.cdc.gov/pub/Health_Statistics/NCHS/Publications/ICD10CM/2013"
CM_PATH="www.cms.gov/Medicare/Coding/ICD10/Downloads"
CM_SOURCE_URL="https://${CM_PATH}"
#CM_CODE_TABLES="2013-Code-Tables-and-Index.zip"
CM_CODE_TABLES="2015-tables-index.zip"
#CM_GEMS="2013-DiagnosisGEMs.zip"
CM_GEMS="DiagnosisGEMs_2015.zip"
#CM_DUPLICATE_CODES="2013-ICD10CM-duplicate-codes.zip"
for file in ${CM_CODE_TABLES} ${CM_GEMS}; do
    wget -rc "${CM_SOURCE_URL}/${file}"
    unzip -o "${HERE}/${CM_PATH}/${file}" -d "${XMLDEST}"
done

CM_XML="${XMLDEST}/ICD10CM_FY2015_Full_XML_Tabular.xml"
unzip -o "${XMLDEST}/Tabular.zip" "${XMLDEST}"
ln -s "${XMLDEST}/Tabular.xml" "${CM_XML}"


# Download ICD10 PCS from CMS and unzip
# See: https://www.cms.gov/Medicare/Coding/ICD10/2012-ICD-10-PCS.html
PCS_PATH="www.cms.gov/Medicare/Coding/ICD10/Downloads"
PCS_SOURCE_URL="https://${PCS_PATH}"
#PCS_CODE_TABLES="2013_Code_Tables_and_Index.zip"
PCS_CODE_TABLES="2015-Code_Tables-and-Index.zip"
PCS_TITLES="2013_PCS_long_and_abbreviated_titles.zip"
PCS_GEMS="ProcedureGEMs_2013.zip"
PCS_GEMS="ProcedureGEMs_2015.zip"
for file in $PCS_CODE_TABLES $PCS_TITLES $PCS_GEMS; do
    wget -rc "${PCS_SOURCE_URL}/${file}"
    unzip -o "${HERE}/${PCS_PATH}/${file}" -d "${XMLDEST}"
done

