from selene import browser, have


class GitHubPage:
    def open(self):
        browser.open("https://github.com")
        return self

    def desktop_sign_in(self):
        browser.element(".HeaderMenu-link--sign-in").click()

    def mobile_sign_in(self):
        browser.element(".Button-label").click()
        browser.element(".HeaderMenu-link--sign-in").click()

    def should_have_text_sign_in(self):
        browser.element("h1").should(have.text("Sign in to GitHub"))


github_page = GitHubPage()
