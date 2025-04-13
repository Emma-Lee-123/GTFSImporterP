this tool only deal with Metrolinx GO information
before running the tool, make sure the folder gtfs exists under the project folder, and download GTFS files from https://www.gotransit.com/en/partner-with-us/software-developers, and paste calendar_dates.txt, routes.txt, shapes.txt, stop_times.txt, stops.txt, and trips.txt into gtfs folder
double check the file structure, make sure it's aligned with what's in config.json
change database connection string in config.json as desired

here is db scripts to create tables:

use your_db_name
go
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'CalendarDates')
begin
CREATE TABLE CalendarDates (
    ServiceId VARCHAR(50) NOT NULL,
    Date CHAR(8) NOT NULL,
    ExceptionType INT NOT NULL
);
end

IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Routes')
begin
CREATE TABLE Routes (
    RouteId varchar(50) PRIMARY KEY,
    AgencyId varchar(10),
    RouteShortName varchar(50),
    RouteLongName varchar(255),
    RouteType INT,
    RouteColor VARCHAR(6),
    RouteTextColor VARCHAR(6)
);
end

IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Shapes')
begin
CREATE TABLE Shapes (
    ShapeId varchar(50) NOT NULL,
    ShapePtLat FLOAT,
    ShapePtLon FLOAT,
    ShapePtSequence INT
);
end

IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Trips')
begin
CREATE TABLE Trips (
    RouteId varchar(50) NOT NULL,
    ServiceId varchar(20) NOT NULL,
    TripId varchar(50) NOT NULL PRIMARY KEY,
	TripHeadsign varchar(255),
    TripShortName varchar(100),
    DirectionId INT,
    BlockId varchar(50),
    ShapeId varchar(50),
    WheelchairAccessible INT,
    BikesAllowed INT,
    RouteVariant varchar(50)
);
end

IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Stops')
begin
CREATE TABLE Stops (
    StopId varchar(10) PRIMARY KEY,
    StopName varchar(255),
    StopLat FLOAT,
    StopLon FLOAT,
    ZoneId varchar(10),
    StopUrl varchar(255),
    LocationType INT,
    ParentStation varchar(10),
    WheelchairBoarding INT,
    StopCode varchar(10)
);
end

IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'StopTimes')
begin
CREATE TABLE StopTimes (
    TripId varchar(50) NOT NULL,
    ArrivalTime varchar(10),
    DepartureTime varchar(10),
    StopId varchar(10),
    StopSequence INT,
    PickupType INT,
    DropOffType INT,
    StopHeadsign varchar(255),
    PRIMARY KEY (TripId, StopSequence)
);
end
