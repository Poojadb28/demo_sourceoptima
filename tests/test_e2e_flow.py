import pytest

# IMPORT YOUR TEST FUNCTIONS
from tests.test_systemadmin_login import test_systemadmin_login
from tests.test_available_plays import test_available_plays
from tests.test_download_logs import test_download_logs
from tests.test_create_user import test_create_user
from tests.test_create_admin import test_create_admin
from tests.test_duplicate_user_creation import test_duplicate_user_creation
from tests.test_duplicate_admin_creation import test_duplicate_admin_creation
from tests.test_export_credit_history import test_export_credit_history
from tests.test_create_rootspace import test_create_rootspace
from tests.test_create_project import test_create_project
from tests.test_create_sub_space import test_create_sub_space
from tests.test_create_new_project import test_create_new_project
from tests.test_add_new_project_upload import test_add_new_project_upload
from tests.test_add_new_file_upload import test_add_new_file_upload
from tests.test_edit_details import test_edit_details
from tests.test_export_classification_to_excel import test_export_classification_to_excel
from tests.test_filter_labels import test_filter_labels
from tests.test_search_file import test_search_file
from tests.test_select_and_deselect_all_files import test_select_and_deselect_all_files
from tests.test_tariff_analysis_play import test_tariff_analysis_play
from tests.test_cost_reduction_play import test_cost_reduction_play
from tests.test_design_review_play import test_design_review_play
from tests.test_drawing_checker_both_play import test_drawing_checker_both_play
from tests.test_drawing_checker_general_play import test_drawing_checker_general_play
from tests.test_drawing_checker_veeco_play import test_drawing_checker_veeco_play
from tests.test_delete_file import test_delete_file
from tests.test_delete_project import test_delete_project
from tests.test_delete_root_space import test_delete_root_space
from tests.test_systemadmin_invalid_login import test_systemadmin_invalid_login
from tests.test_admin_login import test_admin_login
from tests.test_admin_invalid_login import test_admin_invalid_login
from tests.test_user_login import test_user_login
from tests.test_user_invalid_login import test_user_invalid_login
from tests.test_logout import test_logout


@pytest.mark.e2e
def test_end_to_end_flow(browser):

    print("\n STARTING COMPLETE E2E FLOW\n")

    # 1
    test_systemadmin_login(browser)

    # 2
    test_available_plays(browser)

    # 3
    test_download_logs(browser)

    # 4
    test_create_user(browser)

    # 5
    test_create_admin(browser)

    # 6
    test_duplicate_user_creation(browser)

    # 7
    test_duplicate_admin_creation(browser)

    # 8
    test_export_credit_history(browser)

    # 9
    test_create_rootspace(browser)

    # 10
    test_create_project(browser)

    # 11
    test_create_sub_space(browser)

    # 12
    test_create_new_project(browser)

    # 13
    test_add_new_project_upload(browser)

    # 14
    test_add_new_file_upload(browser)

    # 15
    test_edit_details(browser)

    # 16
    test_export_classification_to_excel(browser)

    # 17
    test_filter_labels(browser)

    # 18
    test_search_file(browser)

    # 19
    test_select_and_deselect_all_files(browser)

    # 20
    test_tariff_analysis_play(browser)

    # 21
    test_cost_reduction_play(browser)

    # 22
    test_design_review_play(browser)

    # 23
    test_drawing_checker_both_play(browser)

    # 24
    test_drawing_checker_general_play(browser)

    # 25
    test_drawing_checker_veeco_play(browser)

    # 26
    test_delete_file(browser)

    # 27
    test_delete_project(browser)

    # 28
    test_delete_root_space(browser)

    # 29
    test_systemadmin_invalid_login(browser)

    # 30
    test_admin_login(browser)

    # 31
    test_admin_invalid_login(browser)

    # 32
    test_user_login(browser)

    # 33
    test_user_invalid_login(browser)

    # 34
    test_logout(browser)

    print("\n E2E FLOW COMPLETED SUCCESSFULLY\n")