from storages.backends.s3boto3 import s3Boto3storage


class MediaStorage(s3Boto3storage):
    location = 'media'
    file_overwrite = False