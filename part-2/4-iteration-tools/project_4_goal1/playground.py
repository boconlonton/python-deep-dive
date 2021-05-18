# See a sample of what is in each file
import constants
import parse_utils

for fname, class_name, parser in zip(constants.fnames, constants.class_names, constants.parsers):
    file_iter = parse_utils.iter_file(fname, class_name, parser)
    print(fname)
    for _ in range(3):
        print(next(file_iter))
    print()
