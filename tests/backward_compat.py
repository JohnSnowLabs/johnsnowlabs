import unittest


def replace_string_in_file(file_path, string_to_find, string_to_replace_with):
    # replace_string_in_file and write it back to disk
    # Read the contents of the file
    with open(file_path, "r") as file:
        file_contents = file.read()

    # Replace the target string
    file_contents = file_contents.replace(string_to_find, string_to_replace_with, 1)

    # Write the modified contents back to the file
    with open(file_path, "w") as file:
        file.write(file_contents)


class BackwardCompatTestCase(unittest.TestCase):
    def test_backward_compat(self):
        f = "./johnsnowlabs/medical.py"
        # 1. Inject a "Deprecated" import statement to the medical module and then import it
        replace_string_in_file(
            f,
            string_to_find="from sparknlp_jsl.training import *",
            string_to_replace_with="from sparknlp_jsl.pretrained import InternalBananaDownloader",
        )

        # 2. Globals should be updated properly
        from johnsnowlabs import medical

        self.assertIsNotNone(medical.DistilBertForSequenceClassification)
        self.assertIsNotNone(medical.log_outdated_lib)
        self.assertIsNotNone(medical.AssertionDLModel)

        # 3. Undo the injection
        replace_string_in_file(
            f,
            string_to_replace_with="from sparknlp_jsl.training import *",
            string_to_find="from sparknlp_jsl.pretrained import InternalBananaDownloader",
        )


if __name__ == "__main__":
    unittest.main()
