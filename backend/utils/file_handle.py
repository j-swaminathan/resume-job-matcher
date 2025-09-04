from PyPDF2 import PdfReader


def extract_text(filename):
    '''
    Function to extract the text from the provided PDF file
    '''
    reader = PdfReader(filename)
    page = reader.pages[0]
    page.extract_text()
    return  page.extract_text()

def save_text_in_txt_file(text):
    '''
    Save the text into a text file.
    '''
    with open("resume1.txt", "w", encoding="utf-8") as f:
        f.write(text)
   
def get_job_description():
    '''
    Get input from user regarding job description
    '''
    with open("job_description.txt", "r", encoding="utf-8") as f:
        job_desc = f.read()
    
    cleaned_description = clean_words(job_desc)
    # print(len(cleaned_description),"cleaned text--uncleaned", len(job_desc))
    return cleaned_description
