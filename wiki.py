import wikipediaapi

w = wikipediaapi.Wikipedia(language='en', extract_format=wikipediaapi.ExtractFormat.WIKI)

subjects = ['Maggie Gallagher']

for subject in subjects:
    p = w.page(subject)
    if p.exists():
        print(p.summary, '\n')
        print(p.fullurl, '\n')
    else:
        print(subject + ": No information available.\n")