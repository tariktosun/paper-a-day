import dropbox
import smtplib
import pdb
import random

class paper_a_day:

	read_folder_path = '/read'
	to_read_folder_path = '/to_read'

	def __init__(self):
		self.dbx = dropbox.Dropbox('tmvXV-9BrcEAAAAAAAAjezJz8Vl7XvAZG9_F6Xbam9S8CUkmX8Dk_7s2acAO4yAC')

	def move_file_test(self, fname):
		print ('moved ' + fname) 
	def move_file(self, filename):
		''' move a file from the to_read folder to the read folder'''
		#filename = dbfile.name
		from_path = self.to_read_folder_path + '/' + filename 
		to_path = self.read_folder_path + '/' + filename 
		self.dbx.files_move(from_path, to_path)

	def generate_link(self, dbfile):
		''' generate public dropbox link to file'''
		filepath = dbfile.path_display
		return self.dbx.sharing_create_shared_link(filepath)

	def generate_move_link(self, dbfile):
		''' generate a url that will activate the file-move php script. '''
		filename = dbfile.name
		return 'http://tariktosun.com/paper-a-day/move_file.php?filepath='+filename

	def generate_email(self):
		''' Generates and sends email with link to paper'''
		files_to_read = self.dbx.files_list_folder(self.to_read_folder_path).entries
		if len(files_to_read) > 0:
			#f = files_to_read[0]
			f = random.choice(files_to_read)
			file_link = self.generate_link(f)
			move_file_url = self.generate_move_link(f)
			text = 'Hello Tarik.  Today you should read this paper:\n' + file_link.url + '\nTo register that you have read the paper, click this link:\n' + move_file_url
		else:
			text = 'Hello Tarik. Your to_read folder is empty.  Put some papers in it!' 
		self.send_message(text)

	def send_message(self, text):
		''' Sends the email from paperaday@tariktosun.com '''
		server = smtplib.SMTP('sub5.mail.dreamhost.com', 587)
		server.starttls()
		server.login("paper-a-day@tariktosun.com", "7GTivk-5")
		 
		subject = "Paper-A-Day!"
		#text = "A paper a day keeps the doctor away!"
		msg = 'Subject: {}\n\n{}'.format(subject, text)
		server.sendmail("paper-a-day@tariktosun.com", "tarikt@seas.upenn.edu", msg)
		server.quit()

if __name__ == "__main__":
	p = paper_a_day()
	p.generate_email()	
