import zipfile
import sys
import os
from bs4 import BeautifulSoup as bs

# very cool little snippet to run 2 for loop at the same time
# thanks to 
# http://matteolandi.blogspot.ca/2009/09/python-double-for-loop-statement_06.html
def cross(a, b):
  for i in a:
    for j in b:
      yield (i, j)

class Book:
	""" Represent a book object
	"""

	def __init__(self, epub_file):

		self.metadata = dict()
		self.content = list()
		self.root_file_url = ''
		self.root_file = None

		# get the file
		self.book_file = zipfile.ZipFile(epub_file)

		# read container.xml file for info about the book
		container_soup = bs(self.book_file.read('META-INF/container.xml'), 'xml')

		# get root file and extract metadata
		root = container_soup.find('rootfile')
		self.root_file_url = root.get('full-path')
		self.root_file = bs(self.book_file.read(self.root_file_url), 'xml')
		for s in ['title','language','creator','date','identifier']:
			m = self.root_file.find(s)
			self.metadata[s] = m.text

	def __str__(self):

		return self.metadata['title']+' by '+self.metadata['creator']

	def load_content(self):
		"""Load the book content
		"""

		# get the toc file from the root file
		rel_path = self.root_file_url.replace(os.path.basename(self.root_file_url),'')
		self.toc_file_url = rel_path+self.root_file.find(id="ncx")['href']
		self.toc_file_soup = bs(self.book_file.read(self.toc_file_url), 'xml')

		# get the book content from the toc file


		for n,c in cross(self.toc_file_soup.find_all('navLabel'), self.toc_file_soup.find_all('content')):
			content_soup = bs(self.book_file.read(rel_path+c.get('src')))
			self.content.append({ 'part_name': c.text, 
						  'source_url': c.get('src'), 
						  'content_source': content_soup, 
						  'content_source_text': content_soup.body.text})