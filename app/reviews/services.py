from app.reviews.models import Product, Review


class ProductServices:

    @staticmethod
    def get_product_by_id(product_id: int) -> Product:
        '''
        Get a product by its id
        '''
        #TODO: implement this method
        raise NotImplementedError()
    
    @staticmethod
    def get_product_by_name(product_name: str) -> Product:
        '''
        Get a product by its name
        '''
        #TODO: implement this method
        raise NotImplementedError()

    @staticmethod
    def get_products() -> list[Product]:
        '''
        Get all products
        '''
        #TODO: implement this method
        raise NotImplementedError()
    

class ReviewServices:

    @staticmethod
    def get_review_by_id(review_id: int) -> Review:
        '''
        Get a review by its id
        '''
        #TODO: implement this method
        raise NotImplementedError()

    @staticmethod
    def get_reviews_by_product_id(product_id: int) -> list[Review]:
        '''
        Get reviews by product id
        '''
        #TODO: implement this method
        raise NotImplementedError()

    @staticmethod
    def get_reviews_by_user_id(user_id: int) -> list[Review]:
        '''
        Get reviews by user id
        '''
        #TODO: implement this method
        raise NotImplementedError()

    @staticmethod
    def get_reviews() -> list[Review]:
        '''
        Get all reviews
        '''
        #TODO: implement this method
        raise NotImplementedError()

    @staticmethod
    def create_review(review: Review) -> Review:
        '''
        Create a review
        '''
        #TODO: implement this method
        raise NotImplementedError()
        

    