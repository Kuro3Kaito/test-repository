from time import sleep


class Clock(object):
    """Đồng hồ số"""

    def __init__(self, hour=0, minute=0, second=0):
        """Phương pháp khởi tạo

        :param hour: Giờ
        :param minute: Phút
        :param second: Giây
        """
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        """Đi từ"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """Hiển thị thời gian"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def main():
    clock = Clock(23, 59, 58)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()