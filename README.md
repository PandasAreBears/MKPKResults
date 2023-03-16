# Introduction
Welcome to the Makka Pakka Results Data Analysis repository! This repository
contains the data and analysis tools for evaluating the performance of the
Makka Pakka malware injection system. The aim of this project is to assess the
effectiveness of Makka Pakka and ELF Caver in bypassing antivirus detection
when injecting malicious code into ELF binaries.

The data provided here consists of the results obtained from injecting malware
samples into a range of standard Linux binaries and analyzing their detection
rates using VirusTotal, a reputable third-party service. The analysis relies
on Python data analysis libraries, such as pandas and matplotlib, to
efficiently process and visualize the data.

In this repository, you'll find the raw data, as well as the code and tools
required to reproduce the analysis. The hope is that by open-sourcing this
information, further research with be facilitated and it will enable others to
interrogate the data, identify potential biases, and contribute to the ongoing
development of malware injection techniques to add to the field of
vulnerability research.

# Structure
mkpk - Contains the malicious Makka Pakka source files.
data - stores the data outputs of the experiment, this is the raw data, and the
    graphical visualisations.
src/analysis - Generates the grpahical visualisations based on the raw data.
src/gather - Generates the infected binaries and stores them in the top-level
    `bin` directory.
src/reprot - Queries virus total with the infected binaries, and stores the
    results in the data directory.

# Data Reproduction Methodology
1. Run:
``` bash
source configure.sh
```

2. Create a `bin` folder in the top level directory.

3. Generate the binaries injected binaries by running:
``` bash
python3 src/gather/main.py
```
This will produce a set of folders containing the original binary + the
injected variants.

4. Add a virus total API key to the data reporter. This should be put into the
empty string in src/report/vt_analysis.py:10.

5. Generate the results by running:
``` bash
python3 src/report/main.py
```
This will produce a file - data/results.csv

Note: Due to a daily limit on the Virus Total API, you may need to pause/
resume the data collection over multiple days. To resume the data, put the
number of binary in src/report/main.py:21, and the id next ID in
data/results.csv in src/report/results_csv.py:6.
