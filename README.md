# 🌐 AI Text-Based Language Detection Model

Welcome to the AI Text-Based Language Detection Model project! This Python-based system uses machine learning and natural language processing techniques to identify the language of given text inputs. Developed with simplicity and precision in mind, the model is a command-line application that dynamically improves its dataset and supports multilingual text detection.

## 🧠 Project Overview
This model demonstrates the implementation of supervised learning techniques to detect the language of text inputs. Leveraging Python's robust libraries and a structured dataset, the program identifies languages with accuracy and provides detailed insights into word matches and unmatched words.

## 🖥️ Main Features
- **Language Detection**: Detects languages like English, Spanish, French, Hindi, and Gujarati.
- **Interactive CLI**: An intuitive command-line interface for seamless interaction.
- **Dynamic Dataset Update**: Add unmatched words to the dataset for improved accuracy.
- **Comprehensive Statistics**: Displays language match counts for detailed feedback.
- **Error Handling**: Validates inputs and gracefully handles errors.

## 📋 How It Works
1. **Enter a Sentence**: Type in a sentence to detect its language.
2. **Language Prediction**: The model analyzes the text and predicts the most likely language.
3. **Handle Unmatched Words**: Provides options to add unknown words to the dataset.
4. **Continue or Exit**: Enter another sentence or exit the program as desired.

## 📄 Code & Functionality

### Dataset Preparation
- A `.csv` file contains language-word mappings.
- Words are organized under language-specific headers.

### Core Logic
- **Text Normalization**: Converts text to lowercase and removes unnecessary punctuation.
- **Word Matching**: Maps input words to language-specific dictionaries.
- **Prediction**: Analyzes word matches to determine the most likely language.

### Key Methods
- **`load_dataset()`**: Loads and organizes language-word mappings from the dataset.
- **`detect_language()`**: Identifies the language of input sentences.
- **`handle_unmatched_words()`**: Dynamically updates the dataset with unmatched words.
- **`predict_language()`**: Determines the most probable language(s) from match statistics.

## 💡 Features Explained
- **Dataset Management**: A structured `.csv` file is used to store language-specific word mappings.
- **Real-Time Updates**: Add new words dynamically to improve detection accuracy.
- **Match Statistics**: Provides detailed match counts for each language.
- **Command-Line Interface**: Simplified and intuitive for efficient user interaction.

## 🚀 Installation & Usage
1. **Clone the Repository**: Download or clone the project files.
2. **Set Up Python Environment**: Install necessary libraries using `pip install pandas scikit-learn`.
3. **Run the Application**: Execute the main Python script to start the program.
4. **Provide Input**: Enter text sentences to detect their language.

## 📈 Testing & Results
The model has been tested with multilingual sentences and edge cases. It achieves high accuracy in detecting supported languages and gracefully handles unmatched words and invalid inputs.

## 🛠️ Development Details
- **Programming Language**: Python
- **Libraries Used**: pandas, scikit-learn, string
- **Platform**: Cross-platform compatibility
- **Status**: Fully functional command-line model

## 📝 Contact
For inquiries, feedback, or suggestions, reach out to me at pranavdabhi360@gmail.com.

Thank you for exploring the AI Text-Based Language Detection Model! Your contributions and feedback are highly appreciated.

Made with ❤️ by Pranav Dabhi
