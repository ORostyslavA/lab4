use lab4;

INSERT INTO `river_types` (type_description) VALUES 
('Mountain River'), ('Lowland River'), ('Delta River'), ('Glacial River'), ('Tropical River'),
('Temperate River'), ('Desert River'), ('Underground River'), ('Seasonal River'), ('Perennial River');

INSERT INTO `rivers` (river_name, river_length, river_depth, river_types_id, river_country) VALUES  
('Amazon', 6400, 50.5, 5, 'Brazil'), 
('Nile', 6650, 45.2, 2, 'Egypt'), 
('Yangtze', 6300, 30.3, 6, 'China'), 
('Mississippi', 3730, 20.5, 2, 'USA'), 
('Danube', 2850, 19.1, 6, 'Europe'), 
('Congo', 4700, 25.0, 5, 'Democratic Republic of the Congo'), 
('Mekong', 4350, 10.2, 5, 'Southeast Asia'), 
('Rhine', 1233, 6.4, 1, 'Germany'), 
('Thames', 346, 5.0, 2, 'United Kingdom'), 
('Ganges', 2525, 12.3, 5, 'India'), 
('Murray', 2508, 8.5, 2, 'Australia'), 
('Seine', 777, 3.5, 2, 'France'), 
('Zambezi', 2574, 16.7, 5, 'Africa'), 
('Volga', 3530, 24.8, 6, 'Russia'), 
('Po', 652, 7.1, 2, 'Italy');


INSERT INTO `regions` (region_name, country) VALUES 
('Amazonas', 'Brazil'), ('Upper Egypt', 'Egypt'), ('Hubei', 'China'), ('Louisiana', 'USA'),
('Bavaria', 'Germany'), ('Kinshasa', 'Democratic Republic of the Congo'), ('Mekong Delta', 'Vietnam'),
('Basel', 'Switzerland'), ('Greater London', 'United Kingdom'), ('Uttar Pradesh', 'India'),
('New South Wales', 'Australia'), ('Île-de-France', 'France'), ('Western Province', 'Zambia'),
('Poltava Oblast', 'Ukraine'), ('Lombardy', 'Italy');

INSERT INTO `measurement_locations` (location_name, latitude, longitude, rivers_id, regions_id) VALUES 
('Manaus', -3.1190, -60.0217, 1, 1), ('Aswan', 24.0889, 32.8998, 2, 2),
('Wuhan', 30.5928, 114.3055, 3, 3), ('New Orleans', 29.9511, -90.0715, 4, 4),
('Regensburg', 49.0134, 12.1016, 5, 5), ('Kinshasa City', -4.4419, 15.2663, 6, 6),
('Can Tho', 10.0452, 105.7469, 7, 7), ('Basel City', 47.5596, 7.5806, 8, 8),
('London Bridge', 51.5079, -0.0877, 9, 9), ('Varanasi', 25.3176, 82.9739, 10, 10),
('Mildura', -34.1859, 142.1578, 11, 11), ('Paris', 48.8566, 2.3522, 12, 12),
('Victoria Falls', -17.9243, 25.8572, 13, 13), ('Zaporizhzhia', 47.8388, 35.1396, 14, 14),
('Ferrara', 44.8378, 11.6194, 15, 15);

INSERT INTO `water_levels` (water_level_value, measurement_locations_id, start_date, end_date) VALUES 
(5.2, 1, '2023-01-01', '2023-01-31'), (7.8, 2, '2023-01-01', '2023-01-31'),
(4.5, 3, '2023-01-01', '2023-01-31'), (3.2, 4, '2023-01-01', '2023-01-31'),
(2.7, 5, '2023-01-01', '2023-01-31'), (6.1, 6, '2023-01-01', '2023-01-31'),
(3.9, 7, '2023-01-01', '2023-01-31'), (2.3, 8, '2023-01-01', '2023-01-31'),
(1.8, 9, '2023-01-01', '2023-01-31'), (8.5, 10, '2023-01-01', '2023-01-31'),
(2.1, 11, '2023-01-01', '2023-01-31'), (3.6, 12, '2023-01-01', '2023-01-31'),
(4.7, 13, '2023-01-01', '2023-01-31'), (3.3, 14, '2023-01-01', '2023-01-31'),
(2.9, 15, '2023-01-01', '2023-01-31');

INSERT INTO `hydrological_objects` (object_type, object_description) VALUES 
('Dam', 'Large concrete structure for water control'),
('Bridge', 'Structure spanning the river for transportation'),
('Locks', 'Water elevator for ship navigation'),
('Weir', 'Low dam built across a river to raise the water level'),
('Barrage', 'Artificial barrier across a river'),
('Levee', 'Embankment built to prevent overflow'),
('Floodgate', 'Adjustable gate to control water flow'),
('Reservoir', 'Artificial lake for water storage'),
('Aqueduct', 'Bridge for conveying water across a valley'),
('Culvert', 'Tunnel carrying a stream under a road'),
('Hydroelectric Plant', 'Facility for generating electricity from water'),
('Fish Ladder', 'Structure allowing fish to pass over dams'),
('Intake', 'Structure to extract water from the river'),
('Outfall', 'Discharge point of a waste stream into a river'),
('Pumping Station', 'Facility to move water from low to high elevation');

INSERT INTO `users` (user_name, user_surname, user_email) VALUES 
('John', 'Doe', 'john.doe@email.com'),
('Jane', 'Smith', 'jane.smith@email.com'),
('Alice', 'Johnson', 'alice.johnson@email.com'),
('Bob', 'Williams', 'bob.williams@email.com'),
('Charlie', 'Brown', 'charlie.brown@email.com'),
('Diana', 'Davis', 'diana.davis@email.com'),
('Edward', 'Miller', 'edward.miller@email.com'),
('Fiona', 'Wilson', 'fiona.wilson@email.com'),
('George', 'Moore', 'george.moore@email.com'),
('Hannah', 'Taylor', 'hannah.taylor@email.com'),
('Ian', 'Anderson', 'ian.anderson@email.com'),
('Julia', 'Thomas', 'julia.thomas@email.com'),
('Kevin', 'Jackson', 'kevin.jackson@email.com'),
('Laura', 'White', 'laura.white@email.com'),
('Michael', 'Harris', 'michael.harris@email.com');

INSERT INTO `meteorological_conditions` (condition_type, condition_description) VALUES 
('Sunny', 'Clear sky with abundant sunshine'),
('Cloudy', 'Sky covered with clouds'),
('Rainy', 'Precipitation in the form of water droplets'),
('Snowy', 'Precipitation in the form of snow'),
('Windy', 'Strong air movement'),
('Foggy', 'Low-lying clouds reducing visibility'),
('Stormy', 'Severe weather with strong winds and rain'),
('Hail', 'Precipitation of balls or lumps of ice'),
('Sleet', 'Mix of rain and snow'),
('Freezing Rain', 'Rain that freezes on contact with surfaces'),
('Heat Wave', 'Prolonged period of excessively hot weather'),
('Cold Snap', 'Sudden onset of cold weather'),
('Humid', 'High moisture content in the air'),
('Dry', 'Low moisture content in the air'),
('Overcast', 'Cloudy with no visible sun');

INSERT INTO `water_level_alerts` (water_level, alert_level, alert_date, measurement_locations_id) VALUES 
(8.5, 3, '2023-02-15', 1), (10.2, 4, '2023-03-10', 2),
(6.8, 2, '2023-04-05', 3), (5.5, 1, '2023-05-20', 4),
(4.2, 1, '2023-06-12', 5), (9.7, 3, '2023-07-08', 6),
(7.1, 2, '2023-08-25', 7), (3.9, 1, '2023-09-18', 8),
(3.2, 1, '2023-10-30', 9), (12.3, 4, '2023-11-22', 10),
(4.8, 1, '2023-12-14', 11), (6.3, 2, '2024-01-07', 12),
(8.9, 3, '2024-02-19', 13), (5.7, 2, '2024-03-03', 14),
(4.5, 1, '2024-04-11', 15);

INSERT INTO `water_levels_has_meteorological_conditions` (water_levels_id, meteorological_conditions_id) VALUES 
(1, 1), (2, 2), (3, 3), (4, 4), (5, 5),
(6, 6), (7, 7), (8, 8), (9, 9), (10, 10),
(11, 11), (12, 12), (13, 13), (14, 14), (15, 15);

INSERT INTO `hydrological_objects_has_rivers` (hydrological_objects_id, rivers_id) VALUES 
(1, 1), (2, 2), (3, 3), (4, 4), (5, 5),
(6, 6), (7, 7), (8, 8), (9, 9), (10, 10),
(11, 11), (12, 12), (13, 13), (14, 14), (15, 15);

INSERT INTO `users_has_water_level_alerts` (users_id, water_level_alerts_id) VALUES 
(1, 1), (2, 2), (3, 3), (4, 4), (5, 5),
(6, 6), (7, 7), (8, 8), (9, 9), (10, 10),
(11, 11), (12, 12), (13, 13), (14, 14), (15, 15);


DROP PROCEDURE IF EXISTS get_rivers_after_river_type;
DROP PROCEDURE IF EXISTS get_measurement_locations_after_rivers;
DROP PROCEDURE IF EXISTS get_measurement_locations_after_regions;
DROP PROCEDURE IF EXISTS get_water_level_alerts_after_measurement_locations;
DROP PROCEDURE IF EXISTS get_water_levels_after_measurement_locations;
DROP PROCEDURE IF EXISTS get_rivers;
DROP PROCEDURE IF EXISTS get_water_level_alerts;
DROP PROCEDURE IF EXISTS get_users;
DROP PROCEDURE IF EXISTS get_water_levels;
DROP PROCEDURE IF EXISTS get_meteorological_conditions;
DROP PROCEDURE IF EXISTS get_hydrological_objects;

DELIMITER //

CREATE PROCEDURE get_rivers_after_river_type(
	IN river_type_id INT
)
BEGIN
	SELECT rt.id AS river_types_id, r.id AS rivers_id, r.river_name, r.river_length, r.river_depth, r.river_country
    FROM river_types rt
    JOIN rivers r ON r.river_types_id = rt.id
    WHERE r.river_types_id = river_type_id;
END //

CREATE PROCEDURE get_measurement_locations_after_rivers(
	IN rivers_id INT
)
BEGIN
	SELECT r.id AS rivers_id, m.id AS measurement_locations_id, m.location_name, m.latitude, m.longitude, m.regions_id
    FROM rivers r
    JOIN measurement_locations m ON m.rivers_id = r.id
    WHERE m.rivers_id = rivers_id;
END //

CREATE PROCEDURE get_measurement_locations_after_regions(
	IN regions_id INT
)
BEGIN
	SELECT r.id AS regions_id, m.id AS measurement_locations_id, m.location_name, m.latitude, m.longitude, m.rivers_id
    FROM regions r
    JOIN measurement_locations m ON m.regions_id = r.id
    WHERE m.regions_id = regions_id;
END //

CREATE PROCEDURE get_water_level_alerts_after_measurement_locations(
	IN measurement_locations_id INT
)
BEGIN
	SELECT m.id AS measurement_locations_id, w.id AS water_level_alerts_id, w.water_level, w.alert_level, w.alert_date
    FROM measurement_locations m
    JOIN water_level_alerts w ON w.measurement_locations_id = m.id
    WHERE w.measurement_locations_id = measurement_locations_id;
END //

CREATE PROCEDURE get_water_levels_after_measurement_locations(
	IN measurement_locations_id INT
)
BEGIN
	SELECT m.id AS measurement_locations_id, w.id AS water_levels_id, w.water_level_value, w.start_date, w.end_date
    FROM measurement_locations m
    JOIN water_levels w ON w.measurement_locations_id = m.id
    WHERE w.measurement_locations_id = measurement_locations_id;
END //

CREATE PROCEDURE get_rivers(
	IN rivers_id INT
)
BEGIN
	SELECT ho.id, ho.hydrological_objects_id, ho.rivers_id, r.river_name, r.river_length, r.river_depth, r.river_country, h.object_type, h.object_description
    FROM rivers r
    JOIN hydrological_objects_has_rivers ho ON r.id = ho.rivers_id
    JOIN hydrological_objects h ON h.id = ho.hydrological_objects_id
    WHERE ho.rivers_id = rivers_id;
END //

CREATE PROCEDURE get_hydrological_objects(
	IN hydrological_objects_id INT
)
BEGIN
	SELECT ho.id,  ho.rivers_id, ho.hydrological_objects_id, h.object_type, h.object_description, r.river_name, r.river_length, r.river_depth, r.river_country
    FROM hydrological_objects h
    JOIN hydrological_objects_has_rivers ho ON h.id = ho.hydrological_objects_id
    JOIN rivers r ON ho.rivers_id = r.id
    WHERE ho.hydrological_objects_id = hydrological_objects_id;
END //

CREATE PROCEDURE get_water_level_alerts(
	IN water_level_alerts_id INT
)
BEGIN
	SELECT w.id AS alert_id, w.water_level, w.alert_level, w.alert_date, 
       u.id AS user_id, u.user_name, u.user_surname, u.user_email
	FROM water_level_alerts w
	JOIN users_has_water_level_alerts uh ON w.id = uh.water_level_alerts_id
	JOIN users u ON uh.users_id = u.id
    WHERE uh.water_level_alerts_id = water_level_alerts_id;
END //

CREATE PROCEDURE get_users(
	IN users_id INT
)
BEGIN
	SELECT u.id AS user_id, u.user_name, u.user_surname, u.user_email, 
       w.id AS alert_id, w.water_level, w.alert_level, w.alert_date
	FROM users u
	JOIN users_has_water_level_alerts uh ON u.id = uh.users_id
	JOIN water_level_alerts w ON uh.water_level_alerts_id = w.id
    WHERE uh.users_id = users_id;
END //

CREATE PROCEDURE get_water_levels(
	IN water_levels_id INT
)
BEGIN
	SELECT wl.id, wl.meteorological_conditions_id, wl.water_levels_id, w.water_level_value, w.start_date, w.end_date, m.condition_type, m.condition_description
    FROM water_levels w
    JOIN water_levels_has_meteorological_conditions wl ON w.id = wl.water_levels_id
    JOIN meteorological_conditions m ON m.id = wl.meteorological_conditions_id
    WHERE wl.water_levels_id = water_levels_id;
END //

CREATE PROCEDURE get_meteorological_conditions(
	IN meteorological_conditions_id INT
)
BEGIN
	SELECT wl.id, wl.water_levels_id, wl.meteorological_conditions_id, m.condition_type, m.condition_description,  w.water_level_value, w.start_date, w.end_date
    FROM meteorological_conditions m
    JOIN water_levels_has_meteorological_conditions wl ON m.id = wl.meteorological_conditions_id
    JOIN water_levels w ON w.id = wl.water_levels_id
    WHERE wl.meteorological_conditions_id = meteorological_conditions_id;
END //

DELIMITER //