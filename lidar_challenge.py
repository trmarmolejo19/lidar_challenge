import lidar_range_filter
import lidar_temporal_median_filter

########################################################################################################################
#
# Runs test_inputs through range_filter and median_filter
# Prints out both before and after.
#
########################################################################################################################


def main():
    range_filter = lidar_range_filter.LidarRangeFilter()
    median_filter = lidar_temporal_median_filter.LidarTemporalMedianFilter()
    test_inputs = [[0., 1., 2., 1., 3.],
                   [1., 5., 7., 1., 3.],
                   [2., 3., 4., 1., 0.],
                   [3., 3., 3., 1., 3.],
                   [10., 2., 4., 0., 0.],  # First 5 items from challenge document.
                   [8., 1., 4., 52., 0.],
                   [4., 3., 3., 4., 86.],
                   [3., 67., 1., 3., 2.],
                   [2., 6., 2., 0., 1000.],
                   [0., 5., 4., 100., 0.]]

    print('Range Filter: Crop min and max ranges.')
    for item in test_inputs:
        print('Before crop: {}'.format(item))
        filtered_crop = range_filter.update(input_scan=item[:])
        print('After crop: {}'.format(filtered_crop))

    print('---------------------------------------------')

    scan_records = 3
    print('Median Filter: Get median of current + previous {} scans.'.format(scan_records))
    for item in test_inputs:
        print('Before Median: {}'.format(item))
        filtered_median = median_filter.update(scan_records=scan_records, new_input_scan=item[:])
        print('After Median: {}'.format(filtered_median))


if __name__ == '__main__':
    main()
