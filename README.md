# Pet Veterinary Clinic System

Pet Veterinary Clinic System is a comprehensive web-based solution designed to streamline operations for veterinary clinics. The system caters to pet owners and veterinary staff, ensuring efficient management of appointments, pet health records, billing, and more.

## Project Overview

The Pet Veterinary Clinic System is designed to simplify the management of both administrative and medical tasks within a veterinary clinic. The system provides a seamless experience for both pet owners and veterinary staff to manage appointments, access medical records, and process payments.

The system is built using **Django** for the backend and **HTML** for the frontend, providing a robust platform for managing clinic operations. It is designed with two main user roles:

1. **Pet Owners**: Can book appointments, view pet health records, and access their billing history.
2. **Veterinary Staff**: Can manage appointments, update pet health records, and generate invoices for completed appointments.

The goal of this project is to improve clinic efficiency, reduce administrative workload, and ensure pets receive timely care.

## Technologies Used

Frontend:
    - HTML: For the structure of web pages.
    - Bootstrap CSS: For styling and layout of the frontend.
    - JavaScript: Used for dynamic client-side functionality and interactivity.
Backend:
    - Python: The primary language for backend development.
    - Django: The web framework for building the backend and managing the database.

## Database

We are using **SQLite** as the local database for this project. By default, Django comes with SQLite as the backend database, which is lightweight and easy to configure. It is suitable for development and testing purposes. You don't need to install any additional database management systems to get started with this project.

## Features

### User Side (Pet Owners):

- Book Appointments: Schedule consultations for their pets online.
- Access Medical Records: View their pets’ vaccination schedules and health history.
- Billing and payments history for appointments.

### Vet Side (Management):

- Appointment Management: Track, update, and confirm bookings.
- Pet Health Records: Store and manage detailed medical records and procedures.
- Billing Management: Generate an invoice after a complete appointment request.

## Installation

To get started with the Pet Veterinary Clinic System, follow these steps:

### 1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/karl2522/PetVet.git
    ```

### 2. Navigate to the project directory:

    ```bash
    cd mainpages
    ```

### 3. Create a virtual environment:

    ```bash
    python3 -m venv venv
    ```

### 4. Activate the virtual environment:

    For **macOS/Linux**:

    ```bash
    source venv/bin/activate
    ```

    For **Windows**:

    ```bash
    venv\Scripts\activate
    ```

### 5. Apply Database Migrations:
    Since we are using SQLite as the local database, no additional configuration is needed. Run the following command to apply migrations:

    ```bash
    python manage.py migrate
    ```

### 6. Run the Development Server:

    ```bash
    python manage.py runserver
    ```





