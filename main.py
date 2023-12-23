import os

# change the working directory when script is run through command-line
abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
os.chdir(dirname)

dir_dict = {'Documents': ['.DOC', '.DOCX', '.HTML', '.HTM', '.ODT',
                          '.PDF', '.XLS', '.XLSX', '.ODS', '.PPT', '.PPTX', '.TXT', '.MD'],
            'Pictures': ['.JPEG', '.JPG', '.GIF', '.TIFF', '.PSD', '.EPS', '.AI', '.INDD',
                         '.RAW', '.PNG', '.BMP', '.XCF'],
            'Video': ['.MP4', '.MOV', '.WMV', '.AVI', '.AVCHD', '.FLV', '.F4V', '.SWF',
                      '.MKV', '.WEBM', '.HTML5', '.OGG'],
            'Music': ['.M4A', '.FLAC', '.MP3', '.WAV', '.WMA', '.AAC']}

common_str = '/home/'+os.getlogin()+'/'


def get_extension(filename):

    split_filename = os.path.splitext(filename)

    return split_filename[1].upper()


# get files in working directory
files = os.listdir()
for file in files:

    extension = get_extension(file)
    file_name = dirname+'/'+file

    if extension in dir_dict['Documents']:
        file_str = common_str+'Documents/'+file
    elif extension in dir_dict['Pictures']:
        file_str = common_str+'Pictures/'+file
    elif extension in dir_dict['Video']:
        file_str = common_str+'Video/'+file
    elif extension in dir_dict['Music']:
        file_str = common_str+'Music/'+file

    os.replace(file_name, file_str)
