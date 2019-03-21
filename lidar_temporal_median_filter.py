import numpy

########################################################################################################################
#
# Returns the median of the current and the previous input_scans
#
########################################################################################################################


class LidarTemporalMedianFilter(object):
    def __init__(self):
        """
        Constructor
        """
        self.input_scans = []

    def update(self, scan_records, new_input_scan):
        """ Crops all the values that are below min & max range and replaces them with the min & max value.

        Args:
            scan_records: Int representing number of historical scans.
            new_input_scan: List of floats.

        Returns:
            new_median: List of floats calculated from the median of current scan + scan_records.
        """
        # Save scan.
        if len(self.input_scans) == scan_records + 1:
            del self.input_scans[0]
            self.input_scans.append(new_input_scan)
        else:
            self.input_scans.append(new_input_scan)

        # Filter for median
        temp = []
        new_median = []
        if len(self.input_scans) > 1:
            # Loop based on number of items in the input scan.
            for i in range(len(self.input_scans[0])):
                # Pull item at index of each scan list and add to a temp list.
                for x in range(len(self.input_scans)):
                    temp.append(self.input_scans[x][i])
                # Save median of numbers at index to list.
                new_median.append(numpy.median(temp))
                # Clear temp before moving on to next index.
                temp = []
        else:
            new_median = self.input_scans[0]

        return new_median
