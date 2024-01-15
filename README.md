# NLP_Second_Assignment_VR504755
To run correctly the code it necessary to install the libraries. For this you can run the *requirements.txt* file.

> pip freeze > requirements.txt
> 
> pip install -r requirements.txt

### The project
For the code part I use python with NLTK library.

For this text classifier I create a personalized corpora divided in two categories: MEDICAL and OTHER.
For the creation of this corpora I write the code *corpora_creator.ipynb*. This program takes a page from wikipedia, specifying a topic, and transforms it into a file saving it in the right folder (MEDICAL or OTHER).
In the corpora folder there are 500 MEDICAL files and 500 OTHER files (the topics for the OTHER category are car, artificial intelligence, geography, catholic and videogame).
The execution time for the *corpora_creator.ipynb* is more or less 5 minutes.

The functions that define the text classifier are written in the *first_assignment.ipynb* program. This program creates a list based on the personalized corpora (all text files are mapped with their categories).
The list is processed for all files: the program tokenizes by word the file and then eliminates all words that are not alphanumeric and all words that are numbers. After that it eliminates stop word, uses the Porter's algorithm for the stemming and the last step is the lemmatization with the WordNet Lemmatizer.
After this procedure, the program extract the features for the training of the classifier. For the feature extractor, the program takes the first 2000 most frequent words from the corpus. The feature extraxtor simply checks whether each of these words is present in the list's files. With the feature extractor, the program selects the training set and test set that are used respectively for the training of the Naive Bayes classifier and for the check of the accuracy of the classifier. 

The classifier is ready and now the program waits for an input. The input is an URL of a wikipedia page.
The program takes the text from the page after a request to wikipedia. This text is processed the same way the list was processed (word tokenization; elimination of symbols, numbers and stop words; stemming and lemmatization). Suddenly, the program takes the first 20 most frequent words from the processed text and uses these words for the feature extraction on the text.
Finally, the program classifies the wikipedia page, specifying the category (MEDICAL or OTHER)
These last steps are repeated while the input is not blank.
The execution time for the *first_assignment.ipynb* is more or less 2 minutes for the training part.
