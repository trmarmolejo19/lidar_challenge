########################################################################################################################
#
# Crops all the values that are below range_min (resp. above range_max), and
# replaces them with the range_min value (resp. range_max)
#
########################################################################################################################


class LidarRangeFilter(object):
    def __init__(self):
        """
        Constructor
        """
        self.range_min = 0.03
        self.range_max = 50.0

    def update(self, input_scan):
        """ Crops all the values that are below min & max range and replaces them with the min & max value.

        Args:
            input_scan: List of floats representing distances.

        Returns:
            input_scan: Filtered list of floats.
        """
        for index, item in enumerate(input_scan):
            if item < self.range_min:
                input_scan[index] = self.range_min
            elif item > self.range_max:
                input_scan[index] = self.range_max

        return input_scan
