# Jose Reyes
# Programming Exercise 7
# This program separates a paragraph into individual sentences
# and counts how many sentences are in the paragraph.

import re


# This function replaces extra spacing and newline characters.
def clean_paragraph(paragraph):
    # Replace newline characters with one space.
    paragraph = paragraph.replace("\n", " ")

    # Replace multiple spaces with one space.
    paragraph = re.sub(r"\s+", " ", paragraph)

    # Remove extra spaces from the beginning and end.
    return paragraph.strip()


# This function finds each sentence in the paragraph.
def get_sentences(paragraph):
    # This pattern uses non-greedy matching and look-ahead.
    # It allows sentences to begin with letters or numbers.
    pattern = r"[A-Z0-9].*?[.!?](?=\s+[A-Z0-9]|$)"

    # Find all sentences in the paragraph.
    sentences = re.findall(pattern, paragraph, flags=re.DOTALL)

    # Remove extra spaces from each sentence.
    return [sentence.strip() for sentence in sentences]


# This function displays each sentence and the total count.
def display_sentences(sentences):
    # Display each individual sentence.
    print("\nIndividual Sentences:")

    # Loop through the list and display each sentence with a number.
    for sentence_number, sentence in enumerate(sentences, start=1):
        print(f"{sentence_number}. {sentence}")

    # Display the total number of sentences.
    print(f"\nSentence Count: {len(sentences)}")


# This function tests the sentence finder with sample paragraphs.
def run_tests():
    print("\nTesting Sentence Finder")

    # This test includes a sentence that begins with a number.
    test_paragraph = (
        "Today is a good day. 2 people went to the store! "
        "3 dogs were outside? This is the last sentence."
    )

    # Clean the test paragraph.
    cleaned_test = clean_paragraph(test_paragraph)

    # Find the sentences in the test paragraph.
    test_sentences = get_sentences(cleaned_test)

    # Display the test results.
    display_sentences(test_sentences)


# The main function controls the program.
def main():
    # Ask the user to enter a paragraph.
    paragraph = input("Enter a paragraph: ")

    # Clean the paragraph before searching for sentences.
    cleaned_paragraph = clean_paragraph(paragraph)

    # Get the list of sentences from the paragraph.
    sentences = get_sentences(cleaned_paragraph)

    # Display each sentence and the sentence count.
    display_sentences(sentences)

    # Run valid test examples.
    run_tests()


# Start the program.
if __name__ == "__main__":
    main()