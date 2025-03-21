
use hotal_db;

select * from hotel_reservations_cleaned;

-- Average cancellation rate by market segment 
SELECT market_segment_type, AVG(booking_status) AS cancellation_rate
FROM Hotel_Reservations_Cleaned
GROUP BY market_segment_type;

-- Average Lead Time for Canceled vs. Non-Canceled Bookings 
SELECT booking_status, AVG(lead_time) AS avg_lead_time
FROM Hotel_Reservations_Cleaned
GROUP BY booking_status;

-- Number of Bookings by Room Type 
SELECT room_type_reserved, COUNT(*) AS num_bookings
FROM Hotel_Reservations_Cleaned
GROUP BY room_type_reserved;

-- Cancellation Rate by Number of Special Requests 
SELECT no_of_special_requests, AVG(booking_status) AS cancellation_rate
FROM Hotel_Reservations_Cleaned
GROUP BY no_of_special_requests;

-- Average Price per Room by Room Type
SELECT room_type_reserved, AVG(avg_price_per_room) AS avg_price
FROM Hotel_Reservations_Cleaned
GROUP BY room_type_reserved;

-- Booking Distribution by Arrival Month 
SELECT arrival_month, COUNT(*) AS num_bookings
FROM Hotel_Reservations_Cleaned
GROUP BY arrival_month
ORDER BY arrival_month;

-- Cancellation Rate by Repeated Guests 
SELECT repeated_guest, AVG(booking_status) AS cancellation_rate
FROM Hotel_Reservations_Cleaned
GROUP BY repeated_guest;

-- Average Number of Adults and Children per Booking 
SELECT AVG(no_of_adults) AS avg_adults, AVG(no_of_children) AS avg_children
FROM Hotel_Reservations_Cleaned;

-- Cancellation Rate by Meal Plan 
SELECT type_of_meal_plan, AVG(booking_status) AS cancellation_rate
FROM Hotel_Reservations_Cleaned
GROUP BY type_of_meal_plan;

-- Average Lead Time by Market Segment 
SELECT market_segment_type, AVG(lead_time) AS avg_lead_time
FROM Hotel_Reservations_Cleaned
GROUP BY market_segment_type;

-- Number of Bookings by Number of Weekend Nights 
SELECT no_of_weekend_nights, COUNT(*) AS num_bookings
FROM Hotel_Reservations_Cleaned
GROUP BY no_of_weekend_nights
ORDER BY no_of_weekend_nights;

-- Cancellation Rate by Required Car Parking Space 
SELECT required_car_parking_space, AVG(booking_status) AS cancellation_rate
FROM Hotel_Reservations_Cleaned
GROUP BY required_car_parking_space;
