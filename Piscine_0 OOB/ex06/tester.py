from elements import Html, Head, Body, Title, Meta, H1, H2, Div, Table, \
    P, Tr, Th, Td, Ul, Ol, Li, Span, Text, Hr, Br, Img
from Page import Page


def run_tests():
    # # Test 1: Valid HTML structure with head and body
    print("Test 1: Basic HTML Structure")
    html = Html([Head([Title([Text("Page Title")])]), Body([H1([Text("Hello")]), Div([P([Text("Some paragraph.")])])])])
    page = Page(html)
    if not page.is_valid():
        print("Test 1 failed.")
    else:
        print("Test 1 passed.")
    print("-" * 100)

    # # Test 2: Head without a Title (should be invalid)
    print("Test 2: Head without Title")
    html = Html([Head([]), Body([H1([Text("Hello")])])])
    page = Page(html)
    print(page.is_valid())  # Devrait maintenant afficher False
    if page.is_valid():
        print("Test 2 failed.")
    else:
        print("Test 2 passed.")
    print("-" * 100)

    # # # Test 3: Body contains invalid element (Meta in Body is not allowed)
    print("Test 3: Invalid element in body")
    html = Html([Head([Title([Text("Page Title")])]), Body([Meta([])])])
    page = Page(html)
    if page.is_valid():
        print("Test 3 failed.")
    else:
        print("Test 3 passed.")
    print("-" * 100)

    # # # Test 4: Valid single Text content in Title, H1, Li, etc.
    print("Test 4: Valid single Text content for specific tags")
    html = Html([Head([Title([Text("Valid Title")])]), Body([H1([Text("Heading 1")]), Ol([Li([Text("List item")])])])])
    page = Page(html)
    if not page.is_valid():
        print("Test 4 failed.")
    else:
        print("Test 4 passed.")
    print("-" * 100)

    # # # Test 5: Span with valid content (Text and P)
    print("Test 5: Valid Span content (Text and P)")
    html = Html([Head([Title([Text("Page Title")])]), Body([Span([Text("Span text"), P([Text("Nested paragraph")])])])])
    page = Page(html)
    if not page.is_valid():
        print("Test 5 failed.")
    else:
        print("Test 5 passed.")
    print("-" * 100)

    # Test 6: Ul containing non-Li elements (should be invalid)
    print("Test 6: Ul with invalid content")
    html = Html([Head([Title([Text("Page Title")])]), Body([Ul([Text("Invalid item in list")])])])
    page = Page(html)
    print(page.is_valid())
    if page.is_valid():
        print("Test 6 failed.")
    else:
        print("Test 6 passed.")
    print("-" * 100)

    # # Test 7: Tr containing both Th and Td (should be invalid)
    # print("Test 7: Tr with mixed Th and Td")
    # html = Html([Head([Title([Text("Page Title")])]), Body([Table([Tr([Th([Text("Header")]), Td([Text("Data")])])])])])
    # page = Page(html)
    # if page.is_valid():
    #     print("Test 7 failed.")
    # print("-" * 100)

    # # Test 8: Valid usage of Hr and Br tags with no content
    # print("Test 8: Valid Hr and Br tags")
    # html = Html([Head([Title([Text("Page Title")])]), Body([H1([Text("Heading 1")]), Hr([]), Br([])])])
    # page = Page(html)
    # if not page.is_valid():
    #     print("Test 8 failed.")
    # print("-" * 100)

    # # Test 9: Invalid Hr or Br tags with content
    # print("Test 9: Hr and Br tags with invalid content")
    # html = Html([Head([Title([Text("Page Title")])]), Body([Hr([Text("Invalid content")]), Br([Text("Invalid content")])])])
    # page = Page(html)
    # if page.is_valid():
    #     print("Test 9 failed.")
    # print("-" * 100)

    # # Test 10: HTML output with DOCTYPE
    # print("Test 10: HTML output with DOCTYPE")
    # html = Html([Head([Title([Text("Page Title")])]), Body([H1([Text("Hello World")])])])
    # page = Page(html)
    # expected_output = "<!DOCTYPE html>\n" + str(html)
    # if str(page) != expected_output:
    #     print("Test 10 failed.")
    # print("-" * 100)

    # # Test 11: Valid H2 tag with single Text content
    # print("Test 11: H2 with single Text content")
    # html = Html([Head([Title([Text("Page Title")])]), Body([H2([Text("Subheading")])])])
    # page = Page(html)
    # if not page.is_valid():
    #     print("Test 11 failed.")
    # print("-" * 100)

    # # Test 12: Img tag in Body (self-closing, valid placement)
    # print("Test 12: Img tag in Body")
    # html = Html([Head([Title([Text("Page Title")])]), Body([H1([Text("Hello")]), Img([])])])
    # page = Page(html)
    # if not page.is_valid():
    #     print("Test 12 failed.")
    # print("-" * 100)

    # # Test 13: Valid Table structure with only Tr elements
    # print("Test 13: Table with valid Tr elements")
    # html = Html([Head([Title([Text("Page Title")])]), Body([Table([Tr([Th([Text("Header")])]), Tr([Td([Text("Data")])])])])])
    # page = Page(html)
    # if not page.is_valid():
    #     print("Test 13 failed.")
    # print("-" * 100)

    # # Test 14: Write HTML to file
    # print("Test 14: Write HTML to file")
    # html = Html([Head([Title([Text("Page Title")])]), Body([H1([Text("Hello")])])])
    # page = Page(html)
    # page.write_to_file("output.html")
    # with open("output.html", "r") as file:
    #     content = file.read()
    # expected_content = "<!DOCTYPE html>\n" + str(html)
    # if content != expected_content:
    #     print("Test 14 failed.")
    # print("-" * 100)

    print("All tests completed.")


if __name__ == "__main__":
    try:
        run_tests()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        exit(1)

