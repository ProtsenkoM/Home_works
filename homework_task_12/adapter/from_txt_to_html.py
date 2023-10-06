class TxtAdapter:
    def __init__(self, file_path: str, output_path: str):
        self.__file_path = file_path
        self.__output_path = output_path

    def txt_to_html_reader(self):
        with open(self.__file_path, 'r') as file:
            lines = file.readlines()

        header = lines[0].replace('\n', '').split(',')
        users_data = [user.replace('\n', '').split(',') for user in lines[1:]]
        result = []
        for user in users_data:
            result.append(dict(zip(header, user)))

        with open(self.__output_path, 'w') as f:
            f.write('<html>\n')
            f.write('<head>\n')
            f.write('<title>Users Data</title>\n')
            f.write('</head>\n')
            f.write('<body>\n')
            f.write('<table border="1">\n')
            for single_list in result:
                for header, value in single_list.items():
                    f.write('<tr>\n')
                    f.write(f"<td>&lt;{header}&gt;</td><td>{value}</td><td>&lt;/{header}&gt;</td>\n")
                    f.write('</tr>\n')
            f.write('</table>\n')
            f.write('</body>\n')
            f.write('</html>\n')


if __name__ == '__main__':
    TxtAdapter('test.txt', 'result.html').txt_to_html_reader()
