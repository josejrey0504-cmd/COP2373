# Jose Reyes
# Programming Exercise 2
# This program checks an email message for common spam words and phrases.


def get_email_message():
    # This input is needed so the program has an email message to scan.
    email_message = input("Enter the email message to scan: ")

    return email_message


def get_spam_words():
    # This list is needed so the program has spam words and phrases to compare
    # against the user's email message.
    spam_words = [
        "free",
        "winner",
        "won",
        "cash",
        "prize",
        "guaranteed",
        "limited time",
        "urgent",
        "act now",
        "click here",
        "buy now",
        "exclusive deal",
        "money back",
        "risk free",
        "earn money",
        "work from home",
        "credit card",
        "investment",
        "offer",
        "congratulations",
        "claim now",
        "selected",
        "discount",
        "bonus",
        "gift",
        "no obligation",
        "apply now",
        "cheap",
        "save big",
        "winner selected"
    ]

    return spam_words


def check_spam(message, spam_words):
    # The message is converted to lowercase so matching is not affected by
    # capitalization differences.
    message = message.lower()

    # These variables are needed to count the spam score and remember which
    # words caused the message to be marked as possible spam.
    spam_score = 0
    matched_words = []

    # This loop is needed so every spam word and phrase is checked against
    # the user's email message.
    for word in spam_words:

        # This if statement is needed to add points only when a spam word
        # or phrase is actually found in the email message.
        if word in message:
            spam_score += 1
            matched_words.append(word)

    return spam_score, matched_words


def get_spam_likelihood(spam_score):
    # This decision structure is needed so the numeric spam score can be
    # turned into a clear message for the user.
    if spam_score <= 2:
        likelihood = "Not likely spam"
    elif spam_score <= 5:
        likelihood = "Possibly spam"
    elif spam_score <= 9:
        likelihood = "Likely spam"
    else:
        likelihood = "Highly likely spam"

    return likelihood


def display_results(spam_score, likelihood, matched_words):
    # This output is needed so the user can see the final spam score,
    # likelihood rating, and the words that caused the score.
    print()
    print(f"Spam Score: {spam_score}")
    print(f"Spam Likelihood: {likelihood}")

    # This if statement is needed so the program displays a clear message
    # whether spam words were found or not.
    if matched_words:
        print("Spam Words/Phrases Found:")

        # This loop is needed so each matched spam word is displayed clearly.
        for word in matched_words:
            print(f"- {word}")
    else:
        print("No spam words or phrases were found.")


def main():
    # These function calls organize the program so each part has one job.
    email_message = get_email_message()
    spam_words = get_spam_words()
    spam_score, matched_words = check_spam(email_message, spam_words)
    likelihood = get_spam_likelihood(spam_score)

    display_results(spam_score, likelihood, matched_words)


if __name__ == "__main__":
    main()