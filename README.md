# NLP_Second_Assignment_VR504755
To run correctly the code it necessary to install the libraries. For this you can run the *requirements.txt* file.

> pip freeze > requirements.txt
> 
> pip install -r requirements.txt

### The project
For the code part I use python with NLTK library.

The functions that define the hierarchical system for summarization of documents are written in the *second_assignment.py* program. This program takes in input a set of N documents, the size of the summary for each step and the number of steps for the summarization process. The documents can be taken from the documents folder. 

FIRST STEP: create the bag of words from a document constructed by the usual pipeline of elimination of every digit and punctuation characters, stopword elimination, word tokenization, stemming and lemmatization. In this step we take also sentences from the document using the sentence tokenization.

SECOND STEP: with the sentences obtained from the first step, the program create a dictionary, where for every sentence we assign a score based on its frequency.

THIRD STEP: with the dictionary obtained in the second step, the program sort the score of sentences in a descending order and extract the most important sentences from the dictionary. So now we have generate a summary of the most important sentences with the size of the summary given in input.

FOURTH STEP: with the summary obtained in the third step, the program divides this summary in fragments to create a new summary. This process run until the lenght of the summary will be smaller than the number of steps given in input.

LAST STEP: the program generate the summary of the summaries recursively until the number of steps is exhausted. So the program generate a summary of all documents using the first three steps and then generate a unique summary from the summary of all documents using the fourth step.

The execution time for the *second_assignment.py* depends from the number of documents given in input.


### INPUT EXAMPLES:
med_1.txt, med_2.txt, other_1.txt

3

2
