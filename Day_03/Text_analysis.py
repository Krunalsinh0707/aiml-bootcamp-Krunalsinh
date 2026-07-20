from collections import Counter


with open ("real_prose.txt", "r")as file:
    text=file.read()

frequency = {}


words=text.lower().split()


# for word in words:
#     frequency[word]=frequency.get(word,0) + 1

# print("mannual:" , frequency)

stopwords = ["the", "a", "and"]

counts=Counter(words)

word_counts = Counter(word for word in words if word.lower() not in stopwords)
# print("counter:" , dict(counts)) 


print("top 10:", counts.most_common(10))

print(word_counts.most_common(5))