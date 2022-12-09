from PlateConstants import PLATE_WEIGHTS

class PlateMath:

    def __init__(self, unit='lb', bar_weight=None):

        if unit not in ['lb', 'kg']:
            raise ValueError('Only accepted unit types are lb, kg')

        # Set up basics of plate math
        self.unit = unit
        self.plates = PLATE_WEIGHTS[unit]

        if bar_weight:
            self.bar_weight = bar_weight
        else:
            self.bar_weight = 45 if self.unit == 'lb' else 20

        # Calc max weight possible
        self.max_weight = self.calculateMaxWeight()

        # Plate math also stores a cache for best weight combos!
        self.cache = {}

    def calculateMaxWeight(self):

        plate_weight = sum([key*value for key,value in self.plates.items()])

        return self.bar_weight + plate_weight

    def calculatePlates(self, weight: int):

        # Check that weight is heavier than bar, lighter than max weight, and divisible at least by min plate*2
        if weight < self.bar_weight or weight > self.max_weight or weight%(2*min(self.plates.keys())):
            return {}

        ### Algorithm to determine optimal plate set

        # Corner Case Optimizations
        if weight == self.bar_weight:
            return 0

        if weight == self.max_weight:
            return self.plates

        if weight in self.cache.keys():
            return self.cache[weight]

        # If the answer is not obvious or previously calculated, use the recursive algorithm
        self.cache[weight] = self.rec_plate(weight-self.bar_weight)

        return self.cache[weight]

    # Recursive approach leveraging the cache
    # ref: https://stackoverflow.com/a/58600595
    def rec_plate(self, weight):

        # TODO: Modify so that plate quantities matter

        for plate_weight in sorted(list(self.plates.keys()), reverse=True):

            if weight >= 2*plate_weight:

                return {plate_weight: weight//(2*plate_weight), **self.rec_plate(weight%(2*plate_weight))}

        return {}