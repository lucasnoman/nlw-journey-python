import uuid
from typing import Dict

from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.trips_repository import TripsRepository


class TripCreator:
  def __init__(self, trip_repository: TripsRepository, emails_repository: EmailsToInviteRepository) -> None:
    self.__trip_repository = trip_repository
    self.__emails_repository = emails_repository

  def create(self, body) -> Dict:
    try:
      emails = body.get('emails_to_invite')

      trip_id = str(uuid.uuid4())
      trip_infos = {**body, 'id': trip_id}

      self.__trip_repository.create_trip(trip_infos)

      if emails:
        for email in emails:
          email_infos = {
            'id': str(uuid.uuid4()),
            'trip_id': trip_id,
            'email': email,
          }
          self.__emails_repository.registry_email(email_infos)

      return {
        'body': {'id': trip_id},
        'status_code': 201,
      }
    except Exception as exception:
      return {
        'body': {'error': 'Bad Request', 'message': str(exception)},
        'status_code': 400,
      }
