class Solution:
    def simplifyPath(self, path: str) -> str:
        res = ""

        st = []

        dirs = path.split("/")
        dirs = [x for x in dirs if "/" not in x and x != ""]
        n = len(dirs)

        for i in range(n):
            if dirs[i] == "..":
                if st:
                    st.pop(-1)
            
            else:
                if dirs[i] == ".":
                    continue
                st.append(dirs[i])

        res = "/"
        res += "/".join(st)
        
        return res