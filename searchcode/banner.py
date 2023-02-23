def ascii_banner():
    version_tag = "1.4.0.0"
    ascii_text = f"""
                              __                  __                    __ __ 
.-----.-----.---.-.----.----.|  |--.----.-----.--|  |.-----._____.----.|  |__|
|__ --|  -__|  _  |   _|  __||     |  __|  _  |  _  ||  -__|_____|  __||  |  |
|_____|_____|___._|__| |____||__|__|____|_____|_____||_____|     |____||__|__|
                                                                      v{version_tag}
                                       — Command Line Client for https://searchcode.com
                                                                  """
    return version_tag, ascii_text
