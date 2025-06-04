from playwright.sync_api import Page, expect

def test_wiki(page: Page):
    page.goto('https://www.wikipedia.org/')
    page.get_by_role('link', name='Русский').click()
    expect(page.get_by_text('Добро пожаловать в Википедию,')).to_be_visible()

def test_wiki_2(page: Page):
    page.goto('https://www.wikipedia.org/')
    page.get_by_role('link', name='Русский').click()
    page.get_by_role('link', name='Содержание').click()
    page.get_by_role('link', name='Обсуждений').click()
    expect(page.get_by_text('Обсуждение Википедии:Содержание')).to_be_visible()
