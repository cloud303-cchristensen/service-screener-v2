import os
import time
from utils.Config import Config

class S3Uploader:
    def __init__(self):
        self.s3_client = Config.get('ssBoto').client('s3')
        self.bucket_name = Config.get('s3bucket')
        self.current_date = time.strftime("%Y%m%d")

    def upload_output(self, stsInfo, root_dir):
        local_output = f"{root_dir}/output.zip"
        s3_key = f"screener-results/{stsInfo['Account']}/{self.current_date}/output.zip"
        
        if os.path.exists(local_output):
            try:
                self.s3_client.upload_file(local_output, self.bucket_name, s3_key)
                print(f"\n✅ Upload Successful")
                print(f"📂 Source: {local_output}")
                print(f"🎯 Destination: s3://{self.bucket_name}/{s3_key}\n")
                return True
            except Exception as e:
                print(f"\n❌ Upload Failed")
                print(f"🔍 Error: {str(e)}")
                print(f"📁 File Location: {local_output}\n")
                return False
        else:
            print(f"\n⚠️ Output file not found at: {local_output}")
            return False
