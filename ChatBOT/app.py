import json
import random

try:
    with open('data.json', 'r') as f:
        data = json.load(f)
except (FileNotFoundError, json.decoder.JSONDecodeError):
    data = {}

def frameSentence(inp):
    global data
    inp = inp.lower().strip().replace("?", "")

    sentences = list(data.values())
    phrases = {}

    for sen in sentences:
        for sentence in sen:
            # Lowercase and remove target punctuation before splitting
            clean_sentence = sentence.lower().replace("?", "").replace("!", "")
            words = clean_sentence.split()

            for i in range(2, len(words)):
                w1, w2, w3 = words[i - 2], words[i - 1], words[i]

                if w1 not in phrases:
                    phrases[w1] = {}
                if w2 not in phrases[w1]:
                    phrases[w1][w2] = {}
                if w3 not in phrases[w1][w2]:
                    phrases[w1][w2][w3] = {}

                if i == len(words) - 1:
                    phrases[w1][w2][w3]["_end"] = True

    return phrases


while True:
    inp = input("ChatBOT> ").lower().strip()
    inp = inp.replace("?","")
    
    if inp in data:
        print(random.choice(data[inp]))
    elif inp == "train":
        print(frameSentence(inp))
    else:
        print("We couldn't find that in our dataset please provide 3 possible answers for your question seperated by commmas")
        new_data = input("Answers: ")
        
        data[inp] = new_data.split(',')
        
        with open('data.json', 'w') as f:
            json.dump(data, f)