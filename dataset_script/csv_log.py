import datetime, csv

class csv_log:
	def __init__(self, csv_log_file):
		self.log_file = csv_log_file
		# self.item = write_item

	# @staticmethod
	def write_log(self, item_to_write):
		current_time = "{:%Y-%m-%d--%H-%M-%S}".format(datetime.datetime.time())
		with open(self.log_file, "a", newline="", encoding="utf-8") as csv_log_file:
			csv_writer = csv.writer(csv_log_file, dialect="excel")
			csv_writer.writerow([item_to_write, current_time])
		print("Wrote %s in %s"%(item_to_write, self.log_file))
		return True

	# @staticmethod
	def search_log(self, item_to_search):
		with open(self.log_file, "r", encoding="utf-8") as csv_log_file:
			lines = csv_log_file.readlines()
		found = {}
		line_nb = []
		num = 0
		for n, line in enumerate(lines):
			if item_to_search in line.strip().split(",")[0]:
				num += 1
				line_nb.append(n)
				print('Found "%s" in line %d' % (item_to_search, n))
			else:
				for n_line in line.strip().split(",")[1:]:
					if item_to_search in n_line:
						num += 1
						line_nb.append(n)
						print('Found "%s" in line %d'%(item_to_search, n))
		found["number"]= num
		found["line_list"] = line_nb
		return found

if __name__ == '__main__':
    csv_file = "/Users/taylorguo/Downloads/class-descriptions.csv"
    item_to_search = "Pistachio ice cream"
    log_file = csv_log(csv_file)
    print(log_file.search_log(item_to_search))