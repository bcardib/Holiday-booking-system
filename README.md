# HolidayPlanner

HolidayPlanner is a web application that allows users to book holiday packages, including city tours, beach holidays, and countryside getaways. The app provides features to search, filter, and add packages to a booking cart, then proceed to checkout for payment.

## Features

- **Browse and Search Packages:** Users can view a variety of holiday packages and filter them based on categories, price range, and duration.
- **Add to Cart:** Users can add selected packages to the booking cart and adjust the number of nights.
- **Checkout:** Users can proceed to checkout, provide shipping and payment details, and complete their purchase.
- **Admin Features:** Admins can create, edit, and delete holiday packages.

## Getting Started

### Prerequisites

To run this project locally, ensure you have the following installed:

- [Python 3.13](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/en/latest/) and other dependencies listed in `requirements.txt`

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/HolidayPlanner.git
2. **Navigate to the project directory:**
    ```bash
    cd HolidayPlanner
3. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
4. **Install dependencies:**
    ```bash
    pip install -r requirements.txt

### Running the Application

1. **Start the Flask server:**
    ```bash
    python app.py

2. **Open your browser and navigate to:**
    ```bash
    http://localhost:1204

### Stopping the Server and Clearing the Cart
To stop the server, press CTRL+C. This action will also clear the cart automatically to ensure a fresh start for the next session.

## Project Structure 
HolidayPlanner/
│
├── app.py                # Main application file
├── templates/            # HTML templates for the app
│   ├── home.jinja        # Home page template
│   ├── booking_cart.jinja# Booking cart page template
│   ├── checkout.jinja    # Checkout page template
│   └── other templates...
├── static/               # Static files (CSS, JS, images)
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation


## Usage
1. Browse packages on the home page and use the filters to find suitable holiday options.
2. Add packages to the booking cart and adjust the number of nights.
3. Proceed to checkout to finalize the booking by providing shipping and payment details.

## Admin Features
Admins have additional privileges to:

- Create new packages
- Edit existing packages
- Delete packages

## Development
### To contribute to this project:

1. Create a new branch for your feature:
   ```bash
    git checkout -b your-feature-branch

2. Make your changes and commit them:
   ```bash
    git add .
    git commit -m "Add your message here"

3. Push your changes to the remote branch:
   ```bash
    git push origin your-feature-branch

4. Create a pull request on GitHub:

## License
This project is open-source and available under the MIT License.

## Contact
For any questions, feel free to reach out to Bhakthi Salimath.

# Happy traveling with HolidayPlanner! 🌴✈️🏕️

This `README.md` provides a friendly overview of the project, including how to get started, usage, and contribution guidelines. Let me know if there's anything else you'd like to include!
