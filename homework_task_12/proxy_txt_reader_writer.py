from interfaces.iread import Read
from interfaces.iwrite import Write
from txt_reader import TxtReader
from txt_writer import TxtWriter


class ProxyTxtRW(Read, Write):

    def __init__(self, real_reader: Read, real_writer: Write):
        self.__result = ''
        self.__is_actual = None
        self.__is_actual_w = None
        self.__real_reader = real_reader
        self.__real_writer = real_writer

    def read(self):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__real_reader.read()
            self.__is_actual = True
            return self.__result

    def write(self, data):
        if not self.__is_actual_w:
            self.__real_writer.write(data)
            self.__is_actual_w = True
        else:
            print("Файл фже записаний")


if __name__ == '__main__':
    reader_reader = TxtReader('my_file.txt')
    writer_writer = TxtWriter('output.txt')
    proxy = ProxyTxtRW(reader_reader, writer_writer)
    print(proxy.read())  # тут прочитали файл
    proxy.write("Hello world!")
    print(proxy.read())  # тут вже не читаємо, а забираємо текст файлу
    proxy.write("Hello world!")
