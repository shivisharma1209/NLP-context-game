# WordStorm

WordStorm is a web-based game where players guess a secret word based on its similarity to other words. The game provides feedback on the rank and progress of each guess, helping players to narrow down the correct word.

## Table of Contents

- [WordStorm](#wordstorm)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Setup Guide](#setup-guide)
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

![Screenshot 1](screenshots/screenshot1.png)
*Home page*

![Screenshot 2](screenshots/screenshot2.png)
*Different guesses and their ranks compared to the answer which is "disco"*

![Screenshot 3](screenshots/screenshot3.png)
*Display when the correct word with rank 1 is guessed*

## Credits

- **Developer:** Shivi Sharma
- **Contributors:** @shivisharma1209
- **Special Thanks:** @phantsure

## License

This project is licensed under the MIT License - see the LICENSE file for details.