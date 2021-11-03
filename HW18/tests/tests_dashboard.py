def test_checking_of_three_lang_of_web_application(dashboard):
    dashboard.change_lang_on_russian("Рус")
    dashboard.change_lang_on_english("Eng")
    dashboard.change_lang_on_ukrainian("Укр")

def test_check_policy_service_doc(dashboard):
    dashboard.check_policy_service()

def test_check_policy_doc(dashboard):
    dashboard.check_policy()

def test_rules_doc(dashboard):
    dashboard.check_rules()

def test_sending_link_via_SMS(dashboard):
    dashboard.check_test_send_SMS()
