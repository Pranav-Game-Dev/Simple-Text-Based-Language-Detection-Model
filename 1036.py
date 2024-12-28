import pandas as pd
import string
from collections import Counter
import csv

class LanguageDetectionModel:
    def __init__(self, dataset_path='Dataset.csv'):
        self.dataset_path = dataset_path
        self.languages = {}
        self.load_dataset()

    def load_dataset(self):
        """Load and organize the dataset into a dictionary of language-specific word sets."""
        try:
            # Read the raw content of the CSV file
            with open(self.dataset_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Split content into lines and process each line
            lines = content.strip().split('\n')
            current_language = None
            
            for line in lines:
                if line.startswith('Language,'):
                    current_language = line.split(',')[1].strip()
                    self.languages[current_language] = set()
                elif current_language and line.strip():
                    # Split the line by comma and add words to the language set
                    words = line.split(',')
                    self.languages[current_language].update(
                        word.strip().lower() for word in words if word.strip()
                    )
            
            if not self.languages:
                raise ValueError("No language data loaded from the dataset")
            
            # Debugging: Print loaded languages for verification
            print("Languages loaded:", list(self.languages.keys()))
                    
        except Exception as e:
            print(f"Error loading dataset: {e}")
            exit(1)


    def normalize_text(self, text):
        """Remove punctuation and convert to lowercase."""
        text = text.lower()
        # Remove punctuation except for apostrophes
        text = ''.join(char for char in text if char not in string.punctuation or char == "'")
        return text

    def detect_language(self, sentence):
        """Detect the language of the input sentence."""
        words = self.normalize_text(sentence).split()
        language_matches = {lang: 0 for lang in self.languages}
        unmatched_words = []
    
        for word in words:
            word_matched = False
            for language, word_set in self.languages.items():
                if word in word_set:
                    language_matches[language] += 1
                    word_matched = True
            if not word_matched:
                unmatched_words.append(word)
    
        # Debugging: Check if "English" is processed correctly
        if "English" not in language_matches:
            print("Debug: English language not loaded properly")
        
        return language_matches, unmatched_words


    def handle_unmatched_words(self, unmatched_words):
        """Process unmatched words and add them to the dataset."""
        if not unmatched_words:
            return

        print("\nUnmatched words found:")
        for word in unmatched_words:
            print(f"Word: {word}")
            print("Select language:")
            for idx, language in enumerate(self.languages.keys(), 1):
                print(f"{idx}. {language}")
            
            while True:
                try:
                    choice = int(input("Enter language number: "))
                    if 1 <= choice <= len(self.languages):
                        selected_language = list(self.languages.keys())[choice - 1]
                        # Add to memory
                        self.languages[selected_language].add(word)
                        # Add to file
                        self.append_word_to_file(word, selected_language)
                        break
                    else:
                        print("Invalid choice. Please try again.")
                except ValueError:
                    print("Please enter a valid number.")

    def append_word_to_file(self, word, language):
        """Append a new word to the dataset file."""
        try:
            with open(self.dataset_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            # Find the line containing the language
            for i, line in enumerate(lines):
                if line.startswith(f'Language,{language}'):
                    # Append the word to the next line
                    if i + 1 < len(lines):
                        lines[i + 1] = lines[i + 1].strip() + ',' + word + '\n'
                    break

            with open(self.dataset_path, 'w', encoding='utf-8') as file:
                file.writelines(lines)
        except Exception as e:
            print(f"Error adding word to dataset: {e}")

    def predict_language(self, language_matches):
        """Determine the most likely language(s) based on word matches."""
        if not any(language_matches.values()):
            return "Language detection unavailable - no matches found"

        max_matches = max(language_matches.values())
        if max_matches == 0:
            return "No language matches found"

        predicted_languages = [
            lang for lang, count in language_matches.items() 
            if count == max_matches
        ]

        if len(predicted_languages) == 1:
            return f"Detected language: {predicted_languages[0]} ({max_matches} words matched)"
        else:
            return f"Multiple possible languages detected: {', '.join(predicted_languages)} ({max_matches} words matched in each)"

def main():
    model = LanguageDetectionModel()

    while True:
        print("\nLanguage Detection System")
        print("------------------------")
        sentence = input("Enter a sentence: ")

        if not sentence.strip():
            print("Please enter a valid sentence.")
            continue

        language_matches, unmatched_words = model.detect_language(sentence)
        
        # Display prediction
        prediction = model.predict_language(language_matches)
        print(f"\n{prediction}")
        
        # Display match statistics
        print("\nMatch statistics:")
        for language, count in language_matches.items():
            print(f"{language}: {count} matches")

        # Handle unmatched words
        if unmatched_words:
            print(f"\nUnmatched words: {', '.join(unmatched_words)}")
            add_words = input("Would you like to add these words to the dataset? (y/n): ")
            if add_words.lower() == 'y':
                model.handle_unmatched_words(unmatched_words)

        # Continue or exit
        choice = input("\nWould you like to enter another sentence? (Y/N): ").strip().lower()
        if choice == 'n':
         break

if __name__ == "__main__":
    main()