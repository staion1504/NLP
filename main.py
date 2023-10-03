import re
import csv


def transform_contractions(text):
    contractions_expanded = {
        "ain't": "am not",
        "aren't": "are not",
        "can't": "cannot",
        "can't've": "cannot have",
        "'cause": "because",
        "could've": "could have",
        "couldn't": "could not",
        "couldn't've": "could not have",
        "didn't": "did not",
        "doesn't": "does not",
        "doesn’t": "does not",
        "don't": "do not",
        "don’t": "do not",
        "hadn't": "had not",
        "hadn't've": "had not have",
        "hasn't": "has not",
        "haven't": "have not",
        "he'd": "he had",
        "he'd've": "he would have",
        "he'll": "he will",
        "he'll've": "he will have",
        "he's": "he is",
        "how'd": "how did",
        "how'd'y": "how do you",
        "how'll": "how will",
        "how's": "how is",
        "i'd": "i would",
        "i'd've": "i would have",
        "i'll": "i will",
        "i'll've": "i will have",
        "i'm": "i am",
        "i've": "i have",
        "isn't": "is not",
        "it'd": "it would",
        "it'd've": "it would have",
        "it'll": "it will",
        "it'll've": "it will have",
        "it's": "it is",
        "let's": "let us",
        "ma'am": "madam",
        "mayn't": "may not",
        "might've": "might have",
        "mightn't": "might not",
        "mightn't've": "might not have",
        "must've": "must have",
        "mustn't": "must not",
        "mustn't've": "must not have",
        "needn't": "need not",
        "needn't've": "need not have",
        "o'clock": "of the clock",
        "oughtn't": "ought not",
        "oughtn't've": "ought not have",
        "shan't": "shall not",
        "sha'n't": "shall not",
        "shan't've": "shall not have",
        "she'd": "she would",
        "she'd've": "she would have",
        "she'll": "she will",
        "she'll've": "she will have",
        "she's": "she is",
        "should've": "should have",
        "shouldn't": "should not",
        "shouldn't've": "should not have",
        "so've": "so have",
        "so's": "so is",
        "that'd": "that would",
        "that'd've": "that would have",
        "that's": "that is",
        "there'd": "there would",
        "there'd've": "there would have",
        "there's": "there is",
        "they'd": "they would",
        "they'd've": "they would have",
        "they'll": "they will",
        "they'll've": "they will have",
        "they're": "they are",
        "they've": "they have",
        "to've": "to have",
        "wasn't": "was not",
        "we'd": "we would",
        "we'd've": "we would have",
        "we'll": "we will",
        "we'll've": "we will have",
        "we're": "we are",
        "we've": "we have",
        "weren't": "were not",
        "what'll": "what will",
        "what'll've": "what will have",
        "what're": "what are",
        "what's": "what is",
        "what've": "what have",
        "when's": "when is",
        "when've": "when have",
        "where'd": "where did",
        "where's": "where is",
        "where've": "where have",
        "who'll": "who will",
        "who'll've": "who will have",
        "who's": "who is",
        "who've": "who have",
        "why's": "why is",
        "why've": "why have",
        "will've": "will have",
        "won't": "will not",
        "won't've": "will not have",
        "would've": "would have",
        "wouldn't": "would not",
        "wouldn't've": "would not have",
        "y'all": "you all",
        "y’all": "you all",
        "y'all'd": "you all would",
        "y'all'd've": "you all would have",
        "y'all're": "you all are",
        "y'all've": "you all have",
        "you'd": "you would",
        "you'd've": "you would have",
        "you'll": "you will",
        "you'll've": "you will have",
        "you're": "you are",
        "you've": "you have",
        "ain’t": "am not",
        "aren’t": "are not",
        "can’t": "cannot",
        "can’t’ve": "cannot have",
        "’cause": "because",
        "could’ve": "could have",
        "couldn’t": "could not",
        "couldn’t’ve": "could not have",
        "didn’t": "did not",
        "doesn’t": "does not",
        "don’t": "do not",
        "don’t": "do not",
        "hadn’t": "had not",
        "hadn’t’ve": "had not have",
        "hasn’t": "has not",
        "haven’t": "have not",
        "he’d": "he had",
        "he’d’ve": "he would have",
        "he’ll": "he will",
        "he’ll’ve": "he will have",
        "he’s": "he is",
        "how’d": "how did",
        "how’d’y": "how do you",
        "how’ll": "how will",
        "how’s": "how is",
        "i’d": "i would",
        "i’d’ve": "i would have",
        "i’ll": "i will",
        "i’ll’ve": "i will have",
        "i’m": "i am",
        "i’ve": "i have",
        "isn’t": "is not",
        "it’d": "it would",
        "it’d’ve": "it would have",
        "it’ll": "it will",
        "it’ll’ve": "it will have",
        "it’s": "it is",
        "let’s": "let us",
        "ma’am": "madam",
        "mayn’t": "may not",
        "might’ve": "might have",
        "mightn’t": "might not",
        "mightn’t’ve": "might not have",
        "must’ve": "must have",
        "mustn’t": "must not",
        "mustn’t’ve": "must not have",
        "needn’t": "need not",
        "needn’t’ve": "need not have",
        "o’clock": "of the clock",
        "oughtn’t": "ought not",
        "oughtn’t’ve": "ought not have",
        "shan’t": "shall not",
        "sha’n’t": "shall not",
        "shan’t’ve": "shall not have",
        "she’d": "she would",
        "she’d’ve": "she would have",
        "she’ll": "she will",
        "she’ll’ve": "she will have",
        "she’s": "she is",
        "should’ve": "should have",
        "shouldn’t": "should not",
        "shouldn’t’ve": "should not have",
        "so’ve": "so have",
        "so’s": "so is",
        "that’d": "that would",
        "that’d’ve": "that would have",
        "that’s": "that is",
        "there’d": "there would",
        "there’d’ve": "there would have",
        "there’s": "there is",
        "they’d": "they would",
        "they’d’ve": "they would have",
        "they’ll": "they will",
        "they’ll’ve": "they will have",
        "they’re": "they are",
        "they’ve": "they have",
        "to’ve": "to have",
        "wasn’t": "was not",
        "we’d": "we would",
        "we’d’ve": "we would have",
        "we’ll": "we will",
        "we’ll’ve": "we will have",
        "we’re": "we are",
        "we’ve": "we have",
        "weren’t": "were not",
        "what’ll": "what will",
        "what’ll’ve": "what will have",
        "what’re": "what are",
        "what’s": "what is",
        "what’ve": "what have",
        "when’s": "when is",
        "when’ve": "when have",
        "where’d": "where did",
        "where’s": "where is",
        "where’ve": "where have",
        "who’ll": "who will",
        "who’ll’ve": "who will have",
        "who’s": "who is",
        "who’ve": "who have",
        "why’s": "why is",
        "why’ve": "why have",
        "will’ve": "will have",
        "won’t": "will not",
        "won’t’ve": "will not have",
        "would’ve": "would have",
        "wouldn’t": "would not",
        "wouldn’t’ve": "would not have",
        "y’all": "you all",
        "y’all": "you all",
        "y’all’d": "you all would",
        "y’all’d’ve": "you all would have",
        "y’all’re": "you all are",
        "y’all’ve": "you all have",
        "you’d": "you would",
        "you’d’ve": "you would have",
        "you’ll": "you will",
        "you’ll’ve": "you will have",
        "you’re": "you are",
        "you’re": "you are",
        "you’ve": "you have",
    }

    words = text.split()
    transformed_words = []
    for word in words:
        if word in contractions_expanded:
            transformed_words.extend(contractions_expanded[word].split())
        else:
            transformed_words.append(word)
    return ' '.join(transformed_words)


def cleanWithRegEx(text):
    text = re.sub(r'https?:\/\/.[\r\n]', '', text, flags=re.MULTILINE)
    text = re.sub(r'\<a href', ' ', text)
    text = re.sub(r'[_"\-;%()|+&=*%.,!?:#$@\[\]/]', ' ', text)
    text = re.sub(r'<br />', ' ', text)
    text = re.sub(r'<br>', ' ', text)
    text = re.sub(r'\'', ' ', text)
    text = re.sub(r'>', '', text)
    return text


def convertToLower(irregular_Text):
    lower_case_regularized_text = ""
    for character in irregular_Text:
        if ord(character) >= 65 and ord(character) <= 90:
            lower_case_regularized_text += chr(ord(character)+32)
        else:
            lower_case_regularized_text += character
    return lower_case_regularized_text


def tokenize(string):
    return


stopwords = set(["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as",
                "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"])


def stopword(text):
    str = ""
    word = text.split()
    for eachWord in word:
        if eachWord not in stopwords:
            str = str+eachWord+" "

    return str


def lemmatize(word):
    lemmatized_word = word
    irregular_words = {
        "running": "run",
        "flies": "fly",
        "happily": "happy",
        "generously": "generous",
        "better": "good",
        "mice": "mouse",
        "oxen": "ox",
        "geese": "goose",
        "teeth": "tooth",
        "feet": "foot",
        "is": "be",
        "was": "be",
        "am": "be",
        "has": "have",
        "had": "have",
        "does": "do",
        "did": "do",
        "goes": "go",
        "went": "go",
        "goose": "geese",
        "child": "children",
        "man": "men",
        "woman": "women",
        "person": "people",
        "leaf": "leaves",
        "amazing": "amaze",
        "delicious": "delight",
        "excellent": "excel",
        "fantastic": "fantasy",
        "horrible": "horror",
        "terrible": "terror",
        "wonderful": "wonder",
        "outstanding": "outstand",
        "impressive": "impress",
        "disappointing": "disappoint",
        "satisfying": "satisfy",
        "reviews": "review",
        "feedbacks": "feedback",
        "customers": "customer",
        "products": "product",
        "experience": "experience",
        "service": "service",
        "quality": "quality",
        "positive": "posit",
        "negative": "negat",
        "suggestion": "suggest",
        "improvement": "improve",
        "learning": "learn"
    }

    if lemmatized_word in irregular_words:
        return irregular_words[lemmatized_word]

    return lemmatized_word


def stemming(text):
    result = ""

    for word in text.split(" "):
        if word.endswith("sses"):
            word = word[:-2]

        elif word.endswith("ies"):

            word = word[:-2]
        elif word.endswith("ss"):
            word = word
        elif word.endswith("s"):

            word = word[:-1]
        if word.endswith("eed"):

            if len(word) > 4:

                word = word[:-1]
        elif word.endswith("ed"):

            if "at" not in word:

                word = word[:-2]
                if word.endswith("ed"):

                    word = word[:-2]
        elif word.endswith("ing"):
            if "at" not in word:
                word = word[:-3]
                if word.endswith("ing"):
                    word = word[:-3]
        if len(word) > 2:
            if word[-1] in "ys" and word[-2] not in "aeiou":
                word = word[:-1]
        if word.endswith("tional"):
            word = word[:-6] + "tion"
        elif word.endswith("enci"):
            word = word[:-4] + "ence"
        elif word.endswith("anci"):
            word = word[:-4] + "ance"
        elif word.endswith("izer"):
            word = word[:-4] + "ize"
        elif word.endswith("abli"):
            word = word[:-4] + "able"
        elif word.endswith("alli"):
            word = word[:-4] + "al"
        elif word.endswith("entli"):
            word = word[:-5] + "ent"
        elif word.endswith("eli"):
            word = word[:-3] + "e"
        if len(word) > 2:
            if word[-1] == "e" and word[-2] not in "aeiou" and word[-3] not in "aeiou":
                word = word[:-1]
        if len(word) > 2:
            if word.endswith("ll") and word[-3] not in "aeiou":
                word = word[:-1]

        result = result + " " + word

    return result


def preprocess_text(text):

    text = "Hi i'm NLP student  ,i don't like chocolates <br> Visit this sITe tO gEt CoUpOnS<a href='/'>"

    text = transform_contractions(text)

    text = cleanWithRegEx(text)

    text = convertToLower(text)

    text = stopword(text)

    text = lemmatize(text)

    text = stemming(text)

    print(text)

    return text


preprocess_text("")


with open('./../../Reviews.csv', 'r', newline='') as reviewsFile:
    reviewsLines = csv.reader(reviewsFile)

    for index, line in enumerate(reviewsLines):
        if index == 0:
            continue
        elif index == 5:
            break
        else:
            linex = line[9]
            print("--------------------------------------------------")
            print("Original text:", linex)

            print("-------------------------------------------------")
            print("Cleaned text:", preprocess_text(linex))
            print("-------------------------------------------------")
            print(" ")
            print("  ")
