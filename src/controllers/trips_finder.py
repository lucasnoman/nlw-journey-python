from flask import Blueprint

from src.models.repositories.trips_repository import TripsRepository

trips_routes_bp = Blueprint('trip_routes', __name__)


class TripFinder:
    def __init__(self, trip_repository: TripsRepository) -> None:
        self.__trip_repository = trip_repository

    def find_trip_details(self, trip_id):
        try:
            trip = self.__trip_repository.find_trip_by_id(trip_id)
            if not trip:
                raise Exception('Trip not found')

            return {
                'body': {
                    'trip': {
                        'id': trip[0],
                        'destination': trip[1],
                        'starts_at': trip[2],
                        'ends_at': trip[3],
                        'status': trip[6],
                    }
                },
                'status_code': 200,
            }
        except Exception as exception:
            return {
                'body': {'error': 'Bad Request', 'message': str(exception)},
                'status_code': 400,
            }
