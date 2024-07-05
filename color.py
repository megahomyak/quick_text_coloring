import html

input_ = open("input.txt", encoding="utf-8").read()

parts = iter(input_.split("|"))

def roll():
    try:
        return next(parts)
    except StopIteration:
        print(body)
        raise

body = html.escape(roll())

for part in parts:
    color = part
    text = roll()
    body += f'<span style="color: {color}">{html.escape(text)}</span>'
    body += roll()

open("output.html", "w", encoding="utf-8").write(
"""
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            p {{
                white-space: pre;
                font-family: monospace;
            }}
        </style>
    </head>
    <body>
        <p>{body}</p>
    </body>
</html>
""".format(body=body)
)
