from src.models.repositories.link_repository import LinksRepository


class LinkFinder:
    def __init__(self, link_repository: LinksRepository) -> None:
        self.__link_repository = link_repository

    def find_link(self, link_id: str):
        try:
            links = self.__link_repository.find_links_from_trip(link_id)

            formatted_links = []
            for link in links:
                formatted_links.append(
                    {
                        'id': link[0],
                        'link': link[2],
                        'title': link[3],
                    }
                )

            return {
                'body': {'link': formatted_links},
                'status_code': 200,
            }

        except Exception as exception:
            return {
                'body': {'error': 'Bad Request', 'message': str(exception)},
                'status_code': 400,
            }
