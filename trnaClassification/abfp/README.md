4 classes classification: archaeal, bacterial, fungi and plant tRNA sequences.

Data: train/valid/test = 8000/3000/1000 total samples

Confusion matrix (CM) and metrics notations:

  * CM rows -- classification results, CM columns -- expecred labels for each class
  * accuracy = sum(CM<sub>pp</sub>) / sum(CM<sub>pq</sub>) for all p, q 
  * precision<sub>p</sub> = CM<sub>pp</sub> / sum(CM<sub>pq</sub>) for all q -- precision for fixed class p
  * recall<sub>p</sub> = CM<sub>pp</sub> / sum(CM<sub>qp</sub>) for all q -- recall for fixed class p

Approaches (on the same data):
  
**Images** 

Original sequences of different length. Parsing-provided images resized to 80x80

1. model_30_94

| res\lbl 	| A   	| B   	| F   	| P   	|
|---------	|-----	|-----	|-----	|-----	|
| A       	| 693 	| 29  	| 11  	| 3   	|
| B       	| 14  	| 684 	| 1   	| 16  	|
| F       	| 41  	| 22  	| 720 	| 29  	|
| P       	| 2   	| 15  	| 18  	| 702 	|

   * accuracy = 96.2%
   * precision<sub>a</sub> = 94.2%        recall<sub>a</sub> = 92.4%
   * precision<sub>b</sub> = 95.7%        recall<sub>b</sub> = 91.2%
   * precision<sub>f</sub> = 88.7%        recall<sub>f</sub> = 96.0%
   * precision<sub>p</sub> = 95.3%        recall<sub>p</sub> = 93.6%
   
---------------------------------------------------------------------------------  

**Vectors**

Origial sequences of length 220. Parsing-provided uint32 vectors decompressed to bytes

1. model_51_88

| res\lbl 	| A   	| B   	| F   	| P   	|
|---------	|-----	|-----	|-----	|-----	|
| A       	| 591	 | 18  	| 11  	| 10   |
| B       	| 72  	| 662 	| 24  	| 30  	|
| F       	| 51  	| 39  	| 685 	| 48  	|
| P       	| 36   | 31  	| 30  	| 662 	|

   * accuracy = 86.7%
   * precision<sub>a</sub> = 93.8%        recall<sub>a</sub> = 78.8%
   * precision<sub>b</sub> = 84.0%        recall<sub>b</sub> = 88.3%
   * precision<sub>f</sub> = 83.2%        recall<sub>f</sub> = 91.3%
   * precision<sub>p</sub> = 87.2%        recall<sub>p</sub> = 88.3%

--------------------------------------------------------------------------------- 

**Images extended to sequences**

Original sequences of length 220. Extending trained model for image data (abfp/images/models/model_30_94)

1. model_17_95

| res\lbl 	| A   	| B   	| F   	| P   	|
|---------	|-----	|-----	|-----	|-----	|
| A       	| 739	 | 33  	| 25  	| 10   |
| B       	| 6   	| 716 	| 13  	| 17  	|
| F       	| 4   	| 1  	 | 707 	| 13  	|
| P       	| 1   	| 0   	| 5   	| 710 	|

   * accuracy = 95.7%
   * precision<sub>a</sub> = 91.6%        recall<sub>a</sub> = 98.5%
   * precision<sub>b</sub> = 95.2%        recall<sub>b</sub> = 95.5%
   * precision<sub>f</sub> = 97.5%        recall<sub>f</sub> = 94.3%
   * precision<sub>p</sub> = 99.2%        recall<sub>p</sub> = 94.7%

--------------------------------------------------------------------------------- 

**Vectors extended to sequences**

Original sequences of length 220. Extending trained model for vectorized data (abfp/vectors/models/model_51_88)

1. model_18_96

| res\lbl 	| A   	| B   	| F   	| P   	|
|---------	|-----	|-----	|-----	|-----	|
| A       	| 744 	| 36  	| 25  	| 12   |
| B       	| 3  	 | 713 	| 10   | 12  	|
| F       	| 2  	 | 1   	| 712 	| 8  	 |
| P       	| 1   	| 0   	| 3   	| 718 	|

   * accuracy = 96.2%
   * precision<sub>a</sub> = 91.1%        recall<sub>a</sub> = 99.2%
   * precision<sub>b</sub> = 96.6%        recall<sub>b</sub> = 95.1%
   * precision<sub>f</sub> = 98.5%        recall<sub>f</sub> = 94.9%
   * precision<sub>p</sub> = 99.4%        recall<sub>p</sub> = 95.7%