🤖 AI-Powered Code Reviewer

An AI-powered code reviewing tool that analyzes source code, detects errors, highlights bad practices, and suggests improved versions of the code using AI.

This project is designed to help developers, students, and learners get instant feedback on their code quality.

🚀 Features

🔍 Code Analysis – Checks whether the given code is correct or not

🧠 AI Suggestions – Provides improved and corrected code using AI

🧾 Syntax & Logic Review – Identifies common mistakes and issues

⚡ Fast Feedback – Get instant results by pasting code

🐍 Python-based – Built entirely using Python

🛠️ Tech Stack

Language: Python

Framework / Libraries:

Streamlit (UI)

AST (Abstract Syntax Tree)

AI / LLM integration

Environment: Virtual Environment (venv)

📂 Project Structure Code-Reviewer-Live-Lecture/ │ ├── app.py # Main application entry point ├── ai_suggester.py # AI-based suggestion logic ├── chatbot.py # Chat / interaction logic ├── chatmodel_google.py # AI model integration ├── code_parser.py # Code parsing & analysis ├── demo.py # Demo / testing file ├── demo_ast_parse_unparse.py # AST parsing demo ├── .env.example # Environment variable template ├── .gitignore └── README.md

⚙️ Installation & Setup 1️⃣ Clone the repository git clone https://github.com/Prashant88123/AI-Powered-Code-Reviewer.git cd AI-Powered-Code-Reviewer

2️⃣ Create virtual environment python -m venv venv

Activate it:

Windows

venv\Scripts\activate

Linux / macOS

source venv/bin/activate

3️⃣ Install dependencies pip install -r requirements.txt

4️⃣ Environment variables

Create a .env file using the template:

cp .env.example .env

Fill in required keys (API keys, secrets, etc.).

▶️ Run the Application python app.py

Or if using Streamlit:

streamlit run app.py

🧪 How It Works

User pastes source code into the application

Code is parsed using AST

AI analyzes correctness and logic

Suggestions & corrected code are generated

Output is displayed to the user

🔐 Security Note

.env file is ignored and never committed

Always keep API keys private

Rotate secrets if accidentally exposed

📈 Future Improvements

✅ Support for multiple programming languages

✅ More detailed error explanations

✅ Code complexity analysis

✅ Web deployment

✅ User authentication

🤝 Contributing

Contributions are welcome! Feel free to:

Fork the repo

Create a feature branch

Submit a pull request

📄 License

This project is open-source and available under the MIT License.

🙌 Author

Prashant GitHub: @Prashant88123
