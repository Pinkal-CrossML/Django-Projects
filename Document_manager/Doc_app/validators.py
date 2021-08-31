import os
from django.core.exceptions import ValidationError

def validate_file_extension(value):
    """
    this fuction will validate .pdf file extension as input file only by user 
    """
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', ]
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

def file_size(value):
    """
    this function will restrict user to upload a file size not more then 5 mb
    """
    limit = 5 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 5 MB.')


        