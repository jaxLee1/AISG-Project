# Project Title 

National AI Student Challenge 2022: Bus Dispatch System Report


//Chan Jin Xiang Filbert, Jax Lee Le Sheng, See Wee Shen Rachel, Wong Chu Yi Cloey//


## Description 
This National AI Student Challenge project aims to help improve government planning and enable citizens to be more informed when making decisions. 

This project detects how crowded bus stops in Singapore are by using data collected from CCTV footage from bus stops. The project uses the crowd counting model in PeekingDuck to estimate the crowd size and is updated in real-time. 

Using this crowd size estimation model, the scheduling of buses can be improved and citizens can use this real-time information to better plan their routes to avoid crowds.

This project aims to target other crowded places with CCTV footage such as shopping malls, hawker centres, food courts, libraries, and sports facilities centers, etc.

 
## Installation

The dependencies required can be found in the 'environment.yaml' file. 

Install using mamba/conda: 
```
mamba env create -f environment.yaml
```
then run: 
```
streamlit run ./path/to/main.py
```

## Usage

```python
# importing libraries (as in main.py)
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
```
```python
# loading data (rename accordingly in main.py)

df = pd.read_csv(".\data\\busStop.csv") #busStop location data
df pd.read_csv(".\data\\basketballCourts.csv") #basketballCourts location data
```
