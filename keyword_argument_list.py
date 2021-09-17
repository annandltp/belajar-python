def create_html(tag, text, **attributes):
    html = f"<{tag}"

    for key, value in attributes.items():
        html = html + f" {key}='{value}'"

    html = html + f">{text}</{tag}>"
    return html

html = create_html("p", "Hello", style="paragraf")
print(html)
html = create_html("a", "Link", href="www.google.com", style="link")
print(html)
html = create_html("div", "Ini Div", style="contoh")
print(html)