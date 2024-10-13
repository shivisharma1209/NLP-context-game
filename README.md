# WordStorm

WordStorm is a web-based game where players guess a secret word based on its similarity to other words. The game provides feedback on the rank and progress of each guess, helping players to narrow down the correct word.


![ScreenRecording2024-10-11at5 43 33PM-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/da981449-ff92-4b50-9d26-984de046c1b7)


## Table of Contents

- [WordStorm](#wordstorm)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Setup Guide](#setup-guide)
    - [Word Generator](#word-generator)
    - [Django](#django)
  - [Usage](#usage)
  - [Screenshots](#screenshots)
  - [Credits](#credits)
  - [License](#license)

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/wordstorm.git
    cd wordstorm
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv env
    ```

3. **Activate the virtual environment:**

    - On Windows:

        ```sh
        .\env\Scripts\activate
        ```

    - On macOS and Linux:

        ```sh
        source env/bin/activate
        ```

4. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

## Setup Guide

### Word Generator

1. Download the word embeddings file from the Official GLoVe website: [glove.6B.zip](https://nlp.stanford.edu/projects/glove/). And store in the `WordStorm` directory.
    
    ```bash
    curl -O https://downloads.cs.stanford.edu/nlp/data/glove.6B.zip
    unzip glove.6B.zip
    ```

2. Check if the `glove.6B.300d.txt` file is present in the `WordStorm/glove.6B` directory.
3. Generate the random word to guess and its ranking to other words:

    ```sh
    python word_generator/big_data.py
    python word_generator/ranks.py
    ```

    The script will generate a random word from the `glove.6B.300d.txt` file and rank it against other words based on their similarity.

### Django

1. **Apply database migrations:**

    ```sh
    python manage.py migrate
    ```

2. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

3. **Access the application:**

    Open your web browser and navigate to `http://127.0.0.1:8000`.

## Usage

1. **Enter your guess:**

    Type a word into the input field and click the "Submit" button.

2. **View feedback:**

    The application will display the rank and progress of your guess. Keep guessing to improve your rank and find the correct word.

3. **View previous guesses:**

    The application will display a list of your previous guesses along with their ranks and progress bars.

## Screenshots

<img width="1265" alt="Screenshot 2024-10-11 at 5 31 48 PM" src="https://github.com/user-attachments/assets/4dd715da-547b-4686-a458-9c2094f4b5b1">

*Home page*


<img width="1268" alt="Screenshot 2024-10-11 at 5 32 27 PM" src="https://github.com/user-attachments/assets/b3f3baaf-dfe9-4e82-88c9-63a40debd0ab">

*Different guesses and their ranks compared to the answer which is "disco"*


<img width="1270" alt="Screenshot 2024-10-11 at 5 32 45 PM" src="https://github.com/user-attachments/assets/5848a078-161f-44f7-9dcd-3e7e9c26295e">

*Display when the correct word with rank 1 is guessed*

## Credits

- **Developer:** Shivi Sharma
- **Contributors:** @shivisharma1209
- **Special Thanks:** @phantsure

## License

This project is licensed under the MIT License - see the LICENSE file for details.
