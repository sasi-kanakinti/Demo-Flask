# YouFlask

## Overview

YouFlask is a Flask-based web application that allows users to watch and download YouTube videos. It provides a simple and intuitive interface for video management and downloading capabilities.

## Features

- YouTube video search
- Video download in multiple formats (MP4/MP3)
- Video quality selection
- User-friendly interface
- Download history tracking
- Responsive design for mobile devices

## Tech Stack

- Python 3.x
- Flask
- pytube
- Bootstrap 5
- SQLite/SQLAlchemy

## Installation

1. Clone the repository:

```bash
#git clone https://github.com/sasi-kanakinti/YouFlask.git
git clone https://github.com/username/YouFlask.git
cd YouFlask
```

2. Create and activate virtual environment:

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

1. Create a `.env` file in the root directory
2. Add your configuration:

```
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your_secret_key
```

## Usage

1. Start the server:

```bash
flask run
```

2. Open your browser and navigate to `http://127.0.0.1:5000`

3. Enter a YouTube URL to download or search for videos

## Project Structure

```
YouFlask/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   └── utils.py
├── static/
│   ├── css/
│   └── js/
├── templates/
├── .env
├── requirements.txt
└── README.md
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments

- [Flask Documentation](https://flask.palletsprojects.com/)
- [pytube](https://github.com/pytube/pytube)
- [Bootstrap](https://getbootstrap.com)
