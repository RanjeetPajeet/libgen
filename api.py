"""
api.py
======

Summary of `libgen-api` methods.
"""

import libgen_api


__all__ = ["search"]




class Search:
  def __init__(self):
    self.filters = {
      "Extension": "pdf",
    }
    
  
  
#   @staticmethod
  def by_title(self, title: str):
    s = libgen_api.LibgenSearch()
    results = s.search_title(title)
    return results
  
  
#   @staticmethod
  def by_author(self, author: str):
    s = libgen_api.LibgenSearch()
    results = s.search_author(author)
    return results
  
  
#   @staticmethod
  def by_title_and_author(self, title: str, author: str):
    s = libgen_api.LibgenSearch()
    results = s.search_title_filtered( title, {"Extension":"pdf", "Author":author}, exact_match=True )
    return results
  
  
#   def by_title2(self, title: str, author: str):
#     s = libgen_api.LibgenSearch()
#     results = s.search_title_filtered( title, {"Extension":"pdf"} )
#     filtered = []
#     for result in results:
#       if author.lower() in result["Author"]:
#         filtered.append(result)
#     return filtered, results
  
  
#   @staticmethod
  def get_downloads(self, search_results: list, just_one: bool = False):
    s = libgen_api.LibgenSearch()
    downloads = s.resolve_download_links(search_results[0])
    if just_one:
      return downloads["GET"]
    return downloads

  
  
  
  
  
search = Search()
