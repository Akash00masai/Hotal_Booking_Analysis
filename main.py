import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# Load the dataset
# df = pd.read_csv('Hotel_Reservations.csv')

# # 1. Dataset Processing (Excluding 1.2 to 1.5)
# # Handle missing values
# df.dropna(inplace=True)

# # Remove duplicates
# df.drop_duplicates(inplace=True)

# # Convert 'arrival_date' to datetime
# df['arrival_date'] = pd.to_datetime(df['arrival_date'])

# # Extract useful features from 'arrival_date'
# df['arrival_day'] = df['arrival_date'].dt.day
# df['arrival_month'] = df['arrival_date'].dt.month
# df['arrival_year'] = df['arrival_date'].dt.year
# df['is_weekend'] = df['arrival_date'].dt.weekday >= 5  # 5 and 6 correspond to Saturday and Sunday
# df['is_weekend'] = df['is_weekend'].astype(int)

# # Convert 'booking_status' to binary
# df['booking_status'] = df['booking_status'].apply(lambda x: 1 if x == 'Canceled' else 0)

# Load the Clean dataset
df = pd.read_csv("Hotel_Reservations_Cleaned.csv")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Handle missing values (if any)
df.dropna(inplace=True)

# 2. Exploratory Data Analysis (EDA)
# 2.1 Visualize distributions
plt.figure(figsize=(12, 6))
sns.histplot(df['lead_time'], bins=30, kde=True)
plt.title('Distribution of Lead Time')
plt.xlabel('Lead Time')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(12, 6))
sns.histplot(df['avg_price_per_room'], bins=30, kde=True)
plt.title('Distribution of Average Price per Room')
plt.xlabel('Average Price per Room')
plt.ylabel('Frequency')
plt.show()

# 2.2 Analyze booking distribution
plt.figure(figsize=(12, 6))
sns.countplot(x='room_type_reserved', data=df)
plt.title('Bookings by Room Type')
plt.xlabel('Room Type')
plt.ylabel('Number of Bookings')
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(x='market_segment_type', data=df)
plt.title('Bookings by Market Segment')
plt.xlabel('Market Segment')
plt.ylabel('Number of Bookings')
plt.show()

# 2.3 Investigate relationships
plt.figure(figsize=(12, 6))
sns.scatterplot(x='lead_time', y='avg_price_per_room', hue='booking_status', data=df)
plt.title('Lead Time vs. Average Price per Room')
plt.xlabel('Lead Time')
plt.ylabel('Average Price per Room')
plt.show()

# 2.4 Analyze seasonal trends
plt.figure(figsize=(12, 6))
sns.countplot(x='arrival_month', data=df)
plt.title('Bookings by Month')
plt.xlabel('Month')
plt.ylabel('Number of Bookings')
plt.show()

# 3. Cancellations Analysis
# 3.1 Compare canceled vs. non-canceled bookings
canceled = df[df['booking_status'] == 1]
not_canceled = df[df['booking_status'] == 0]

plt.figure(figsize=(12, 6))
sns.boxplot(x='booking_status', y='lead_time', data=df)
plt.title('Lead Time for Canceled vs. Non-Canceled Bookings')
plt.xlabel('Booking Status (0: Not Canceled, 1: Canceled)')
plt.ylabel('Lead Time')
plt.show()

plt.figure(figsize=(12, 6))
sns.boxplot(x='booking_status', y='avg_price_per_room', data=df)
plt.title('Average Price per Room for Canceled vs. Non-Canceled Bookings')
plt.xlabel('Booking Status (0: Not Canceled, 1: Canceled)')
plt.ylabel('Average Price per Room')
plt.show()

# 3.2 Analyze repeated guests
plt.figure(figsize=(12, 6))
sns.countplot(x='repeated_guest', hue='booking_status', data=df)
plt.title('Cancellations by Repeated Guests')
plt.xlabel('Repeated Guest (0: No, 1: Yes)')
plt.ylabel('Number of Bookings')
plt.show()

# 3.3 Analyze special requests and room types
plt.figure(figsize=(12, 6))
sns.countplot(x='no_of_special_requests', hue='booking_status', data=df)
plt.title('Cancellations by Number of Special Requests')
plt.xlabel('Number of Special Requests')
plt.ylabel('Number of Bookings')
plt.show()

# 3.4 Analyze lead time and price
plt.figure(figsize=(12, 6))
sns.scatterplot(x='lead_time', y='avg_price_per_room', hue='booking_status', data=df)
plt.title('Lead Time vs. Average Price per Room (Canceled vs. Non-Canceled)')
plt.xlabel('Lead Time')
plt.ylabel('Average Price per Room')
plt.show()

# 3.5 Analyze market segments
plt.figure(figsize=(12, 6))
sns.countplot(x='market_segment_type', hue='booking_status', data=df)
plt.title('Cancellations by Market Segment')
plt.xlabel('Market Segment')
plt.ylabel('Number of Bookings')
plt.show()

# 4. Data Aggregation and Grouping
# 4.1 Group data by relevant categories
cancellation_rates = df.groupby('market_segment_type')['booking_status'].mean().reset_index()
cancellation_rates.columns = ['market_segment_type', 'cancellation_rate']

# 4.2 Visualize aggregated results
plt.figure(figsize=(12, 6))
sns.barplot(x='market_segment_type', y='cancellation_rate', data=cancellation_rates)
plt.title('Cancellation Rates by Market Segment')
plt.xlabel('Market Segment')
plt.ylabel('Cancellation Rate')
plt.show()

# 5. Correlation and Feature Importance Analysis
# 5.1 Calculate correlation matrix
# df_numerical = df.select_dtypes(include=["number"])  # Select numerical columns only
# corr_matrix = df_numerical.corr()

# Select numerical columns
df_numerical = df.select_dtypes(include=["number"])

# Identify and remove columns with only one unique value
constant_columns = df_numerical.nunique()[df_numerical.nunique() == 1].index.tolist()
df_numerical = df_numerical.drop(columns=constant_columns)

# Compute correlation matrix and handle NaN values
corr_matrix = df_numerical.corr().fillna(0)

# Plot the heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Feature Correlation Heatmap")
plt.show()

# 5.2 Visualize correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# 6. Data Visualization
# 6.1 Create visualizations
plt.figure(figsize=(12, 6))
sns.countplot(x='arrival_month', hue='booking_status', data=df)
plt.title('Bookings and Cancellations by Month')
plt.xlabel('Month')
plt.ylabel('Number of Bookings')
plt.show()

plt.figure(figsize=(12, 6))
sns.boxplot(x='room_type_reserved', y='avg_price_per_room', hue='booking_status', data=df)
plt.title('Average Price per Room by Room Type (Canceled vs. Non-Canceled)')
plt.xlabel('Room Type')
plt.ylabel('Average Price per Room')
plt.show()


# 6.2 Use pair plots
sns.pairplot(df[['lead_time', 'avg_price_per_room', 'no_of_week_nights', 'booking_status']], hue='booking_status')
plt.show()



# 7. SQL Database Integration
# 7.1 Set up MySQL connection
# Replace 'username', 'password', 'host', and 'database_name' with your MySQL credentials
from sqlalchemy import create_engine
db_url = 'mysql+pymysql://root:Akash1999@localhost/hotal_db'
engine = create_engine(db_url)

# # Test the connection
# try:
#     connection = engine.connect()
#     print("Connection successful!")
# except Exception as e:
#     print(f"Connection failed: {e}")

# 7.2 Load the cleaned dataset into MySQL
df.to_sql('Hotel_Reservations_Cleaned', con=engine, if_exists='replace', index=False)

# 7.3 Perform SQL queries
# Query 1: Average cancellation rate by market segment
query1 = """
SELECT market_segment_type, AVG(booking_status) AS cancellation_rate
FROM Hotel_Reservations_Cleaned
GROUP BY market_segment_type;
"""
result1 = pd.read_sql(query1, engine)
print("\nAverage Cancellation Rate by Market Segment:")
print(result1)

# Query 2: Average Lead Time for Canceled vs. Non-Canceled Bookings
query2 = """
SELECT booking_status, AVG(lead_time) AS avg_lead_time
FROM Hotel_Reservations_Cleaned
GROUP BY booking_status;
"""
result2 = pd.read_sql(query2, engine)
print("\n\nAverage Lead Time for Canceled vs. Non-Canceled Bookings:")
print(result2)

# Query 3: Number of Bookings by Room Type
query3 = """
SELECT room_type_reserved, COUNT(*) AS num_bookings
FROM Hotel_Reservations_Cleaned
GROUP BY room_type_reserved;
"""
result3 = pd.read_sql(query3, engine)
print("\n\nNumber of Bookings by Room Type:")
print(result3)

# Query 4: Cancellation Rate by Number of Special Requests
query4 = """
SELECT no_of_special_requests, AVG(booking_status) AS cancellation_rate
FROM Hotel_Reservations_Cleaned
GROUP BY no_of_special_requests;
"""
result4 = pd.read_sql(query4, engine)
print("\n\nCancellation Rate by Number of Special Requests:")
print(result4)

# Query 5: Average Price per Room by Room Type
query5 = """
SELECT room_type_reserved, AVG(avg_price_per_room) AS avg_price
FROM Hotel_Reservations_Cleaned
GROUP BY room_type_reserved;
"""
result5 = pd.read_sql(query5, engine)
print("\n\nAverage Price per Room by Room Type:")
print(result5)

# Query 6: Booking Distribution by Arrival Month
query6 = """
SELECT arrival_month, COUNT(*) AS num_bookings
FROM Hotel_Reservations_Cleaned
GROUP BY arrival_month
ORDER BY arrival_month;
"""
result6 = pd.read_sql(query6, engine)
print("\n\nBooking Distribution by Arrival Month:")
print(result6)

# Query 7: Cancellation Rate by Repeated Guests
query7 = """
SELECT repeated_guest, AVG(booking_status) AS cancellation_rate
FROM Hotel_Reservations_Cleaned
GROUP BY repeated_guest;
"""
result7 = pd.read_sql(query7, engine)
print("\n\nCancellation Rate by Repeated Guests:")
print(result7)

# Query 8: Average Number of Adults and Children per Booking
query8 = """
SELECT AVG(no_of_adults) AS avg_adults, AVG(no_of_children) AS avg_children
FROM Hotel_Reservations_Cleaned;
"""
result8 = pd.read_sql(query8, engine)
print("\n\nAverage Number of Adults and Children per Booking:")
print(result8)

# Query 9: Cancellation Rate by Meal Plan
query9 = """
SELECT type_of_meal_plan, AVG(booking_status) AS cancellation_rate
FROM Hotel_Reservations_Cleaned
GROUP BY type_of_meal_plan;
"""
result9 = pd.read_sql(query9, engine)
print("\n\nCancellation Rate by Meal Plan:")
print(result9)

# Query 10: Average Lead Time by Market Segment
query10 = """
SELECT market_segment_type, AVG(lead_time) AS avg_lead_time
FROM Hotel_Reservations_Cleaned
GROUP BY market_segment_type;
"""
result10 = pd.read_sql(query10, engine)
print("\n\nAverage Lead Time by Market Segment:")
print(result10)

# Query 11: Number of Bookings by Number of Weekend Nights
query11 = """
SELECT no_of_weekend_nights, COUNT(*) AS num_bookings
FROM Hotel_Reservations_Cleaned
GROUP BY no_of_weekend_nights
ORDER BY no_of_weekend_nights;
"""
result11 = pd.read_sql(query11, engine)
print("\n\nNumber of Bookings by Number of Weekend Nights:")
print(result11)

# Query 12: Cancellation Rate by Required Car Parking Space
query12 = """
SELECT required_car_parking_space, AVG(booking_status) AS cancellation_rate
FROM Hotel_Reservations_Cleaned
GROUP BY required_car_parking_space;
"""
result12 = pd.read_sql(query12, engine)
print("\n\nCancellation Rate by Required Car Parking Space:")
print(result12)


