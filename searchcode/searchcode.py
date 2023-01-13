import logging
import argparse
import requests
from rich.tree import Tree
from rich import print as xprint
from rich.logging import RichHandler


# Getting code results; given a searchcode unique code ID
def code_results(api_endpoint):
    response = requests.get(api_endpoint).json()
    xprint(response['code'])


# Querying the searchcode index
def code_search(api_endpoint):
    response = requests.get(api_endpoint).json()
    if args.raw:
        xprint(response['results'])
    else:
        for count, item in enumerate(response['results'], start=1):
            code_data = {"ID": item['id'],
                         "Repo": item['repo'],
                         "Lines": item['linescount'],
                         "Filename": item['filename'],
                         "Location": item['location'],
                         "Language(s)": item['language'],
                         "Search term": response['searchterm']}
            result_tree = Tree(f"\n\nResult {count} of {response['total']}\n{item['name'].upper()}")
            for data_key, data_value in code_data.items():
                result_tree.add(f"{data_key}: {data_value}")
            
            xprint(result_tree)
            for line, code in item['lines'].items():
                xprint(f"{line}: {code}")
            xprint("-" * 100)


# Getting related code results; given a searchcode unique code ID
def related_results(api_endpoint):
    response = requests.get(api_endpoint).json()
    if args.raw:
        xprint(response)
    else:
        for item in response:
            code_data  = {"ID": item['id'],
                          "Lines": item['linescount'], 
                          "Filename": item['filename'],
                          "Source": item['source'],
                          "Source URI": item['sourceurl'],
                          "Location": item['location'],
                          "Language(s)": item['language'],
                          "MD5": item['md5hash']}
            result_tree = Tree(f"\n{item['reponame'].upper()}")
            for code_key, code_value in code_data.items():
                result_tree.add(f"{code_key}: {code_value}")
            xprint(result_tree)


def check_updates():
    current_version_tag = "1.3.0"
    """
    Checks if the release tag matches the current tag in the program
    If there's a match, ignore
    """
    response = requests.get("https://api.github.com/repos/rly0nheart/searchcode-cli/releases/latest").json()
    if response['tag_name'] == current_version_tag:
        pass
    else:
        xprint(f"[[green]UPDATE[/]] A new release of searchcode-cli is available ({response['tag_name']}). Run 'pip3 install --upgrade searchcode-cli' to install the updates.")
            
            
def usage():
    return """
    Basic usage:
        # code_search 
        searchcode code_search --query <query>

        # code_result
        searchcode code_result --code-id <code_id>

        # related_results
        searchcode related_results --code-id <code_id>
        
    Docker image usage:
        # code_search 
        docker run -it rly0nheart/searchcode-cli code_search --query <query>
        
        # code_search 
        docker run -it rly0nheart/searchcode-cli relate_results --code-id <code_id>
        """


def create_parser():
    parser = argparse.ArgumentParser(description="searchcode-cli: command line client for searchcode.com — by Richard Mwewa | https:about.me/rly0nheart", epilog="Search 75 billion lines of code from 40 million projects. Helping you find real world examples of functions, API's and libraries in 243 languages across 10+ public code sources", usage=usage())
    parser.add_argument("mode", 
                        help="""options:
                                      code_search - Queries the code index and returns at most 100 results.
                                      code_result - Returns the raw data from a code file given the code id which can be found as the id in a code search result.
                                      related_result - Returns an array of results given a searchcode unique code id which are considered to be duplicates.""", 
                        choices=['code_search', 'code_result', 'related_results'])
    parser.add_argument("-q", "--query", help="search query")
    parser.add_argument("-ci", "--code-id", help="code id (can be found as ID/id in a code_search result).", dest="code_id")
    parser.add_argument("-p", "--page", help="page number (default: %(default)s)", default=1)
    parser.add_argument("-r", "--raw", help="return results in raw json format", action="store_true")
    parser.add_argument("-sf", "--source-filter", help=argparse.SUPPRESS)  # Filters feature coming soon..
    parser.add_argument("--output",help=argparse.SUPPRESS)  # Output feature coming soon..
    parser.add_argument("-d", "--debug", help="enable debug mode (shows network logs)", action="store_true")
    return parser


def searchcode():
    api_endpoint = "https://searchcode.com/api"
    args_map = [('code_search',  code_search, f"{api_endpoint}/codesearch_I/?q={args.query}&p={args.page}&per_page=100"),
                ('code_result', code_results, f"{api_endpoint}/result/{args.code_id}"),
                ('related_results', related_results, f"{api_endpoint}/related_results/{args.code_id}")]
    if args.debug:
        logging.basicConfig(level='NOTSET', format='%(message)s', handlers=[RichHandler()]) 
    try:
        check_updates()
        for mode, function, endpoint in args_map:
            if args.mode == mode:
                function(endpoint)
    except KeyboardInterrupt:
    	xprint("[yellow]CtrlC detected.[/]")
    except Exception as error:
        xprint(f"[red]{error}[/]")
        
        
arg_parser = create_parser()
args = arg_parser.parse_args()
            
