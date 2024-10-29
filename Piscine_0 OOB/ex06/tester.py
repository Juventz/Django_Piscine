from elements import Html, Head, Body, Title, Meta, H1, H2, Div, Table, Tr, Th, Td, Ul, Ol, Li, Span, Text, Hr, Br
from Page import Page

def run_tests():
    # Test 1: Valid HTML structure with head and body
    print("Test 1: Basic HTML Structure")
    html = Html([Head([Title([Text("Page Title")])]), Body([H1([Text("Hello")]), Div([P([Text("Some paragraph.")])])])])
    page = Page(html)
    assert page.is_valid() == True, "Test 1 failed."

    # Test 2: Head without a Title
    print("Test 2: Head without Title (should be invalid)")
    html = Html([Head([]), Body([H1([Text("Hello")])])])
    page = Page(html)
    assert page.is_valid() == False, "Test 2 failed."

    # Test 3: Body contains invalid element
    print("Test 3: Invalid element in body")
    html = Html([Head([Title([Text("Page Title")])]), Body([Meta([])])])  # Meta is not allowed in Body
    page = Page(html)
    assert page.is_valid() == False, "Test 3 failed."

    # Test 4: Valid single Text content in title, h1, li, etc.
    print("Test 4: Valid single Text content for specific tags")
    html = Html([Head([Title([Text("Valid Title")])]),
                 Body([H1([Text("Heading 1")]), Ol([Li([Text("List item")])])])])
    page = Page(html)
    assert page.is_valid() == True, "Test 4 failed."

    # Test 5: Span with valid content (Text and P)
    print("Test 5: Valid Span content (Text and P)")
    html = Html([Head([Title([Text("Page Title")])]),
                 Body([Span([Text("Span text"), P([Text("Nested paragraph")])])])])
    page = Page(html)
    assert page.is_valid() == True, "Test 5 failed."

    # Test 6: Ul containing non-Li elements (should be invalid)
    print("Test 6: Ul with invalid content")
    html = Html([Head([Title([Text("Page Title")])]),
                 Body([Ul([Text("Invalid item in list")])])])
    page = Page(html)
    assert page.is_valid() == False, "Test 6 failed."

    # Test 7: Tr containing both Th and Td (should be invalid)
    print("Test 7: Tr with mixed Th and Td")
    html = Html([Head([Title([Text("Page Title")])]),
                 Body([Table([Tr([Th([Text("Header")]), Td([Text("Data")])])])])])
    page = Page(html)
    assert page.is_valid() == False, "Test 7 failed."

    # Test 8: Valid usage of Hr and Br tags with no content
    print("Test 8: Valid Hr and Br tags")
    html = Html([Head([Title([Text("Page Title")])]),
                 Body([H1([Text("Heading 1")]), Hr([]), Br([])])])
    page = Page(html)
    assert page.is_valid() == True, "Test 8 failed."

    # Test 9: Invalid Hr or Br tags with content
    print("Test 9: Hr and Br tags with invalid content")
    html = Html([Head([Title([Text("Page Title")])]),
                 Body([Hr([Text("Invalid content")]), Br([Text("Invalid content")])])])
    page = Page(html)
    assert page.is_valid() == False, "Test 9 failed."

    # Test 10: Checking the HTML output string for DOCTYPE
    print("Test 10: HTML output with DOCTYPE")
    html = Html([Head([Title([Text("Page Title")])]), Body([H1([Text("Hello World")])])])
    page = Page(html)
    expected_output = "<!DOCTYPE html>\n" + str(html)
    assert str(page) == expected_output, "Test 10 failed."

    print("All tests passed.")

run_tests()
