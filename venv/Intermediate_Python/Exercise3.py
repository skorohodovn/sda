import json


class JSONOutput:
    def __init__(self, *args, **kwargs):
        pass

    def to_json(self):
        return json.dumps(self)


class SimpleRow(dict, JSONOutput):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _headers(self):
        header_width = max(len(str(k)) for k in self)
        headers = " | ".join(str(k).center(header_width) for k in self)
        return f"| {headers} |"

    def _values(self):
        header_width = max(len(str(k)) for k in self)
        values = " | ".join(str(v).center(header_width) for v in self.values())
        return f"| {values} |"

    def table(self):
        return f"{self._headers()}\n{self._values()}"


class SimpleTable(list, JSONOutput):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def table(self):
        index = 0
        result = ""
        for row in self:
                if index == 0:
                    result += row.table()
                else:
                    result += f"\n{row._values()}"
                index += 1
        return result



row1 = SimpleRow(no=1, name="Mark",surname = "Connor", nationality="Irish")
row2 = SimpleRow(no=2, name="Basar", surname = "Turgut", nationality="Turkish")
row3 = SimpleRow(no=3, name="Basar", surname = "Skorohodov", nationality="Russian")
table = SimpleTable()
table.append(row1)
table.append(row2)
table.append(row3)

print(table.table())