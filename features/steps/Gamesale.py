from behave import given, when, then

@given(u'I navigate to the index pages')
def nav(context):

    context.browser.get('http://localhost:5000/index')

@when(u'I click on the link to GameSale details')
def click(context):

    context.browser.find_element_by_partial_link_text('2').click()

@then(u'I should see the Gamelist for that Gamesale')
def details(context):

    print(context.browser.page_source)
    assert context.browser.current_url == 'http://localhost:5000/Gamesale/2'
    assert '01595 Video Game Sales' in context.browser.page_source