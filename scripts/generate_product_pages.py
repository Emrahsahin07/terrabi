import json
from pathlib import Path

PRODUCTS_DIR = Path(__file__).resolve().parents[1] / "products"
TEMPLATE = """
<!DOCTYPE html>
<html lang=\"en\">
<head>
<meta charset=\"UTF-8\">
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
<title>{title} - Terrabi</title>
<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">
<link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>
<link href=\"https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Open+Sans:wght@400;500;600&family=Pacifico&display=swap\" rel=\"stylesheet\">
<script src=\"https://cdn.tailwindcss.com/3.4.16\"></script>
<link href=\"https://cdnjs.cloudflare.com/ajax/libs/remixicon/4.6.0/remixicon.min.css\" rel=\"stylesheet\">
</head>
<body class=\"bg-gray-50 font-sans\">
<header class=\"bg-white shadow-sm\">
  <div class=\"max-w-7xl mx-auto p-4\">
    <a href=\"index.html\" class=\"text-primary\">&larr; Back to products</a>
  </div>
</header>
<main class=\"max-w-3xl mx-auto p-4\">
  <h1 class=\"text-3xl font-bold mb-4\">{title}</h1>
  <img src=\"{image}\" alt=\"{title}\" class=\"w-full mb-4 rounded\">
  <p class=\"mb-4\">{description}</p>
  <table class=\"w-full mb-4\">
    <tr><td class=\"font-semibold pr-2\">Category:</td><td>{category}</td></tr>
    <tr><td class=\"font-semibold pr-2\">Origin:</td><td>{origin}</td></tr>
    <tr><td class=\"font-semibold pr-2\">Price:</td><td>${price} / MT</td></tr>
    <tr><td class=\"font-semibold pr-2\">Min Order:</td><td>{min_order} MT</td></tr>
  </table>
  {packaging_block}
  {cert_block}
</main>
</body>
</html>
"""

def format_list_block(title, items):
    if not items:
        return ""
    lis = "\n".join(f"<li>{item}</li>" for item in items)
    return f"<h2 class=\"text-xl font-semibold mb-2\">{title}</h2>\n<ul class=\"list-disc pl-5 mb-4\">{lis}</ul>"

def main():
    for json_file in PRODUCTS_DIR.glob("*.json"):
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        packaging_block = format_list_block("Packaging", data.get("packaging"))
        cert_block = format_list_block("Certifications", data.get("certifications"))
        html = TEMPLATE.format(
            title=data.get("title", ""),
            image=data.get("image", ""),
            description=data.get("description", ""),
            category=data.get("category", ""),
            origin=data.get("origin", ""),
            price=data.get("price", ""),
            min_order=data.get("min_order", ""),
            packaging_block=packaging_block,
            cert_block=cert_block,
        )
        out_file = PRODUCTS_DIR / f"{json_file.stem}.html"
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated {out_file}")

if __name__ == "__main__":
    main()
