def get_level():
    level = input("What difficulty setting do you want? Please enter easy, medium or hard.\n")
    level = level.lower()
    if level == 'easy':
        answer = random_word(easy_words(dictionary))
    elif level == 'medium':
        answer = random_word(medium_words(dictionary))
    else:
        answer = random_word(hard_words(dictionary))
    return answer