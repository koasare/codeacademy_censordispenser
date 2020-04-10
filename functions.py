def censor_text(email_text, censor_phrase):
    """
    The function censor text takes in the content of an email given with
    input email_text and replaces information determined by the 'censor' input
    with 'x'
    """
    censored_text = ""
    for i in range(0, len(censor)):
        if censor[i] == " ":
            censored_text += " "
        else:
            censored_text += "x"
    return email_text.replace(censor, censored_text)

proprietary_terms = ["she", "personality matrix", "sense of self",
"self-preservation", "learning algorithm", "her", "herself"]

def censor_text_plus(email_text, censor_list):
    """

    """
    for word in censor_list:
        censored_text = ""
        for i in range(0, len(word)):
            if word[i] == " ":
                censored_text += " "
            else:
                censored_text += "x"
        email_text = email_text.replace(word, censored_text)
    return email_text

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming",
"alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful",
"broken", "damage", "damaging", "dismal", "distressed", "distressed",
"concerning", "horrible", "horribly", "questionable"]

def censor_negative(email_text, censor_list, negative_words):
    input_words = []
    for x in email_text.split(" "):
        x1 = x.split("\n")
        for word in x1:
            input_words.append(word)
    for i in range(0, len(input_words)):
        if input_words[i] in censor_list:
            word_clean = input_words[i]
            censored_word = ""
            for x in range(0, len(word_clean)):
                censored_word = censored_word + "x"
            input_words[i] = input_words[i].replace(word_clean, censored_word)
        count = 0
        for i in range(0, len(input_words)):
            if (input_words[i] in negative_words):
                count += 1
                if count > 2:
                    word_clean = input_words[i]
                    for x in punctuation:
                        word_clean = word_clean.strip(x)
                    censored_word = ""
                    for x in range(0, len(word_clean)):
                        censored_word = censored_word + "x"
                    input_words[i] = input_words[i].replace(word_clean, censored_word)
    return " ".join(input_words)

    
