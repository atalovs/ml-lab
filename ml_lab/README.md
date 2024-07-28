## ML Lab Project

ML Lab is a Django-based web application designed to facilitate learning and practicing machine learning. The platform provides users with video lessons, interactive playgrounds, competitions, and more.

### Features

- **Home Page**: Welcome page with an introduction to ML Lab and featured video lessons.
- **Competitions**: A section dedicated to machine learning competitions.
- **Lessons**: A comprehensive collection of video lessons.
- **Playground**: An interactive environment to experiment with machine learning models and datasets.
- **About**: Information about the ML Lab platform.

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd ml_lab
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   Open your web browser and navigate to `http://127.0.0.1:8000/`.

8. **Admin panel**:
   Access the admin panel at `http://127.0.0.1:8000/admin/` to manage content.

### Application Structure

- **ml_learning/**: Project configuration directory.
  
- **main/**: Main application.

- **competitions/**: Competitions application.

- **lessons/**: Lessons application.

- **playground/**: Playground application.

### Adding Video Lessons

To add new video lessons, follow these steps:

1. Log in to the admin panel at `http://127.0.0.1:8000/admin/`.
2. Navigate to the **Lessons** section.
3. Click on **Add Lesson**.
4. Fill in the details for the lesson (title, description, and YouTube URL).
5. Save the lesson.
6. The new lesson will be displayed on the Lessons page at `http://127.0.0.1:8000/lessons/`.

### Customization

You can customize the content and appearance of the ML Lab platform by modifying the templates and views in their respective application directories. For example, to update the home page content, edit `main/templates/main/home.html`.

### Contributions

We welcome contributions to improve the ML Lab platform. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push the branch to your fork.
4. Submit a pull request with a detailed description of your changes.
