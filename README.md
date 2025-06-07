# Thesis_Manon_Kooning
Individual files of Manon Kooning

**Studentnumber**: S5221838  
**Date**: 30-05-2025

## Repository Structure and File Descriptions

This repository contains files related to the thesis of Manon Kooning. Below is a description of the files and their purposes:

- **Notebooks** 
  Contains Google Colab links to the classification tasks (elements & topic using BERT models).

- **correlations**
  Used to calculate the chi-square statistic between elements and delta.

- **gold_standard_test**  
  Test file using 5 classes (annotated).

- **gold_standard_train**  
  Train file using 5 classes (annotated).

- **modified_test**  
  `gold_standard_test` modified to contain only 2 classes (binary).

- **modified_train**  
  `gold_standard_train` modified to contain only 2 classes (binary).

- **classified_output_error_analysis_distilbert.csv**
  This file contains the model's labeled output on the test set. I used this file to perform an error analysis.

- **classified_output_error_analysis_roberta.csv**
  This file contains the model's labeled output on the test set. I used this file to perform an error analysis.

- **topic_distribution**  
  Displays the distribution of topics in the labeled dataset.

## Google Drive

All other shared files can be found on Google Drive. The file called `threads1000_format_preprocessed.csv` was used for labeling.

The file `classified_output_topics.csv` contains the results of classifying story, agency, and event sequencing using DistilBERT, world making (oversampled) using RoBERTa, and topic classification using DeBERTa. This file was later used as input for the script `correlations.py.`

https://drive.google.com/drive/folders/1PclYOGt4jK8dUiOy74PvkWd5HfnA3uX6?usp=drive_link

## How to Conduct the Research

1. Use the DistilBERT binary classification Google Colab file to label everything except `world_making`. Label the file called `threads1000_format_preprocessed.csv`. Use the files called `modified_train` to train the model on and `modified_test` to test the model on.
2. Use the RoBERTa binary classification Google Colab file to label `world_making` on the output file of step 1. Use the files called `modified_train` to train the model on and `modified_test` to test the model on.
3. Use the DeBERTa topic classification Google Colab file to add the topics to the file from the output of step 2.
4. Use the file called `correlations.py` to perfrom the Chi-Square test on the file from the output of step 3. Or you can use the file called `classified_output_topics.csv` as input for this script if you want to skip step 1, 2, and 3.
