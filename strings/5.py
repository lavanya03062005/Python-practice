#Convert a sentence to title case but keep known abbreviations (e.g., AI, ML) uppercase.

def title_case_conversion(sentence):
    abbreviations = {'AI', 'ML', 'NLP', 'CV'}
    result = []
    for word in sentence.split():
        if word.upper() in abbreviations:
            result.append(word.upper())
        else:
            result.append(word.capitalize())
    return " ".join(result)

print(title_case_conversion("the future of ai and ml is bright"))