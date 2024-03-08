class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split("/")
        ret = ["/"]
        for dirname in dirs:
            if dirname == "" or dirname == ".":
                continue
            if dirname == "..":
                if ret[-1] != "/":
                    ret.pop()
            else:
                ret.append(dirname)
        return ret[0] + "/".join(ret[1:])
