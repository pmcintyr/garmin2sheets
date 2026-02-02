# Garmin Training Data to Google Sheets

A simple Python script that automatically transfers your Garmin watch training data to Google Sheets for easy tracking and analysis. Stop manually copying data across platforms every week!

## 🎯 Overview

This project was born out of frustration with manually transferring training data between platforms. The script can be run as a Google Colab notebook, making it accessible from anywhere - even your phone!

## ✨ Features

- **Automated Data Transfer**: Seamlessly sync your Garmin training data to Google Sheets
- **Google Colab Support**: Run the script directly in your browser without local setup
- **Mobile-Friendly**: Execute from your phone using Google Colab
- **CSV Export**: Includes sample data structure for reference

## 📋 Prerequisites

- A Garmin Connect account with activity data
- Google account with Google Sheets access
- Google Cloud project with Sheets API enabled (for authentication)

## 🚀 Getting Started

### Option 1: Google Colab (Recommended)

1. Open the script in Google Colab
2. Upload your `credentials.json` file (Google API credentials)
3. Run the cells sequentially
4. Authorize access to your Google Sheets when prompted
5. Your Garmin data will be automatically synced!

### Option 2: Local Setup

1. Clone the repository:
```bash
git clone https://github.com/pmcintyr/garmintrainingdata.git
cd garmintrainingdata
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up Google Sheets API credentials:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select an existing one
   - Enable the Google Sheets API
   - Create credentials (OAuth 2.0 Client ID)
   - Download the credentials and save as `credentials.json`

4. Run the script:
```bash
python garminscript.py
```

## 📁 Project Structure

```
garmintrainingdata/
├── garminscript.py      # Main Python script
├── credentials.json     # Google API credentials (not tracked in git)
├── Activities.csv       # Sample activity data structure
└── README.md           # This file
```

## 🔐 Authentication

The script uses Google OAuth 2.0 for authentication. On first run:

1. A browser window will open asking you to authorize the application
2. Grant the necessary permissions
3. A token will be saved locally for future runs
4. Subsequent runs won't require re-authentication

## 📊 Data Structure

The script exports training data including (but not limited to):
- Activity date and time
- Activity type (run, bike, swim, etc.)
- Distance
- Duration
- Average heart rate
- Calories burned
- And more...

## 🛠️ Configuration

You can customize which metrics to export by modifying the script. Look for the data extraction section in `garminscript.py`.

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or find bugs:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Notes

- Keep your `credentials.json` file secure and never commit it to version control
- The script respects Garmin's API rate limits
- First-time setup requires a few extra steps for authentication

## 🐛 Troubleshooting

**Authentication Issues**: Make sure your `credentials.json` is properly configured and the Google Sheets API is enabled in your Google Cloud project.

**Data Not Syncing**: Verify that you have activities in your Garmin Connect account and that your Garmin credentials are correct.

**Import Errors**: Ensure all required Python packages are installed using `pip install -r requirements.txt`.

## 📄 License

This project is open source and available for personal use. Please check with Garmin's Terms of Service regarding data usage.

## 👤 Author

**pmcintyr**
- GitHub: [@pmcintyr](https://github.com/pmcintyr)

## 🙏 Acknowledgments

- Thanks to the Garmin Connect API community
- Google Sheets API documentation
- All contributors who help improve this tool

---

**Star ⭐ this repo if you find it helpful!**
