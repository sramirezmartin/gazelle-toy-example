from subdir1.test import main

from google.cloud import aiplatform
from google.cloud import storage

# import google.cloud.storage as aiplatform
# import google.cloud.storage as storage

if(__name__=="__main__"):
    main()
    a = dir(aiplatform)
    b = dir(storage)