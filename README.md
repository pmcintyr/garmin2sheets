# Garmin Training Data to Google Sheets

A simple Python script that automatically transfers your Garmin watch training data to Google Sheets for easy tracking and analysis. Stop manually copying data across platforms every week!

## 🎯 Overview

This project was born out of frustration with manually transferring training data between platforms. The script can be run as a Google Colab notebook, making it accessible from anywhere - even your phone!

## ✨ Features

- **Automated Data Transfer**: Seamlessly sync your Garmin training data to Google Sheets
- **Google Colab Support**: Run the script directly in your browser without local setup
- **Mobile-Friendly**: Execute from your phone using Google Colab
- **CSV Export**: Includes sample data structure for reference

## 📝 Quick Start Checklist

Before you begin, make sure you have:

- [ ] Downloaded your activities CSV from Garmin Connect
- [ ] Created a Google Cloud project with Sheets and Drive APIs enabled
- [ ] Downloaded your `credentials.json` file
- [ ] Created a Google Sheet (or noted the name of an existing one)
- [ ] Updated the configuration variables in `garminscript.py`

## 📋 Prerequisites

- A Garmin Connect account with activity data
- Google account with Google Sheets access
- Google Cloud project with Sheets API enabled (for authentication)

## 🚀 Getting Started

### Step 1: Download Your Garmin Data

1. Log in to [Garmin Connect](https://connect.garmin.com/)
2. Navigate to Activities
3. Export your activities as a CSV file
4. Save the file as `Activities.csv` (or note the filename for configuration)

### Step 2: Set Up Google Sheets API

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the **Google Sheets API** and **Google Drive API**
4. Create credentials (OAuth 2.0 Client ID)
   - Application type: Desktop app
5. Download the credentials and save as `credentials.json`

### Step 3: Run the Script

#### Option A: Google Colab (Recommended)

1. Open the script in Google Colab
2. **Connect to Google Drive** when prompted (required to access your files)
3. Upload your `credentials.json` file to Colab or Drive
4. Upload your `Activities.csv` file from Garmin Connect
5. **Configure the script** (see Configuration section below)
6. Run the cells sequentially
7. Authorize access when prompted
8. Your data will be synced to your specified Google Sheet!

#### Option B: Local Setup

1. Clone the repository:
```bash
git clone https://github.com/pmcintyr/garmintrainingdata.git
cd garmintrainingdata
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Place your files:
   - Add `credentials.json` to the project directory
   - Add your Garmin `Activities.csv` to the project directory

4. Configure the script (see Configuration section below)

5. Run the script:
```bash
python garminscript.py
```

## 🛠️ Configuration

Before running the script, you need to configure three variables at the beginning of `garminscript.py`:

```python
# === CONFIGURATION ===
csv_file = 'Activities.csv'          # Name of your Garmin activities CSV file
google_sheets_doc = 'testfile'       # Name of your Google Sheets document
credentials_file = 'credentials.json' # Your Google API credentials file
```

**Configuration Steps:**

1. **csv_file**: Set this to the name of your downloaded Garmin activities CSV file
   - Default: `'Activities.csv'`
   - Change if you named your file differently

2. **google_sheets_doc**: Set this to the name of the Google Sheet where you want your data
   - Default: `'testfile'`
   - **Important**: Create a Google Sheet with this exact name before running the script, or change this value to match an existing sheet

3. **credentials_file**: Set this to your Google API credentials filename
   - Default: `'credentials.json'`
   - Only change if you named your credentials file differently

## 📁 Project Structure

```
garmintrainingdata/
├── garminscript.py      # Main Python script
├── credentials.json     # Google API credentials (not tracked in git)
├── Activities.csv       # Sample activity data structure
└── README.md           # This file
```

## 🔐 Authentication

The script uses Google OAuth 2.0 for authentication and requires access to both Google Sheets and Google Drive.

**First Run:**

1. The script will prompt you to connect to **Google Drive** (necessary to access your files)
2. A browser window will open asking you to authorize the application
3. Grant permissions for both **Google Sheets** and **Google Drive** access
4. A token will be saved locally for future runs
5. Subsequent runs won't require re-authentication

**Required Permissions:**
- Google Sheets API (to write data)
- Google Drive API (to access and manage files)

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

**"File not found" errors**: 
- Ensure `Activities.csv` is in the same directory as the script
- Verify the `csv_file` variable matches your actual CSV filename
- In Google Colab, make sure you've connected to Google Drive and uploaded the file

**Authentication Issues**: 
- Make sure your `credentials.json` is properly configured
- Verify that both Google Sheets API and Google Drive API are enabled in your Google Cloud project
- Try deleting the saved token and re-authenticating

**Google Sheets not found**: 
- Create a Google Sheet with the exact name specified in `google_sheets_doc`
- Or update the `google_sheets_doc` variable to match an existing sheet name
- Make sure you're signed in to the correct Google account

**Data Not Syncing**: 
- Verify that your `Activities.csv` contains data and is properly formatted
- Check that you've downloaded the CSV from Garmin Connect correctly
- Ensure the CSV follows Garmin's standard export format

**Import Errors**: 
- Ensure all required Python packages are installed: `pip install -r requirements.txt`
- Common packages needed: `gspread`, `oauth2client`, `pandas`

**Google Colab specific issues**:
- Remember to connect to Google Drive at the start of your session
- Re-upload files if your Colab session disconnects
- Check that file paths are correct for the Colab environment

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
