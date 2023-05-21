# Search code api endpoints
from typing import Union, Literal
from searchcode.connection import __api_handler
from searchcode.miscellaneous import __code_sources, __code_languages, __api_endpoints  # searchcode API endpoints


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


def code_search(query: str,
                page_number: int = 0,
                per_page: int = 10,
                code_sources: Union[Literal['Google Code'],
                                    Literal['GitHub'],
                                    Literal['BitBucket'],
                                    Literal['Sourceforge'],
                                    Literal['CodePlex'],
                                    Literal['Minix3'],
                                    Literal['Fedora Project'],
                                    Literal['Seek Quarry'],
                                    Literal['Tizen'],
                                    Literal['Gitorious'],
                                    Literal['Google Android'],
                                    Literal['GitLab'],
                                    Literal['Codeberg'],
                                    Literal['Repo.or.cz'],
                                    Literal['Sr.ht']] = None,

                code_languages: Union[Literal['XAML'],
                                      Literal['ASP.NET'],
                                      Literal['HTML'],
                                      Literal['Unknown'],
                                      Literal['MSBuild scripts'],
                                      Literal['C#'],
                                      Literal['XSD'],
                                      Literal['XML'],
                                      Literal['CMake'],
                                      Literal['C++ Header'],
                                      Literal['C++'],
                                      Literal['Makefile'],
                                      Literal['CSS'],
                                      Literal['Python'],
                                      Literal['MATLAB'],
                                      Literal['Objective C'],
                                      Literal['JavaScript'],
                                      Literal['Java'],
                                      Literal['PHP'],
                                      Literal['Erlang'],
                                      Literal['FORTRAN Legacy'],
                                      Literal['FORTRAN Modern'],
                                      Literal['C'],
                                      Literal['Lisp'],
                                      Literal['Visual Basic'],
                                      Literal['Shell'],
                                      Literal['Ruby'],
                                      Literal['Vim Script'],
                                      Literal['Assembly'],
                                      Literal['Objective C++'],
                                      Literal['Document Type Definition'],
                                      Literal['SQL'],
                                      Literal['YAML'],
                                      Literal['Ruby HTML'],
                                      Literal['Haskell'],
                                      Literal['Bash'],
                                      Literal['ActionScript'],
                                      Literal['MXML'],
                                      Literal['ASP'],
                                      Literal['D'],
                                      Literal['Pascal'],
                                      Literal['Scala'],
                                      Literal['Batch'],
                                      Literal['Groovy'],
                                      Literal['Extensible Stylesheet Language Transformations'],
                                      Literal['Perl'],
                                      Literal['Teamcenter def'],
                                      Literal['IDL'],
                                      Literal['Lua'],
                                      Literal['Go'],
                                      Literal['yacc'],
                                      Literal['Cython'],
                                      Literal['LEX'],
                                      Literal['Ada'],
                                      Literal['sed'],
                                      Literal['m4'],
                                      Literal['OCaml'],
                                      Literal['Smarty Template'],
                                      Literal['ColdFusion'],
                                      Literal['NAnt scripts'],
                                      Literal['Expect'],
                                      Literal['C Shell'],
                                      Literal['VHDL'],
                                      Literal['TCL'],
                                      Literal['JavaServer Pages'],
                                      Literal['SKILL'],
                                      Literal['AWK'],
                                      Literal['MUMPS'],
                                      Literal['SQL Data'],
                                      Literal['Korn Shell'],
                                      Literal['Patran Command Language'],
                                      Literal['DAL'],
                                      Literal['Fortran 95'],
                                      Literal['Octave'],
                                      Literal['Oracle Forms'],
                                      Literal['Dart'],
                                      Literal['COBOL'],
                                      Literal['Modula3'],
                                      Literal['Rexx'],
                                      Literal['Oracle Reports'],
                                      Literal['Softbridge Basic'],
                                      Literal['bc'],
                                      Literal['Teamcenter met'],
                                      Literal['Kermit'],
                                      Literal['Teamcenter mth'],
                                      Literal['AMPLE'],
                                      Literal['CCS'],
                                      Literal['JCL'],
                                      Literal['ABAP'],
                                      Literal['Clojure'],
                                      Literal['OpenCL'],
                                      Literal['CoffeeScript'],
                                      Literal['QML'],
                                      Literal['AutoHotkey'],
                                      Literal['ClojureScript'],
                                      Literal['ColdFusion CFScript'],
                                      Literal['gitignore'],
                                      Literal['Config'],
                                      Literal['Patch'],
                                      Literal['Markdown'],
                                      Literal['JSON'],
                                      Literal['Portable Object'],
                                      Literal['Certificate'],
                                      Literal['Hg Ignore'],
                                      Literal['MSBuild'],
                                      Literal['Windows Module Definition'],
                                      Literal['HLSL'],
                                      Literal['Sass'],
                                      Literal['LESS'],
                                      Literal['CUDA'],
                                      Literal['Swift'],
                                      Literal['Maven'],
                                      Literal['Visualforce Component'],
                                      Literal['Verilog-SystemVerilog'],
                                      Literal['JavaServer Faces'],
                                      Literal['Racket'], 
                                      Literal['R'],
                                      Literal['Kotlin'],
                                      Literal['Powershell'],
                                      Literal['Rust'],
                                      Literal['Velocity Template Language'],
                                      Literal['Razor'],
                                      Literal['F#'],
                                      Literal['TypeScript'],
                                      Literal['NAnt script'],
                                      Literal['Ant'],
                                      Literal['Arduino Sketch'],
                                      Literal['Haml'],
                                      Literal['Grails'],
                                      Literal['Puppet'],
                                      Literal['Vala'],
                                      Literal['Windows Resource File'],
                                      Literal['Unity-Prefab'],
                                      Literal['Handlebars'],
                                      Literal['Robot Framework'],
                                      Literal['Pig Latin'],
                                      Literal['WiX source'],
                                      Literal['WiX include'],
                                      Literal['Mustache'],
                                      Literal['Windows Message File'],
                                      Literal['XQuery'],
                                      Literal['ECPP'],
                                      Literal['Visualforce Page'],
                                      Literal['WiX string localization'],
                                      Literal['Apex Trigger'],
                                      Literal['Vala Header'],
                                      Literal['xBase Header'],
                                      Literal['xBase'],
                                      Literal['InstallShield'],
                                      Literal['Harbour'],
                                      Literal['Forth'],
                                      Literal['PL/I'],
                                      Literal['CSON'],
                                      Literal['TeX'],
                                      Literal['Brainfuck'],
                                      Literal['Elixir'],
                                      Literal['zsh'],
                                      Literal['Julia'],
                                      Literal['dtrace'],
                                      Literal['Mathematica'],
                                      Literal['Standard ML'],
                                      Literal['SAS'],
                                      Literal['Haxe'],
                                      Literal['Nim'],
                                      Literal['TTCN'],
                                      Literal['Mercury'],
                                      Literal['Clean'],
                                      Literal['Prolog'],
                                      Literal['PureScript'],
                                      Literal['ERB'],
                                      Literal['Stylus'],
                                      Literal['XHTML'],
                                      Literal['Qt Project'],
                                      Literal['diff'],
                                      Literal['INI'],
                                      Literal['JSX'],
                                      Literal['Qt Linguist'],
                                      Literal['Qt'],
                                      Literal['Jam'],
                                      Literal['Protocol Buffers'],
                                      Literal['liquid'],
                                      Literal['Pug'],
                                      Literal['Freemarker Template'],
                                      Literal['XMI'], 
                                      Literal['ClojureC'],
                                      Literal['Titanium Style Sheet'],
                                      Literal['Coq'],
                                      Literal['Crystal'],
                                      Literal['AspectJ'],
                                      Literal['EEx'],
                                      Literal['Elm'],
                                      Literal['Twig'],
                                      Literal['Slim'],
                                      Literal['Logtalk'],
                                      Literal['GDScript'],
                                      Literal['PowerBuilder'],
                                      Literal['Blade'],
                                      Literal['builder'],
                                      Literal['Visual Fox Pro'],
                                      Literal['SQL Stored Procedure'],
                                      Literal['License'],
                                      Literal['Agda'],
                                      Literal['Alchemist'],
                                      Literal['Alex'],
                                      Literal['Alloy'],
                                      Literal['Android Interface Definition Language'],
                                      Literal['Arvo'],
                                      Literal['AsciiDoc'],
                                      Literal['ATS'],
                                      Literal['Autoconf'],
                                      Literal['Basic'],
                                      Literal['Bazel'],
                                      Literal['Bitbake'],
                                      Literal['Bitbucket Pipeline'],
                                      Literal['Boo'],
                                      Literal['Bosque'],
                                      Literal['BuildStream'],
                                      Literal['C Header'],
                                      Literal['Cabal'],
                                      Literal['Cargo Lock'],
                                      Literal['Cassius'],
                                      Literal['Ceylon'],
                                      Literal['Closure Template'],
                                      Literal['Cogent'],
                                      Literal['Creole'],
                                      Literal['CSV'],
                                      Literal['Device Tree'],
                                      Literal['Dhall'],
                                      Literal['Docker ignore'],
                                      Literal['Dockerfile'],
                                      Literal['Emacs Dev Env'],
                                      Literal['Emacs Lisp'],
                                      Literal['F*'],
                                      Literal['FIDL'],
                                      Literal['Fish'],
                                      Literal['Flow9'],
                                      Literal['Fragment Shader File'],
                                      Literal['Futhark'],
                                      Literal['Game Maker Language'],
                                      Literal['Game Maker Project'],
                                      Literal['Gemfile'],
                                      Literal['Gherkin Specification'],
                                      Literal['GLSL'],
                                      Literal['GN'],
                                      Literal['Go Template'],
                                      Literal['Gradle'],
                                      Literal['Hamlet'],
                                      Literal['Happy'],
                                      Literal['HEX'],
                                      Literal['Idris'],
                                      Literal['ignore'],
                                      Literal['Intel HEX'],
                                      Literal['Isabelle'],
                                      Literal['Jade'],
                                      Literal['JAI'],
                                      Literal['Janet'],
                                      Literal['Jenkins Buildfile'],
                                      Literal['Jinja'],
                                      Literal['JSONL'],
                                      Literal['Julius'],
                                      Literal['Jupyter'],
                                      Literal['Just'],
                                      Literal['LaTeX'],
                                      Literal['LD Script'],
                                      Literal['Lean'],
                                      Literal['LOLCODE'],
                                      Literal['Lucius'],
                                      Literal['Luna'],
                                      Literal['Macromedia eXtensible Markup Language'],
                                      Literal['Madlang'],
                                      Literal['Mako'],
                                      Literal['Meson'],
                                      Literal['Module-Definition'],
                                      Literal['Monkey C'],
                                      Literal['MQL Header'],
                                      Literal['MQL4'],
                                      Literal['MQL5'],
                                      Literal['Nix'],
                                      Literal['nuspec'],
                                      Literal['Opalang'],
                                      Literal['Org'],
                                      Literal['Oz'],
                                      Literal['PKGBUILD'],
                                      Literal['PL/SQL'],
                                      Literal['Plain Text'],
                                      Literal['Polly'],
                                      Literal['Pony'],
                                      Literal['Processing'],
                                      Literal['Properties File'],
                                      Literal['PSL Assertion'],
                                      Literal['Q#'],
                                      Literal['QCL'],
                                      Literal['Rakefile'],
                                      Literal['Report Definition Language'],
                                      Literal['ReStructuredText'],
                                      Literal['Scheme'],
                                      Literal['Scons'],
                                      Literal['SPDX'],
                                      Literal['Specman e'],
                                      Literal['Spice Netlist'],
                                      Literal['SRecode Template'],
                                      Literal['Stata'],
                                      Literal['SVG'],
                                      Literal['Swig'],
                                      Literal['Systemd'],
                                      Literal['SystemVerilog'],
                                      Literal['TaskPaper'],
                                      Literal['Terraform'],
                                      Literal['Thrift'],
                                      Literal['TOML'],
                                      Literal['Twig Template'],
                                      Literal['TypeScript Typings'],
                                      Literal['Unreal Script'],
                                      Literal['Ur/Web'],
                                      Literal['Ur/Web Project'],
                                      Literal['V'],
                                      Literal['Varnish Configuration'],
                                      Literal['Verilog'],
                                      Literal['Verilog Args File'],
                                      Literal['Vertex Shader File'],
                                      Literal['Visual Basic for Applications'],
                                      Literal['Vue'],
                                      Literal['Web Services Description Language'],
                                      Literal['Wolfram'],
                                      Literal['Wren'],
                                      Literal['Xcode Config'],
                                      Literal['XML Schema'],
                                      Literal['Xtend'],
                                      Literal['Yarn'],
                                      Literal['Zig'],
                                      Literal['bait'],
                                      Literal['CloudFormation (JSON)'],
                                      Literal['CloudFormation (YAML)'],
                                      Literal['CodeQL'],
                                      Literal['DM'],
                                      Literal['Fennel'],
                                      Literal['FSL'],
                                      Literal['FXML'],
                                      Literal['hoon'],
                                      Literal['Nial'],
                                      Literal['ReasonML'],
                                      Literal['Sieve'],
                                      Literal['Solidity'],
                                      Literal['Teal'],
                                      Literal['TL']] = None) -> list:
    
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

    return __api_handler(code_search_endpoint.format(query, page_number, per_page, sources, languages))['results']


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
    return __api_handler(code_result_endpoint.format(code_id))['code']


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
