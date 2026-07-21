import re
from collections import Counter
from functools import reduce


class TextAnalyzer:

    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_lines(self):
        try:
            with open(self.file_path) as file:
                for line in file:
                    yield line
        except FileNotFoundError:
            print("File not found")

    def get_word(self):
        words = []
        for line in self.read_lines():
            line = line.lower()
            line = re.sub(r"[^\w\s]", "", line)
            words.extend(line.split())
        return words

    def top_words(self):
        words = self.get_word()
        counts = Counter(words)
        return counts.most_common(10)

    def extract_contacts(self):
        emails = []
        phones = []
        for line in self.read_lines():
            email = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", line)
            phone = re.findall(r"\d{10}", line)
            emails.extend(email)
            phones.extend(phone)

        return emails, phones

    def average_word_length(self):
        words = self.get_word()
        long_words = filter(lambda word: len(word) > 4, words)
        lengths = list(map(len, long_words))
        total = reduce(lambda x, y: x + y, lengths)
        average = total / len(lengths)
        if len(lengths) == 0:
            return 0
        return average

    def __str__(self):
        words = self.get_word()
        total_lines = sum(1 for _ in self.read_lines())
        total_words = len(words)
        unique_words = len(set(words))

        return (
            f"Text Analyzer Summary\n"
            f"---------------------\n"
            f"Total Lines : {total_lines}\n"
            f"Total Words : {total_words}\n"
            f"Unique Words: {unique_words}"
        )

    def __repr__(self):
        return f"TextAnalyzer('{self.file_path}')"


def main():

    pass


if __name__ == "__main__":
    main()
