from elements import Html, Head, Body, Title, Meta, H1, H2, Div, Table, \
    P, Tr, Th, Td, Ul, Ol, Li, Span, Text, Hr, Br, Img
from Page import Page


def run_tests():
    print("Test 1: Basic HTML Structure")
    html = Html([Head([Title([Text("Page Title")])]), Body([H1([Text("Hello")]), Div([P([Text("Some paragraph.")])])])])
    page = Page(html)
    if not page.is_valid():
        print("Test 1 failed.")
    else:
        print("Test 1 passed.")
    print("-" * 100)

    print("Test 2: Head without Title")
    html = Html([Head([]), Body([H1([Text("Hello")])])])
    page = Page(html)
    if page.is_valid():
        print("Test 2 failed.")
    else:
        print("Test 2 passed.")
    print("-" * 100)

    print("Test 3: Invalid element in body")
    html = Html([Head([Title([Text("Page Title")])]), Body([Meta([])])])
    page = Page(html)
    if page.is_valid():
        print("Test 3 failed.")
    else:
        print("Test 3 passed.")
    print("-" * 100)

    print("Test 4: Valid single Text content for specific tags")
    html = Html([Head([Title([Text("Valid Title")])]), Body([H1([Text("Heading 1")]), Ol([Li([Text("List item")])])])])
    page = Page(html)
    if not page.is_valid():
        print("Test 4 failed.")
    else:
        print("Test 4 passed.")
    print("-" * 100)

    print("Test 5: Valid Span content (Text and P)")
    html = Html([Head([Title([Text("Page Title")])]), Body([Span([Text("Span text"), P([Text("Nested paragraph")])])])])
    page = Page(html)
    if not page.is_valid():
        print("Test 5 failed.")
    else:
        print("Test 5 passed.")
    print("-" * 100)

    print("Test 6: Ul with invalid content")
    html = Html([Head([Title([Text("Page Title")])]), Body([Ul([Text("Invalid item in list")])])])
    page = Page(html)
    if page.is_valid():
        print("Test 6 failed.")
    else:
        print("Test 6 passed.")
    print("-" * 100)

    print("Test 7: Tr with mixed Th and Td")
    html = Html([Head([Title([Text("Page Title")])]), Body([Table([Tr([Th([Text("Header")]), Td([Text("Data")])])])])])
    page = Page(html)
    print(page.is_valid())
    if page.is_valid():
        print("Test 7 failed.")
    else:
        print("Test 7 passed.")
    print("-" * 100)

    print("Test 8: Valid Hr and Br tags in Body")
    html = Html([Head([Title([Text("Page Title")])]), Body([H1([Text("Heading 1")]), Hr([]), Br([])])])
    page = Page(html)
    if page.is_valid():
        print("Test 8 failed.")
    else:
        print("Test 8 passed.")
    print("-" * 100)

    print("Test 9: Hr and Br tags with invalid content")
    html = Html([Head([Title([Text("Page Title")])]), Body([Hr([Text("Invalid content")]), Br([Text("Invalid content")])])])
    page = Page(html)
    if page.is_valid():
        print("Test 9 failed.")
    else:
        print("Test 9 passed.")
    print("-" * 100)

    print("Test 10: HTML output with DOCTYPE")
    html = Html([Head([Title([Text("Page Title")])]), Body([H1([Text("Hello World")])])])
    page = Page(html)
    expected_output = "<!DOCTYPE html>\n" + str(html)
    if str(page) != expected_output:
        print("Test 10 failed.")
    else:
        print("Test 10 passed.")
    print("-" * 100)

    print("Test 11: H2 with single Text content")
    html = Html([Head([Title([Text("Page Title")])]), Body([H2([Text("Subheading")])])])
    page = Page(html)
    if not page.is_valid():
        print("Test 11 failed.")
    else:
        print("Test 11 passed.")
    print("-" * 100)

    print("Test 12: Img tag in Body")
    html = Html([Head([Title([Text("Page Title")])]), Body([H1([Text("Hello")]), Img([])])])
    page = Page(html)
    if page.is_valid():
        print("Test 12 failed.")
    else:
        print("Test 12 passed.")
    print("-" * 100)

    print("Test 13: Table with valid Tr elements")
    html = Html([Head([Title([Text("Page Title")])]), Body([Table([Tr([Th([Text("Header")])]), Tr([Td([Text("Data")])])])])])
    page = Page(html)
    if not page.is_valid():
        print("Test 13 failed.")
    else:
        print("Test 13 passed.")
    print("-" * 100)

    print("Test 14: Write HTML to file")
    html = Html([Head([Title([Text("Page Title")])]), Body([H1([Text("Hello")])])])
    page = Page(html)
    page.write_to_file("output.html")
    with open("output.html", "r") as file:
        content = file.read()
    expected_content = "<!DOCTYPE html>\n" + str(html)
    if content != expected_content:
        print("Test 14 failed.")
    else:
        print("Test 14 passed.")
    print("-" * 100)

    print("All tests completed.")

# def run_tests():
#     # Test 1: Affichage de la page vide
#     print("Test 1: Page vide")
#     page1 = Page(Html([Head(), Body()]))
#     print(page1)
#     print("Expected output: <!doctype html>\n<html>\n<head></head>\n<body></body>\n</html>\n")
    
#     # Test 2: Validation de la page vide
#     print("Test 2: Validation de la page vide")
#     assert not page1.is_valid(), "Test 2 failed: Page should not be valid."
#     print("Test 2 passed.")

#     # Test 3: Validation avec titre
#     print("Test 3: Validation avec titre")
#     page2 = Page(Html([Head(Title(Text('title'))), Body()]))
#     assert page2.is_valid(), "Test 3 failed: Page should be valid."
#     print("Test 3 passed.")

#     # Test 4: Validation avec un <li> dans le <body>
#     print("Test 4: Validation avec un <li> dans le <body>")
#     page3 = Page(Html([Head(Title(Text('title'))), Body(Li())]))
#     assert not page3.is_valid(), "Test 4 failed: Page should not be valid."
#     print("Test 4 passed.")

#     # Test 5: Validation avec un <ol> contenant un <li>
#     print("Test 5: Validation avec un <ol> contenant un <li>")
#     page4 = Page(Html([Head(Title(Text('title'))), Body(Ol(Li(Text('foo'))))]))
#     assert page4.is_valid(), "Test 5 failed: Page should be valid."
#     print("Test 5 passed.")

#     # Test 6: Écriture dans un fichier
#     print("Test 6: Écriture dans un fichier test.html")
#     page2.write_to_file("test.html")
#     print("test.html file created successfully.")


if __name__ == "__main__":
    try:
        run_tests()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        exit(1)
