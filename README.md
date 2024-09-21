# Flight Deal Finder (Project)
 
Flight Deal Finder is a Python-based project designed to help users discover the best flight deals by integrating multiple APIs, including Sheety and Amadeus. This tool automates the process of searching for flight prices from various sources and compiles the data into an easy-to-read format. Ideal for travelers looking for cost-effective flight options!

🚀 Features
Search for Flight Deals: Fetch real-time flight prices using the Amadeus API and filter them based on your destination, budget, and preferences.
Data Integration with Sheety API: Store and retrieve personalized flight deal information such as preferred routes and price limits from Google Sheets using the Sheety API.
User-Friendly Interface: Retrieve flight data in a well-organized dictionary format for easy processing and integration with front-end applications.
Environment Variables: Securely manage API keys using .env files with the help of python-dotenv.
🛠️ Tech Stack
Python: The core programming language for fetching and processing flight data.
APIs Used:
Amadeus API: Provides detailed flight information and allows users to search for flights across multiple airlines.
Sheety API: Facilitates seamless integration with Google Sheets to store and update flight prices dynamically.
Requests Library: For handling HTTP requests to the various APIs.
dotenv: For managing environment variables and API keys.
📈 How it Works
The user specifies their destination, budget, and travel preferences.
Amadeus API is called to fetch real-time flight data for the desired route.
The results are stored using the Sheety API for personalized tracking of flight deals over time.
The tool outputs the best flight deals in an easy-to-read format (dictionary or list).
🏗️ Setup Instructions
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/flight-deal-finder.git
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set up environment variables in a .env file:

plaintext
Copy code
SHEETY_TOKEN=your_sheety_token
AMADEUS_API_KEY=your_amadeus_api_key
AMADEUS_API_SECRET=your_amadeus_api_secret
Run the script:

bash
Copy code
python main.py
🔍 Future Enhancements
Add filtering options based on airline preferences, layovers, and travel dates.
Implement a notification system to alert users when flight prices drop below a certain threshold.
Integrate additional APIs for enhanced flight search capabilities.
