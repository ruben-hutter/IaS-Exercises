import os
import os.path
import subprocess
from shutil import make_archive
from shutil import move

SUB_HEADER = 'ias-u'
PART_NAMES = 'tobiashafner-rubenhutter'

def crawl_directory(work_dir):
	"""Crawls the directory for subfolders to process.

        All subfolders on the first layer named ias-u<num> are processed.
        The procsssing consist of a pdf export of the answers.md file,
        the compression of the directoy itself an automatic push to github.
        """

	for sub_dir in next(os.walk(work_dir))[1]:
		if sub_dir[:5] != SUB_HEADER:
			continue

		print('Processing', sub_dir, '...')
		ex_num = sub_dir[5:]
		sub_path = os.path.join(work_dir, sub_dir)
		md_path = os.path.join(sub_path, 'answers.md')
		pdf_path = os.path.join(sub_path, 'answers.pdf')
		zip_path = PART_NAMES+'-'+SUB_HEADER+ex_num

		if os.path.exists(md_path):
			export_pdf(md_path, pdf_path)

		compress_directory(zip_path, sub_path, work_dir)

	print('Done.')
	return

def export_pdf(md_path, pdf_path):
	"""Searches the directory for a answers.md file and exports it to pdf.

	The specified directory is searched for an answers.md file.
	If found the file is converted to pdf using pandoc.
	The pandoc output is  saved in the passed directory.
	"""
	print('Converting markdown to pdf...')
	options = ['pandoc', md_path, '-o', pdf_path]
	return subprocess.check_call(options)

def compress_directory(zip_path, sub_path, work_dir):
	"""Creates a zip archive of the passed directory.

	A zip archive containing the content of the specified director
	gets created. The archive itself is then stored in the specified
	directory.
	"""
	print('Creating zip-file...')
	print(zip_path)
	print(sub_path)
	make_archive(zip_path, 'zip', sub_path)
	move(os.path.join(work_dir, zip_path+'.zip'), os.path.join(sub_path, zip_path+'.zip'))
	return

def add_github(file):
	"""Adds the specified file to the git repo.

	The specified file gets added to the git repository by calling
	git add <filname>.
	"""

	return

def push_github():
	"""A commit is created for the newly create files and then
	automatically pushed to git.

	Calls git commit -m and  git push to update the git repository.
	"""


if __name__ == "__main__":
	# get directory the script was called from
	work_dir = os.path.dirname(os.path.realpath(__file__))
	# start crawling
	crawl_directory(work_dir)
