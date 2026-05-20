import string

def create_hashtag(text: str) -> str:
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator)
    words = cleaned_text.split()
    capitalized_words = [word.capitalize() for word in words]
    hashtag_body = "".join(capitalized_words)
    full_hashtag = f"#{hashtag_body}"
  
    return full_hashtag[:140]
