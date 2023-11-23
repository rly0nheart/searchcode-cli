# Search code api endpoints
from typing import Literal

from searchcode.connection import __api_handler
from searchcode.coreutils import (
    __code_sources,
    __code_languages,
    __api_endpoints,
)  # searchcode API endpoints


def __join_parameters(names, sources) -> str:
    """
    Returns a single string of joined parameters for the given list of filter names and sources.

    Parameters:
    -----------
    names (list):
        A list of names used as filters.
    sources (list):
        A list of tuples representing the sources to be filtered.

    Returns:
    --------
    str: A single string of joined parameters for the given list of filter names.

    About
    -----
    The __join_parameters function takes a list of names and sources as input and iterates over each name.
    For each name, it iterates over the sources list and compares the lowercase version of the
    source name to the lowercase version of each source name in the sources list.
    If a match is found, the corresponding parameter is added to the parameters string,
    and the loop breaks out of the inner loop to move on to the next source name.
    After iterating over all the source names, the function returns the parameters string.
    """
    parameters = ""
    for name in names:
        for source_name, source_parameter in sources:
            if source_name.lower() == name.lower():
                parameters += source_parameter
                break

    return parameters


def code_search(
    query: str,
    page_number: int = 0,
    per_page: int = 10,
    code_sources: Literal[
        "Google Code",
        "GitHub",
        "BitBucket",
        "Sourceforge",
        "CodePlex",
        "Minix3",
        "Fedora Project",
        "Seek Quarry",
        "Tizen",
        "Gitorious",
        "Google Android",
        "GitLab",
        "Codeberg",
        "Repo.or.cz",
        "Sr.ht",
    ] = None,
    code_languages: Literal[
        "XAML",
        "ASP.NET",
        "HTML",
        "Unknown",
        "MSBuild scripts",
        "C#",
        "XSD",
        "XML",
        "CMake",
        "C++ Header",
        "C++",
        "Makefile",
        "CSS",
        "Python",
        "MATLAB",
        "Objective C",
        "JavaScript",
        "Java",
        "PHP",
        "Erlang",
        "FORTRAN Legacy",
        "FORTRAN Modern",
        "C",
        "Lisp",
        "Visual Basic",
        "Shell",
        "Ruby",
        "Vim Script",
        "Assembly",
        "Objective C++",
        "Document Type Definition",
        "SQL",
        "YAML",
        "Ruby HTML",
        "Haskell",
        "Bash",
        "ActionScript",
        "MXML",
        "ASP",
        "D",
        "Pascal",
        "Scala",
        "Batch",
        "Groovy",
        "Extensible Stylesheet Language Transformations",
        "Perl",
        "Teamcenter def",
        "IDL",
        "Lua",
        "Go",
        "yacc",
        "Cython",
        "LEX",
        "Ada",
        "sed",
        "m4",
        "OCaml",
        "Smarty Template",
        "ColdFusion",
        "NAnt scripts",
        "Expect",
        "C Shell",
        "VHDL",
        "TCL",
        "JavaServer Pages",
        "SKILL",
        "AWK",
        "MUMPS",
        "SQL Data",
        "Korn Shell",
        "Patran Command Language",
        "DAL",
        "Fortran 95",
        "Octave",
        "Oracle Forms",
        "Dart",
        "COBOL",
        "Modula3",
        "Rexx",
        "Oracle Reports",
        "Softbridge Basic",
        "bc",
        "Teamcenter met",
        "Kermit",
        "Teamcenter mth",
        "AMPLE",
        "CCS",
        "JCL",
        "ABAP",
        "Clojure",
        "OpenCL",
        "CoffeeScript",
        "QML",
        "AutoHotkey",
        "ClojureScript",
        "ColdFusion CFScript",
        "gitignore",
        "Config",
        "Patch",
        "Markdown",
        "JSON",
        "Portable Object",
        "Certificate",
        "Hg Ignore",
        "MSBuild",
        "Windows Module Definition",
        "HLSL",
        "Sass",
        "LESS",
        "CUDA",
        "Swift",
        "Maven",
        "Visualforce Component",
        "Verilog-SystemVerilog",
        "JavaServer Faces",
        "Racket",
        "R",
        "Kotlin",
        "Powershell",
        "Rust",
        "Velocity Template Language",
        "Razor",
        "F#",
        "TypeScript",
        "NAnt script",
        "Ant",
        "Arduino Sketch",
        "Haml",
        "Grails",
        "Puppet",
        "Vala",
        "Windows Resource File",
        "Unity-Prefab",
        "Handlebars",
        "Robot Framework",
        "Pig Latin",
        "WiX source",
        "WiX include",
        "Mustache",
        "Windows Message File",
        "XQuery",
        "ECPP",
        "Visualforce Page",
        "WiX string localization",
        "Apex Trigger",
        "Vala Header",
        "xBase Header",
        "xBase",
        "InstallShield",
        "Harbour",
        "Forth",
        "PL/I",
        "CSON",
        "TeX",
        "Brainfuck",
        "Elixir",
        "zsh",
        "Julia",
        "dtrace",
        "Mathematica",
        "Standard ML",
        "SAS",
        "Haxe",
        "Nim",
        "TTCN",
        "Mercury",
        "Clean",
        "Prolog",
        "PureScript",
        "ERB",
        "Stylus",
        "XHTML",
        "Qt Project",
        "diff",
        "INI",
        "JSX",
        "Qt Linguist",
        "Qt",
        "Jam",
        "Protocol Buffers",
        "liquid",
        "Pug",
        "Freemarker Template",
        "XMI",
        "ClojureC",
        "Titanium Style Sheet",
        "Coq",
        "Crystal",
        "AspectJ",
        "EEx",
        "Elm",
        "Twig",
        "Slim",
        "Logtalk",
        "GDScript",
        "PowerBuilder",
        "Blade",
        "builder",
        "Visual Fox Pro",
        "SQL Stored Procedure",
        "License",
        "Agda",
        "Alchemist",
        "Alex",
        "Alloy",
        "Android Interface Definition Language",
        "Arvo",
        "AsciiDoc",
        "ATS",
        "Autoconf",
        "Basic",
        "Bazel",
        "Bitbake",
        "Bitbucket Pipeline",
        "Boo",
        "Bosque",
        "BuildStream",
        "C Header",
        "Cabal",
        "Cargo Lock",
        "Cassius",
        "Ceylon",
        "Closure Template",
        "Cogent",
        "Creole",
        "CSV",
        "Device Tree",
        "Dhall",
        "Docker ignore",
        "Dockerfile",
        "Emacs Dev Env",
        "Emacs Lisp",
        "F*",
        "FIDL",
        "Fish",
        "Flow9",
        "Fragment Shader File",
        "Futhark",
        "Game Maker Language",
        "Game Maker Project",
        "Gemfile",
        "Gherkin Specification",
        "GLSL",
        "GN",
        "Go Template",
        "Gradle",
        "Hamlet",
        "Happy",
        "HEX",
        "Idris",
        "ignore",
        "Intel HEX",
        "Isabelle",
        "Jade",
        "JAI",
        "Janet",
        "Jenkins Buildfile",
        "Jinja",
        "JSONL",
        "Julius",
        "Jupyter",
        "Just",
        "LaTeX",
        "LD Script",
        "Lean",
        "LOLCODE",
        "Lucius",
        "Luna",
        "Macromedia eXtensible Markup Language",
        "Madlang",
        "Mako",
        "Meson",
        "Module-Definition",
        "Monkey C",
        "MQL Header",
        "MQL4",
        "MQL5",
        "Nix",
        "nuspec",
        "Opalang",
        "Org",
        "Oz",
        "PKGBUILD",
        "PL/SQL",
        "Plain Text",
        "Polly",
        "Pony",
        "Processing",
        "Properties File",
        "PSL Assertion",
        "Q#",
        "QCL",
        "Rakefile",
        "Report Definition Language",
        "ReStructuredText",
        "Scheme",
        "Scons",
        "SPDX",
        "Specman e",
        "Spice Netlist",
        "SRecode Template",
        "Stata",
        "SVG",
        "Swig",
        "Systemd",
        "SystemVerilog",
        "TaskPaper",
        "Terraform",
        "Thrift",
        "TOML",
        "Twig Template",
        "TypeScript Typings",
        "Unreal Script",
        "Ur/Web",
        "Ur/Web Project",
        "V",
        "Varnish Configuration",
        "Verilog",
        "Verilog Args File",
        "Vertex Shader File",
        "Visual Basic for Applications",
        "Vue",
        "Web Services Description Language",
        "Wolfram",
        "Wren",
        "Xcode Config",
        "XML Schema",
        "Xtend",
        "Yarn",
        "Zig",
        "bait",
        "CloudFormation (JSON)",
        "CloudFormation (YAML)",
        "CodeQL",
        "DM",
        "Fennel",
        "FSL",
        "FXML",
        "hoon",
        "Nial",
        "ReasonML",
        "Sieve",
        "Solidity",
        "Teal",
        "TL",
    ] = None,
) -> list:
    """
    Queries the code index and returns at most 10 results.
    If the results list is empty, then this indicates that you have reached the end of the available results.
    To fetch all results for a given query, keep incrementing 'page_number'
    until you get a response with an empty results list.

    Parameters:
    ----------
    query (str):
        The search query string.
    page_number (int):
        Result page starting at 0 through to 49.
    per_page (int):
        Number of results wanted per page max 100.
    code_sources : list
        A list of source names used as filters.
    code_languages : list
        A list of programming language names used as filters.

    Returns:
    -------
    list: A list of code search results.

    About
    -----
    The code_search function queries the code index by sending an HTTP request to the code_search API endpoint.
    It accepts several optional parameters, including query, page_number, per_page, max_retries, backoff_time,
    code_sources, and code_languages.
    The sources and languages lists are filtered by calling the __join_parameters function,
    which returns a single string of joined parameters based on the filter names and sources.
    The function then calls the __api_handler function to handle the API request, which returns a dictionary of results.
    The results list is then extracted and returned.
    If the results list is empty, this indicates that you have reached the end of the available results.
    To fetch all results for a given query,
    keep incrementing 'page_number' until you get a page with an empty results list.
    """
    if code_languages is None:
        code_languages = []
    if code_sources is None:
        code_sources = []

    code_search_endpoint = __api_endpoints()[0]
    sources = __join_parameters(code_sources, __code_sources())
    languages = __join_parameters(code_languages, __code_languages())

    return __api_handler(
        code_search_endpoint.format(query, page_number, per_page, sources, languages)
    )["results"]


def code_result(code_id: int) -> str:
    """
    Retrieves the raw data for a code file based on the given code ID.

    Parameters:
    -----------
    code_id (int):
        The ID of the code file to retrieve.

    Returns:
    --------
    str: The raw data for the code file, if the API call is successful.

    About
    -----
    This function takes a `code_id` parameter which is the ID of a code file as returned by a code_search
    result. It then sends a request to the corresponding API endpoint to retrieve the raw data for that
    code file. If the request is successful, the raw data is returned.
    """
    code_result_endpoint = __api_endpoints()[1]
    return __api_handler(code_result_endpoint.format(code_id))["code"]


def related_results(code_id: int) -> list:
    """
    Queries the related code results endpoint of the Searchcode API and returns an array of results
    that are considered to be duplicates of the code file identified by the given code_id.

    Parameters:
    -----------
    code_id (int):
        The unique code id of the code file for which to retrieve related results.

    Returns:
    --------
        list: A list of related results, where each result is a dictionary containing metadata
        about a code file, such as its filename, repository, and lines of code.
    """
    related_results_endpoint = __api_endpoints()[2]
    return __api_handler(related_results_endpoint.format(code_id))
