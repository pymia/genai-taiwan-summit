
import re

def remove_html_tags(html_string):
    # Define the regular expression pattern for HTML tags
    pattern = r'<[^>]*>'
    
    # Use re.sub to remove all occurrences of the HTML tags
    cleaned_string = re.sub(pattern, '', html_string)
    
    return cleaned_string