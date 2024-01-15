from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

stop_words = set(stopwords.words('english'))

def read_document(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        document = file.read()
    return document

def processed_document(document):
    # Sentence tokenization
    sentences = sent_tokenize(document)
    # Word tokenization
    tokenize_text = word_tokenize(document)

    # Remove every word that isn't an alfanumeric word (ex.: '(', ',', '.', '[' etc.).
    text_only_alnum = [word for word in tokenize_text if word.isalnum()]
    # Remove from the text every number.
    text_without_digit = [word for word in text_only_alnum if not word.isdigit()]
    # Remove from the text every english stop words.
    sw_remove_text = [word.lower() for word in text_without_digit if not word.lower() in stop_words]

    # Stemming and lemmatization method.
    stemmed = [PorterStemmer().stem(w) for w in sw_remove_text]
    lemmed = [WordNetLemmatizer().lemmatize(w) for w in stemmed]

    return sentences, lemmed

# This function calculate the importance of all sentences as a dictionary.
def calculate_sentence_scores(sentences, words):
    sentence_scores = {}
    for sentence in sentences:
        for word in words:
            if word in sentence.lower():
                if sentence in sentence_scores:
                    sentence_scores[sentence] += 1
                else:
                    sentence_scores[sentence] = 1

    return sentence_scores

# This function generate a summary for each document of the given size.
def generate_summary(sentence_scores, summary_size):
    # Sort the scores(key=lambda x: x[1]) of the sentence in a descending order
    sorted_sentences = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)
    # Extracting the most important sentences.
    summary_sentences = [sentence[0] for sentence in sorted_sentences[:summary_size]]

    return summary_sentences

# This function collate the summaries in documents based on the number of steps.
def collate_summaries(summaries, num_steps):
    # Collate a summary until summaries will be smaller than the number of steps.
    while len(summaries) > num_steps:
        new_summaries = []

        for i in range(0, len(summaries), num_steps):
            collated_summary = summaries[i:i + num_steps]
            new_summaries.append(collated_summary)

        summaries = new_summaries

    return summaries

# This function generate the summary of the summaries recursively until the number of steps is exhausted.
def hierarchical_summarization(document_paths, summary_size, num_steps):
    document_summaries = []

    for document_path in document_paths:
        document = read_document(document_path)
        sentences, words = processed_document(document)
        sentence_scores = calculate_sentence_scores(sentences, words)
        summary = generate_summary(sentence_scores, summary_size)
        document_summaries.append(summary)

    collated_summaries = collate_summaries(document_summaries, num_steps)

    return collated_summaries

def main():
    print("If you want to terminate the program leave the list of documents in blank!")

    while True:
        input_documents = input("Insert a list of documents (use commas to divide the document's name): ")
        if input_documents == "":
            break

        summary_size = input("Insert the size of the summary for each step as a integer: ")
        while summary_size == "" and summary_size != summary_size.isdigit():
            summary_size = input("Insert the size of the summary for each step as a integer: ")

        num_steps = input("Insert the number of steps for the summarization process as a integer: ")
        while num_steps == "" and num_steps != num_steps.isdigit():
            num_steps = input("Insert the number of steps for the summarization process as a integer: ")

        document_names = input_documents.split(", ")
        document_paths = []
        for i in range(len(document_names)):
            document_paths.append("documents\\" + document_names[i])

        final_summaries = hierarchical_summarization(document_paths, int(summary_size), int(num_steps))

        for i, summary in enumerate(final_summaries):
            print(f"Step {i + 1} Summary:\n{summary}\n")


if __name__ == "__main__":
    main()
