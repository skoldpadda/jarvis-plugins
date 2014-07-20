'''Open a browser, optionally to a specified URL or search query.'''
import webbrowser
import urllib

# @TODO: Make URL recognition more robust (like Chrome's omnibox, it can tell that amazon.com --> http://www.amazon.com)
# http://dev.chromium.org/user-experience/omnibox
# https://github.com/niklasb/vimium/blob/fuzzy/lib/completion.js

# http://stackoverflow.com/questions/827557/how-do-you-validate-a-url-with-a-regular-expression-in-python
def is_valid_url(url):
	import re
	regex = re.compile(
		r'^https?://'  # http:// or https://
		r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
		r'localhost|'  # localhost...
		r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
		r'(?::\d+)?'  # optional port
		r'(?:/?|[/?]\S+)$', re.IGNORECASE)
	return url is not None and regex.search(url)

def _run(args):

	@cli.cmd
	@cli.cmd_arg('url', nargs='*', default='https://www.google.com/')
	def web(url):
		url = ' '.join(url)
		if not is_valid_url(url):
			url = 'https://www.google.com/#q={}'.format(urllib.quote(url, ''))
		shell.out('Opening {}'.format(url))
		webbrowser.open(url)

	cli.run(args, main=web)
