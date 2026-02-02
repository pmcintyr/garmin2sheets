import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from datetime import timedelta

# === CONFIGURATION ===
csv_file = 'Activities.csv'
google_sheets_doc = 'testfile'
credentials_file = 'credentials.json'


# === GOOGLE SHEETS AUTHENTICATION ===
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    credentials_file,
    ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
)
client = gspread.authorize(credentials)
sheet = client.open(google_sheets_doc).sheet1


# === LOAD CSV ===
df = pd.read_csv(csv_file)


# --- Convert Time to seconds (H:MM or H:MM:SS) ---
def to_seconds(t):
    if pd.isna(t):
        return 0
    parts = str(t).strip().split(':')
    try:
        parts = [float(p) for p in parts]
    except ValueError:
        return 0

    if len(parts) == 2:      # H:MM
        h, m = parts
        s = 0
    elif len(parts) == 3:    # H:MM:SS
        h, m, s = parts
    else:
        return 0

    return int(h * 3600 + m * 60 + s)


df["Seconds"] = df["Time"].apply(to_seconds)

# --- Handle Date ---
df["Date"] = pd.to_datetime(df["Date"], errors="coerce").dt.date
df = df.dropna(subset=["Date"])

# --- Sum by Date ---
grouped_df = df.groupby("Date").agg({"Distance": "sum", "Seconds": "sum"}).reset_index()

# --- Fill missing days between first and last ---
if not grouped_df.empty:
    full_range = pd.date_range(start=grouped_df["Date"].min(),
                               end=grouped_df["Date"].max()).date
    full_df = pd.DataFrame({"Date": full_range})
    grouped_df = full_df.merge(grouped_df, on="Date", how="left")
    grouped_df["Distance"] = grouped_df["Distance"].fillna(0)
    grouped_df["Seconds"] = grouped_df["Seconds"].fillna(0)

# --- Reverse order (latest first) ---
grouped_df = grouped_df[::-1]


# --- Prepare data for upload ---
existing_data = sheet.get_all_values()

new_data = []
for _, row in grouped_df.iterrows():
    total_seconds = int(row["Seconds"])
    h = total_seconds // 3600
    m = (total_seconds % 3600) // 60
    s = total_seconds % 60
    time_str = f"{h:02}:{m:02}:{s:02}"
    date_str = pd.to_datetime(row["Date"]).strftime("%d/%m/%Y")
    distance = row["Distance"]
    new_data.append([time_str, date_str, distance])

# Clean strings
new_data = [[str(v).lstrip("'") if isinstance(v, str) else v for v in row] for row in new_data]

# Combine with existing sheet data
final_data = existing_data + new_data


# --- Upload to Google Sheets ---
sheet.update("A1", final_data)

print("✅ Done. Empty days filled, time interpreted as H:MM and summed correctly.")
