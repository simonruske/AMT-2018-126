# AMTD-2018-126
This repository includes code for the production of results and figures in the manuscript AMTD-2018-126.

Note that the following datasets were used to produce the results 
1) Polystyrene latex spheres 
2) Laboratory generated aerosol collected in 2008
3) Laboratory generated aerosol collected in 2014

Note that only the PSL data is included in the repostiory. To fully reproduce all results the raw data collected in 2008 and 2014 will need to placed into folders of the same name. This data is available at request from the first author. 

Access to the paper itself and for further information on the dicussion and peer review can be found at
* https://www.atmos-meas-tech.net/11/6203/2018/

To reproduce the results the following was conducted
1) Create filelist using Create Filelist.ipynb
2) Label files in the filelist (see /backup/Filelist for how we labelled our files)
3) Create data files using Create data csv file.ipynb
4) Run analysis using Main Analysis.ipynb
