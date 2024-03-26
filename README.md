# EIRA - Deep Learning GuideBot

**Author:** Shubham Namdev  
**GitHub Username:** shubham-namdev  
**Email:** shubhamsnamdev124@gmail.com  

## Overview

EIRA (Enhanced Intelligent Response Assistant) is a college-related information system designed to provide quick and accurate responses to user queries. The system utilizes a Feedforward Neural Network (FNN) interacting with an SQLite database containing comprehensive data about the college.

## Features

- **Voice Interaction**: EIRA allows users to interact with the system using voice commands, making the user experience more intuitive and accessible.
- **Query Handling**: The system listens to user queries, processes speech, and retrieves relevant data from the SQLite database.
- **User Interface**: A custom Tkinter GUI provides users with an interface to interact with EIRA. Users can start the chatbot, change themes, log in, and access various functionalities.
- **Admin Panel**: After logging in, administrators can add, delete, or update data, change passwords, adjust settings, and access training functionalities.
- **Training Functionality**: The system can be trained to improve accuracy using the provided training module.
- **Responsive Design**: EIRA aims to streamline the process of accessing college information, providing a convenient and efficient way to get the answers users need.
- **Assets Folder**: Contains all the PNG files used in the project.

## Repository Structure

- **run.py**: Main file to execute the program, starting at the home page.
- **bot_utils.py**: Utility functions for the chatbot. Uncomment `nltk.download('punkt')` in this file before running the app for the first time.
- **model.py**: Contains the Feedforward Neural Network (FNN) model.
- **database.db**: SQLite database containing college-related information.
- **requirements.txt**: File containing all required libraries.
- **assets**: Folder containing PNG files used in the project.

## Functionalities of Pages

- **Home Page**: 
  - Start the chatbot.
  - Change themes (Dark and Light).
  - Exit the application.
  - Log in to access admin functionalities.

- **Login Page**:
  - Enter password to access admin functionalities.
  - Option to use master password if the user forgot their password.

- **Admin Panel**:
  - **Add Data**: Add new information to the database.
    - After adding, the bot needs to be trained and restarted for the changes to take effect.
  - **Delete Data**: Remove existing data from the database.
    - After deleting, the bot needs to be trained and restarted for the changes to take effect.
  - **Update Data**: Modify existing data in the database.
    - After updating, the bot needs to be trained and restarted for the changes to take effect.
  - **Change Password**: Change the admin password for accessing admin functionalities.
  - **Settings**: Adjust system settings.
  - **About EIRA**: Learn more about the project.
  - **Train the Bot**: Improve accuracy through training.
    - After training, the bot needs to be restarted for the changes to take effect.

**Note**: After adding, removing, or updating data, changing the password, or training the bot, the bot needs to be restarted for the changes to be reflected in its responses.

## Running for the First Time

When running EIRA for the first time, follow these steps:

1. Clone the repository:

git clone https://github.com/shubham-namdev/EIRA-Deeplearning-Guidebot.git

2. Install the required libraries:

pip install -r requirements.txt

3. Uncomment `nltk.download('punkt')` in `bot_utils.py` before running the app for the first time.

4. Run the main file:

python run.py

5. When prompted, train the bot using the provided training functionality.

6. Interact with EIRA through the user interface or via voice commands.

## Contributing

Contributions are welcome! If you'd like to contribute to EIRA, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature-name`).
6. Create a new Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).

