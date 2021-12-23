# import logging

# logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")


# # logging level -> debug< info < warning < error <critical
# logging.debug("Ah, Who made these codes?")
# logging.info("Preparation for automation")
# logging.warning("These scripts are out of data. It may have a problem in executing.")
# logging.error("Error occurred, the error code is ....")
# logging.critical("An irrecoverble problem has occurred.")


#터미널 과 파일에 합께 로그 남기기

import logging
from datetime import datetime

 # 시간[로그레벨] 메시지 형태로 로그를 작성
logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger()
#로그 레벨 설성
logger.setLevel(logging.DEBUG)

# 스트림
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)

# 파일
filename = datetime.now().strftime("mylogfile_%H%M%S_%m%d%Y.log")
fileHandler = logging.FileHandler(filename, encoding = "utf-8")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

logger.debug("execute the test that leaves a log")