from sys import argv
import requests
import json
import dewiki


def main():
    try:
        if len(argv) != 2:
            raise ValueError("Usage: python request_wikipedia.py <article_name>")

        article_name = argv[1]
        filename = article_name.replace(" ", "_") + ".wiki"

        url = "https://fr.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "format": "json",
            "prop": "extracts",
            "titles": article_name,
            "explaintext": True
        }

        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()
        print(json.dumps(data, indent=4))
        page = data.get("query", {}).get("pages", {})
        page_id = next(iter(page.values()))

        if "extract" not in page_id:
            raise ValueError(f"Article {article_name} not found")

        article_text = dewiki.from_string(page_id["extract"])
        with open(filename, "w") as file:
            file.write(article_text)

        print(f"Article {article_name} saved in {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return

    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return


if __name__ == "__main__":
    main()
