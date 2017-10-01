class FtpCrawler:
    def __init__(self, base_path, ftplib):
        self.base_path = base_path
        self.ftplib = ftplib

    def get_all_entries(self):
        def make_path(components):
            return '/'.join(components)

        self.ftplib.login()

        result = list()

        stack = [self.base_path]

        while len(stack) > 0:
            cwd_path = stack.pop()
            print("cwd to:" + cwd_path)
            self.ftplib.cwd(cwd_path)

            cwd_entries = self.__cwd_entries()
            for (entry_name, is_dir) in cwd_entries:
                if is_dir:
                    stack.append(make_path([cwd_path, entry_name]))
                else:
                    result.append(make_path([cwd_path, entry_name]))

        return result

    def __cwd_entries(self):
        # TODO: Check if this holds true for all FTP directory entries
        def is_dir(ent):
            return ent[0] == 'd'

        entry_list = list()
        self.ftplib.dir(lambda ent: entry_list.append(ent))
        # FTP.nlst() to avoid issues extracting entry names that have spaces
        names = self.ftplib.nlst()

        results = list()
        for (i, entry) in enumerate(entry_list):
            attributes = entry.strip().split()
            results.append((names[i], is_dir(entry)))

        return results
