# This is standUpReminder V0.1 by hao
import time
from plyer import notification

if __name__ == '__main__':

    while True:
        try:
            notification.notify(
                title = "您好，赶紧站起来!",
                message = "活动有益健康",
                app_icon = "walk.png",
                timeout = 5
            )
            time.sleep(60*60)
        except Exception as e:
            notification.notify(
                title="报错",
                message=str(e)
            )


