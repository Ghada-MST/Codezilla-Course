import re
import csv

# Make a csv file from employees emails file

def main():
  job_application = read_txt_file("job_apllications_emails.txt",
                                  'job_application')

  extracted_data_txt = extracted_data(job_application)


  csv_extracted_data_file = add_extracted_data_to_csv(extracted_data_txt,
                                                      "new_csv_data_file.csv")

def read_txt_file(txt_file, data_file):
  with open("job_apllications_emails.txt") as f:
    """Get txt file
    open txt file
    Read txt file

      Parameter: txt_file:main data file, data_file: the suggested name for data txt file returned

      return: varible data_file that contains readeable data in the txt file
      """
    data_file = f.read()
    return data_file


def extracted_data(data_file):
  """Get the readed txt file 
  match the pattern with the readable txt file

  Parameter: readeable txt file 

  return: variable data_match : contains list of tuples for the data matched with a special pattern
  """
  # Extract the name, email, phone number, address, date of birth and the experience
  data_pattern = r"Name: (.+)\nEmail: (.+)\nPhone: (.+)\nAddress: (.+)\nDOB: (.+)\n\s+.+ (\d+) year"

  data_match = re.findall(data_pattern, data_file)

  return data_match



def add_extracted_data_to_csv(data_match, csv_data_file):
  """Get the data match varialable 
  write a csv file to the extracted data

  Parameter: data match varialable contains list of tuples for the data matched with a special pattern, csv_file: the suggested name for data csv file wil be returned

  return: new csv file 
  """
  with open(csv_data_file, 'w', newline="") as f:
    csv_writer = csv.writer(f)
    fields = [
      'name', 'email', 'phone', 'address', 'date_of_birth', 'experience'
    ]
    csv_writer.writerow(fields)
    csv_writer.writerows(data_match)


  if __name__=="__main__":
    main()