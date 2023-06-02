import click, json, requests
from flask import Flask, render_template
from flask.cli import FlaskGroup
from bs4 import BeautifulSoup

app = Flask(__name__)
cli = FlaskGroup(app)


@app.cli.command()
@click.argument('query')
def search(query):

    url = f'https://www.google.com/search?q={query}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    search_results = soup.find_all('div', class_='BNeawe')
    results = [result.text for result in search_results]
    
    dict = {
        "query": query,
        "results": results
    }

    path1 = './search.json'
    json_file = open(path1, mode="w")
    json.dump(dict, json_file, indent=3, ensure_ascii=False)
    json_file.close()

    click.echo(f'{dict}!')


if __name__ == '__main__':
    cli()
