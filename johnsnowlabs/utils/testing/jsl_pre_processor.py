from nbconvert.preprocessors import ExecutePreprocessor
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError  # noqa
from nbformat import NotebookNode

from johnsnowlabs.utils.testing import test_settings, nb_code_match
import re


def flatten(text):
    return [item for sublist in text for item in sublist]


class JslPreprocessor(ExecutePreprocessor):
    def preprocess(self, nb: NotebookNode, resources=None, km=None):
        """
        See ExecutePreprocessor.preprocess for more infos
        """
        NotebookClient.__init__(self, nb, km)
        self.reset_execution_trackers()
        self._check_assign_resources(resources)

        # Inject custom nodes by prepending them
        for inject_node in test_settings.inject_header_nodes:
            nb['cells'].insert(0, inject_node)

        with self.setup_kernel():
            info_msg = self.wait_for_reply(self.kc.kernel_info())
            self.nb.metadata["language_info"] = info_msg["content"]["language_info"]
            for index, cell in enumerate(self.nb.cells):
                self.preprocess_cell(cell, resources, index)
        self.set_widgets_metadata()

        return self.nb, self.resources

    def preprocess_cell(self, cell, resources, index):
        """
        See ExecutePreprocessor.preprocess_cell for more infos
        See test_settings.py for all filter settings.
        Preprocess filters with the following rules :
        1. Replace line on Equality Match
        2. Replace line on Sub-String Match
        3. Drop line on Equality Match
        4. Drop line on Sub-String Match
        5. Drop on Regex Match
        """

        if cell['cell_type'] == 'code':
            # Full Cell Code based Preprocessing
            cell_code = nb_code_match.replace_on_sub_string_match(cell['source'],
                                                                  test_settings.sub_string_replacement_cells)
            code_lines = cell_code.split('\n')
            new_lines = []
            # Single Line based Preprocessing - Apply rules to each line individually
            for code_line in code_lines:
                # Replacements for singe lines of code
                code_line = nb_code_match.replace_on_equal_string_match(
                    code_line, test_settings.equal_string_replacement_lines, log_type='line')

                code_line = nb_code_match.replace_on_sub_string_match(
                    code_line, test_settings.sub_string_replacement_lines, log_type='line')

                # Dropping Lines of code
                if nb_code_match.equals_sub_string(code_line, test_settings.equal_string_drop_lines):
                    print(f'[JSL-PREPROCESSOR]: DROPPING <<<{code_line}>>>')
                    continue

                # Sub-String Check
                if nb_code_match.contains_sub_string(code_line, test_settings.sub_string_drop_lines):
                    print(f'[JSL-PREPROCESSOR]: DROPPING <<<{code_line}>>>')
                    continue

                new_lines.append(code_line)

            new_lines = '\n'.join(new_lines)

            # Clean anything that matches the regexes
            matches_to_clean = [re.findall(r, new_lines, re.DOTALL) for r in
                                test_settings.regex_cell_content_drop_matcher]
            for m in flatten(matches_to_clean):
                new_lines = new_lines.replace(m, '')

            cell['source'] = new_lines
            if test_settings.print_cell_before_executing:
                print(f'[JSL-PREPROCESSOR]: EXECUTING CELL \n <<<{cell["source"]}>>> \n')
            self._check_assign_resources(resources)
            cell = self.execute_cell(cell, index, store_history=True)
            return cell, self.resources

        return super().preprocess_cell(cell, resources, index)
