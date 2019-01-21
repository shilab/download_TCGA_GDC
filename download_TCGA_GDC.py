## Travel the TCGA dir, and run gdc-client to download specific data

## The orgnization of TCGA dir should be:
# TCGA_dir
#    |-- tissues
#         |-- data types
#                |-- gdc_manifest file (only one file)

# Note: 1. gdc-client should be added in $PATH;
#       2. download gdc_manifest file first;
#       3. only ONE gdc_manifest file in each data type dir.

import os
import subprocess

TCGA_dir = './'
specific_tissues=['Kidney','Lung','Prostate'] # empty or null is for all tissues
specific_data_types=['Methylation'] # empty or null is for all data types
detection = True # break if empty or more than one file in data type dir


# Splitting a Path to a list
def splitpath(path, maxdepth=20):
     ( head, tail ) = os.path.split(path)
     return splitpath(head, maxdepth - 1) + [ tail ] \
         if maxdepth and head and head != path \
         else [ head or tail ]


# store Popen process
ps=[]

# find gdc_manifest file, change to that dir and run gdc-client
for root, dirs, files in os.walk(TCGA_dir):
    for f in files:
        if f.startswith('gdc_manifest'):
            tissue, data_type = splitpath(root)[-2], splitpath(root)[-1]
            
            if (not specific_tissues) or (tissue in specific_tissues) :
                if (not specific_data_types) or (data_type in specific_data_types):
                    if detection:
                        assert len(os.listdir(root)) == 1 # assert break
                    
                    print(root)
                    print(tissue, data_type, f)
                    
                    cmd = 'cd {}; gdc-client download -m {}'.format(root, f)
                    print(cmd)
            
                    p = subprocess.Popen(cmd, shell=True)
                    ps.append(p)
            
# wait until all processing is finished
for p in ps:
    p.communicate()
    
print('All done!')
