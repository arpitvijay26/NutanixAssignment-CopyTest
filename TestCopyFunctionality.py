# -*- encoding: utf-8 -*-


from NutanixAssignment.FeatureHelper.CopyValidation import CopyValidator
import json


class TestCopy:
    """
    TestCopy class has validate_if_copy_worked_correctly function which will test copy function on all methods available
    in CopyValidation class. For copy function to work correctly, following things are applicable:
    1. All files from Source should be copied to Destination
    2. In Destination folder, we should not have any additional files/folders present which are not in Source folder
    3. In Destination folder, we should not have any files/folders missing which are present in Source folder
    4. File Integrity check: MD5 for files in Source folder should be same as of MD5 for files in Destination folder
    """

    def __init__(self, source, destination, os):
        """
        Constructor for initializing
        :param source: String -> Path of Source folder/file
        :param destination: String -> Path of Destination folder/file
        :param os: String -> OS on which test is to be run
        """
        self.source = source
        self.destination = destination
        self.os = os

    def validate_if_copy_worked_correctly(self):
        """
        Test Function which will validate copy functionality completely
        :return: Tuple with list of 4 things in that order:
            1. Files/Folders copied successfully
            2. Junk file/folder only present in Destination
            3. File/Folder in Source but missing in Destination
            4. Files with integrity issue
        """
        copy_validator = CopyValidator(self.source, self.destination, self.os)
        list_of_files_directories_copied = copy_validator.list_of_files_directories_copied()
        list_of_junk_files_in_destination = copy_validator.list_of_junk_files_in_destinaton()
        list_of_missing_files_in_destination = copy_validator.list_of_missing_files_in_destination()
        list_of_files_with_integrity_problem = copy_validator.list_of_files_integrity_problem()
        return list_of_files_directories_copied, list_of_junk_files_in_destination, \
               list_of_missing_files_in_destination, list_of_files_with_integrity_problem


if __name__ == '__main__':
    with open("../TestFolder/test_file.json", "r") as fp:
        test_data = json.load(fp)

    for data in test_data['test_data_details']:
        test = TestCopy(data["source"], data["destination"], data["os"])
        print(test.validate_if_copy_worked_correctly())



