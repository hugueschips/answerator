class DummyRatingPredictor:
    def predict(self, comment: str):
        return 5 + len(comment) - len(comment)


class DummyHatefulnessPredictor:
    def predict(self, comment: str):
        return 0.5 + len(comment) - len(comment)


class ClassifiedComment:
    def __init__(self, comment, rating, pred_rating, pred_hatefulness):
        self.comment = comment
        self.rating = rating
        self.pred_rating = pred_rating
        self.pred_hatefulness = pred_hatefulness

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"comment={self.comment!r}, "
            f"rating={self.rating}, "
            f"pred_rating={self.pred_rating}, "
            f"pred_hatefulness={self.pred_hatefulness})"
        )


class CommentClassifier:
    """
    TODO
    """

    def __init__(self):
        self.rating_predictor = DummyRatingPredictor()
        self.hatefulness_predictor = DummyHatefulnessPredictor()

    def classify(self, comment, rating=None):
        assert isinstance(comment, str)
        assert rating is None or isinstance(rating, int) and 1 <= rating <= 5
        return ClassifiedComment(
            comment,
            rating,
            pred_rating=self.rating_predictor.predict(comment),
            pred_hatefulness=self.hatefulness_predictor.predict(comment),
        )
