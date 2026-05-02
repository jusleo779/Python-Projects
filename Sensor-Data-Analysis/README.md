# Sensor Data Analysis

## Introduction
Data analysis is an essential skill in hardware engineering, used in daily testing. These projects cover the three essential Python libraries for hardware data analysis, **NumPy**, **Pandas**, and **Matplotlib**,
taking raw datasets to analysis-ready outputs.

## NumPy Project
Processes a human activity dataset (jogging, walking, sitting) from a CSV file and 
computes the RMS (Root Mean Square) value per activity using vectorized operations.

### Learnings
- **Vectorized math** — applying operations to every element without loops
- **Boolean masking** — filtering arrays using conditions directly in the index
- **Broadcasting** — automatic resizing of arrays to match shapes for operations
- **Fancy indexing** — selecting multiple indices in a single call
- **Slicing** — extracting ranges of data with custom step sizes
- **dtypes** — managing variable types and bit sizing for memory efficiency

## Pandas Project
Processes a solar power generation dataset, then cleans the raw data to compute the mean, std, 
and max by Source ID, and outputs flagged readings exceeding 3σ from the mean.

### Learnings
- **Data loading** — importing CSVs with column names and index handling preserved
- **Cleaning** — handling missing values with fillna, dropna, and interpolate
- **Grouping** — aggregating data by recurring sensor IDs
- **Aggregation** — running multiple math methods in a single operation
- **Time series** — parsing datetime strings into datetime64 for time-based analysis

## Matplotlib Project
Visualizes the solar power dataset, comparing AC and DC power output on a shared 
plot with a threshold line flagging exceeding power limits.

### Learnings
- **Subplots** — plotting multiple channels on a shared figure
- **Threshold annotation** — drawing limit lines with axhline and labeling exceeding data
- **Twin axes** — overlaying two y-scales on one plot to compare AC vs DC power
- **Figure export** — saving plot at 300 DPI for report-quality output

## Connection to Hardware Engineering
- **NumPy** — automates large-scale numerical operations on sensor data, replacing 
  manual calculations with reliable, repeatable scripts
- **Pandas** — cleans and organizes raw measurement logs into structured datasets 
  ready for analysis or reporting
- **Matplotlib** — turns thousands of data points into clear visual outputs that 
  can be saved and shared in engineering reports