**Frontend**
# ShasthyaSetu

ShasthyaSetu is a web-based platform designed to provide users with easy access to healthcare services. The website allows users to browse available doctors, view their details, book appointments, and interact with healthcare professionals in a seamless and user-friendly environment. The platform supports the SDG 3 (Good Health and Well-being) by facilitating access to healthcare services for all.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Setup Instructions](#setup-instructions)
5. [Usage Guide](#usage-guide)
6. [Project Structure](#project-structure)
7. [Contributing](#contributing)
8. [License](#license)

## Introduction

ShasthyaSetu is a dynamic healthcare website that allows users to:

- Browse a list of healthcare professionals (e.g., doctors, pharmacists, neurologists).
- View detailed profiles of healthcare professionals, including their specialties, ratings, and more.
- Book an appointment with doctors directly through the website.
- Use a responsive, mobile-friendly interface to ensure access across devices.

## Features

- **Doctor Profiles**: Each healthcare professional has a detailed profile that includes their name, specialty, rating, and availability for appointments.
- **Appointment Booking**: Users can book an appointment with their preferred doctor by clicking the "Make an Appointment" button on the doctor’s profile page.
- **Rating System**: Users can see doctors’ ratings based on previous patient reviews, with the rating displayed as filled and unfilled stars.
- **Responsive Design**: The website is fully responsive and works seamlessly across desktop, tablet, and mobile devices.
- **Easy Navigation**: A simple and intuitive user interface makes it easy to find doctors and book appointments.

## Technologies Used

- **Frontend**: React.js, Tailwind CSS
- **Backend**: Node.js (optional, depending on your setup)
- **Database**: MongoDB (or another database, depending on your choice)
- **Routing**: Next.js (for dynamic routing)
- **APIs**: Optional, for fetching doctor details, ratings, and managing appointments.

## Setup Instructions

### Prerequisites

- Node.js (>= 14.x)
- npm (or yarn)

### Clone the Repository

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/shasthya-setu.git
   cd shasthya-setu
   ```

### Install Dependencies

2. Install project dependencies:

   ```bash
   npm install
   ```

   or if using yarn:

   ```bash
   yarn install
   ```

### Run the Development Server

3. Start the development server:

   ```bash
   npm run dev
   ```

   or with yarn:

   ```bash
   yarn dev
   ```

4. Open your browser and visit [http://localhost:3000](http://localhost:3000).

## Usage Guide

### Browsing Doctors

1. Upon visiting the homepage, you will be presented with a list of doctors.
2. Each doctor is displayed in a card format with their name, specialty, and rating.
3. You can click on the doctor’s name or image to view their **profile page**.

### Doctor Profile Page

1. The **Doctor Details Page** includes the doctor’s full profile with their specialty, ratings, and a brief bio.
2. You will also see an **appointment button** on the profile page.
3. Ratings are displayed with a star system, where filled stars represent the doctor’s rating based on user reviews.

### Booking an Appointment

1. On the doctor’s profile page, click the **"Make an Appointment"** button.
2. This will redirect you to the **appointment page**, where you can choose a date and time for your appointment.
3. Complete the necessary details (e.g., name, contact information, etc.) and submit the appointment request.
4. After submitting, you will receive a confirmation message, and your appointment will be scheduled.

### User Interaction

- **Appointment Confirmation**: After booking an appointment, users will receive a confirmation email or on-screen message with the appointment details (if integrated with email services).
- **Responsive Interface**: The interface is designed to be mobile-friendly, ensuring a seamless user experience on different devices.

## Project Structure

```plaintext
/shasthya-setu                         # Root directory of the project
│
├── /app                                # Main application logic and pages
│   ├── /doctor                         # Doctor-related pages and components
│   │   ├── [id].js                     # Dynamic doctor profile page (doctor details)
│   │   ├── DoctorList.js               # Displays all doctors with brief info
│   │   └── DoctorCard.js               # Individual doctor card component (used in DoctorList)
│   │
│   ├── /appointment                    # Appointment-related pages and components
│   │   ├── AppointmentPage.js          # Main page for appointment booking
│   │   └── AppointmentForm.js          # Form for selecting doctor, date, time
│   │
│   ├── /home                           # Homepage
│   │   ├── HomePage.js                 # Landing page with doctor cards
│   │   └── HeroSection.js              # Hero section at the top (intro, call-to-action)
│   │
│   └── /shared                         # Shared components across pages
│       ├── Navbar.js                   # Navigation bar
│       ├── Footer.js                   # Footer component
│       ├── RatingStars.js              # Star rating component for doctors
│       └── Button.js                   # Reusable button component
│
├── /public                             # Static files (images, fonts, etc.)
│   ├── /images                         # Folder for storing images (doctor images, logos)
│   │   └── doctor1.jpg                 # Example doctor image
│   └── favicon.ico                     # Favicon for the website
│
├── /components                         # Reusable UI components (Doctor profile, appointment, UI elements)
│   ├── /DoctorProfile                  # Components for displaying doctor details
│   ├── /Appointment                    # Components related to appointments (form, calendar)
│   └── /UI                             # UI components (cards, modals, buttons)
│
├── /hooks                              # Custom hooks for data fetching and form logic
│   ├── useGetAllDoctors.js             # Fetch all doctors
│   ├── useGetDoctor.js                 # Fetch specific doctor by ID
│   └── useSubmitAppointment.js         # Submit the appointment form
│
├── /styles                             # Styling-related files
│   ├── tailwind.config.js              # Tailwind CSS configuration
│   ├── globals.css                     # Global styles for the website
│
├── /pages                              # The main pages for routing in Next.js
│   ├── index.js                        # Main landing page (Home page)
│   └── /doctor                         # Folder for doctor-related routes
│       ├── [id].js                     # Dynamic route for displaying doctor details
│   ├── /appointment                    # Appointment-related routes
│   │   └── book.js                     # Appointment booking page
│
├── package.json                        # Project metadata and dependencies
├── tailwind.config.js                  # Tailwind CSS configuration file
└── README.md                           # Project documentation
```
## Contributing

We welcome contributions! Here’s how you can help improve the project:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add new feature'`)
5. Push to the branch (`git push origin feature-name`)
6. Open a pull request

Please make sure your code adheres to the project’s coding standards.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



**Backend**






# ShasthyaSetu - Personalized AI-Generated Health Tips API

ShasthyaSetu is a Django-based healthcare platform that provides personalized **AI-generated health tips** based on users' health data, such as **steps**, **heart rate**, and **mood**. The API allows users to create and view health data, and generate personalized health tips without requiring authentication.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Setup and Configuration](#setup-and-configuration)
- [Usage](#usage)
- [Testing the API](#testing-the-api)
- [Admin Panel](#admin-panel)
- [License](#license)

## Project Overview

ShasthyaSetu helps users track their health metrics, receive personalized health tips, and get insights into their wellness based on the data they input. The platform is built using **Django**, **Django REST Framework**, and **SQLite** as the database.

## Features

- **Create Health Data**: Users can create health data (e.g., steps, heart rate, mood) using the API.
- **Generate Health Tips**: The platform provides personalized health tips based on the health data of the user.
- **No Authentication Required**: The platform is open and does not require authentication for public access to health tips.
- **Django Admin Panel**: You can manage the health data and health tips using the Django admin panel.

## Installation

### Step 1: Clone the Repository
Clone the project repository to your local machine:

```bash
git clone https://github.com/yourusername/shasthyasetu.git
cd shasthyasetu
```

### Step 2: Set Up a Virtual Environment
Create and activate a virtual environment:

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies
Install the required Python packages from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

If you don't have `requirements.txt`, manually install the dependencies:
```bash
pip install django djangorestframework
```

### Step 4: Apply Migrations
Run the following commands to apply migrations and create the necessary tables in the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create a Superuser (Optional)
If you want to access the Django admin panel, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to create the superuser credentials.

### Step 6: Run the Server
Start the Django development server:

```bash
python manage.py runserver
```

Your API will be available at `http://127.0.0.1:8000/`.

## Setup and Configuration

- **Database**: By default, the project uses **SQLite** as the database.
- **Django REST Framework**: The API is built using **Django REST Framework (DRF)** for easy handling of HTTP requests and responses.

In **`settings.py`**, the **`INSTALLED_APPS`** should include the following:

```python
INSTALLED_APPS = [
    # other apps
    'rest_framework',
    'healthcare',
]
```

## Usage

### 1. Create Health Data
To create health data (e.g., steps, heart rate, or mood) for a user, send a `POST` request to the `/api/health-data/` endpoint with the following body:

#### Request:
```json
{
  "user_id": 1,
  "metric_type": "Steps",
  "value": 7000
}
```

#### Example cURL command:
```bash
curl -X POST http://127.0.0.1:8000/api/health-data/ \
-H "Content-Type: application/json" \
-d '{"user_id": 1, "metric_type": "Steps", "value": 7000}'
```

#### Expected Response:
```json
{
  "id": 1,
  "user_id": 1,
  "metric_type": "Steps",
  "value": 7000,
  "timestamp": "2024-12-06T12:00:00Z"
}
```

### 2. Generate Health Tips
To generate personalized health tips for a user, send a `POST` request to `/api/health-tips/` with the `user_id`.

#### Request:
```json
{
  "user_id": 1
}
```

#### Example cURL command:
```bash
curl -X POST http://127.0.0.1:8000/api/health-tips/ \
-H "Content-Type: application/json" \
-d '{"user_id": 1}'
```

#### Expected Response:
```json
{
  "id": 1,
  "tip": "Your activity level is low. Try to walk at least 10,000 steps daily.",
  "user_id": 1
}
```

### 3. View Health Tips
You can retrieve a list of all health tips by sending a `GET` request to `/api/health-tips/`.

```bash
curl http://127.0.0.1:8000/api/health-tips/
```

---

## Admin Panel

To manage **health data** and **health tips**, log in to the Django Admin panel:

- **URL**: `http://127.0.0.1:8000/admin/`
- **Superuser Credentials**: Use the credentials created when running `python manage.py createsuperuser`.

Once logged in, you can:
- Add, edit, or delete health data entries.
- Manage health tips for users.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Notes:
- **Health Data Models**: Users can input data such as steps, heart rate, and mood, and the system will generate relevant health tips.
- **Public Access**: This project allows public access to the health tips API with no authentication, making it easy to integrate with other services or apps.
```

