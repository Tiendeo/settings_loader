from configuration_loader.mergers.base import Base


class DefaultMerger(Base):
    def merge(self, dict_a, dict_b, path=None):
        """"
            Merges b into a
        """
        if path is None:
            path = []
        for key in dict_b:
            if key in dict_a:
                if isinstance(dict_a[key], dict) and isinstance(dict_b[key], dict):
                    self.merge(dict_a[key], dict_b[key], path + [str(key)])
                elif dict_a[key] != dict_b[key]:
                    dict_a[key] = dict_b[key]
            else:
                dict_a[key] = dict_b[key]
        return dict_a
