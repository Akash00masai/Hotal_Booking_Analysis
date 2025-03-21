# **  Hotal_Booking_Analysis **

## **Overview**
This Power BI Dashboard is a 2-page interactive report designed for **hotel reservation analytics**. It provides insights into occupancy trends, revenue performance, customer behavior, and special requests to aid in data-driven decision-making.

---
## ** Page 1: Business Overview & KPIs**
### **🔹 Key Performance Indicators (KPIs)**
1. **Occupancy Rate (Gauge Chart)**  Occupancy Rate (Gauge) – Measures the percentage of booked rooms vs. total available rooms.
   - **DAX Formula:**
     ```DAX
     Occupancy Rate = 
     DIVIDE(
         COUNTROWS('Hotel_Reservations_Cleaned'), 
         COUNTROWS(ALL('Hotel_Reservations_Cleaned'))
     ) * 100
     ```
   - **Min Value:** 0 | **Max Value:** 100 | **Color:** Green to Red

2. **Cancellation Rate (Gauge Chart)**  Cancellation Rate (Gauge) – Shows the percentage of canceled bookings.
   - **DAX Formula:**
     ```DAX
     Cancellation Rate = 
     DIVIDE(
         CALCULATE(COUNTROWS('Hotel_Reservations_Cleaned'), 'Hotel_Reservations_Cleaned'[booking_status] = 1), 
         COUNTROWS('Hotel_Reservations_Cleaned')
     ) * 100
     ```
   - **Color:** Red to Green

3. **Average Lead Time (Card)**  Average Lead Time (Card) – Displays the average time between booking and check-in.
   - **DAX Formula:**
     ```DAX
     Avg Lead Time = AVERAGE('Hotel_Reservations_Cleaned'[lead_time])
     ```

4. **Revenue per Available Room (RevPAR) (Card)**  Revenue per Available Room (RevPAR) (Card) – Evaluates revenue efficiency per available room.
   - **DAX Formula:**
     ```DAX
     RevPAR = 
     DIVIDE(
         SUM('Hotel_Reservations_Cleaned'[avg_price_per_room]), 
         COUNTROWS(ALL('Hotel_Reservations_Cleaned'))
     )
     ```

5. **Customer Retention Rate (Gauge Chart)** Customer Retention Rate (Gauge) – Indicates the percentage of returning customers.
   - **DAX Formula:**
     ```DAX
     Retention Rate = 
     DIVIDE(
         CALCULATE(COUNTROWS('Hotel_Reservations_Cleaned'), 'Hotel_Reservations_Cleaned'[repeated_guest] = 1), 
         COUNTROWS('Hotel_Reservations_Cleaned')
     ) * 100
     ```

### **🔹 Visualizations**
- **Line Chart:** Occupancy Rate Over Time
- **Stacked Bar Chart:** Cancellation Rate by Market Segment
- **Bar Chart:** Average Lead Time by Room Type
- **Pie Chart:** Booking Distribution (Repeated vs. New Customers)
- **Stacked Column Chart:** Revenue by Market Segment
- **Line Chart:** Revenue Trend Over Time

### **🔹 Filters & Navigation**
- **Slicers:** Arrival Year, Arrival Month, Market Segment Type, Room Type
- **Navigation Button:** Next Page → Customer Behavior & Special Requests

---
## ** Page 2: Customer Behavior & Special Requests**
### **🔹 Customer Behavior Insights**
- **Retention Rate (Gauge Chart)**
- **Average Special Requests per Booking (Card)**

### **🔹 Special Requests Analysis**
- **Donut Chart:** Special Requests Fulfillment Rate
- **Bar Chart:** Special Requests by Room Type

### **🔹 Filters & Navigation**
- **Slicers:** Arrival Month, Market Segment Type, Special Requests
- **Navigation Buttons:** 
  - Previous Page → Business Overview & KPIs

--- 
## **✅ Dashboard Completed! **

