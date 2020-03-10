def censor_text(email_text):
    """
    The function censor text takes in text from an email
    and censors the phrase 'learning algorithms' from email_one
    """

    email_text.replace("learning algorithms", "xxxxxxxxxxxxxxxxxxx")
    return email_text

def censor_text_plus(email_text):
    """
    The function censor text plus takes in text from an email
    and censors lists, words and phrases and returns the email_text
    """

    proprietary_terms = ["she", "personality matrix", "sense of self",
    "self-preservation", "learning algorithm", "her", "herself"]

    email_text.split()
