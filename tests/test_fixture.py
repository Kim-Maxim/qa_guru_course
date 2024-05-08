from pages.github_page import github_page


def test_github_desktop(desktop_version):
    github_page.open()
    github_page.desktop_sign_in()
    github_page.should_have_text_sign_in()


def test_github_mobile(mobile_version):
    github_page.open()
    github_page.mobile_sign_in()
    github_page.should_have_text_sign_in()
