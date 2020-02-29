from factory import Factory, Sequence, SubFactory
from factory.fuzzy import FuzzyChoice

from gatekeeper.domain.models.barriers import Barrier
from gatekeeper.domain.models.stations import Station


class BarrierFactory(Factory):
    class Meta:
        model = Barrier

    is_open = FuzzyChoice([True, False])


class StationFactory(Factory):
    class Meta:
        model = Station

    name = Sequence(lambda n: f"station_{n}")
    barrier = SubFactory(BarrierFactory, is_open=True)
