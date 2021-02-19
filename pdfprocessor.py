import pdfminer
import re
from pdfminer.high_level import extract_text
import pandas as pd


class PDFprocess:
    def __init__(self):
        self.text = ""
        self.wc = dict()

    def extract_from_pdf(self):
        self.text = extract_text('./saved_file/saved_file.pdf')
        return self.text

    def wordcount(self, text):
        # self.text = self.extract_from_pdf()
        self.text = text.lower()
        self.text = re.sub(r'[^\w\s]+', ' ', self.text)
        tokens = list(set(self.text.split()))
        for token in tokens:
            self.wc[token] = self.text.count(token)
        df = pd.DataFrame(self.wc.items())
        df.columns = ['word', 'count']
        df.to_csv('./extracted_text/output.csv', index=False)
        return "success"
