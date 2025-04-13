# Column mappings for different GTFS files

# Mapping for calendar_dates.txt
calendar_dates_mapping = {
    'service_id': 'ServiceId',
    'date': 'Date',
    'exception_type': 'ExceptionType'
}

# Mapping for stops.txt
stops_mapping = {
    'stop_id': 'StopId',
    'stop_name': 'StopName',
    'stop_lat': 'StopLat',
    'stop_lon': 'StopLon',
    'zone_id': 'ZoneId',
    'stop_url': 'StopUrl',
    'location_type': 'LocationType',
    'parent_station': 'ParentStation',
    'wheelchair_boarding': 'WheelchairBoarding',
    'stop_code': 'StopCode'
}

# Mapping for trips.txt
trips_mapping = {
    'route_id': 'RouteId',
    'service_id': 'ServiceId',
    'trip_id': 'TripId',
    'trip_headsign': 'TripHeadsign',
    'trip_short_name': 'TripShortName',
    'direction_id': 'DirectionId',
    'block_id': 'BlockId',
    'shape_id': 'ShapeId',
    'wheelchair_accessible': 'WheelchairAccessible',
    'bikes_allowed': 'BikesAllowed',
    'route_variant': 'RouteVariant'
}

# Mapping for routes.txt
routes_mapping = {
    'route_id': 'RouteId',
    'agency_id': 'AgencyId',
    'route_short_name': 'RouteShortName',
    'route_long_name': 'RouteLongName',
    'route_type': 'RouteType',
    'route_color': 'RouteColor',
    'route_text_color': 'RouteTextColor'
}

# Mapping for shapes.txt
shapes_mapping = {
    'shape_id': 'ShapeId',
    'shape_pt_lat': 'ShapePtLat',
    'shape_pt_lon': 'ShapePtLon',
    'shape_pt_sequence': 'ShapePtSequence'
}

stop_times_mapping = {
    'trip_id': 'TripId',
    'arrival_time': 'ArrivalTime',
    'departure_time': 'DepartureTime',
    'stop_id': 'StopId',
    'stop_sequence': 'StopSequence',
    'pickup_type': 'PickupType',
    'drop_off_type': 'DropOffType',
    'stop_headsign': 'StopHeadsign'
}
