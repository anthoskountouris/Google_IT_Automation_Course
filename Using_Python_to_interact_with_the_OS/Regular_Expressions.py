import re
from unicodedata import name

result = re.search(r"aza", "plaza") # the r indicates that it is a Rawstring
# print(result)
# <re.Match object; span=(2, 5), match='aza'>
# The span indicates the range
# If regex does not find a match it returns None

print(re.search(r"p.ng", "Pengae", re.IGNORECASE)) #case insensitive
print(re.search(r"[Pp]ython", "Python")) #Either P or p
print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search("cloud[a-zA-Z0-9]","cloudy"))
print(re.search("cloud[a-zA-Z0-9]","cloud9"))

print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces,")) # ^ indicates characters that we dont want match
print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I like dogs."))
print(re.search(r"cat|dog", "I like cats and dogs.")) #we only get the first one

# If we want to find them all
print(re.findall(r"cat|dog", "I like cats and dogs.")) #we only get the first one

# Repetition Qualifiers
print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Python Programming"))

print(re.search(r"o+l+", "goldfish")) # one ore more form rhis characters
print(re.search(r"o+l+", "goolldfish"))

print(re.search(r"\.com", "mydomain.com"))
print(re.search(r"\w*", "This is an example")) #it matches it until space
print(re.search(r"\w*", "This_is_another_example")) #it matches all the characters

print(re.search(r"\w\s+\w", "123  Ready Set GO")) #has at least 2 groups of alphanumeric characters (including letters, numbers, and underscores) separated by one or more whitespace characters.

pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_name"))
print(re.search(pattern, "this is a valid name"))
print(re.search(pattern, "my_variable_9"))
print(re.search(pattern, "my_variable_;"))
print(re.search(pattern, "5my_variable_"

"""
The check_web_address function checks if the text 
passed qualifies as a top-level web address, 
meaning that it contains alphanumeric characters 
(which includes letters, numbers, and underscores), 
as well as periods, dashes, and a plus sign, followed 
by a period and a character-only top-level domain such as 
".com", ".info", ".edu", etc. Fill in the regular expression 
to do that, using escape characters, wildcards, repetition 
qualifiers, beginning and end-of-line characters, and 
character classes.
"""

def check_web_address(text):
  pattern = r'^[\w\._-]*\.[A-Za-z]*$'
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True


"""
The check_time function checks for the 
time format of a 12-hour clock, as follows: 
the hour is between 1 and 12, with no leading zero, 
followed by a colon, then minutes between 00 and 59, 
then an optional space, and then AM or PM, in upper or 
lower case. Fill in the regular expression to do that. 
How many of the concepts that you just learned can you use here?
"""

def check_time(text):
  pattern = r'^(1[0-2]|1?[1-9]):([0-5][0-9])( ?([AaPp][Mm]))'
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False

"""
The contains_acronym function checks the 
text for the presence of 2 or more characters 
or digits surrounded by parentheses, with at 
least the first character in uppercase (if it's a letter), 
returning True if the condition is met, or False otherwise. 
For example, "Instant messaging (IM) is a set of communication 
technologies used for text-based communication" should return 
True since (IM) satisfies the match conditions." Fill in the 
regular expression in this function: 
"""
def contains_acronym(text):
  pattern = r'\(+[A-Z0-9][a-zA-Z]*\)'
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True


"""
Fill in the code to check if the 
text passed includes a possible U.S. 
zip code, formatted as follows: exactly 5 digits, 
and sometimes, but not always, followed by a dash with 4 more digits. 
The zip code needs to be preceded by at least one space, 
and cannot be at the start of the text.
"""

import re
def check_zip_code (text):
  result = re.search(r' \d{5}| \d{5}-\d{4}', text)
  return result != None

print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False

#Creating groups

def rearrange_name(name):
    result = re.search(r"^(\w*),(\w*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])        

rearrange_name("Lovelace, Ada")
# 'Ada Lovelace'
rearrange_name("Panikkos, Dennis")
# 'Dennis Panikkos '
rearrange_name("Hopper, Grace M.")
# 'Hopper, Grace M.'

#Capturing groups

def rearrange_name(name):
  result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

name=rearrange_name("Kennedy, John F.")
print(name)

#Repetition Qualifiers
print(re.search(r"[a-zA-Z"{5}, "a ghost"))
# 'ghost'
print(re.search(r"[a-zA-Z"{5}, "a scary ghost appeared"))
# 'scary'
print(re.findall(r"[a-zA-Z"{5}, "a scary ghost appeared"))
# '[scary, ghost, appea]'
print(re.findall(r"\b[a-zA-Z{5}\b", "a scary ghost appeared"))
# '[scary, ghost]'
print(re.findall(r"\w{5,10}", "I really like strawberries"))
# '['really', 'strawberri]'
print(re.findall(r"\w{5,}", "I really like strawberries"))
# '['really', 'strawberries]'
print(re.search(r"s\w{,20}", "I really like strawberries"))
# 'strawberries'


"""
The long_words function returns all words 
that are at least 7 characters. Fill in the 
regular expression to complete this function.
"""
def long_words(text):
  pattern = r'\w{7,}'
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []

# Extracting a PID Using regexes in Python

def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]

print(extract_pid(log_line("ferfff [12345]")))
# '12345'
print(extract_pid(log_line("ferfff [erfer]")))
# 'erfer'

"""
Add to the regular expression used in the 
extract_pid function, to return the uppercase message 
in parenthesis, after the process id.
"""
import re
def extract_pid(log_line):
    regex = r"\[(\d+)\]: (\w+)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1],result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)

# Splitting and Replacing

re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com")
# 'Received an email for [REDACTED]'

re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada"
# 'Ada Lovelace'

# Practice Quiz: Advanced Regular Expressions

"""
We're working with a CSV file, which contains employee information. 
Each record has a name field, followed by a phone number field, and a 
role field. The phone number field contains U.S. phone numbers, and needs 
to be modified to the international format, with "+1-" in front of the phone number. 
Fill in the regular expression, using groups, to use the transform_record function to do that."""

def transform_record(record):
  new_record = re.sub(r",(\d{3})",r",+1-\1",record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer

"""
The multi_vowel_words function returns all words with 3 or more consecutive vowels 
(a, e, i, o, u). Fill in the regular expression to do that.
"""

def multi_vowel_words(text):
  pattern = r'\w+[aiueo]{3,}\w+'
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# ['queue']

print(multi_vowel_words("Hello world!")) 
# []

"""
The transform_comments function converts comments in a Python script 
into those usable by a C compiler. This means looking for text that begins 
with a hash mark (#) and replacing it with double slashes (//), which is t
he C single-line comment indicator. For the purpose of this exercise, we’ll 
ignore the possibility of a hash mark embedded inside of a Python command, and 
assume that it’s only used to indicate a comment. We also want to treat repetitive 
hash marks (###), (####), etc., as a single comment indicator, to be replaced with just 
(//) and not (#//) or (//#). Fill in the parameters of the substitution method to complete this function:
"""
def transform_comments(line_of_code):
  result = re.sub(r'\#{1,}', r'//', line_of_code)
  return result

print(transform_comments("#### Start of program")) 
# Should be "// Start of program"
print(transform_comments("  number = 0   ### Initialize the variable")) 
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable")) 
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)")) 
# Should be "  return(number)"

"""
The convert_phone_number function checks for a U.S. phone number
format: XXX-XXX-XXXX (3 digits followed by a dash, 3 more digits 
followed by a dash, and 4 digits), and converts it to a more formal 
format that looks like this: (XXX) XXX-XXXX. Fill in the regular 
expression to complete this function.
"""

def convert_phone_number(phone):
  result = re.sub(r"\b(\d{3})-(\d{3})-(\d{4})\b", r"(\1) \2-\3", phone)
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300

# GRADED ASSESMENT

'''It's time to put your new skills to the test! In this lab, you'll have to find the users using an old email domain in a big list using regular expressions. To do so, you'll need to write a script that includes:

Replacing the old domain name (abc.edu) with a new domain name (xyz.edu).
Storing all domain names, including the updated ones, in a new file.'''

#!/usr/bin/env python3
import re
import csv
def contains_domain(address, domain):
  """Returns True if the email address contains the given,domain,in the domain position, false if not."""
  domain = r'[\w\.-]+@'+domain+'$'
  if re.match(domain,address):
    return True
  return False
def replace_domain(address, old_domain, new_domain):
  """Replaces the old domain with the new domain in the received address."""
  old_domain_pattern = r'' + old_domain + '$'
  address = re.sub(old_domain_pattern, new_domain, address)
  return address
def main():
  """Processes the list of emails, replacing any instances of the old domain with the new domain."""
  old_domain, new_domain = 'abc.edu', 'xyz.edu'
  csv_file_location = '<csv_file_location>'
  report_file = '<path_to_home_directory>' + '/updated_user_emails.csv'
  user_email_list = []
  old_domain_email_list = []
  new_domain_email_list = []
  with open(csv_file_location, 'r') as f:
    user_data_list = list(csv.reader(f))
    user_email_list = [data[1].strip() for data in user_data_list[1:]]
    for email_address in user_email_list:
      if contains_domain(email_address, old_domain):
        old_domain_email_list.append(email_address)
        replaced_email = replace_domain(email_address,old_domain,new_domain)
        new_domain_email_list.append(replaced_email)
    email_key = ' ' + 'Email Address'
    email_index = user_data_list[0].index(email_key)
    for user in user_data_list[1:]:
      for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
        if user[email_index] == ' ' + old_domain:
          user[email_index] = ' ' + new_domain
  f.close()
  with open(report_file, 'w+') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(user_data_list)
    output_file.close()
main()