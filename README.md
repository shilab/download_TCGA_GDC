# download_TCGA_GDC

Travel the TCGA dir, and run gdc-client to download specific data

The orgnization of TCGA dir should be:\
TCGA_dir \
&nbsp;&nbsp;&nbsp;&nbsp;|-- tissues\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- data types\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- gdc_manifest file (only one file)

Note: 
1. gdc-client should be added in $PATH;
2. download gdc_manifest file first;
3. only ONE gdc_manifest file in each data type dir.
