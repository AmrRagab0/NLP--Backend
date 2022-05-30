class Product:
    product_name: str
    product_id: int
    total_rating: float
    agents_ids: list[str]

    def __init__(self, product_name: str, product_id: int, total_rating: float, agents_ids: list[str]):
        self.product_name = product_name
        self.product_id = product_id
        self.total_rating = total_rating
        self.agents_ids = agents_ids

    @staticmethod
    def from_json(json: dict):
        '''
        Create a Product from a json
        '''
        # TODO: implement this method
        raise NotImplementedError()

    def to_json(self) -> dict:
        '''
        Create a json from a Product
        '''
        # TODO: implement this method
        raise NotImplementedError()


class Review:
    review_id: str
    product: Product
    rating: float
    review: str
    user_id: str

    def __init__(self, review_id: str, product: Product, rating: float, review: str, user_id: str):
        self.review_id = review_id
        self.product = product
        self.rating = rating
        self.review = review
        self.user_id = user_id

    @staticmethod
    def from_json(json: dict):
        '''
        Create a Review from a json
        '''
        # TODO: implement this method
        raise NotImplementedError()

    def to_json(self) -> dict:
        '''
        Create a json from a Review
        '''
        # TODO: implement this method
        raise NotImplementedError()
