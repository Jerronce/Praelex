#!/usr/bin/env python3
"""
Praelex - AI Lexical Analysis and NLP Toolkit
Tokenization, NER, and sentiment analysis.
Created by Jerronce | PraeTech
"""

import re
from typing import List, Dict
from collections import Counter

class Tokenizer:
    def __init__(self):
        self.tokens = []
        
    def tokenize(self, text: str) -> List[str]:
        # Simple word tokenization
        self.tokens = re.findall(r'\w+', text.lower())
        return self.tokens

class SentimentAnalyzer:
    def __init__(self):
        self.positive_words = {'good', 'great', 'excellent', 'amazing', 'wonderful'}
        self.negative_words = {'bad', 'poor', 'terrible', 'awful', 'horrible'}
        
    def analyze(self, text: str) -> Dict:
        words = text.lower().split()
        pos_count = sum(1 for w in words if w in self.positive_words)
        neg_count = sum(1 for w in words if w in self.negative_words)
        
        if pos_count > neg_count:
            sentiment = 'positive'
        elif neg_count > pos_count:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
            
        return {
            'sentiment': sentiment,
            'positive_score': pos_count,
            'negative_score': neg_count
        }

class NERExtractor:
    def __init__(self):
        self.entities = []
        
    def extract(self, text: str) -> List[str]:
        # Simple capitalized word extraction as entities
        self.entities = re.findall(r'\b[A-Z][a-z]+\b', text)
        return self.entities

class NLPPipeline:
    def __init__(self):
        self.tokenizer = Tokenizer()
        self.sentiment = SentimentAnalyzer()
        self.ner = NERExtractor()
        
    def process(self, text: str) -> Dict:
        tokens = self.tokenizer.tokenize(text)
        sentiment = self.sentiment.analyze(text)
        entities = self.ner.extract(text)
        
        return {
            'tokens': tokens,
            'sentiment': sentiment,
            'entities': entities
        }

if __name__ == "__main__":
    print("Praelex - Understanding language with AI")
