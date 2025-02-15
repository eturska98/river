"""Ensemble learning.

Broadly speaking, there are two kinds of ensemble approaches. There are those that copy a single
model several times and aggregate the predictions of said copies. This includes bagging as well as
boosting. Then there are those that are composed of an arbitrary list of models, and can therefore
aggregate predictions from different kinds of models.

"""
from .bagging import (
    ADWINBaggingClassifier,
    BaggingClassifier,
    BaggingRegressor,
    LeveragingBaggingClassifier,
)
from .boosting import AdaBoostClassifier, ADWINBoostingClassifier, BOLEClassifier, ADAC2BoostingClassifier
from .ewa import EWARegressor
from .stacking import StackingClassifier
from .streaming_random_patches import SRPClassifier, SRPRegressor
from .voting import VotingClassifier

__all__ = [
    "AdaBoostClassifier",
    "ADWINBaggingClassifier",
    "ADWINBoostingClassifier",
    "BaggingClassifier",
    "BaggingRegressor",
    "BOLEClassifier",
    "ADAC2BoostingClassifier",
    "EWARegressor",
    "LeveragingBaggingClassifier",
    "SRPClassifier",
    "SRPRegressor",
    "StackingClassifier",
    "VotingClassifier",
]
