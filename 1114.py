import threading


class Foo(object):
    mutex1 = threading.Lock()
    mutex2 = threading.Lock()

    def __init__(self):
        self.mutex1.acquire()
        self.mutex2.acquire()

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """

        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.mutex1.release()

    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        self.mutex1.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.mutex2.release()

    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        self.mutex1.acquire()
        self.mutex2.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()


def stringToIntegerList(input):
    return json.loads(input)


def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.next()
            nums = stringToIntegerList(line)

            ret = Solution().foobar(nums)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()