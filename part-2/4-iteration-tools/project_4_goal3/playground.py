# See a sample of what is in each file
import constants
import parse_utils
import datetime

# for fname, class_name, parser in zip(constants.fnames, constants.class_names, constants.parsers):
#     file_iter = parse_utils.iter_file(fname, class_name, parser)
#     print(fname)
#     for _ in range(3):
#         print(next(file_iter))
#     print()

cutoff_date = datetime.datetime(2018, 3, 1)
filtered_iter = parse_utils.filtered_iter_combined(constants.fnames, constants.class_names,
                                                   constants.parsers, constants.compress_fields,
                                                   key=lambda row: row.last_updated >= cutoff_date)

