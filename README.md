![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Azure SQL](https://img.shields.io/badge/Azure%20SQL-Database-blue?style=flat-square&logo=microsoftsqlserver&logoColor=white)

### GTFS Importer
This tool ingests GTFS data files provided by Metrolinx GO Transit into a Microsoft SQL Server database. It is built with **Python** and intended for use in backend projects that rely on accurate and structured transit schedule data (e.g., route planners or trip finders).

### Tech Stack
- **Language/Library:** Python, pyodbc, pandas, numpy
- **Database:** SQL Server

### Features
- Parses and imports GTFS files into structured SQL tables
- Supports essential GTFS files: calendar_dates.txt, routes.txt, shapes.txt, stop_times.txt, stops.txt, trips.txt
- Designed to work with Metrolinx's GTFS feed

### Future Improvements
- Integrate with other transit agencies’ open data
- implement it in Azure Functions to automate the import process

### Setup Instructions
1. Download the latest GTFS feed from https://www.gotransit.com/en/partner-with-us/software-developers
2. Extract the following files into a folder named gtfs under the project directory
	<pre> <code>
	gtfs/
	├── calendar_dates.txt
	├── routes.txt
	├── shapes.txt
	├── stop_times.txt
	├── stops.txt
	└── trips.txt
	</code> </pre>
3. Before running the importer, create the necessary SQL tables in your database. Here are the scripts required:
	<pre> <code>
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
	</code> </pre>
